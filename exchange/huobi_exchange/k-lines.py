from PythonCoding.exchange.huobi_exchange.huobiservice import Huobi
from pprint import pprint

'''
"BTC_CW"表示BTC当周合约
"BTC_NW"表示BTC次周合约
"BTC_CQ"表示BTC季度合约
'''


URL = 'https://api.hbdm.com'
'https://api.huobipro.com/'
dm = Huobi()

# print(u' 获取K线数据 ')

respons = dm.get_contract_kline(symbol='MAN_CW', period='1week', size=1)

pprint(respons)

'''
{'ch': 'market.BTC_CW.kline.1week',
 'data': [{'amount': 18251.1284226161,
           'close': 3227.16,
           'count': 17888,
           'high': 3248.97,
           'id': 1544976000,
           'low': 3170,
           'open': 3209.67,
           'vol': 585026}],
 'status': 'ok',
 'ts': 1545037558536}

 
 "data": [
{
    "id": K线id（时间戳）,
    "amount": 成交量,
    "count": 成交笔数,
    "open": 开盘价,
    "close": 收盘价,当K线为最晚的一根时，是最新成交价
    "low": 最低价,
    "high": 最高价,
    "vol": 成交额, 即 sum(每一笔成交价 * 该笔的成交量)
  }
]
'''
print('------------------------------------------------')

respons = dm.get_contract_trade(symbol='MAN_CWW', size=1)

pprint(respons)
'''

{'ch': 'market.BTC_CW.trade.detail',
 'status': 'ok',
 'tick': {'data': [{'amount': '40',
                    'direction': 'sell',
                    'id': 206941574105213288,
                    'price': '3228',
                    'ts': 1545037559415}],
          'id': 1545037559482,
          'ts': 1545037559482},
 'ts': 1545037559482}
 
 
"tick": {
    "id": 消息id,
    "ts": 最新成交时间,
    "data": [
      {
        "id": 成交id,
        "price": 成交价钱,
        "amount": 成交量,
        "direction": 主动成交方向,
        "ts": 成交时间
      }
    ]
  }

'''
print('------------------------------------------------')

respons = dm.get_contract_market_merged(symbol='MAN_CW')

pprint(respons)

'''

{'ch': 'market.BTC_CW.detail.merged',
 'status': 'ok',
 'tick': {'amount': '26504.3720657652828169268627818831988717942',
          'ask': [3229.9, 34],
          'bid': [3227.18, 5],
          'close': '3229.3',
          'count': 25463,
          'high': '3248.97',
          'id': 1545037560,
          'low': '3170',
          'open': '3209.67',
          'ts': 1545037560379,
          'vol': '850478'},
 'ts': 1545037560379}
 


"tick": {
    "id": K线id（时间戳）,
    "amount": 成交量,
    "count": 成交笔数,
    "open": 开盘价,
    "close": 收盘价,当K线为最晚的一根时，是最新成交价
    "low": 最低价,
    "high": 最高价,
    "vol": 成交额, 即 sum(每一笔成交价 * 该笔的成交量)
    "bid": [买1价,买1量],
    "ask": [卖1价,卖1量]
  }
'''
