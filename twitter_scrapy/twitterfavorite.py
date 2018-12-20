import tweepy
import os
from bayes.dataflow.twitter.constant import TwitterConstant


class TwitterFavorite:
    def __init__(self, api=TwitterConstant.api, twitter_path=TwitterConstant.twitter_path,
                 id_list=TwitterConstant.id_list):
        self.api = api
        self.twitter_path = twitter_path
        self. id_list = id_list

    @staticmethod
    def init_data(twitter_path, dir_path):
        if not os.path.exists(twitter_path):
            os.mkdir(twitter_path)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        return

    @staticmethod
    def get_exist_date(file_path, file):
        """
        get latest date of existing data
        :param file_path: path of target file
        :param file: target file
        :return:
        """
        if not os.path.getsize(file_path):
            return None
        lines = file.readlines()
        date = lines[0][0:19]
        return date

    def get_twitter_favorite(self):
        twitter_path = self.twitter_path
        dir_path = twitter_path + 'favorite/'
        self.init_data(twitter_path, dir_path)
        api = self.api
        id_list = self.id_list
        for name in id_list:
            file_path = dir_path + '%s.txt' % name
            if not os.path.exists(file_path):
                new_file = open(file_path, 'w')
                new_file.close()
            file = open(file_path, 'r+', encoding='utf-8')
            file.seek(0, 0)
            print('upgrading message data of %s...' % name)
            exist_date = self.get_exist_date(file_path, file)
            # use cursor to traverse history favorite tweets of the target user, get data
            for status in tweepy.Cursor(api.favorites, id=name).items():
                content = '%s\t%s\t%s\n' % (status.created_at, status.id_str, status.text)
                date = str(status.created_at)
                # check whether current date have reached existing date
                if not date == exist_date:
                    file.write(content)
                else:
                    print('%s favorite data are up to date' % name)
                    break
            file.close()
        return


if __name__ == '__main__':
    c = TwitterFavorite()
    # get favorite message data according to the id list
    c.get_twitter_favorite()
