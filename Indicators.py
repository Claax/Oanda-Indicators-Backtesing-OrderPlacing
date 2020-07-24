#!python


from ForexBot.Engine import Engine


class Indicators(Engine):

    def __init__(self):

        Engine.__init__(self)

        self.sma_10 = []
        self.sma_10_w_index = []
        self.sma_20 = []
        self.sma_20_w_index = []
        self.sma_50 = []
        self.sma_50_w_index = []
        self.sma_60 = []
        self.sma_60_w_index = []
        self.sma_100 = []
        self.sma_100_w_index = []
        self.sma_200 = []
        self.sma_200_w_index = []
        self.sma_240 = []
        self.sma_240_w_index = []
        self.sma_500 = []
        self.sma_500_w_index = []
        self.sma_960 = []
        self.sma_960_w_index = []

        self.ema_8 = []
        self.ema_12 = []
        self.ema_26 = []
        self.ema_50 = []

        self.macd_line = []
        self.macd_line_w_index = []
        self.macd_signal_line = []

        self.rsi = []

        self.k = []
        self.d = []

        self.indexes = []
        self.conversion_line = []
        self.base_line = []
        self.lagging_span = []
        self.line_a = []
        self.zip_lines = []
        self.line_b = []
        self.lines_w_close_prices = []
        self.cloud_w_close_prices = []
        self.cloud_color = []
        self.trend = []

        self.cloud_color_26 = []
        self.conversion_line_26 = []
        self.base_line_26 = []
        self.lagging_span_26 = []
        self.close_prices_26 = []
        self.open_prices_26 = []
        self.low_prices_26 = []
        self.high_prices_26 = []
        self.trend_26 = []
        self.line_a_26 = []
        self.line_b_26 = []

        self.cloud_color_52 = []
        self.conversion_line_52 = []
        self.base_line_52 = []
        self.lagging_span_52 = []
        self.close_prices_52 = []
        self.open_prices_52 = []
        self.low_prices_52 = []
        self.high_prices_52 = []
        self.trend_52 = []
        self.line_a_52 = []
        self.line_b_52 = []

    def sma_10_20_50_60_100_200_240_960_indicator(self, forex_pair, num_of_candles, interval):

        self.__init__()
        self.historical_klines(forex_pair, num_of_candles, interval)

        indexes = [i for i in range(len(self.red_green_candles))]

        # 10
        if len(self.red_green_candles) < 10:

            return "LESS THAN 10 CANDLES"

        else:

            start = 0
            stop = 10

            flag = True

            while flag:

                self.sma_10.append(round(sum(self.close_prices[start: stop]) / 10, 4))

                if stop > len(self.close_prices) - 1:
                    flag = False

                start += 1
                stop += 1

            self.sma_10_w_index = list(zip(self.sma_10, indexes[9:]))

        # 20
        if len(self.red_green_candles) < 20:

            return "LESS THAN 20 CANDLES"

        else:

            start = 0
            stop = 20
            flag = True

            while flag:

                self.sma_20.append(round(sum(self.close_prices[start: stop]) / 20, 4))

                if stop > len(self.close_prices) - 1:
                    flag = False

                start += 1
                stop += 1

            self.sma_20_w_index = list(zip(self.sma_20, indexes[19:]))

        # 50
        if len(self.red_green_candles) < 50:

            return "LESS THAN 50 CANDLES"

        else:

            start = 0
            stop = 50
            flag = True

            while flag:

                self.sma_50.append(round(sum(self.close_prices[start: stop]) / 50, 4))

                if stop > len(self.close_prices) - 1:
                    flag = False

                start += 1
                stop += 1

            self.sma_50_w_index = list(zip(self.sma_50, indexes[49:]))

        # 60
        if len(self.red_green_candles) < 60:

            return "LESS THAN 60 CANDLES"

        else:

            start = 0
            stop = 60

            flag = True

            while flag:

                self.sma_60.append(round(sum(self.close_prices[start: stop]) / 60, 4))

                if stop > len(self.close_prices) - 1:
                    flag = False

                start += 1
                stop += 1

            self.sma_60_w_index = list(zip(self.sma_60, indexes[59:]))

        # 100
        if len(self.red_green_candles) < 100:

            return "LESS THAN 100 CANDLES"

        else:

            start = 0
            stop = 100

            flag = True

            while flag:

                self.sma_100.append(round(sum(self.close_prices[start: stop]) / 100, 4))

                if stop > len(self.close_prices) - 1:
                    flag = False

                start += 1
                stop += 1

            self.sma_100_w_index = list(zip(self.sma_100, indexes[99:]))

        # 200
        if len(self.red_green_candles) < 200:

            return "LESS THAN 200 CANDLES"

        else:

            start = 0
            stop = 200

            flag = True

            while flag:

                self.sma_200.append(round(sum(self.close_prices[start: stop]) / 200, 4))

                if stop > len(self.close_prices) - 1:
                    flag = False

                start += 1
                stop += 1

            self.sma_200_w_index = list(zip(self.sma_200, indexes[199:]))

        # 240
        if len(self.red_green_candles) < 240:

            return "LESS THAN 240 CANDLES"

        else:
            
            start = 0
            stop = 240
            flag = True

            while flag:

                self.sma_240.append(round(sum(self.close_prices[start: stop]) / 240, 4))

                if stop > len(self.close_prices) - 1:
                    flag = False

                start += 1
                stop += 1

            self.sma_240_w_index = list(zip(self.sma_240, indexes[239:]))

        # 500
        if len(self.red_green_candles) < 500:

            return "LESS THAN 500 CANDLES"

        else:

            start = 0
            stop = 500
            flag = True

            while flag:

                self.sma_500.append(round(sum(self.close_prices[start: stop]) / 500, 4))

                if stop > len(self.close_prices) - 1:
                    flag = False

                start += 1
                stop += 1

            self.sma_500_w_index = list(zip(self.sma_500, indexes[499:]))

        # 960
        if len(self.red_green_candles) < 960:

            return "LESS THAN 960 CANDLES"

        else:

            start = 0
            stop = 960
            flag = True

            while flag:

                self.sma_960.append(round(sum(self.close_prices[start: stop]) / 960, 4))

                if stop > len(self.close_prices) - 1:
                    flag = False

                start += 1
                stop += 1

            self.sma_960_w_index = list(zip(self.sma_960, indexes[959:]))

    def ema_8_12_26_50_indicator(self, forex_pair, num_of_candles, interval):

        self.__init__()
        self.historical_klines(forex_pair, num_of_candles, interval)

        # EMA 8
        previous_ema = round(sum(self.close_prices[: 8]) / 8, 4)  # ? JUST A STARTING POINT

        k = 2 / (8 + 1)
        flag = True
        idx = 8  # ? IDX OF THE 8TH CANDLE

        while flag:

            current_ema = round((self.close_prices[idx] * k) + (previous_ema * (1 - k)), 4)

            self.ema_8.append(current_ema)

            previous_ema = current_ema

            idx += 1

            if idx > len(self.close_prices) - 1:
                flag = False

        # EMA 12
        previous_ema = round(sum(self.close_prices[: 12]) / 12, 4)  # ? JUST A STARTING POINT

        k = 2 / (12 + 1)
        flag = True
        idx = 12  # ? IDX OF THE 12TH CANDLE
        
        while flag:

            current_ema = round((self.close_prices[idx] * k) + (previous_ema * (1 - k)), 4)

            self.ema_12.append(current_ema)

            previous_ema = current_ema

            idx += 1

            if idx > len(self.close_prices) - 1:
                flag = False

        # EMA 26
        previous_ema = round(sum(self.close_prices[: 26]) / 26, 4)  # ? JUST A STARTING POINT

        k = 2 / (26 + 1)
        flag = True
        idx = 26  # ? IDX OF THE 12TH CANDLE

        while flag:

            current_ema = round((self.close_prices[idx] * k) + (previous_ema * (1 - k)), 4)

            self.ema_26.append(current_ema)

            previous_ema = current_ema

            idx += 1

            if idx > len(self.close_prices) - 1:
                flag = False

        # EMA 50
        previous_ema = round(sum(self.close_prices[: 50]) / 50, 4)  # ? JUST A STARTING POINT

        k = 2 / (50 + 1)
        flag = True
        idx = 50  # ? IDX OF THE 50TH CANDLE

        while flag:

            current_ema = round((self.close_prices[idx] * k) + (previous_ema * (1 - k)), 4)

            self.ema_50.append(current_ema)

            previous_ema = current_ema

            idx += 1

            if idx > len(self.close_prices) - 1:
                flag = False

    def macd_12_26_indicator(self, forex_pair, num_of_candles, interval):
        
        self.__init__()
        self.historical_klines(forex_pair, num_of_candles, interval)

        # EMA 12
        previous_ema = round(sum(self.close_prices[: 12]) / 12, 4)  # ? JUST A STARTING POINT
        
        k = 2 / (12 + 1)
        flag = True
        idx = 12  # ? IDX OF THE 12TH CANDLE

        while flag:

            current_ema = round((self.close_prices[idx] * k) + (previous_ema * (1 - k)), 4)

            self.ema_12.append(current_ema)

            previous_ema = current_ema

            idx += 1

            if idx > len(self.close_prices) - 1:
                flag = False

        # EMA 26
        previous_ema = round(sum(self.close_prices[: 26]) / 26, 4)  # ? JUST A STARTING POINT

        k = 2 / (26 + 1)
        flag = True
        idx = 26  # ? IDX OF THE 12TH CANDLE

        while flag:

            current_ema = round((self.close_prices[idx] * k) + (previous_ema * (1 - k)), 4)

            self.ema_26.append(current_ema)

            previous_ema = current_ema

            idx += 1

            if idx > len(self.close_prices) - 1:
                flag = False

        # MACD LINE / SIGNAL LINE

        for el1, el2 in zip(self.ema_12[14:], self.ema_26):
            self.macd_line.append(round(el1 - el2, 4))

        self.macd_line_w_index = list(zip(self.macd_line, ))

        previous_ema = round(sum(self.macd_line[: 9]) / 9, 4)  # JUST A STARTING POINT

        k = 2 / (9 + 1)
        flag = True
        idx = 9  # IDX OF THE 12TH CANDLE

        while flag:

            current_ema = round((self.macd_line[idx] * k) + (previous_ema * (1 - k)), 4)

            self.macd_signal_line.append(current_ema)

            previous_ema = current_ema

            idx += 1

            if idx > len(self.macd_line) - 1:
                flag = False

    def rsi_14_indicator(self, forex_pair, num_of_candles, interval):
        
        self.__init__()
        self.historical_klines(forex_pair, num_of_candles, interval)

        assert len(self.red_green_candles) > 21, "NOT ENOUGH CANDLES"

        # UP / DOWN CHANGES

        up_movement = []
        down_movement = []

        idx = 1
        flag = True

        while flag:

            if idx > len(self.close_prices) - 1:

                flag = False

            elif self.close_prices[idx] - self.close_prices[idx - 1] > 0:

                up_movement.append(round(abs(self.close_prices[idx] - self.close_prices[idx - 1]), 8))

                down_movement.append(0)

            else:

                up_movement.append(0)

                down_movement.append(round(abs(self.close_prices[idx] - self.close_prices[idx - 1]), 8))

            idx += 1

        # SMMA

        average_up_movement = sum(up_movement[: 14]) / 14
        average_down_movement = sum(down_movement[: 14]) / 14

        smmas_up = [average_up_movement]  # ? ALL THE CHANGES
        smmas_down = [average_down_movement]  # ? ALL THE CHANGES

        flag = True
        idx = 14

        while flag:

            if idx > len(up_movement) - 1:

                flag = False

            else:

                average_up_movement_change = (up_movement[idx] + (average_up_movement * (14 - 1))) / 14

                smmas_up.append(average_up_movement_change)

                average_up_movement = average_up_movement_change

                average_down_movement_change = (down_movement[idx] + (average_down_movement * (14 - 1))) / 14

                smmas_down.append(average_down_movement_change)

                average_down_movement = average_down_movement_change

            idx += 1

        # RS
        rs = []
        flag = True
        idx = 0

        while flag:

            if idx > len(smmas_up) - 1:

                flag = False

            else:

                rs.append(smmas_up[idx] / smmas_down[idx])

            idx += 1

        # RSI
        flag = True
        idx = 0

        while flag:

            if idx > len(rs) - 1:

                flag = False

            else:

                r_s_i = round(100 - 100 / (1 + rs[idx]), 4)

                self.rsi.append(r_s_i)

            idx += 1

    def stochastic_indicator(self, forex_pair, num_of_candles, interval):

        self.__init__()
        self.historical_klines(forex_pair, num_of_candles, interval)

        # * K

        flag = True
        start = 0
        stop = 14

        while flag:

            value = round((((self.close_prices[stop - 1] - min(self.low_prices[start: stop])) / (
                        max(self.high_prices[start: stop]) - min(self.low_prices[start: stop]))) * 100), 4)

            self.k.append(value)

            if stop == len(self.close_prices):
                flag = False

            start += 1
            stop += 1

        # D

        flag = True
        start = 0
        stop = 3

        while flag:

            self.d.append(round(sum(self.k[start: stop]) / 3, 4))

            if stop > len(self.k) - 1:
                flag = False

            start += 1
            stop += 1

    def stochastic_rsi_14_indicator(self, forex_pair, num_of_candles, interval):

        self.__init__()
        self.historical_klines(forex_pair, num_of_candles, interval)

        assert len(self.red_green_candles) > 21, "NOT ENOUGH CANDLES"

        """
        ON TRADING VIEW YOU HAVE TO PUT THE SETTING OF THE K SMOOTH ON 1 INSTEAD OF 3 OTHERWISE YOU WILL NEED TO ADD 
        SOME LINES OF CODE TO MAKE THE AVERAGE OF THE LAST N Ks
        """

        # UP / DOWN CHANGES
        up_movement = []
        down_movement = []

        idx = 1
        flag = True

        while flag:

            if idx > len(self.close_prices) - 1:

                flag = False

            elif self.close_prices[idx] - self.close_prices[idx - 1] > 0:

                up_movement.append(round(abs(self.close_prices[idx] - self.close_prices[idx - 1]), 8))

                down_movement.append(0)

            else:

                up_movement.append(0)

                down_movement.append(round(abs(self.close_prices[idx] - self.close_prices[idx - 1]), 8))

            idx += 1

        # SMMA
        average_up_movement = sum(up_movement[: 14]) / 14
        average_down_movement = sum(down_movement[: 14]) / 14

        smmas_up = [average_up_movement]  # ? ALL THE CHANGES
        smmas_down = [average_down_movement]  # ? ALL THE CHANGES

        flag = True
        idx = 14

        while flag:

            if idx > len(up_movement) - 1:

                flag = False

            else:

                average_up_movement_change = (up_movement[idx] + (average_up_movement * (14 - 1))) / 14

                smmas_up.append(average_up_movement_change)

                average_up_movement = average_up_movement_change

                average_down_movement_change = (down_movement[idx] + (average_down_movement * (14 - 1))) / 14

                smmas_down.append(average_down_movement_change)

                average_down_movement = average_down_movement_change

            idx += 1

        # RS
        rs = []

        flag = True
        idx = 0

        while flag:

            if idx > len(smmas_up) - 1:

                flag = False

            else:

                rs.append(smmas_up[idx] / smmas_down[idx])

            idx += 1

        # RSI

        flag = True
        idx = 0

        while flag:

            if idx > len(rs) - 1:

                flag = False

            else:

                r_s_i = round(100 - 100 / (1 + rs[idx]), 4)

                self.rsi.append(r_s_i)

            idx += 1

        # K

        flag = True
        start = 0
        stop = 14

        while flag:

            if stop > len(self.rsi) - 1:
                flag = False

            value = round((((self.rsi[stop - 1] - min(self.rsi[start: stop])) / (
                        max(self.rsi[start: stop]) - min(self.rsi[start: stop]))) * 100), 4)

            self.k.append(value)

            start += 1
            stop += 1

        # D

        flag = True
        start = 0
        stop = 3

        while flag:

            self.d.append(round(sum(self.k[start: stop]) / 3, 4))

            if stop > len(self.k) - 1:
                flag = False

            start += 1
            stop += 1

    def ichimoku_52_indicator(self, forex_pair, num_of_candles, interval):

        self.__init__()
        self.historical_klines(forex_pair, num_of_candles, interval)

        # MINIMUM LENGTH NEEDED

        assert len(self.red_green_candles) > 101, f"LENGHT LESS THAN {101} CANDLES"

        # if len( self.red_green_candles ) > 101 * assertion_factor:

        # raise Exception(f"LENGHT LESS THAN { 101 * assertion_factor } CANDLES")

        self.indexes = [el for el in range(len(self.red_green_candles))]

        # CONVERSION LINE ( 9 PERIODS )

        flag = True
        start = 0
        stop = 9

        while flag:

            max_high = max(self.high_prices[start: stop])
            min_low = min(self.low_prices[start: stop])

            self.conversion_line.append(round(((max_high + min_low) / 2), 5))

            if stop > len(self.high_prices) - 1:
                flag = False

            start += 1
            stop += 1

        # BASE LINE
        flag = True
        start = 0
        stop = 26

        while flag:

            max_high = max(self.high_prices[start: stop])
            min_low = min(self.low_prices[start: stop])

            self.base_line.append(round(((max_high + min_low) / 2), 5))

            if stop > len(self.high_prices) - 1:
                flag = False

            start += 1
            stop += 1

        # LAGGING SPAN TWO PERIODS
        #  NORMAL CLOSING PRICES REPRESENTED 26 SIX PERIOD BEFORE
        # ..( EX : THE CURRENT PRICE IS PUT 26 DAYS AGO , THE PRICE DOESN'T CHANGE ONLY IT'S BEEN PUT IN THE PAST  )
        #  USED TO COMPARE THE CLOSING PRICE WITH THE PRICE THAT WAS 26 PERIODS BEFORE
        # THE THE PRICE GOES ABOVE THE 26 PERDIODS BEFORE PRICE IS BULLISH SIGN IF IT'S BELOW IT'S A BEARISH SIGN

        # ? FIRST IS THE CURRENT PRICE THE SECOND IS THE PRICE 26 PERIODS BEFORE
        self.lagging_span = list(zip(self.close_prices[26:], self.close_prices[: -26]))

        # ? 50 ARE THE DAYS IN BETWEEN THE END OF THE CLOUD AND THE LAGGING LINE
        self.lagging_span = self.lagging_span + (["no data" for el in range(26)] * 2)

        # TWO LINES SHIFTED 26 PERIODS IN THE FUTURE
        # LINE A
        self.zip_lines = list(zip(self.conversion_line[17:], self.base_line))

        flag = True
        idx = 17

        while flag:

            for el1, el2 in list(zip(self.conversion_line[idx:], self.base_line)):

                self.line_a.append(round(((el1 + el2) / 2), 5))

                if idx > len(self.base_line) - 1:
                    flag = False

                idx += 1

        # LINE B
        flag = True
        start = 0
        stop = 52

        while flag:

            max_high = max(self.high_prices[start: stop])
            min_low = min(self.low_prices[start: stop])

            self.line_b.append(round(((max_high + min_low) / 2), 5))

            if stop > len(self.high_prices) - 1:
                flag = False

            start += 1
            stop += 1

        # CLOUD
        zip_line_a_line_b = list(zip(self.line_a[26:], self.line_b))

        """
        SINCE LINE A AND LINE B ARE 26 PERIOD IN THE FUTURE I ADD 26 "Future"
        TO THE CLOSE PRICES SO THE LENGTH IS THE SAME AND I COULD ZIP ALL OF THEM
        """

        close_prices_future = self.close_prices + ["Future" for el in range(0, 26)]

        self.lines_w_close_prices = list(zip(close_prices_future[-len(zip_line_a_line_b):], zip_line_a_line_b))

        self.cloud_w_close_prices = [(el1, el2, "Green Cloud") if el2[0] > el2[1] else (el1, el2, "Red Cloud") for
                                     el1, el2 in self.lines_w_close_prices]

        self.cloud_color = ["Green Cloud" if el[0] > el[1] else "Red Cloud" for el in zip_line_a_line_b]

        # TREND BASED ON THE BASE_LINE
        """
        THIS IS JUST FOR THE STRATEGY I USE - IT IS NOT PART OF THE INDICATOR ITSELF
        """
        flag = True
        idx = 1

        while flag:

            if idx <= len(self.base_line) - 1:

                if self.base_line[idx] > self.base_line[idx - 1]:

                    self.trend.append(1)

                elif self.base_line[idx] == self.base_line[idx - 1]:

                    self.trend.append(0)

                elif self.base_line[idx] < self.base_line[idx - 1]:

                    self.trend.append(-1)

            else:

                flag = False

            idx += 1

        # GIVE ALL THE VARIABLES THE SAME LENGTH / DAYS RANGE SO I HAVE THE SAME INDEX FOR ALL THE VARIABLES

        span = ["no data" for el in range(26)]

        self.cloud_color_26 = span + self.cloud_color

        idx = -len(self.cloud_color_26)

        self.conversion_line_26 = self.conversion_line + span
        self.conversion_line_26 = self.conversion_line_26[idx:]

        self.base_line_26 = self.base_line + span
        self.base_line_26 = self.base_line_26[idx:]

        self.lagging_span_26 = self.lagging_span
        self.lagging_span_26 = self.lagging_span_26[idx:]

        self.close_prices_26 = self.close_prices + span
        self.close_prices_26 = self.close_prices_26[idx:]

        self.open_prices_26 = self.open_prices + span
        self.open_prices_26 = self.open_prices_26[idx:]

        self.low_prices_26 = self.low_prices + span
        self.low_prices_26 = self.low_prices_26[idx:]

        self.high_prices_26 = self.high_prices + span
        self.high_prices_26 = self.high_prices_26[idx:]

        self.trend_26 = self.trend + span
        self.trend_26 = self.trend_26[idx:]

        self.line_a_26 = self.line_a[idx:]

        self.line_b_26 = span + self.line_b

    def ichimoku_104_indicator(self, forex_pair, num_of_candles, interval):

        self.__init__()
        self.historical_klines(forex_pair, num_of_candles, interval)

        assert len(self.red_green_candles) > 210, f"LENGTH LESS THAN {210} CANDLES"

        self.indexes = [el for el in range(len(self.red_green_candles))]

        # CONVERSION LINE ( 18 PERIODS )

        flag = True
        start = 0
        stop = 18

        while flag:

            max_high = max(self.high_prices[start: stop])
            min_low = min(self.low_prices[start: stop])

            self.conversion_line.append(round(((max_high + min_low) / 2), 5))

            if stop > len(self.high_prices) - 1:
                flag = False

            start += 1
            stop += 1

        # BASE LINE
        flag = True
        start = 0
        stop = 52

        while flag:

            max_high = max(self.high_prices[start: stop])
            min_low = min(self.low_prices[start: stop])

            self.base_line.append(round(((max_high + min_low) / 2), 5))

            if stop > len(self.high_prices) - 1:
                flag = False

            start += 1
            stop += 1

        # LAGGING SPAN TWO PERIODS
        self.lagging_span = list(zip(self.close_prices[52:], self.close_prices[: -52]))

        self.lagging_span = self.lagging_span + (["no data" for el in range(52)] * 2)

        # LINE A
        self.zip_lines = list(zip(self.conversion_line[34:], self.base_line))

        flag = True
        idx = 34

        while flag:

            for el1, el2 in list(zip(self.conversion_line[idx:], self.base_line)):

                self.line_a.append(round(((el1 + el2) / 2), 5))

                if idx > len(self.base_line) - 1:
                    flag = False

                idx += 1

        # LINE B
        flag = True
        start = 0
        stop = 104

        while flag:

            max_high = max(self.high_prices[start: stop])
            min_low = min(self.low_prices[start: stop])

            self.line_b.append(round(((max_high + min_low) / 2), 5))

            if stop > len(self.high_prices) - 1:
                flag = False

            start += 1
            stop += 1

        # CLOUD
        zip_line_a_line_b = list(zip(self.line_a[52:], self.line_b))

        # ? SINCE LINE A AND LINE B ARE 52 PERDIOD IN THE FUTURE I ADD 52 "Future"
        # TO THE CLOSE PRICES SO THE LENGHT IS THE SAME AND I COULD ZIP ALL OF THEM
        close_prices_future = self.close_prices + ["Future" for el in range(0, 52)]

        self.lines_w_close_prices = list(zip(close_prices_future[-len(zip_line_a_line_b):], zip_line_a_line_b))

        self.cloud_w_close_prices = [(el1, el2, "Green Cloud") if el2[0] > el2[1] else (el1, el2, "Red Cloud") for
                                     el1, el2 in self.lines_w_close_prices]

        self.cloud_color = ["Green Cloud" if el[0] > el[1] else "Red Cloud" for el in zip_line_a_line_b]

        # * TREND BASED ON THE BASE_LINE
        flag = True
        idx = 1

        while flag:

            if idx <= len(self.base_line) - 1:

                if self.base_line[idx] > self.base_line[idx - 1]:

                    self.trend.append(1)

                elif self.base_line[idx] == self.base_line[idx - 1]:

                    self.trend.append(0)

                elif self.base_line[idx] < self.base_line[idx - 1]:

                    self.trend.append(-1)

            else:

                flag = False

            idx += 1

        # * GIVE ALL THE VARIABLES THE SAME LENGTH / DAYS RANGE SO I HAVE THE SAME INDEX FOR ALL THE VARIABLES

        span = ["no data" for el in range(52)]

        self.cloud_color_52 = span + self.cloud_color

        idx = -len(self.cloud_color_52)

        self.conversion_line_52 = self.conversion_line + span
        self.conversion_line_52 = self.conversion_line_52[idx:]

        self.base_line_52 = self.base_line + span
        self.base_line_52 = self.base_line_52[idx:]

        self.lagging_span_52 = self.lagging_span
        self.lagging_span_52 = self.lagging_span_52[idx:]

        self.close_prices_52 = self.close_prices + span
        self.close_prices_52 = self.close_prices_52[idx:]

        self.open_prices_52 = self.open_prices + span
        self.open_prices_52 = self.open_prices_52[idx:]

        self.low_prices_52 = self.low_prices + span
        self.low_prices_52 = self.low_prices_52[idx:]

        self.high_prices_52 = self.high_prices + span
        self.high_prices_52 = self.high_prices_52[idx:]

        self.trend_52 = self.trend + span
        self.trend_52 = self.trend_52[idx:]

        self.line_a_52 = self.line_a[idx:]

        self.line_b_52 = span + self.line_b

# ***************************************** END OF THE SCRIPT *********************************************************


