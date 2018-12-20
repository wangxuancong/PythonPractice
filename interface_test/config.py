import os
import datetime
import time


class HelpFunction:
    today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    back_file = os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def get_sentiment(coin, start):
        return 'http://bayes.tech:8200/api/sentiment/{coin}/{start}/{end}'.format(coin=coin, start=start,
                                                                                  end=HelpFunction.today)

    @staticmethod
    def get_words(coin, start):
        return 'http://bayes.tech:8200/api/word/{coin}/{start}/{end}'.format(coin=coin, start=start,
                                                                             end=HelpFunction.today)

    @staticmethod
    def get_chat(coin, start):
        return 'http://bayes.tech:8200/api/basic/{coin}/{start}/{end}'.format(coin=coin, start=start,
                                                                              end=HelpFunction.today)

    @staticmethod
    def time_list(starttime, endtime):
        datestart = datetime.datetime.strptime(starttime, '%Y-%m-%d')
        dateend = datetime.datetime.strptime(endtime, '%Y-%m-%d')
        datelist = []
        datelist.append(datestart.strftime('%Y-%m-%d'))
        while datestart < dateend:
            datestart += datetime.timedelta(days=+1)
            datelist.append(datestart.strftime('%Y-%m-%d'))
        return datelist

    @staticmethod
    def get_date():
        file = '36.csv'
        # class Earlist:
        #     def get_item(self):
        with open(file) as f:
            lines = f.readlines()
        earliest = {}
        coins = [i.strip().split(' ')[0] for i in lines]
        date = [i.strip().split(' ')[1] for i in lines]
        for i in range(len(coins)):
            earliest[coins[i]] = date[i]
        return earliest


print(HelpFunction.back_file)
