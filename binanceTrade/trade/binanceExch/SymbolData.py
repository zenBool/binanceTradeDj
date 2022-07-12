import pandas as pd

from binance.websocket.spot.websocket_client import SpotWebsocketClient as WSClient
from . import Client

class SymbolTFData:
    _symbol: str
    _period: str
    _df: pd.DataFrame
    client = Client()

    def __init__(self, symbol: str, period: str):
        self._symbol = symbol.lower()
        self._period = period

    def __str__(self):
        return f'{self._symbol}_{self._period}'
