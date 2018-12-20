import os

from Matrix.Goldbach.Arim.bin import ArimaModel
import os
import numpy as np
import pandas as pd
from pandas import Series as sr
import logging
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(module)s  %(funcName)s [%(lineno)s] %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename="Arima_log",
                    filemode="a"
                    )

coin_file = '../input_data/top100_data'
coins_name = os.listdir(coin_file)



class Maba(object):



    # get coin abs path and coin name
    def train_path(self):

        csv_list = []   # 每种货币的绝对路径
        for i in coins_name:
            csv_list.append(os.path.join(os.path.abspath('../'),'input_data','top100_data',i))
        return csv_list

    def train(self):


        csvs = self.train_path()
        # computed = self.get_compute()
        tmp = [i for i in range(5)]    # 数数范围
        p,q  = tmp[0::1],tmp[0::1]
        for n,i in enumerate(csvs):
            result = pd.DataFrame(columns=['p', 'd', 'q', 'error'])
            option = {}
            pt = []
            qt = []
            dt = []
            e = []
            for j  in tmp:
                for k in tmp:
                    test = 0
                    option['p'] = j
                    option['q'] = k
                    ar = ArimaModel.Ar_model(i,is_normalization=True)
                    option['d'] = ar.check()
                    try:
                        error,_ = ar.forecasting(option)
                    except Exception as er :
                        test= 1
                        logging.info('The coin is :%s, p is: %s,q is: %s ,d is :%s'%(i,option['p'],option['q'],option['d']))
                        logging.error(er)
                    if test == 0:
                        pt.append(option['p'])
                        qt.append(option['q'])
                        dt.append(option['d'])
                        e.append(option['error'])
            result['p'] = pt
            result['d'] = dt
            result['q'] = qt
            result['error'] = e
            save_path = os.path.join('../', 'result', coins_name[n].strip('.csv'), coins_name[n].strip('.csv'))
            result.sort_values(by='error')
            para = result.iloc[0]
            dir_path = os.path.join('../', 'result',coins_name[n].strip('.csv'))
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            para.to_csv(save_path,mode='w',header=False)

        # get coins name of suit to Arima
    def get_compute(self):

        coin_file = '../result'
        compute_list = os.listdir(coin_file)
        return compute_list
    def is_suit(self):

        compute_coins = self.get_compute()

        coin_name = [i.strip('.csv') for i in coins_name]
        not_suit = list(set(coin_name).difference(set(compute_coins)))

        return not_suit
    def is_plt(self):

        coin = coins_name
        para_path = [os.path.join('../', 'result', coin[i].strip('.csv'), coin[i].strip('.csv')) for i in coin]
        # for i in coin:
        #     file_path.append(os.path.join('../', 'result', coin[i].strip('.csv'), coin[i].strip('.csv')))
        # get best data parameters
        for i in para_path:
            option = {}
            with open(i[0], 'r') as f:
                f = f.read().split('\n')
                option['p'] = int(f[0][-2])
                option['d'] = int(f[1][-2])
                option['q'] = int(f[2][-2])
                error, forecasting  =ArimaModel.Ar_model(is_normalization=True).forecasting(option)

                plt.figure(figsize=(20,10))



a = Maba().train()
b = a.is_suit()





















