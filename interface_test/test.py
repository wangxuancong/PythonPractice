import requests


url = 'http://bayes.tech:8200/api/sentiment/MAN/2018-01-19/2018-11-20'
#url = 'http://bayes.tech:8200/api/basic/MAN/2018-01-19/2018-11-20'
#url = 'http://bayes.tech:8200/api/word/MAN/2018-01-19/2018-11-20'
inf = requests.get(url=url).json()
print(inf)

