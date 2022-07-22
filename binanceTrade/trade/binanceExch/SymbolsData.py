import time

from trade.binanceExch import Client, enums
from trade.binanceExch.indicators.MA import MA

from functools import reduce
import pandas as pd

"""
class SymbolsTFData
- при обращении к def get_all_indexpower и def get_indexpower проверять актуальность уже имеющихся данных
    и уменьшить количество обращений к серверу  Binance
- добавить обновление данных через websocket
- 
"""
class SymbolsTFData:
    client = Client(test_mode=False)

    def __init__(self, interval: str, short=5, middle=13, long=34, limit=500):
        if interval not in enums.INTERVALS:
            raise Exception("Incorrect parameter <interval>")
        self._interval = interval

        if not all([isinstance(short, int), isinstance(middle, int), isinstance(long, int), isinstance(limit, int)]):
            raise Exception("Parameters <short>, <middle> and <long> must be int")
        self._short = short
        self._middle = middle
        self._long = long
        self._limit = limit

        # {symbol: {
        #     'time': time.time()*1000,
        #     'data': pd.DataFrame()
        # }}
        self._dataframes = {}
        self._idx_dataframes = {}

        ls = reduce(
            lambda x, y: x + y,
            enums.IDX_COIN.values()
        )
        smbls = list(set(ls))
        self._symbols = list(set(smbls))

        self._columns = ['Open_time', 'ma_power_' + str(self._short), 'ma_power_' + str(self._middle),
                         'ma_power_' + str(self._long)]
        # self._columns=['Open time', 'ma_'+str(self._short), 'ma_'+str(self._middle), 'ma_'+str(self._long), 'ma_power_'+str(self._short), 'ma_power_'+str(self._middle), 'ma_power_'+str(self._long)]

    def get_all_indexpower(self):
        for idxname in enums.IDX_COIN.keys():
            idx = self.get_indexpower(idxname)
            self._idx_dataframes[idxname] = {'time': int(time.time()) * 1000, 'data': idx.get(idxname)}

        return self._idx_dataframes

    def get_indexpower(self, idxname: str):
        """
        Return dictionary {idxname: pandas.DataFrame}

        Желательно добавить защиту от пустых DataFrame при расчете индекса
        """
        if idxname not in enums.IDX_COIN:
            raise Exception('Incorrect parameter <idxname> of get_indexpower() function')

        symbols = enums.IDX_COIN.get(idxname)
        idxset = {}
        for symbol in symbols:
            idxset.update(self.get_symbolpower(symbol))

        coin = idxname[3:]
        idx = pd.DataFrame(columns=self._columns)
        idx = idx.set_index('Open_time')
        for symbol, df in idxset.items():
            df = df.set_index('Open_time')
            if symbol.startswith(coin):
                idx = idx.add(df, fill_value=0)
            else:
                df = df.div(-1)
                idx = idx.add(df, fill_value=0)

        idx = idx.div(len(symbols))
        idx = idx.reset_index()

        return {idxname: idx}

    def get_symbolpower(self, symbol):
        """
        Function return <SymbolPower> by one pair (<symbol>) from self._dataframes or
        recalculate data in  self._load_symbol_data() if data dataframe oldest 3 minutes
        """
        if symbol not in self._symbols:
            raise Exception(f'No data for symbol {symbol}')

        if self._dataframes.get(symbol) is None:
            self._load_symbol_data(symbol)

        time_now = int(time.time()) * 1000
        time_df = self._dataframes.get(symbol).get('time')

        # if data in df oldest 3 minutes recall data from server
        if time_now > time_df + 3 * 60 * 1000:
            self._load_symbol_data(symbol)
            df = self._dataframes.get(symbol).get('data')
        else:
            df = self._dataframes.get(symbol).get('data')

        df = df[self._columns]

        return {symbol: df}

    def _load_all_data(self, smbls=None):
        symbols = self._symbols if smbls is None else smbls
        for symbol in symbols:
            self._load_symbol_data(symbol)

    def _load_symbol_data(self, symbol):
        """
        For all in symbols
        Take data from Binance.
        Add Columns ma_ and ma_diff_
        Save all in dict _dataframes = {symbol: pd.DataFrame}
        """
        df = self._get_klines(symbol)

        self._add_columns_ma_power(df, self._short)
        self._add_columns_ma_power(df, self._middle)
        self._add_columns_ma_power(df, self._long)

        self._dataframes[symbol] = {'time': int(time.time()) * 1000, 'data': df}

    def _add_columns_ma_power(self, df, ma_period, prefix='ma_', column_price='Close'):
        # add MA column
        column_ma = prefix + str(ma_period)
        df.loc[0, column_ma] = df.loc[0, column_price]
        for i in range(1, len(df)):
            df.loc[i, column_ma] = MA.ema(df.loc[i, column_price], df.loc[i - 1, column_ma], ma_period)

        # add MA_DIFF column
        column_power = prefix + 'power_' + str(ma_period)
        df[column_power] = MA.ema_power(df[column_ma].shift(1), df[column_ma])

    def _get_klines(self, symbol, lim=None):
        """
        Load klines data from server for <symbol> and <self._interval>
        Converts object(string) data to numeric
        return pandas.DataFrame()
        """
        limit = self._limit if lim is None else lim

        columns = ['Open_time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close_time', 'Qt_asset_vol',
                   'Num_of_trades', 'Base_vol', 'Qt_vol', 'Ignr']

        df = pd.DataFrame(self.client.klines(symbol, self._interval, limit=limit), columns=columns)

        df['Close'] = df['Close'].astype('float')
        df['Open'] = df['Open'].astype('float')
        df['High'] = df['High'].astype('float')
        df['Low'] = df['Low'].astype('float')
        df['Volume'] = df['Volume'].astype('float')
        df['Qt_asset_vol'] = df['Qt_asset_vol'].astype('float')
        df['Base_vol'] = df['Base_vol'].astype('float')
        df['Qt_vol'] = df['Qt_vol'].astype('float')
        time.sleep(.5)

        return df