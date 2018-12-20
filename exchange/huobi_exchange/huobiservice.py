from PythonCoding.exchange.huobi_exchange.utils import http_get_request


class Huobi:

    def __init__(self, url):
       
        self.__url = url

    # 获取KLine
    def get_contract_kline(self, symbol, period, size=150):
        """
        :param symbol  BTC_CW, BTC_NW, BTC_CQ , ...
        :param period: 可选值：{1min, 5min, 15min, 30min, 60min, 4hour, 1day, 1week, 1mon }
        :param size: [1,2000]
        :return:
        """
        params = {'symbol': symbol,
                  'period': period}
        if size:
            params['size'] = size

        url = self.__url + '/market/history/kline'
        return http_get_request(url, params)

    # 获取聚合行情
    def get_contract_market_merged(self, symbol):
        """
        :symbol	    "BTC_CW","BTC_NW", "BTC_CQ" ...
        """
        params = {'symbol': symbol}

        url = self.__url + '/market/detail/merged'
        
        return http_get_request(url, params)

    # 获取市场最近成交记录
    def get_contract_trade(self, symbol, size=1):
        """
        :param symbol: 可选值：{ BTC_CW, BTC_NW, BTC_CQ, etc. }
        :return:
        """
        params = {'symbol': symbol,
                  'size': size}

        url = self.__url + '/market/trade'
        return http_get_request(url, params)


