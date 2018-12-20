import numpy as np

class Pulic_function:

    # label type
    @staticmethod
    def get_labe():
        return ['1+', '2+', '3+', '1-', '2-', '3-']

    @staticmethod
    def label(value):

        if 0 <= value <= 0.003:
            return '1+'
        elif 0.003 < value < 0.01:
            return '2+'
        elif value > 0.003:
            return '3+'
        elif -0.003 <= value <= 0:
            return '1-'
        elif -0.01 < value < -0.003:
            return '2-'
        else:
            return '3-'

    # calculate change rate compare to previous time
    @staticmethod
    def rate(df, newname, column1, column2):

        df[newname] = (df[column1] - df[column2]) / df[column2]

        return df[newname]

    # calculate residual compare to previous time
    @staticmethod
    def residual(df, newname, column1, column2):

        df[newname] = df[column1] - df[column2]
        return df[newname]

    @staticmethod
    def read_step(df, start, step):

        return df.loc[start::step]

    @staticmethod
    def label_type():

        return ['1-', '2-', '3-', '1+', '2+', '3+']

    @staticmethod
    def log_columns(df, col1, col2):

        fun = lambda x: np.log(x)

        df[col2] = df[col1].apply(fun)

    @staticmethod
    def get_step():

        return {'5min': 1, '15min': 3, '30min': 6, '1h': 12, '4h': 12 * 4, '8h': 12 * 8, '12h': 12 * 12,
                '24h': 12 * 24}

    @staticmethod
    def classify_data(data, label):

        return data.loc[data.loc[:, 'trend'] == label, :]

    @staticmethod
    def split_data(df, column, rate):

        length = df.shape[0]
        train = int(length * rate)
        train_set = df[['Date', column, 'trend']][:train]

        return train, train_set
