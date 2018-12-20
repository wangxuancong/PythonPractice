import sys
import os
fpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(fpath)
from pra_g.PythonCoding.interface_test.config import HelpFunction
import requests
import time
import pandas as pd
import json
import re

class GetData(object):
    out_put = os.path.join(HelpFunction.back_file,'out_put')
    if not os.path.exists(out_put):
        os.makedirs(out_put)
    today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    earliest = HelpFunction.get_date()
    @staticmethod
    def save_sentiment():
        fpath = os.path.join(GetData.out_put,'sentiment')
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        for coda in GetData.earliest.items():
            coin = coda[0]
            start = coda[1]
            url = HelpFunction.get_sentiment('MAN','2018-01-19')
            info = requests.get(url).json()
            while info['status'] == 0:
                points = info['data']['trends']
                data_points = {}
                for point in points:
                    time = re.findall(r'\d\d\d\d-\d\d-\d\d',point['time'])[0]
                    data_points[time] = point['point']
                time_points = list(data_points.items())
                df = pd.DataFrame(time_points,columns=['date','sentiment'])
                df.sort_values('date',inplace=True)
                new_index = [i for i in range(df.shape[0])]
                df.index = new_index
                df.reindex
                save_name = os.path.join(fpath,coin,'csv')
                df.to_csv(save_name,index=False)
    @staticmethod
    def save_words():
        fpath = os.path.join(GetData.out_put,'words')
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        url = 'http://bayes.tech:8200/api/word/MAN/2018-01-19/2018-11-20'
        info = requests.get(url).json()
        file = os.path.join(fpath,'man.csv')


        print(info.text)
    @staticmethod
    def save_chats():
        url = 'http://bayes.tech:8200/api/basic/AGI/2017-10-01/2018-11-20/'
        info = requests.get(url)
        print(info.text)








if __name__ == '__main__':
    #GetData.save_sentiment()
    GetData.save_words()








