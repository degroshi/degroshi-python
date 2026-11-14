from __future__ import annotations

from decimal import Decimal
from ..._decimal import decimal_in, decimal_out

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.transaction_treatment_source import check_transaction_treatment_source
from ..models.transaction_treatment_source import TransactionTreatmentSource
from typing import cast


T = TypeVar("T", bound="TransactionTreatment")


@_attrs_define
class TransactionTreatment:
    """
    Attributes:
        affects_closed_period (bool): The row changes a period whose declaration was already due.
        class_ (str): The treatment; only revenue (net of refund_to_customer) feeds the single-tax base.
        confidence (Decimal): 0–1 (three decimals).
        fiscal_receipt_missing (bool):
        fiscal_required (bool): Revenue that needs a fiscal receipt (none linked when `fiscal_receipt_missing`).
        needs_review (bool): The review queue lists it.
        reviewed (bool): Reviewed: a person confirmed or set it.
        source (TransactionTreatmentSource): Who decided it: default_rule, user_rule, linker, ai or user.
        version (int): The treatment's version (its If-Match).
    """

    affects_closed_period: bool
    class_: str
    confidence: Decimal
    fiscal_receipt_missing: bool
    fiscal_required: bool
    needs_review: bool
    reviewed: bool
    source: TransactionTreatmentSource
    version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affects_closed_period = self.affects_closed_period

        class_ = self.class_

        confidence = decimal_out(self.confidence)

        fiscal_receipt_missing = self.fiscal_receipt_missing

        fiscal_required = self.fiscal_required

        needs_review = self.needs_review

        reviewed = self.reviewed

        source: str = self.source

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "affects_closed_period": affects_closed_period,
                "class": class_,
                "confidence": confidence,
                "fiscal_receipt_missing": fiscal_receipt_missing,
                "fiscal_required": fiscal_required,
                "needs_review": needs_review,
                "reviewed": reviewed,
                "source": source,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affects_closed_period = d.pop("affects_closed_period")

        class_ = d.pop("class")

        confidence = decimal_in(d.pop("confidence"))

        fiscal_receipt_missing = d.pop("fiscal_receipt_missing")

        fiscal_required = d.pop("fiscal_required")

        needs_review = d.pop("needs_review")

        reviewed = d.pop("reviewed")

        source = check_transaction_treatment_source(d.pop("source"))

        version = d.pop("version")

        transaction_treatment = cls(
            affects_closed_period=affects_closed_period,
            class_=class_,
            confidence=confidence,
            fiscal_receipt_missing=fiscal_receipt_missing,
            fiscal_required=fiscal_required,
            needs_review=needs_review,
            reviewed=reviewed,
            source=source,
            version=version,
        )

        transaction_treatment.additional_properties = d
        return transaction_treatment

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
