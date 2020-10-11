import datetime
from typing import Any, Dict, List

import attr
import cattr

AccountId = str
MerchantId = str
TransactionId = str


@attr.s(auto_attribs=True, frozen=True)
class Account:
    id: AccountId
    closed: bool
    created: datetime.datetime
    description: str
    type: str
    currency: str
    country_code: str
    owners: List[Dict]


@attr.s(auto_attribs=True, frozen=True)
class Transaction:
    id: TransactionId
    created: datetime.datetime
    description: str
    amount: int
    currency: str
    merchant: MerchantId
    notes: str
    category: str
    account_id: AccountId


converter = cattr.Converter()
structure = converter.structure
unstructure = converter.unstructure


def structure_datetime(timestamp: str, _: Any) -> datetime.datetime:
    # timestamp: 2020-10-11T20:46:06.619Z
    timestamp_with_microseconds = timestamp.replace("Z", "000")
    return datetime.datetime.fromisoformat(timestamp_with_microseconds)


converter.register_structure_hook(datetime.datetime, structure_datetime)
