import logging
import os

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s [%(lineno)s] %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename="wrong",
                    filemode="a"
                    )



coin_file = '../input_data/top100_data'
coin_list = os.listdir(coin_file)   # 货币的种类
csv_list = []   # 每种货币的绝对路径
for i in coin_list:
    csv_list.append(os.path.join(os.path.abspath('../'),'input_data','top100_data',i))
i = 1
file = os.path.join('../', 'result', coin_list[i].strip('.csv'), coin_list[i].strip('.csv'))
print(file)

