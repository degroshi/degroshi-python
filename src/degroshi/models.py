"""The API's request and response models: the types the client returns, and the bodies it sends.

Every model reads and writes the API's JSON (``Model.from_dict(...)``, ``model.to_dict()``). A write also takes a
plain dict in that shape, so building a model is optional:

>>> from degroshi.models import CreateTransactionRequest
>>> degroshi.transactions.create(CreateTransactionRequest.from_dict({...}))

``UNSET`` marks a field the API didn't send (or that a body leaves out); test for it with ``isinstance(x, Unset)``.
"""

from ._generated import models as _generated
from ._generated.models import *
from ._generated.types import UNSET, Unset

__all__ = ["UNSET", "Unset"]
__all__ += _generated.__all__
