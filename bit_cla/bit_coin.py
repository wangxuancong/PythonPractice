from cryptocmd import CmcScraper

sa  = CmcScraper('BTC')

data = sa.get_dataframe()

data.to_csv('bit.csv',index=False)