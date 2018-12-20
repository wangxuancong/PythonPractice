from cryptocmd import CmcScraper
import os

coin_list = ['BTC','XRP','ETH','BCH','XLM','EOS','LTC','USDT','ADA','XMR','TRX',
             'DASH','MIOTA','BNB','XEM']


back_path = os.path.dirname(os.path.abspath(__file__))

for coin in coin_list:
    data = CmcScraper(coin)
    data = data.get_dataframe()
    file = os.path.join(back_path,'input',coin+'.csv')
    data.to_csv(file,index=False)


