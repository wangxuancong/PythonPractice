import sys
import os

fpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(fpath)
from config import HelpFunction
import requests
import time
import pandas as pd
import json
import re


class Save_man():
    out_put = os.path.join(HelpFunction.back_file, 'out_put')
    if not os.path.exists(out_put):
        os.makedirs(out_put)
    today = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    @staticmethod
    def save_sentiment():
        fpath = os.path.join(Save_man.out_put, 'sentiment')
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        url = 'http://bayes.tech:8200/api/sentiment/man/2018-01-19/{today}'.format(today=Save_man.today)
        inf = requests.get(url)
        info = inf.json()
        points = info['data']['all']['trends']
        data_points = {}
        for point in points:
            time = re.findall(r'\d\d\d\d-\d\d-\d\d', point['time'])[0]
            data_points[time] = point['point']
        time_points = list(data_points.items())
        df = pd.DataFrame(time_points, columns=['date', 'sentiment'])
        df.sort_values('date', inplace=True)
        new_index = [i for i in range(df.shape[0])]
        df.index = new_index
        df.reindex
        save_name = os.path.join(fpath, 'man.csv')
        df.to_csv(save_name, index=False)

    @staticmethod
    def save_conersation():
        fpath = os.path.join(Save_man.out_put, 'conversation')
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        url = 'http://bayes.tech:8200/api/word/MAN/2018-01-19/{date}'.format(date=Save_man.today)
        info = requests.get(url).json()
        file = os.path.join(fpath, 'MAN')
        daily_info = info['userCreationsData']
        userCreation = daily_info['userCreationData']
        conversation = daily_info['conversationsData']
        conversationsPer = daily_info['conversationsPerHeadData']
        dayTrends = daily_info['dayTrends']
        weekTrends = daily_info['weekTrends']
        conversation_list = [userCreation, conversation, conversationsPer]
        trends_list = [dayTrends, weekTrends]
        for character in conversation_list:
            file = os.path.join(file, character + '.csv')
            timelist = []
            pointlist = []
            for item in character:
                timelist.append(re.findall(r'\d\d\d\d-\d\d-\d\d', item['time'])[0])
                pointlist.append(item['point'])
            tmp = pd.DataFrame()
            tmp['Date'] = timelist
            tmp['Points'] = pointlist
            if not os.path.exists(file):
                tmp.to_csv(file, index=False, mode='w')
        for trend in trends_list:
            file = os.path.join(file, trend + '.csv')
            timelist = []
            pointlist = []
            for item in trend:
                timelist.append(item['label'])
                pointlist.append(item['point'])
            tmp = pd.DataFrame()
            tmp['Label'] = timelist
            tmp['Points'] = pointlist
            if not os.path.exists(file):
                tmp.to_csv(file, index=False, mode='w')


if __name__ == '__main__':
    Save_man.save_conersation()
