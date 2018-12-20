'''
This api is a data feature engineering to ascending dimension，split data in some ways ,
all of function named by usage

'''

import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import preprocessing
import time



class DEF(object):
    def __init__(self,stock_name = None):
        self.stock_name = stock_name
        try:
            self.data = pd.read_csv(self.stock_name)
        except FileExistsError:
            print("read data error ")

    def read_Data(self):

        return self.data
    # 按时间排序
    def reshape_date(self):
        pass

    # 协方差计算
    def the_correlation(self,feature,feature2 = None,plt = False) -> 'DataFrame':
        corr_matrix = self.data.corr()
        if plt == True:
            self.data.plot(kind = 'scatter ',x = feature,y = feature2 ,alpha = 0.1)
            plt.show()
        return corr_matrix[feature].sort_values(ascending = False)
    # 数据集划分
    def data_split(self) -> 'DataFrame' :
        train_data ,test_data = train_test_split(self.data,test_size=0.2,random_state=42)
        return train_data,test_data

    # new_column -> new data
    # note : new_column must fit self.data
    def add_feature(self,feature_name,new_column):
        try:
            self.data[feature_name] = new_column
        except :
            print("new_feature error ")
        return self.data.to_csv(self.stock_name,index=False)

    def map_season(self,month):
        month_dic = {1: 1, 2: 1, 3: 2, 4: 2, 5: 3, 6: 3, 7: 3, 8: 3, 9: 3, 10: 4, 11: 4, 12: 1}
        return month_dic[month]
    def add_timedate(self):
        # date = self.read_Data()['Date'].tolist()
        # weekday = [str(time.strptime(i, '%Y-%m-%d').tm_wday) for i in date]
        # mon  = [str(time.strptime(i, '%Y-%m-%d').tm_mon) for i in date]
        # mday = [str(time.strptime(i, '%Y-%m-%d').tm_mday) for i in date]
        # feature = {'weekday':weekday,
        #            'mon':mon,
        #            'mday':mday
        #            }
        # for i in feature:
        #     self.add_feature(i,feature[i])
        self.data.columns = ["Date", "Open", "High", "Low", "Close", "Volume", "Market Cap"]
        data = self.data
        data['Date'] = pd.to_datetime(data['Date'])
        data['dayofweek'] = data['Date'].apply(lambda x: x.dayofweek)
        data['dayofyear'] = data['Date'].apply(lambda x: x.dayofyear)
        data['dayofmon'] = data['Date'].apply(lambda x: x.day)
        data['month'] = data['Date'].apply(lambda x: x.month)
        data['year'] = data['Date'].apply(lambda x: x.year)
        data['weekofyear'] = data['Date'].apply(lambda x: x.weekofyear).astype('str')
        if 'month' in data.columns.values:
            data['season'] = data['month'].apply(lambda x: self.map_season(x))
#        data.to_csv(self.stock_name,index=False)
    def add_math_index(self):
        data = self.data
        if 'month' not in data.columns.values:
            data['season'] = data['month'].apply(lambda x: self.map_season(x))
            data.to_csv(self.stock_name,index=False)

        data['daily_mean'] = (data['High'] + data['Low']) / 2
        #　To calculate each week
        week_state = data.groupby(by=['year', 'weekofyear'])[['Date', 'High', 'Low']].agg(['mean', 'std'])
        week_state.columns = week_state.columns.droplevel(0)
        week_state = week_state.reset_index()
        week_state.columns = ['year', 'weekofyear', 'w_h_m', 'w_h_s', 'w_l_m', 'w_l_s']

        month_state = data.groupby(by=['year', 'month'])[['Date', 'High', 'Low']].agg(['mean', 'std'])
        month_state.clumns = month_state.columns.droplevel(0)
        month_state = month_state.reset_index()
        month_state.columns = ['year', 'month', 'm_h_m', 'm_h_s', 'm_l_m', 'm_l_s']

        season_state = data.groupby(by=['year', 'season'])[['Date', 'High', 'Low']].agg(['mean', 'std'])
        season_state.columns = season_state.columns.droplevel(0)
        season_state = season_state.reset_index()
        season_state.columns = ['year', 'season', 's_h_m', 's_h_s', 's_l_m', 's_l_s']

        data = pd.merge(data, week_state[['year', 'weekofyear', 'w_h_m', 'w_h_s', 'w_l_m', 'w_l_s']], how='inner',
                        on=['year', 'weekofyear'])
        data = pd.merge(data, month_state[['year', 'month', 'm_h_m', 'm_h_s', 'm_l_m', 'm_l_s']], how='inner',
                        on=['year', 'month'])
        data = pd.merge(data, season_state[['year', 'season', 's_h_m', 's_h_s', 's_l_m', 's_l_s']], how='inner',
                        on=['year', 'season'])
        data.to_csv(self.stock_name,index = False)
    def add_rate(self):
        pass














