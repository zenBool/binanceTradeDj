## Installing the dependencies

`pip install -r requirements.txt`

## Running the scripts

`export STORE_DIRECTORY=<your desired path>`

This will configure the default storing directory of the downloaded data. This can be 
overwritten <br/> by setting an argument(example given below). 

### Download klines
`python3 download-kline.py -t <market_type>` <br/>

Running this command will download all available monthly and daily **spot**, **USD-M Futures** or **COIN-M Futures** kline data for all symbols and intervals. 

#### Running with arguments

These are the available arguments that can be used when running `download-kline.py`<br>
Some arguments come with a default value if not declared.

| Argument        | Explanation | Default | Mandatory |      
| :---------------: | ---------------- | :----------------: | :----------------: |
| -t              | Market type: **spot**, **um** (USD-M Futures), **cm** (COIN-M Futures) | spot | Yes |
| -s              | Single **symbol** or multiple **symbols** separated by space | All symbols | No |
| -i              | single kline **interval** or multiple **intervals** separated by space      | All intervals | No |
| -y              | Single **year** or multiple **years** separated by space| All available years | No |
| -m              | Single **month** or multiple **months** separated by space | All available months | No |
| -d              | single **date** or multiple **dates** separated by space    | All available dates | No |
| -startDate      | **Starting date** to download in [YYYY-MM-DD] format    | - | No |
| -endDate        | **Ending date** to download in [YYYY-MM-DD] format     | - | No |
| -skip-monthly   | 1 to skip downloading of monthly data | 0 | No |
| -skip-daily     | 1 to skip downloading of daily data | 0 | No |
| -folder         | **Directory** to store the downloaded data    | Current directory | No |
| -c              | 1 to download **checksum file** | 0 | No |
| -h              | show help messages| - | No |

#### Example

e.g download ETHUSDT BTCUSDT BNBBUSD spot kline of 1 week interval from year 2020, month of Feb and Dec with CHECKSUM file:<br/>
`python3 download-kline.py -t spot -s ETHUSDT BTCUSDT BNBBUSD -i 1w -y 2020 -m 02 12 -c 1`

e.g download all symbols' daily USD-M futures kline of 1 minute interval from 2021-01-01 to 2021-02-02:
`python3 download-kline.py -t um -i 1m -skip-monthly 1 -startDate 2021-01-01 -endDate 2021-02-02`

### Download trades

`python3 download-trade.py -t <market_type>` <br/>

Running this command will download all available monthly and daily **spot**, **USD-M Futures** or **COIN-M Futures** trade data for all symbols.

#### Running with arguments

These are the available arguments that can be used when running `download-trade.py`<br>
Some arguments come with a default value if not declared.

| Argument        | Explanation | Default | Mandatory |       
| :---------------: | ---------------- | :----------------: | :----------------: |
| -t              | Market type: **spot**, **um** (USD-M Futures), **cm** (COIN-M Futures) | spot | Yes |
| -s              | Single **symbol** or multiple **symbols** separated by space | All symbols | No |
| -y              | Single **year** or multiple **years** separated by space| All available years | No |
| -m              | Single **month** or multiple **months** separated by space | All available months | No |
| -d              | single **date** or multiple **dates** separated by space    | All available dates | No |
| -startDate      | **Starting date** to download in [YYYY-MM-DD] format    | - | No |
| -endDate        | **Ending date** to download in [YYYY-MM-DD] format     | - | No |
| -skip-monthly   | 1 to skip downloading of monthly data | 0 | No |
| -skip-daily     | 1 to skip downloading of daily data | 0 | No |
| -folder         | **Directory** to store the downloaded data    | Current directory | No |
| -c              | 1 to download **checksum file** | 0 | No |
| -h              | show help messages| - | No |

#### Example

e.g download ETHUSDT BTCUSDT BNBBUSD spot trades from year 2020, month of Feb and Dec with CHECKSUM file:<br/>
`python3 download-trade.py -t spot -s ETHUSDT BTCUSDT BNBBUSD -y 2020 -m 02 12 -c 1`

e.g download all symbols' daily USD-M futures trades from 2021-01-01 to 2021-02-02:
`python3 download-trade.py -t um -skip-monthly 1 -startDate 2021-01-01 -endDate 2021-02-02`

### Download aggTrades

`python3 download-aggTrade.py -t <market_type> ` <br/>

Running this command will download all available monthly and daily **spot**, **USD-M Futures** or **COIN-M Futures** aggregated trades data for all symbols.

#### Running with arguments

These are the available arguments that can be used when running `download-aggTrade.py`<br>
Some arguments come with a default value if not declared.

| Argument        | Explanation | Default | Mandatory |       
| :---------------: | ---------------- | :----------------: | :----------------: |
| -t              | Market type: **spot**, **um** (USD-M Futures), **cm** (COIN-M Futures) | spot | Yes |
| -s              | Single **symbol** or multiple **symbols** separated by space | All symbols | No |
| -y              | Single **year** or multiple **years** separated by space| All available years | No |
| -m              | Single **month** or multiple **months** separated by space | All available months | No |
| -d              | single **date** or multiple **dates** separated by space    | All available dates | No |
| -startDate      | **Starting date** to download in [YYYY-MM-DD] format    | - | No |
| -endDate        | **Ending date** to download in [YYYY-MM-DD] format     | - | No |
| -skip-monthly   | 1 to skip downloading of monthly data | 0 | No |
| -skip-daily     | 1 to skip downloading of daily data | 0 | No |
| -folder         | **Directory** to store the downloaded data    | Current directory | No |
| -c              | 1 to download **checksum file** | 0 | No |
| -h              | show help messages| - | No |

#### Example

e.g download ETHUSDT BTCUSDT BNBBUSD spot aggTrades from year 2020, month of Feb and Dec with CHECKSUM file:<br/>
`python3 download-aggTrade.py -t spot -s ETHUSDT BTCUSDT BNBBUSD -y 2020 -m 02 12 -c 1`

e.g download all symbols' daily USD-M futures aggTrades from 2021-01-01 to 2021-02-02:
`python3 download-aggTrade.py -t um -skip-monthly 1 -startDate 2021-01-01 -endDate 2021-02-02`


### Futures-Only Data 

The 3 scripts below are only used for futures klines data.

`python3 download-futures-indexPriceKlines.py -t <market_type>` <br/>
`python3 download-futures-markPriceKlines.py -t <market_type>` <br/>
`python3 download-futures-premiumPriceKlines.py -t <market_type>` 

#### Running with arguments

These are the available arguments that can be used when running the scripts.<br>
**`-t`, type,  is a mandatory argument which consist of 2 different futures type: `um`, `cm`**. Some arguments come with a default value if not declared.

| Argument        | Explanation | Default | Mandatory |      
| :---------------: | ---------------- | :----------------: | :----------------: |
| -t              | Market type: **um** (USD-M Futures), **cm** (COIN-M Futures)| - | Yes |
| -s              | Single **symbol** or multiple **symbols** separated by space | All symbols | No |
| -i              | single kline **interval** or multiple **intervals** separated by space      | All intervals | No |
| -y              | Single **year** or multiple **years** separated by space| All available years | No |
| -m              | Single **month** or multiple **months** separated by space | All available months | No |
| -d              | single **date** or multiple **dates** separated by space    | All available dates | No |
| -startDate      | **Starting date** to download in [YYYY-MM-DD] format    | - | No |
| -endDate        | **Ending date** to download in [YYYY-MM-DD] format     | - | No |
| -skip-monthly   | 1 to skip downloading of monthly data | 0 | No |
| -skip-daily     | 1 to skip downloading of daily data | 0 | No |
| -folder         | **Directory** to store the downloaded data    | Current directory | No |
| -c              | 1 to download **checksum file** | 0 | No |
| -h              | show help messages| - | No |

e.g download Futures BTCUSDT USD-M indexPriceKlines
`python3 download-futures-indexPriceKlines.py -t um -s BTCUSDT`

e.g download ETHUSDT BTCUSDT BNBUSDT USD-M markPriceKlines of 1 week from year 2020, month of Feb and Dec with CHECKSUM file:<br/>
`python3 download-futures-markPriceKlines.py -t um -s ETHUSDT BTCUSDT BNBUSDT -i 1w -y 2020 -m 02 12 -c 1`

e.g download all symbols' daily COIN-M premiumPriceKlines of 1 minute interval from 2021-01-01 to 2021-02-02:
`python3 download-futures-premiumPriceKlines.py -t cm -skip-monthly 1 -i 1m  -startDate 2021-01-01 -endDate 2021-02-02`
# Binance Public Data

To help users download our public data easily, we've put all Kline, Trade, and AggTrade data for all pairs, month by month, online.


## What data is available

We provide both `daily` and `monthly` intervals for each data. `daily` data will be uploaded in the next day, and we start to upload `monthly` data from the beginning of next month.

### SPOT

* `AggTrades`
* `Klines`
* `Trades`


#### AggTrades
The aggTrades is downloaded from `/api/v3/aggTrades` and the title for each column:

|Aggregate tradeId|Price|Quantity|First tradeId|Last tradeId|Timestamp|Was the buyer the maker|Was the trade the best price match|
| -- | -- | -- | -- | -- | -- | -- | -- |
|0|0.20000000|50.00000000|0|0|1608872400000|False|True|

#### Klines
The klines data is downloaded from `/api/v3/klines` and the title for each column in the kline data:

|Open time|Open|High|Low|Close|Volume|Close time|Quote asset volume|Number of trades|Taker buy base asset volume|Taker buy quote asset volume|Ignore|
| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
|1601510340000|4.15070000|4.15870000|4.15060000|4.15540000|539.23000000|1601510399999|2240.39860900|13|401.82000000|1669.98121300|0|

#### Trades
The trades data is downloaded from `/api/v3/historicalTrades`, the title for each column in the trades data:
|trade Id| price| qty|quoteQty|time|isBuyerMaker|isBestMatch|
| -- | -- | -- | -- | -- | -- | -- |
|51175358|17.80180000|5.69000000|101.29224200|1583709433583|True|True|



### FUTURES
* USD-M Futures
* COIN-M Futures

#### AggTrades
The aggTrades is same as `/fapi/v1/aggTrades`, `/dapi/v1/aggTrades` and the title for each column:

|Aggregate tradeId|Price|Quantity|First tradeId|Last tradeId|Timestamp|Was the buyer the maker|
| -- | -- | -- | -- | -- | -- | -- |
|26129|0.01633102|4.70443515|27781|27781|1498793709153|true|

#### Klines
The klines data is same as `/fapi/v1/klines`, `/dapi/v1/klines` and the title for each column:

USD-M Futures

|Open time|Open|High|Low|Close|Volume|Close time|Quote asset volume|Number of trades|Taker buy base asset volume|Taker buy quote asset volume|Ignore|
| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
|1499040000000|0.01634790|0.80000000|0.01575800|0.01577100|148976.11427815|1499644799999|2434.19055334|308|1756.87402397|28.46694368|17928899.62484339|

COIN-M Futures

|Open time|Open|High|Low|Close|Volume|Close time|Base asset volume|Number of trades|Taker buy volume|Taker buy base asset volume|Ignore|
| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
|1591258320000|9640.7|9642.4|9640.6|9642.0|206|1591258379999|2.13660389|48|119|1.23424865|0|

#### Trades
The trades data is same as `/fapi/v1/trades`, `/dapi/v1/trades`, the title for each column:

USD-M Futures

|trade Id| price| qty|quoteQty|time|isBuyerMaker|
| -- | -- | -- | -- | -- | -- |
|28457|4.00000100|12.00000000|48.00|1499865549590|true|

COIN-M Futures

|trade Id| price| qty|baseQty|time|isBuyerMaker|
| -- | -- | -- | -- | -- | -- |
|28457|9635.0|1|0.01037883|1591250192508|true|

## Where do I access it

The base url is `https://data.binance.vision` and you can use your browser to view and download the data.

### Klines

All symbols are supported, the file format is:<br/>
`<base_url>/data/spot/monthly/klines/<symbol_in_uppercase>/<interval>/<symbol_in_uppercase>-<interval>-<year>-<month>.zip`<br/><br/>
e.g. the url for BNBUSDT 1m klines for 2019-01 is:<br/>
`https://data.binance.vision/data/spot/monthly/klines/BNBUSDT/1m/BNBUSDT-1m-2019-01.zip`


#### Intervals

All intervals are supported: 
`1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1mo`
- `1mo` is used instead of `1M` to supprt non-case sensitive file systems.

### Trades

All symbols are supported, the file format is:<br/>
`<base_url>/data/spot/monthly/trades/<symbol_in_uppercase>/<symbol_in_uppercase>-trades-<year>-<month>.zip`<br/><br/>
e.g. the url BNBUSDT trades in 2019-01 is:<br/>
`https://data.binance.vision/data/spot/monthly/trades/BNBUSDT/BNBUSDT-trades-2019-01.zip`

### AggTrades

This section will be updated when the data is uploaded.


## How to download programatically

```shell

# download a single file
curl -s "https://data.binance.vision/data/spot/monthly/klines/ADABKRW/1h/ADABKRW-1h-2020-08.zip" -o ADABKRW-1h-2020-08.zip
wget "https://data.binance.vision/data/spot/monthly/klines/ADABKRW/1h/ADABKRW-1h-2020-08.zip"
```

We will expand this section with more methods in the future.

There are additional helper scripts both in python and shell in their respective folders of this repository.

## CHECKSUM
Each zip file has a `.CHECKSUM` file together in the same folder to verify data integrity.

To Check:

```shell
# From Linux, sha256sum -c <zip_file_name.CHECKSUM>
sha256sum -c BNBUSDT-1m-2021-01.zip.CHECKSUM

# From MacOS
shasum -a 256 -c BNBUSDT-1m-2021-01.zip.CHECKSUM
```


## I have an issue/question

Please open an issue [here](https://github.com/binance/binance-public-data/issues). 

## Licence
MIT
