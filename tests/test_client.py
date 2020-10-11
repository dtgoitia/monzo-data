from unittest.mock import MagicMock

from monzo.client import Client


def test_client_base_url_get():
    client = Client(base_url="http://foo.com/bar", token="baz")
    mock_session = MagicMock()
    client._session = mock_session

    client.get("bubu")

    mock_session.get.assert_called_once_with(url="http://foo.com/bar/bubu")


def test_client_base_url_post():
    client = Client(base_url="http://foo.com/bar", token="baz")
    mock_session = MagicMock()
    client._session = mock_session

    client.post("bubu")

    mock_session.post.assert_called_once_with(url="http://foo.com/bar/bubu")
