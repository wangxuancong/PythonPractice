from PythonCoding.exchange.huobi_exchange.huobiservice import Huobi
from datetime import datetime
import time
import pandas as pd


class Data_save:
    '''
    -------------------
    -------------------
    save data by sizes

    "BTC_CW"表示BTC当周合约
    "BTC_NW"表示BTC次周合约
    "BTC_CQ"表示BTC季度合约

    -------------------
    -------------------
    '''

    URL = 'https://api.huobipro.com'

    loader = Huobi(URL)

    def get_periods(self):

        return ['1min', '5min', '15min', '30min', '60min', '1day', '1week', '1mon']

    def symbols(self):

        return ['btcusdt','ethusdt','manbtc']

    def save_kline(self, periods):

        '''
        :param periods: different periods
        :return:
        '''

        datas = self.loader.get_contract_kline(symbol='btcusdt', period=periods, size=2000)['data']
        amount = []
        close = []
        count = []
        high = []
        date = []
        low = []
        open = []
        vol = []
        for data in datas:
            amount.append(data['amount'])
            close.append(data['close'])
            count.append(data['count'])
            high.append(data['high'])
            date.append(self.to_date(data['id'], 'mins'))
            low.append(data['low'])
            open.append(data['open'])
            vol.append(data['vol'])


    def to_date(self, timestamp, type=None):
        '''
        :param timestamp:
        :param type: mins or day
        :return: two kinds of time type
        '''

        struct_time = time.gmtime(timestamp)

        if type == 'mins':

            return time.strftime("%Y-%m-%d %H:%M:%S", struct_time)

        else:

            return time.strftime("%Y-%m-%d", struct_time)
