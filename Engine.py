#!python


class Engine:

    def __init__(self):

        import os
        import oandapyV20
        from oandapyV20 import API

        password = os.environ.get("Your_API_Key")
        user_name = os.environ.get("Your_Oanda_Account")

        api = API(access_token=password)
        accountID = user_name

        self.client = oandapyV20.API(access_token=password)

        self.open_prices = []
        self.high_prices = []
        self.low_prices = []
        self.close_prices = []
        self.date_time = []

        self.forex_pairs = []
        self.forex_pairs_no_jpy = []

        self.red_green_candles = []
        self.candles_size = []

        self.forex_pairs = ["AUD_CAD", "AUD_CHF", "AUD_JPY", "AUD_NZD", "AUD_USD", "AUD_SGD", "CAD_CHF", "CAD_JPY",
                            "CAD_SGD", "CHF_JPY",
                            "EUR_AUD", "EUR_CAD", "EUR_JPY", "EUR_NZD", "EUR_CHF", "EUR_GBP", "EUR_SGD", "EUR_USD",
                            "GBP_AUD", "GBP_CAD", "GBP_JPY", "GBP_NZD", "GBP_USD",
                            "NZD_CAD", "NZD_CHF", "NZD_JPY", "NZD_SGD", "NZD_USD", "SGD_CHF", "SGD_JPY", "USD_CAD",
                            "USD_CHF", "USD_JPY", "USD_SGD", ]

        self.forex_pairs_no_jpy = ["AUD_CAD", "AUD_CHF", "AUD_NZD", "AUD_USD", "AUD_SGD", "CAD_CHF", "CAD_SGD",
                                   "EUR_AUD", "EUR_CAD", "EUR_NZD", "EUR_SGD", "EUR_USD", "GBP_AUD", "GBP_CAD",
                                   "GBP_NZD", "GBP_USD",
                                   "NZD_CAD", "NZD_CHF", "NZD_SGD", "NZD_USD", "SGD_CHF", "USD_CAD", "USD_CHF",
                                   "USD_SGD", ]

    # *****************************************************************************************************************

    def historical_klines(self, forex_pair, num_of_candles, interval):

        import oandapyV20.endpoints.instruments as instruments

        parameters = {"count": num_of_candles, "granularity": interval}
        r = instruments.InstrumentsCandles(instrument=forex_pair, params=parameters)
        self.client.request(r)
        forex_pair_data_raw = r.response

        # OHLC
        flag_historical = True
        idx_historical = 0

        while flag_historical:

            self.open_prices.append(float(forex_pair_data_raw["candles"][idx_historical]["mid"]["o"]))
            self.high_prices.append(float(forex_pair_data_raw["candles"][idx_historical]["mid"]["h"]))
            self.low_prices.append(float(forex_pair_data_raw["candles"][idx_historical]["mid"]["l"]))
            self.close_prices.append(float(forex_pair_data_raw["candles"][idx_historical]["mid"]["c"]))

            self.date_time.append(forex_pair_data_raw["candles"][idx_historical]["time"][: -11])

            if idx_historical == num_of_candles - 1:
                flag_historical = False

            idx_historical += 1

        self.red_green_candles = ["Green" if x[0] < x[1] else "Red" for x in zip(self.open_prices, self.close_prices)]

        self.candles_size = [round((((x[1] - x[0]) * 100) / x[0]), 3) for x in zip(self.open_prices, self.close_prices)]

