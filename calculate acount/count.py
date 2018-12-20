import pandas as pd
import time

'''
data from 

https://etherscan.io/token/0xe25bcec5d3801ce3a794079bf94adf1b8ccd802d

'''


class Count:
    file = 'from12.02.csv'

    def get_exchange_site(self):

        return {'Gate': ['0x1c4b70a3968436b9a0a9cf5205c787eb81bb558c',
                         '0x0d0707963952f2fba59dd06f2b425ace40b492fe'],
                'Huobi': ['0xfdb16996831753d5331ff813c29a93c76834a0ad',
                          '0xe93381fb4c4f14bda253907b18fad305d799241a',
                          '0x1062a747393198f70f71ec65a582423dba7e5ab3',
                          '0xeee28d484628d41a82d01e21d12e2e78d69920da',
                          '0xadb2b42f6bd96f5c65920b9ac88619dce4166f94',
                          '0x5c985e89dde482efe97ea9f1950ad149eb73829b',
                          '0xab5c66752a9e8167967685f1450532fb96d5d24f',
                          '0x6748f50f686bfbca6fe8ad62b22228b87f31ff2b',
                          '0xfa4b5be3f2f84f56703c42eb22142744e95a2c58',
                          '0x46705dfff24256421a05d056c29e81bdc09723b8'],
                'IDEX': ['0x2a0c0dbecc7e4d658f48e01e3fa353f44050c208 '],
                'Kucoin': ['0x2b5634c42055806a59e9107ed44d43c426e58258']
                }

    def deal_data(self):

        data = pd.read_csv(self.file)

        data['Date'] = data['UnixTimestamp'].apply(lambda x: time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(x)))

        data['Day'] = data['UnixTimestamp'].apply(lambda x: time.strftime('%Y-%m-%d', time.gmtime(x)))

        data['Day'] = data['Day'] = pd.to_datetime(data['Day'])

        data['Week'] = data['Day'].apply(lambda x: x.weekofyear)

        return data

    def classify_by_date(self, start, end):

        data = self.deal_data()

        start_time = pd.to_datetime(start)

        end_time = pd.to_datetime(end)

        interval = data.loc[(data['Day'] >= start_time) & (data['Day'] <= end_time)]

        return interval

    def count_amount_quantity(self, start, end):

        interval_data = self.classify_by_date(start, end)

        amount_all = interval_data.shape[0]

        quantity_all = interval_data['Quantity'].sum()

        exchange_site = self.get_exchange_site()

        score = {}

        for _, exchange in enumerate(exchange_site):

            score[exchange] = []

            from_a, to_a, from_q, to_q = 0, 0, 0, 0

            for site in exchange_site[exchange]:
                from_table = interval_data.loc[interval_data['From'] == site]

                to_table = interval_data.loc[interval_data['To'] == site]

                from_amount_all = from_table.shape[0]

                from_quantity_all = from_table['Quantity'].sum()

                to_amount_all = to_table.shape[0]

                to_quantity_all = to_table['Quantity'].sum()

                from_a += from_amount_all

                from_q += from_quantity_all

                to_a += to_amount_all

                to_q += to_quantity_all

            all_amount = from_a + to_a

            all_quantity = from_q + to_q

            score[exchange].append(all_amount)

            score[exchange].append(all_quantity)

        return amount_all, quantity_all, score

    def count_threshold(self, start, end, threshould):

        interval_data = self.classify_by_date(start, end)

        th_table = interval_data.loc[interval_data['Quantity'] > threshould]

        amount = th_table.shape[0]

        quantity = interval_data['Quantity'].sum()

        day_range = '%s_%s' % (start, end)

        file = day_range + '_threshould.csv'

        df = pd.DataFrame()

        df[day_range] = day_range

        df['amount'] = [amount]

        df['quantity'] = [quantity]

        df.to_csv(file, index=False)

    def save_data(self, start, end):

        amount_all, quantity_all, score = self.count_amount_quantity(start, end)

        day_range = '%s_%s' % (start, end)

        file_cla = day_range + '_classfiy.csv'

        file_exchange = day_range + '_exchange.csv'

        df1 = pd.DataFrame()

        df1[day_range] = day_range

        df1['amount'] = [amount_all]

        df1['quantity'] = [quantity_all]

        df1.to_csv(file_cla, index=False)

        exchange_table = pd.DataFrame(score, index=['amount','quanlity'])

        exchange_table.to_csv(file_exchange)

    def main(self, start, end, threshould=None):

        self.save_data(start, end)

        if threshould != None:

            self.count_threshold(start, end, threshould)


if __name__ == '__main__':
    start = '2018-12-10'
    end = '2018-12-16'
    threshould = ''
    count = Count()
    count.main(start,end,120000)