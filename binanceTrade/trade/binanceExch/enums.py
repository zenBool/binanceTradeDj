from datetime import *

YEARS = ['2018', '2019', '2020', '2021', '2022']
INTERVALS = ["1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "12h", "1d", "3d", "1w", "1mo"]
DAILY_INTERVALS = ["1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "12h", "1d"]
TRADING_TYPE = ["spot", "um", "cm"]
MONTHS = list(range(1,13))
MAX_DAYS = 35
BASE_URL = 'https://data.binance.vision/'
START_DATE = date(int(YEARS[0]), MONTHS[0], 1)
END_DATE = datetime.date(datetime.now())
TIME_INTERVALS = {
    "1m": 1000 * 60,
    "3m": 1000 * 60 * 3,
    "5m": 1000 * 60 * 5,
    "15m": 1000 * 60 * 15,
    "30m": 1000 * 60 * 30,
    "1h": 1000 * 60 * 60,
    "2h": 1000 * 60 * 60 * 2,
    "4h": 1000 * 60 * 60 * 4,
    "6h": 1000 * 60 * 60 * 6,
    "8h": 1000 * 60 * 60 * 8,
    "12h": 1000 * 60 * 60 * 12,
    "1d": 1000 * 60 * 60 * 24,
    "3d": 1000 * 60 * 60 * 24 * 3,
    "1w": 1000 * 60 * 60 * 24 * 7
}
SYMBOLS = ('BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'SOLUSDT', 'ADAUSDT', 'XRPUSDT', 'LUNAUSDT',
           'DOTUSDT', 'AVAXUSDT', 'DOGEUSDT', 'SHIBUSDT', 'MATICUSDT', 'LINKUSDT', 'UNIUSDT',
           'ALGOUSDT', 'LTCUSDT', 'NEARUSDT', 'ATOMUSDT', 'BCHUSDT', 'ICPUSDT', 'TRXUSDT',
           'XLMUSDT', 'FTMUSDT', 'MANAUSDT', 'FTTUSDT', 'VETUSDT', 'HBARUSDT', 'FILUSDT',
           'AXSUSDT', 'SANDUSDT', 'THETAUSDT', 'EGLDUSDT', 'ETCUSDT', 'XTZUSDT', 'HNTUSDT',
           'ONEUSDT', 'KLAYUSDT', 'XMRUSDT', 'IOTAUSDT', 'AAVEUSDT', 'CAKEUSDT', 'GRTUSDT',
           'EOSUSDT', 'STXUSDT', 'FLOWUSDT', 'BTTCUSDT', 'GALAUSDT', 'CRVUSDT', 'LRCUSDT',
           'KSMUSDT', 'MKRUSDT', 'QNTUSDT', 'RUNEUSDT', 'ENJUSDT', 'ZECUSDT', 'AMPUSDT',
           'CELOUSDT', 'XECUSDT', 'ARUSDT', 'NEOUSDT', 'CHZUSDT', 'BATUSDT', 'DASHUSDT',
           'WAVESUSDT', 'TUSDUSDT', 'COMPUSDT', 'YFIUSDT', 'ROSEUSDT', 'MINAUSDT', 'HOTUSDT',
           'RVNUSDT', 'XEMUSDT', 'IOTXUSDT', '1INCHUSDT', 'SCRTUSDT', 'SUSHIUSDT', 'TFUELUSDT',
           'GNOUSDT', 'BNTUSDT', 'LPTUSDT', 'WAXPUSDT', 'KDAUSDT', 'BTTUSDT', 'DAIUSDT', 'USDPUSDT',
           'ETHBTC', 'BNBBTC', 'SOLBTC', 'ADABTC', 'XRPBTC', 'DOTBTC', 'AVAXBTC', 'DOGEBTC',
           'SHIBBTC', 'MATICBTC', 'LINKBTC', 'UNIBTC', 'ALGOBTC', 'LTCBTC', 'NEARBTC', 'ATOMBTC',
           'BCHBTC', 'ICPBTC', 'TRXBTC', 'XLMBTC', 'FTMBTC', 'MANABTC', 'FTTBTC', 'VETBTC',
           'HBARBTC', 'FILBTC', 'AXSBTC', 'EOSBTC', 'MKRBTC', 'BNBETH', 'SOLETH', 'ADAETH',
           'XRPETH', 'DOTETH', 'AVAXETH', 'MATICETH', 'LTCETH', 'SOLBNB', 'ADABNB', 'XRPBNB',
           'DOTBNB', 'AVAXBNB', 'MATICBNB', 'LTCBNB', 'TRXBTC', 'TRXETH', 'TRXBNB'
           )
IDX_COIN = {'idxusdt': ('BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'SOLUSDT', 'ADAUSDT', 'XRPUSDT', 'DOTUSDT',
                       'AVAXUSDT', 'MATICUSDT', 'LTCUSDT'),
            'idxbtc': ('TRXBTC', 'ETHBTC', 'BNBBTC', 'SOLBTC', 'ADABTC', 'XRPBTC', 'DOTBTC', 'AVAXBTC',
                       'MATICBTC', 'LTCBTC'),
            'idxbnb': ('TRXBNB', 'BNBETH', 'BNBBTC', 'SOLBNB', 'ADABNB', 'XRPBNB', 'DOTBNB', 'AVAXBNB',
                       'MATICBNB', 'LTCBNB'),
            'idxeth': ('TRXETH', 'ETHBTC', 'BNBETH', 'SOLETH', 'ADAETH', 'XRPETH', 'DOTETH', 'AVAXETH',
                       'MATICETH', 'LTCETH'),
            'idxsol': ('SOLBTC', 'SOLETH', 'SOLBNB'),
            'idxada': ('ADABTC', 'ADAETH', 'ADABNB'),
            'idxxrp': ('XRPBTC', 'XRPETH', 'XRPBNB'),
            'idxdot': ('DOTBTC', 'DOTETH', 'DOTBNB'),
            'idxavax': ('AVAXBTC', 'AVAXETH', 'AVAXBNB'),
            'idxmatic': ('MATICBTC', 'MATICETH', 'MATICBNB'),
            'idxltc': ('LTCBTC', 'LTCETH', 'LTCBNB'),
            'idxtrx': ('TRXBTC', 'TRXETH', 'TRXBNB'),
            }
IDX_USD30 = {'idxusdt30': ('BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'SOLUSDT', 'ADAUSDT', 'XRPUSDT', 'DOTUSDT',
                          'AVAXUSDT', 'DOGEUSDT', 'SHIBUSDT', 'MATICUSDT', 'LINKUSDT', 'UNIUSDT', 'ALGOUSDT',
                          'LTCUSDT', 'NEARUSDT', 'ATOMUSDT', 'BCHUSDT', 'ICPUSDT', 'TRXUSDT', 'XLMUSDT',
                          'FTMUSDT', 'MANAUSDT', 'FTTUSDT', 'VETUSDT', 'HBARUSDT', 'FILUSDT', 'AXSUSDT',
                          'EOSUSDT', 'MKRUSDT'
                          )}
IDX_BTC30 = {'idxbtc30': ('BTCUSDT', 'ETHBTC', 'BNBBTC', 'SOLBTC', 'ADABTC', 'XRPBTC', 'DOTBTC', 'AVAXBTC',
                          'DOGEBTC', 'SHIBBTC', 'MATICBTC', 'LINKBTC', 'UNIBTC', 'ALGOBTC', 'LTCBTC', 'NEARBTC',
                          'ATOMBTC', 'BCHBTC', 'ICPBTC', 'TRXBTC', 'XLMBTC', 'FTMBTC', 'MANABTC', 'FTTBTC',
                          'VETBTC', 'HBARBTC', 'FILBTC', 'AXSBTC', 'EOSBTC', 'MKRBTC'
                          )}


if __name__ == '__main__':
    print([sym for sym in IDX_BTC30['idxbtc30'] if sym not in SYMBOLS])
