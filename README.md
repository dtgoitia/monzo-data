## Python version

This project has been developed using Python `3.8.5`.

## Configuration

Set the following environment variables:

* `MONZO_API`: `https://api.monzo.com`
* `MONZO_AUTH_API`: `https://auth.monzo.com`
* `MONZO_CLIENT_ID`: [_Monzo Developers Portal_][1] > _Clients_ > `monzo-data` > `Client ID`.
* `MONZO_CLIENT_SECRET`: [_Monzo Developers Portal_][1] > _Clients_ > `monzo-data` > `Client secret`.
* `MONZO_ACCESS_TOKEN`: [_Monzo Developers Portal_][1] > _Playground_ > `Access token`.

[1]: https://docs.monzo.com/#refreshing-access "Monzo Developers Portal"

TODO:

- Get a [_refresh token_](https://docs.monzo.com/#refreshing-access) and obtain an _access token_ on the go on each CLI execution.
- [Invalidate](https://docs.monzo.com/#log-out) each _access token_ before completing every CLI execution.
