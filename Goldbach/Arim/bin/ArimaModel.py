
'''
功能
        1. 断是否是稳定数据， ADT 值
        2. 预测数据
        3 .数据处理
'''

import pandas as pd
from pandas.tools.plotting import outer
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error as mse
import matplotlib.pyplot as plt
import logging

class Ar_model(object):

    def __init__(self,file,column='Open' ,rate = 0.8,is_normalization = False):

        self.file = file
        self.rate  = rate
        self.column = column
        self.is_normalization = is_normalization
        self.data = self._get_data()
        self.train,self.test = self._data_set()
    def _get_data(self):

        data = pd.read_csv(self.file)
        data.columns = ["Date","Open","High","Low","Close","Volume","Market Cap"]
        data['Date'] = pd.to_datetime(data['Date'])
        data.sort_values('Date',inplace=True)
        data.index = data.Date
        return data
    # split train data
    def _data_set(self,normalization = False):

        data = self.data

        if normalization == True:

            data[self.column].astype('float64')
            data[self.column] = (data[self.column] - data[self.column].mean()) / data[self.column].std()

        data = data.loc[:, [self.column]]

        train_num = int(data.shape[0] * self.rate)

        train_set,test_set = data.iloc[:train_num] ,data.iloc[train_num:]

        train_set = [i[0] for i in train_set.values]

        test_set  = [i[0] for i in test_set.values]

        return train_set,train_set

    def num(self):

        data = self.data
        data[self.column].astype('float64')
        data[self.column] = (data[self.column]-data[self.column].mean()) / data[self.column].std()
        mean = data[self.column].mean()
        std = data[self.column].std()

        return mean,std

    def revivification(self,prediction):

        mean ,std = self.num()

        pre = [(i*std)+mean for i in prediction]

        return pre

    def forecasting(self,option):

        prediction = []
        train, test = self.train,self.test

        history = train.copy()

        # 几个参数  p d q disp
        for i in range(len(test)):
            model = ARIMA(history, order=(option['p'], option['d'], option['q']))  # Arima 模型的参数是一个 list
            model_fit = model.fit(disp=0.1)
            output = model_fit.forecast() # 默认是一天
            yhat = output[0]
            prediction.append(yhat)
            obs = test[i]
            history.append(obs)
            # print('predicted = %f,expected = %f' % (yhat, obs))

        if self.is_normalization == True:
            prediction = self.revivification(prediction)
            test = self.revivification(test)
        error = mse(test, prediction)
        option['error'] = error
        print('Test MSE:%.3f' % error)
        return error,prediction
        # plt.figure(figsize=(18, 9))
        # plt.plot(test_np, label='test')
        # plt.plot(prediction, color='red', label='forecast')
        # plt.show()
    def check(self):  # 假设检验
        train_set = self.train
        # train_set = [ i[0] for i in train_set]
        result = adfuller(train_set)
        if result[0] < result[4]['1%']:
            return 0
        elif result[4]['5%'] > result[0] > result[4]['1%']:
            return 1
        else:
            return 2




















