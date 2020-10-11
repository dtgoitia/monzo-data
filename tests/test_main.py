import os

import pytest

from monzo.client import MonzoClient
from monzo.types import Transaction


@pytest.mark.skip
def test_integration():
    token = os.environ["MONZO_ACCESS_TOKEN"]
    client = MonzoClient(token=token)
    accounts = client.get_accounts()

    account = next(
        account
        for account in accounts
        if account.closed is False and len(account.owners) == 1
    )

    transactions = client.get_transactions(account_id=account.id, limit=2)

    assert len(transactions) == 2
    assert type(transactions[0]) == Transaction
