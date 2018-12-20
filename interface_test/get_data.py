from cryptocmd import CmcScraper
import os


scrawler = CmcScraper('BTC')

data = scrawler.get_dataframe()

save = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'data','interface','data','BTC.csv')

data.to_csv(save,index=False)

print('over......')
