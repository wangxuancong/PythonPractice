import pandas as pd
import os


class Get_DF:
    @staticmethod
    def get_df():
        up_path = os.path.dirname(os.path.abspath(__file__))

        file = os.path.join(up_path, 'kol.txt')

        with open(file, 'r')as f:

            lines = f.readlines()

        data = []
        
        for num, text in enumerate(lines):
            if num == 0:
                column = text.split('\t')
                column[-1] = column[-1].split('\n')[0]
            else:
                data.append(text.split('\t'))
                data[num - 1][-1] = data[num - 1][-1].split('\n')[0]

        kol_df = pd.DataFrame(data=data, columns=column)

        names = kol_df['Twitter']

        file = os.path.join(os.path.dirname(os.path.abspath(__file__)),'id_list.txt')

        with open(file, "a+", encoding='utf-8') as f :

            for name in names:

                f.write('%s\n'%name )

        return kol_df

Get_DF.get_df()