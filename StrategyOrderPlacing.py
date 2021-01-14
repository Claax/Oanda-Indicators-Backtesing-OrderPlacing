#!python


"""
THIS IS NOT ONE OF MY STRATEGIES NOR IS PROFITABLE - IT'S JUST TO SHOW YOU HOW I BUILT THE PLACING ORDER SYSTEM
"""

class Claax1:
    forex_pairs = ["AUD_CAD", "AUD_CHF", "AUD_HKD", "AUD_JPY", "AUD_NZD", "AUD_SGD", "AUD_USD",
                   "CAD_CHF", "CAD_HKD", "CAD_JPY", "CAD_SGD",
                   "CHF_HKD", "CHF_JPY",
                   "EUR_AUD", "EUR_CAD", "EUR_CHF", "EUR_HKD", "EUR_JPY", "EUR_NZD", "EUR_GBP", "EUR_SGD", "EUR_USD",
                   "GBP_AUD", "GBP_CAD", "GBP_CHF", "GBP_HKD", "GBP_JPY", "GBP_NZD", "GBP_SGD", "GBP_USD",
                   "NZD_CAD", "NZD_CHF", "NZD_HKD", "NZD_JPY", "NZD_SGD", "NZD_USD",
                   "SGD_CHF", "SGD_HKD", "SGD_JPY",
                   "USD_CAD", "USD_CHF", "USD_JPY", "USD_SGD"]

    # 140 PIPS == 1£
    pairs_units_140 = {'AUD_CAD': -125, 'AUD_CHF': -68, 'AUD_HKD': -68, 'AUD_JPY': -95,
                       'AUD_NZD': -148, 'AUD_SGD': -126, 'AUD_USD': -88,
                       'CAD_CHF': -85, 'CAD_HKD': -68, 'CAD_JPY': -95, 'CAD_SGD': -126,
                       'CHF_HKD': -68, 'CHF_JPY': -95,
                       'EUR_AUD': -140, 'EUR_CAD': -125, 'EUR_HKD': -68, 'EUR_JPY': -95,
                       'EUR_NZD': -148, 'EUR_CHF': -68, 'EUR_GBP': -72, 'EUR_SGD': -126,
                       'EUR_USD': -88, 'GBP_AUD': -140, 'GBP_CAD': -125, 'GBP_CHF': -68, 'GBP_HKD': -68,
                       'GBP_JPY': -95, 'GBP_NZD': -148, 'GBP_SGD': -126, 'GBP_USD': -88,
                       'NZD_CAD': -125, 'NZD_CHF': -68, 'NZD_HKD': -68, 'NZD_JPY': -95,
                       'NZD_SGD': -126, 'NZD_USD': -88,
                       'SGD_CHF': -68, 'SGD_HKD': -68, 'SGD_JPY': -95,
                       'USD_CAD': -125, 'USD_CHF': -68, 'USD_JPY': -95, 'USD_SGD': -126}

    delayed_pairs = []

    def __init__(self):

        import os
        import oandapyV20

        password = os.environ.get("Your_API_Key")
        user_name = os.environ.get("Your_Oanda_Account")

        self.accountID = user_name
        self.client = oandapyV20.API(access_token=password)

        self.ema_60 = []
        self.ema_20 = []

        self.close_prices_60 = []
        self.open_prices_60 = []
        self.low_prices_60 = []
        self.high_prices_60 = []
        self.ema_20_60 = []
        self.date_time_60 = []

        self.open_prices = []
        self.high_prices = []
        self.low_prices = []
        self.close_prices = []
        self.date_time = []
        self.last_candle_time = int()

        self.open_positions = []
        self.unrealised_p_l = 0
        self.account_info = {}

        self.open_positions_for_db = []
        self.account_info_for_db = []
        self.open_positions_records = []
        self.hours_db_records = []
        self.recent_closed_trades = []

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

    def last_candle_time_check(self, forex_pair, interval):

        import oandapyV20.endpoints.instruments as instruments

        parameters = {"count": 1, "granularity": interval}
        r = instruments.InstrumentsCandles(instrument=forex_pair, params=parameters)
        self.client.request(r)
        forex_pair_data_raw = r.response

        if forex_pair_data_raw["candles"][0]["time"][11] != "0":
            self.last_candle_time = int(forex_pair_data_raw["candles"][0]["time"][11:13])
        else:
            self.last_candle_time = int(forex_pair_data_raw["candles"][0]["time"][12])

    def open_positions_info(self):

        import oandapyV20.endpoints.positions as positions

        r_p = positions.OpenPositions(accountID=self.accountID)
        self.client.request(r_p)
        open_pos = r_p.response

        for idx in range(len(open_pos["positions"])):
            self.open_positions.append(open_pos["positions"][idx]["instrument"])

    def account_summary(self):

        import time
        import oandapyV20.endpoints.accounts as accounts

        t = time.gmtime()
        date_time = f"{t[0]}/{t[1]}/{t[2]} - {t[3]}:{t[4]}:{t[5]}"

        r_a = accounts.AccountSummary(accountID=self.accountID)

        self.client.request(r_a)

        a_i = r_a.response

        self.account_info = {"Date & Time": date_time, "Balance": a_i['account']['balance'],
                             "Unrealized P/L": a_i['account']['unrealizedPL'],
                             "Financing": a_i['account']['financing'],
                             "Margin Used": a_i['account']['marginCallPercent'],
                             "Open Positions": a_i['account']['openPositionCount']}

        self.account_info_for_db = [el for el in self.account_info.values()]

    @staticmethod
    def create_data_base():  # ONLY TO RUN ONE TIME

        import sqlite3

        conn = sqlite3.connect("Claax1_Forex_Open_Positions.db")
        open_pos_db = conn.cursor()
        open_pos_db.execute("CREATE TABLE Claax1_Forex_O_P (Date_Time, Open Positions)")
        conn.close()

        conn2 = sqlite3.connect("Claax1_Forex_Account_Summary.db")
        account_info_db = conn2.cursor()
        account_info_db.execute("""CREATE TABLE Claax1_Forex_A_S ( Date_Time, Balance, Unrealized PL, 
                                            Financing, Margin Used, Open Positions )""")
        conn2.close()

        print("DATA BASES CREATED")

    def account_summary_db_writing(self):

        import sqlite3
        self.account_info_for_db = []

        self.account_summary()

        try:

            conn2 = sqlite3.connect("Claax1_Forex_Account_Summary.db")
            acc_info = conn2.cursor()
            acc_info.execute("INSERT INTO Claax1_Forex_A_S VALUES (?, ?, ?, ?, ?, ?)",
                             tuple(self.account_info_for_db))
            conn2.commit()
            conn2.close()

        except:

            print("ERROR MEANWHILE WRITING ACCOUNT INFO")

    @staticmethod
    def account_summary_db_reading():

        import sqlite3

        conn2 = sqlite3.connect("Claax1_Forex_Account_Summary.db")
        acc_info = conn2.cursor()
        for row in acc_info.execute("SELECT * FROM Claax1_Forex_A_S"):
            print(row)
        conn2.close()

    def open_positions_db_writing(self):

        import time
        import sqlite3

        self.open_positions = []
        self.open_positions_for_db = ""

        self.open_positions_info()

        t = time.gmtime()
        date_time = f"{t[0]}/{t[1]}/{t[2]} - {t[3]}:{t[4]}:{t[5]}"

        open_pos_str = ""

        for el in self.open_positions:
            open_pos_str += el + " "

        open_pos_str = open_pos_str[:-1]

        self.open_positions_for_db = [date_time, open_pos_str]

        try:

            conn = sqlite3.connect("Claax1_Forex_Open_Positions.db")
            open_pos = conn.cursor()
            open_pos.execute('INSERT INTO Claax1_Forex_O_P VALUES (?, ?)', tuple(self.open_positions_for_db))
            conn.commit()
            conn.close()

        except:

            print("ERROR MEANWHILE WRITING OPEN POSITIONS")

    @staticmethod
    def open_positions_db_reading():

        import sqlite3

        conn = sqlite3.connect("Claax1_Forex_Open_Positions.db")
        open_pos = conn.cursor()
        for row in open_pos.execute("SELECT * FROM Claax1_Forex_O_P"):
            print(row)
        conn.close()

    def open_positions_db_converting(self):  # CONVERTS THE STRINGS BACK TO LISTS

        import re
        import sqlite3

        self.recent_closed_trades = []

        try:
            conn = sqlite3.connect("Claax1_Forex_Open_Positions.db")
            open_pos = conn.cursor()

            for row in open_pos.execute("SELECT * FROM Claax1_Forex_O_P"):
                self.open_positions_records.append(row[1].split(" "))

                regex = re.compile(r"\s\d{1,2}:")
                mo = regex.search(row[0])
                self.hours_db_records.append(int(mo.group()[1:-1]))

            conn.close()

        except:

            print("ERROR MEANWHILE CONVERTING")

    @staticmethod
    def send_telegram_message(text_to_send):

        import requests
        import json
        import os

        try:

            token = "1217610741:AAE_aUNnfQABvzSrQ6LjgeMHCyf60DGewKc"
            url_api = f'https://api.telegram.org/bot{token}'

            url_message = url_api + "/sendmessage?chat_id={}&text={}".format(1039138030, text_to_send)
            response = requests.get(url_message)
            content = response.content.decode("utf8")
            data_json = json.loads(content)
            print(data_json)

        except:

            print("TELEGRAM CONNECTION PROBLEM")

    # *************************************************************************************************************

    def indicators(self, forex_pair, num_of_candles, interval):

        self.__init__()
        self.historical_klines(forex_pair, num_of_candles, interval)

        # ASSERT
        assert len(self.close_prices) > 60, "NOT ENOUGH CANDLES"

        # EMA 60
        previous_ema = round(sum(self.close_prices[: 60]) / 60, 5)
        k_ema_60 = 2 / (60 + 1)
        flag_ema_60 = True
        idx_ema_60 = 60

        while flag_ema_60:

            current_ema = round((self.close_prices[idx_ema_60] * k_ema_60) + (previous_ema * (1 - k_ema_60)), 5)
            self.ema_60.append(current_ema)
            previous_ema = current_ema

            idx_ema_60 += 1

            if idx_ema_60 > len(self.close_prices) - 1:
                flag_ema_60 = False

        # EMA 20
        previous_ema = round(sum(self.close_prices[: 20]) / 20, 5)  # STARTING POINT

        k = 2 / (20 + 1)
        flag = True
        idx = 20

        while flag:

            current_ema = round((self.close_prices[idx] * k) + (previous_ema * (1 - k)), 5)
            self.ema_20.append(current_ema)
            previous_ema = current_ema

            idx += 1

            if idx > len(self.close_prices) - 1:
                flag = False

        len_diff = len(self.ema_60)
        self.close_prices_60 = self.close_prices[-len_diff:]
        self.open_prices_60 = self.open_prices[-len_diff:]
        self.low_prices_60 = self.low_prices[-len_diff:]
        self.high_prices_60 = self.high_prices[-len_diff:]
        self.ema_20_60 = self.ema_20[-len_diff:]
        self.date_time_60 = self.date_time[-len_diff:]

    # ************************************** SINGLE PAIR ***********************************************
    """
    ONE OF THE STRATEGIES I WAS TESTING SEEMED TO WORK ONLY GOING SHORT SO THAT'S THE ONLY PART I IMPLEMENTED 
    IF YOU NEED TO GO LONG YOU NEED TO BUILD IT (JUST INVERT WHAT I DID AND DON'T USE NEGATIVE NUMBERS AS UNITS INSIDE
    pairs_units_140 DICTIONARY)
    """

    def place_order_single_pair(self, forex_pair, num_of_candles, interval, take_profit, stop_loss):

        import json
        import oandapyV20.endpoints.orders as orders
        from oandapyV20.contrib.requests import MarketOrderRequest
        from oandapyV20.contrib.requests import StopLossOrderRequest
        from oandapyV20.contrib.requests import TakeProfitOrderRequest

        self.indicators(forex_pair, num_of_candles, interval)

        if "JPY" in forex_pair:
            take_profit_pair = take_profit * 0.01
            stop_loss_pair = stop_loss * 0.01
            price_gap = 5 * 0.01
        elif "HKD" in forex_pair:
            take_profit_pair = take_profit * 0.001
            stop_loss_pair = stop_loss * 0.001
            price_gap = 5 * 0.001
        else:
            take_profit_pair = take_profit * 0.0001
            stop_loss_pair = stop_loss * 0.0001
            price_gap = 5 * 0.0001

        if self.ema_20_60[-2] >= self.close_prices_60[-2] <= self.ema_60[-2] and \
                self.close_prices_60[-2] - self.open_prices_60[-7] <= price_gap:

            mo = MarketOrderRequest(instrument=forex_pair, units=self.pairs_units_140[forex_pair])
            r = orders.OrderCreate(self.accountID, data=mo.data)
            # ? perform the request
            rv = self.client.request(r)
            print(json.dumps(rv, indent=4))

            trade_id = rv["orderFillTransaction"]["tradeOpened"]["tradeID"]
            open_trade_price = float(rv["orderFillTransaction"]["price"])

            if "JPY" in forex_pair:
                stop_loss_price = str(round(open_trade_price - stop_loss_pair, 3))  # - AS IT'S BEAR SCENARIO
                take_profit_price = str(round(open_trade_price - take_profit_pair, 3))
            else:
                stop_loss_price = str(round(open_trade_price - stop_loss_pair, 5))
                take_profit_price = str(round(open_trade_price - take_profit_pair, 5))  # - AS IT'S BEAR SCENARIO

            ordr_sl = StopLossOrderRequest(tradeID=trade_id, price=stop_loss_price)
            r_sl = orders.OrderCreate(self.accountID, data=ordr_sl.data)
            # perform the request
            rv_sl = self.client.request(r_sl)
            print(json.dumps(rv_sl, indent=4))

            ordr_tp = TakeProfitOrderRequest(tradeID=trade_id, price=take_profit_price)
            r_tp = orders.OrderCreate(self.accountID, data=ordr_tp.data)
            # perform the request
            rv_tp = self.client.request(r_tp)
            print(json.dumps(rv_tp, indent=4))

    # ************************************** SINGLE PAIR 21 ***********************************************

    def place_order_single_pair_21(self, forex_pair, num_of_candles, interval, take_profit, stop_loss):

        import json
        import oandapyV20.endpoints.orders as orders
        from oandapyV20.contrib.requests import MarketOrderRequest
        from oandapyV20.contrib.requests import StopLossOrderRequest
        from oandapyV20.contrib.requests import TakeProfitOrderRequest

        self.indicators(forex_pair, num_of_candles, interval)

        if "JPY" in forex_pair:
            take_profit_pair = take_profit * 0.01
            stop_loss_pair = stop_loss * 0.01
            price_gap = 5 * 0.01
        elif "HKD" in forex_pair:
            take_profit_pair = take_profit * 0.001
            stop_loss_pair = stop_loss * 0.001
            price_gap = 5 * 0.001
        else:
            take_profit_pair = take_profit * 0.0001
            stop_loss_pair = stop_loss * 0.0001
            price_gap = 5 * 0.0001

        if self.ema_20_60[-1] >= self.close_prices_60[-1] <= self.ema_60[-1] and \
                self.close_prices_60[-1] - self.open_prices_60[-6] <= price_gap:

            mo = MarketOrderRequest(instrument=forex_pair, units=self.pairs_units_140[forex_pair])
            r = orders.OrderCreate(self.accountID, data=mo.data)
            # ? perform the request
            rv = self.client.request(r)
            print(json.dumps(rv, indent=4))

            trade_id = rv["orderFillTransaction"]["tradeOpened"]["tradeID"]
            open_trade_price = float(rv["orderFillTransaction"]["price"])

            if "JPY" in forex_pair:
                stop_loss_price = str(round(open_trade_price - stop_loss_pair, 3))  # - AS IT'S BEAR SCENARIO
                take_profit_price = str(round(open_trade_price - take_profit_pair, 3))
            else:
                stop_loss_price = str(round(open_trade_price - stop_loss_pair, 5))
                take_profit_price = str(round(open_trade_price - take_profit_pair, 5))  # - AS IT'S BEAR SCENARIO

            ordr_sl = StopLossOrderRequest(tradeID=trade_id, price=stop_loss_price)
            r_sl = orders.OrderCreate(self.accountID, data=ordr_sl.data)
            # perform the request
            rv_sl = self.client.request(r_sl)
            print(json.dumps(rv_sl, indent=4))

            ordr_tp = TakeProfitOrderRequest(tradeID=trade_id, price=take_profit_price)
            r_tp = orders.OrderCreate(self.accountID, data=ordr_tp.data)
            # perform the request
            rv_tp = self.client.request(r_tp)
            print(json.dumps(rv_tp, indent=4))

    # ************************************************** ALL PAIRS *************************************************

    def place_order_all_pairs(self, num_of_candles, interval, take_profit, stop_loss):

        import time

        self.open_positions_records = []
        self.recent_closed_trades = []
        self.open_positions_db_converting()

        self.open_positions = []
        self.open_positions_info()

        self.delayed_pairs = []

        # TO CHECK IF THE RECORD ON THE db[-1] BELONGS TO ONE HOUR AGO
        tc = time.gmtime()
        if tc[3] == 0:
            tcr = 24
        else:
            tcr = tc[3]

        if self.hours_db_records and tcr - self.hours_db_records[-1] == 1:

            open_pos_plus_recent_closing = list(set(self.open_positions + self.open_positions_records[-1]))

            print(open_pos_plus_recent_closing)

        else:
            open_pos_plus_recent_closing = self.open_positions

            print(open_pos_plus_recent_closing)

        not_open_pos = [el for el in self.forex_pairs if el not in open_pos_plus_recent_closing]

        for p in not_open_pos:

            try:

                self.last_candle_time_check(p, interval)

                if self.last_candle_time == tc[3]:

                    self.place_order_single_pair(p, num_of_candles, interval, take_profit, stop_loss)

                else:

                    self.delayed_pairs.append(p)

                    print(f"{p} DATA IS DELAYED ")

            except:

                print("ERROR WITH", p)

                self.delayed_pairs.append(p)

        if self.delayed_pairs:

            counter_len = len(self.delayed_pairs)
            counter_five = len(self.delayed_pairs) * 20  # TO AVOID AN INFINITE LOOP IN CASE OF PROBLEMS

            flag_1 = True

        else:

            counter_len = 0
            counter_five = 0

            flag_1 = False

        while flag_1:

            for pa in self.delayed_pairs:

                try:

                    counter_five -= 1

                    self.last_candle_time_check(pa, interval)

                    if counter_five == 0:

                        print("TRIED 20 TIMES BUT THE DATA WASN'T READY YET")

                        flag_1 = False

                        break

                    elif self.last_candle_time == tc[3]:

                        self.place_order_single_pair(pa, num_of_candles, interval, take_profit,
                                                     stop_loss)

                        counter_len -= 1

                        if counter_len == 0:
                            flag_1 = False

                            break

                    else:

                        time.sleep(10)

                except:

                    print("ERROR WITH DELAYED PAIR", pa)

                    time.sleep(40)

                    try:

                        self.last_candle_time_check(pa, interval)

                        if self.last_candle_time == tc[3]:

                            self.place_order_single_pair(pa, num_of_candles, interval, take_profit,
                                                         stop_loss)

                            counter_len -= 1

                            print(pa, "DELAYED PAIR ERROR FIXED ")

                            if counter_len == 0:
                                flag_1 = False

                                break

                    except:

                        counter_len -= 1

                        print(pa, "DELAYED PAIR ERROR NOT FIXED")

                        if counter_len == 0:
                            flag_1 = False

                            break

    # ************************************************* ALL PAIRS 21 **********************************************

    def place_order_all_pairs_21(self, num_of_candles, interval, take_profit, stop_loss):

        import time

        self.open_positions_records = []
        self.recent_closed_trades = []
        self.open_positions_db_converting()

        self.open_positions = []
        self.open_positions_info()

        self.delayed_pairs = []

        """      
        CHECK IF THE RECORD ON THE db[-1] BELONGS TO THE SAME HOUR
        TO MAKE SURE THE DATA WAS RECORDED PROPERLY
        """

        tc = time.gmtime()

        if tc[3] == self.hours_db_records[-1]:

            open_pos_plus_recent_closing = list(set(self.open_positions + self.open_positions_records[-1]))

            print(open_pos_plus_recent_closing)

        else:
            open_pos_plus_recent_closing = self.open_positions

            print(open_pos_plus_recent_closing)

        not_open_pos = [el for el in self.forex_pairs if el not in open_pos_plus_recent_closing]

        for p in not_open_pos:

            try:

                self.last_candle_time_check(p, interval)

                if self.last_candle_time == tc[3]:

                    self.place_order_single_pair_21(p, num_of_candles, interval, take_profit, stop_loss)

                else:

                    self.delayed_pairs.append(p)

                    print(f"{p} DATA IS DELAYED ")

            except:

                print("ERROR WITH", p)

                self.delayed_pairs.append(p)

        if self.delayed_pairs:

            counter_len = len(self.delayed_pairs)
            counter_five = len(self.delayed_pairs) * 5  # TO AVOID AN INFINITE LOOP IN CASE OF PROBLEMS

            flag_1 = True

        else:

            counter_len = 0
            counter_five = 0

            flag_1 = False

        while flag_1:

            for pa in self.delayed_pairs:

                try:

                    counter_five -= 1

                    self.last_candle_time_check(pa, interval)

                    if counter_five == 0 or counter_len == 0:

                        print("TRIED 5 TIMES BUT THE DATA WASN'T READY YET")

                        flag_1 = False

                        break

                    elif self.last_candle_time == tc[3]:

                        self.place_order_single_pair_21(pa, num_of_candles, interval, take_profit,
                                                        stop_loss)

                        counter_len -= 1

                        if counter_len == 0:
                            flag_1 = False

                            break

                    else:

                        time.sleep(10)

                except:

                    print("ERROR WITH DELAYED PAIR", pa)

                    time.sleep(20)

                    try:

                        self.place_order_single_pair_21(pa, num_of_candles, interval, take_profit,
                                                        stop_loss)

                        counter_len -= 1

                        print(pa, "DELAYED PAIR ERROR FIXED ")

                        if counter_len == 0:
                            flag_1 = False

                            break

                    except:

                        counter_len -= 1

                        print(pa, "DELAYED PAIR ERROR NOT FIXED")

                        if counter_len == 0:
                            flag_1 = False

                            break

    # ********************************************** RUN IT **********************************************************

    def run_it_24_7(self):

        import time

        while True:

            ti = time.gmtime()

            if (ti.tm_wday == 5) or (ti.tm_wday == 6 and ti[3] < 21) or (ti.tm_wday == 4 and ti[3] >= 21):

                time.sleep(10)

                continue

            elif ti.tm_wday == 4 and ti[3] == 20 and ti[4] >= 56:  # todo check the end of the trading week timing

                try:

                    tm = time.gmtime()
                    print(f"**************\nTIME: {tm[3]}:{tm[4]}:{tm[5]} - CHECK")

                    self.place_order_all_pairs_21(510, "M15", 125, -125)

                    tme = time.gmtime()
                    print(f"TIME: {tme[3]}:{tme[4]}:{tme[5]} - CHECK DONE\n**************")

                    self.open_positions_db_writing()

                    self.account_summary_db_writing()

                    self.send_telegram_message("Claax6 M15 checked")

                    time.sleep(60)

                except:

                    tm = time.gmtime()

                    print(f"**************\nTIME: {tm[3]}:{tm[4]}:{tm[5]} "
                          f"AN ERROR AS OCCURRED MEANWHILE CONNECTING\n**************")

                    self.send_telegram_message("Claax6 M15 connection problem")

                    time.sleep(240)

                finally:

                    time.sleep(400)  # to make sure it pauses till the trading week is over

            elif ti[4] in [0, 15, 30, 45]:

                try:

                    tm = time.gmtime()
                    print(f"**************\nTIME: {tm[3]}:{tm[4]}:{tm[5]} - CHECK")

                    self.place_order_all_pairs(510, "M15", 125, -125)

                    tme = time.gmtime()
                    print(f"TIME: {tme[3]}:{tme[4]}:{tme[5]} - CHECK DONE\n**************")

                    self.open_positions_db_writing()

                    self.account_summary_db_writing()

                    self.send_telegram_message("Claax6 M15 checked")

                    time.sleep(60)

                except:

                    tm = time.gmtime()

                    print(f"**************\nTIME: {tm[3]}:{tm[4]}:{tm[5]} "
                          f"AN ERROR AS OCCURRED MEANWHILE CONNECTING\n**************")

                    self.send_telegram_message("Claax6 M15 connection problem")

                    time.sleep(240)

                finally:

                    time.sleep(10)
                

# ************************************************* END OF THE SCRIPT **************************************************


Claax1().run_it_24_7()

# c = Claax1

# c.place_order_all_pairs(400, "H1", 140, -140)
# c.place_order_all_pairs_21(400, "H1", 140, -140)

#c.create_data_base()

# c.open_positions_db_reading()
# c.account_summary_db_reading()

#c.open_positions_db_writing()

#c.open_positions_db_converting()

#print(c.hours_db_records)

