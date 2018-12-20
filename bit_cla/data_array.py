import pandas as pd
import os
from datetime import datetime
import numpy as np
from PythonCoding.bit_cla.func import Pulic_function as pf


class All_Data:

    '''

    put all datas by time line into data_dir

    this class make all daily data merge into a big table

    '''

    data_dir = '/Users/yif_z/Yif/pra_g/PythonCoding/data/bit_cla/input'

    def sort_date(self):

        file_list = os.listdir(self.data_dir)
        file = [file.split('.csv')[0] for file in file_list]
        date_list = [datetime.strptime(date, "%Y-%m-%d") for date in file]
        return sorted(date_list)

    def sort_file(self):

        date_list = self.sort_date()
        files = [datetime.strftime(date, "%Y-%m-%d") + '.csv' for date in date_list]
        up_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_file = [os.path.join(up_dir, 'data', 'bit_cla', 'input', file) for file in files]
        return data_file

    def merge_all(self):

        time_serise = []

        price_list = []

        for file in self.sort_file():

            tmp = pd.read_csv(file)

            for date in tmp['Date'].values:

                time_serise.append(date)

            for price in tmp['Price'].values:

                price_list.append(price)

        data = pd.DataFrame()
        
        data['Date'] = time_serise
        
        data['Price'] = price_list
        
        data['shift_1'] = data['Price'].shift(1)
        
        data.dropna(axis=0, inplace=True)
        
        data['residual'] = data['Price'] - data['shift_1']
        
        data['rate'] = (data['Price'] - data['shift_1']) / data['shift_1']
        
        ra = data['rate'].values
        
        trend = [pf.label(i) for i in ra]
        
        data['trend'] = trend
        
        up_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        save_dir = os.path.join(up_dir, 'data', 'bit_cla', 'output')
        
        if not os.path.exists(save_dir):
            
            os.makedirs(save_dir)
            
        save_file = os.path.join(save_dir, 'all_data.csv')
        
        data.to_csv(save_file, index=False)


All_Data().merge_all()
