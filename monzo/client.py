import os
from typing import Dict, List, Optional

import requests

from monzo.types import Account, AccountId, Transaction, structure

AccessToken = str


class Client:
    def __init__(self, *, base_url: str, token: AccessToken) -> None:
        # TODO: validate url is valid
        self.base_url = base_url

        session = requests.Session()
        session.headers.update({"Authorization": f"Bearer {token}"})
        self._session = session

    def get(self, path: str, **kwargs: Dict) -> Dict:
        response = self._session.get(url=f"{self.base_url}/{path}", **kwargs)
        response.raise_for_status()
        return response.json()

    def post(self, path: str, **kwargs: Dict) -> Dict:
        response = self._session.post(url=f"{self.base_url}/{path}", **kwargs)
        response.raise_for_status()
        return response.json()


class MonzoClient(Client):
    def __init__(self, *, token: AccessToken) -> None:
        self._client = Client(base_url=os.environ["MONZO_API"], token=token)

    def get_accounts(self) -> List[Account]:
        data = self._client.get("accounts")
        return structure(data["accounts"], List[Account])

    def get_transactions(
        self, *, account_id: AccountId, limit: Optional[int] = None
    ) -> List[Transaction]:
        params = {"account_id": account_id}
        if limit:
            params.update({"limit": str(limit)})
        data = self._client.get("transactions", params=params)

        return data["transactions"]
