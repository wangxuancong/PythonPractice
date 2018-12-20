from PythonCoding.exchange.huobi_exchange.HuobiDMService import HuobiDM
from pprint import pprint

#### input huobi_exchange dm url
URL = 'https://api.hbdm.com'

####  input your access_key and secret_key below:
ACCESS_KEY = 'b7272d78-4ab92c81-6c3d3844-138fe'
SECRET_KEY = '93afe8cb-995efc05-ab48eb28-dc117'

dm = HuobiDM(URL, ACCESS_KEY, SECRET_KEY)

#### another account:
# dm2 = HuobiDM(URL, "ANOTHER ACCOUNT's ACCESS_KEY", "ANOTHER ACCOUNT's SECRET_KEY")

# %%  market data api ===============

# print(u' 获取合约信息 ')
# pprint(dm.get_contract_info(symbol="BTC", contract_type="quarter"))
# pprint(dm.get_contract_info(contract_code="BTC181228"))
#
# print(u' 获取合约指数信息 ')
# pprint(dm.get_contract_index("BTC"))
#
# print(u' 获取合约最高限价和最低限价 ')
# pprint(dm.get_contract_price_limit(symbol='BTC', contract_type='quarter'))
# pprint(dm.get_contract_price_limit(contract_code='BTC181228'))

# print(u' 获取当前可用合约总持仓量 ')
# pprint(dm.get_contract_open_interest(symbol='BTC', contract_type='quarter'))
# pprint(dm.get_contract_open_interest(contract_code='BTC181228'))


print(u' 获取K线数据 ')
pprint(dm.get_contract_kline(symbol='BTC_CW', period='60min', size=20))

