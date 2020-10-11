import datetime

from monzo.types import Account, Transaction, structure


def test_structure_account():
    data = {
        "id": "acc_00009DdqlDwFBomf84rllJ",
        "closed": True,
        "created": "2013-10-24T12:14:44.956Z",
        "description": "user_00009DNG86t3UFxodPz2PZ",
        "type": "uk_prepaid",
        "currency": "GBP",
        "country_code": "GB",
        "owners": [
            {
                "user_id": "user_00009DNG86t3UFxodPz2PZ",
                "preferred_name": "John Doe",
                "preferred_first_name": "John",
            },
        ],
    }

    account = structure(data, Account)

    assert account.created.isoformat() == "2013-10-24T12:14:44.956000"

    assert account == Account(
        id="acc_00009DdqlDwFBomf84rllJ",
        closed=True,
        created=datetime.datetime(2013, 10, 24, 12, 14, 44, 956000),
        description="user_00009DNG86t3UFxodPz2PZ",
        type="uk_prepaid",
        currency="GBP",
        country_code="GB",
        owners=[
            {
                "user_id": "user_00009DNG86t3UFxodPz2PZ",
                "preferred_name": "John Doe",
                "preferred_first_name": "John",
            },
        ],
    )


def test_structure_transaction():
    data = {
        "id": "tx_0000B02xeFCtqusyW6yKLR",
        "created": "2020-10-11T08:40:33.806Z",
        "description": "LUCIA COFFEE HOUSE     LONDON  N22   GBR",
        "amount": -2180,
        "fees": {},
        "currency": "GBP",
        "merchant": "merch_00009dJsgV0VotW3KBPyC1",
        "notes": "Yummy breakfast\n#social",
        "metadata": {
            "ledger_insertion_id": "entryset_0000A02xeDrwpKU0LHtIKg",
            "mastercard_approval_type": "full",
            "mastercard_auth_message_id": "mcauthmsg_0000A02xeDHR15pzfjY8pd",
            "mastercard_card_id": "mccard_00009lmDABsdIyGQHCOwqX",
            "mastercard_lifecycle_id": "mclifecycle_0000A02xeDZruY1NRDQr9V",
            "mcc": "5812",
            "notes": "Yummy breakfast\n#social",
        },
        "labels": None,
        "attachments": [],
        "international": None,
        "category": "eating_out",
        "categories": {"eating_out": -2180},
        "is_load": False,
        "settled": "",
        "local_amount": -2180,
        "local_currency": "GBP",
        "updated": "2020-10-11T09:28:36.509Z",
        "account_id": "acc_00009DdqlDwFBomf84rllJ",
        "user_id": "user_00009DNG86t3UFxodPz2PZ",
        "counterparty": {},
        "scheme": "mastercard",
        "dedupe_id": "mclifecycle:mclifecycle_0000A02xeDZruY1NRDQr9V:MASTERCARD_AUTH:mcauthmsg_0000A02xeDHR15pzfjY8pd",  # noqa
        "originator": False,
        "include_in_spending": True,
        "can_be_excluded_from_breakdown": True,
        "can_be_made_subscription": True,
        "can_split_the_bill": True,
        "can_add_to_tab": True,
        "amount_is_pending": False,
        "atm_fees_detailed": None,
    }

    transaction = structure(data, Transaction)

    assert transaction == Transaction(
        id="tx_0000B02xeFCtqusyW6yKLR",
        created=datetime.datetime(2020, 10, 11, 8, 40, 33, 806000),
        description="LUCIA COFFEE HOUSE     LONDON  N22   GBR",
        amount=-2180,
        currency="GBP",
        merchant="merch_00009dJsgV0VotW3KBPyC1",
        notes="Yummy breakfast\n#social",
        category="eating_out",
        account_id="acc_00009DdqlDwFBomf84rllJ",
    )
