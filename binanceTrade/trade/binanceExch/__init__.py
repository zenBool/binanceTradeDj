import os

from binance.spot import Spot


class Client(Spot):
    """
    It's custom Spot client
    """
    def __init__(self, key=None, secret=None, test_mode=True, **kwargs):
        if test_mode:
            kwargs["base_url"] = 'https://testnet.binance.vision'
        else:
            kwargs["base_url"] = self._server_choice()
            if key is None:
                key = os.getenv("BINANCE_API_KEY")
            if secret is None:
                secret = os.getenv("BINANCE_API_SECRET")

        super().__init__(key, secret, **kwargs)

    def _server_choice(self):
        """
        Server choice

        ! Implement later
        """
        return "https://api2.binance.com"

    def margin_account(self):
        """Remove don't use assets"""
        margin = super().margin_account()
        assets = [el for el in margin["userAssets"] if (el['free'] != '0' or \
                                                        el['locked'] != '0' or \
                                                        el['borrowed'] != '0' or \
                                                        el['interest'] != '0' or \
                                                        el['netAsset'] != '0')]
        margin["userAssets"] = assets

        return margin
