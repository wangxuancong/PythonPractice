from PythonCoding.bit_cla.func import Pulic_function as pf
import pandas as pd
import os
from PythonCoding.constant import Constant


class Label:

    all_data = os.path.join(Constant.data_path, 'bit_cla', 'output', 'all_data.csv')

    origin_data = pd.read_csv(all_data)

    def get_mins_data(self):
        '''
        split data in some steps
        :return:
        '''
        steps = pf.get_step()

        all_data = self.origin_data

        file_list = []

        for min, step in steps.items():

            df = pf.read_step(all_data, 0, step)

            write_file = os.path.join(Constant.data_path, 'bit_cla', 'output', min + 's.csv')

            file_list.append(write_file)

            df.to_csv(write_file, index=False)

        return file_list

    def split_train_test(self, df, window, ratio):
        '''
        :param df: dateframe
        :param step: length of each set
        :param ratio: the proportion of all data sets
        :return: all original data split in train set and test set
        '''

        length = df.shape[0]

        remainder = length % window

        data = df[:-remainder]

        train_num, train_set = pf.split_data(data, "Price", ratio)

        test_set = data[train_num:-remainder]

        return train_set, test_set

    def to_json(self,data, window,classify = None):
        '''
        :param data  dataframe.columns = ['Date','Price','trend']
        :param step
        :return: data like { ['2013-04-29 00:05:01' - '2013-04-29 00:15:01']:[[ ten numbers ],[label]].....}
        '''

        da_va = data.values

        if classify == 2 :

            trend = [trend[1] for trend in data['trend'].values]

        else:

            trend = [trend for trend in data['trend'].values]

        final_data = {}

        time_list = []

        price_list = []

        for index in range(len(da_va)):

            time_list.append(da_va[index][0])

            price_list.append(da_va[index][1])

            if index == len(trend) - 1:

                return final_data

            if (index + 1) % window == 0:

                key = time_list[0] + ' to ' + time_list[-1]

                final_data[key] = [[price_list], trend[index + 1]]

                time_list = []

                price_list = []

    # def get_train_set(self,data,kind):
    #     '''
    #     :param data:  type(da ta) == json
    #     :return:
    #     '''
    #     labels = pf.get_labe()
    #
    #     classify = {}
    #
    #     if kind == 2:
    #
    #         for label in labels:
    #
    #             classify[label[1]] = []
    #     else:
    #         for label in labels:
    #
    #             classify[label] = []
    #
    #     for key, value in data.items():
    #
    #         tmp_label = value[1]
    #
    #         classify[tmp_label].append(value[0])
    #
    #     train_set = classify.values()
    #
    #     return list(train_set)

    def main(self, window,ratio,classify):

        train, test = self.split_train_test(self.origin_data, window, ratio)

        train_set, test_set = self.to_json(train, window,classify), self.to_json(test, window,classify)

        # cla_train = self.get_train_set(train_set)

        train_data = [data[0] for data in train_set.values()]

        train_label = [data[1] for data in train_set.values()]

        test_label = [labels[1] for labels in test_set.values()]

        test_data = [data[0] for data in test_set.values()]

        data = {'train_data': train_data,

                'train_label': train_label,

                'test_data': test_data,

                'test_label': test_label}

        return data
