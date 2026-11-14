"""The result types: every resource method names the type the API returns, and the ``Async…`` twins that type
checkers see for ``AsyncDegroshi`` match the classes ``Degroshi`` uses. Read from the source, so a method added
without its type, or without its async twin, fails here."""

import ast
import typing
from pathlib import Path

import pytest

from degroshi import _client

SOURCE = ast.parse(Path(_client.__file__).read_text())
RESOURCES = [
    "Spaces",
    "Accounts",
    "Transactions",
    "Categories",
    "Budgets",
    "Recurring",
    "Analytics",
    "Sources",
    "Changes",
    "Events",
]


def _classes(nodes: list[ast.stmt]) -> dict[str, ast.ClassDef]:
    return {node.name: node for node in nodes if isinstance(node, ast.ClassDef)}


def _methods(cls: ast.ClassDef) -> dict[str, ast.FunctionDef | ast.AsyncFunctionDef]:
    return {
        node.name: node
        for node in cls.body
        if isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef) and not node.name.startswith("_")
    }


def _type_checking_block() -> list[ast.stmt]:
    for node in SOURCE.body:
        if isinstance(node, ast.If) and ast.unparse(node.test) == "TYPE_CHECKING":
            return node.body
    raise AssertionError("no `if TYPE_CHECKING:` block in _client.py")


SYNC = _classes(SOURCE.body)
ASYNC = _classes(_type_checking_block())


def _annotation(node: ast.expr | None) -> str:
    return ast.unparse(node).replace("builtins.", "") if node is not None else ""


def _call(method: ast.FunctionDef | ast.AsyncFunctionDef) -> tuple[str, str]:
    """The mode helper the method calls (``one``, ``page``, ``done``…) and the generated operation it passes."""
    for node in ast.walk(method):
        if isinstance(node, ast.Call) and ast.unparse(node.func).startswith("self._m."):
            helper = ast.unparse(node.func).removeprefix("self._m.")
            operation = ast.unparse(node.args[0]) if node.args else ""
            return helper, operation
    raise AssertionError(f"{method.name} doesn't call self._m")


def _data_type(operation: str) -> str:
    """What the operation's envelope carries in ``data``, as the generated model writes it."""
    module = getattr(_client, operation)
    returned = typing.get_type_hints(module.sync)["return"]
    envelopes = [arg for arg in typing.get_args(returned) if arg.__name__.endswith(("Envelope", "Page"))]
    assert len(envelopes) == 1, f"{operation}: expected one envelope in {returned}"
    return envelopes[0].__annotations__["data"]


def _cases() -> list[tuple[str, str]]:
    return [(resource, name) for resource in RESOURCES for name in _methods(SYNC[resource])]


@pytest.mark.parametrize(("resource", "name"), _cases())
def test_a_method_returns_what_its_operation_returns(resource: str, name: str) -> None:
    # Arrange
    method = _methods(SYNC[resource])[name]
    helper, operation = _call(method)

    # Act
    actual = _annotation(method.returns)

    # Assert
    if helper == "one":
        assert actual == _data_type(operation)
    elif helper == "page":
        assert actual == _data_type(operation).replace("list[", "Page[", 1)
    elif helper == "done":
        assert actual == "None"
    else:
        assert actual and actual != "Any", f"{resource}.{name} names no type"


@pytest.mark.parametrize(("resource", "name"), _cases())
def test_the_async_twin_matches(resource: str, name: str) -> None:
    # Arrange
    sync = _methods(SYNC[resource])[name]
    twin = _methods(ASYNC[f"Async{resource}"]).get(name)

    # Act & Assert
    assert twin is not None, f"Async{resource}.{name} is missing"
    assert ast.unparse(twin.args) == ast.unparse(sync.args)
    returns = _annotation(sync.returns)
    if returns.startswith("Iterator["):
        assert isinstance(twin, ast.FunctionDef)
        assert _annotation(twin.returns) == "Async" + returns
    elif returns == "ChangeFeed":
        assert isinstance(twin, ast.FunctionDef)
        assert _annotation(twin.returns) == "AsyncChangeFeed"
    else:
        assert isinstance(twin, ast.AsyncFunctionDef)
        assert _annotation(twin.returns) == returns


def test_the_async_twins_have_no_extra_methods() -> None:
    for resource in RESOURCES:
        assert set(_methods(ASYNC[f"Async{resource}"])) == set(_methods(SYNC[resource])), resource
