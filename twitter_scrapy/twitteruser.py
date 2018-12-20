import tweepy
import os
from bayes.dataflow.twitter.constant import TwitterConstant


class TwitterUser:
    def __init__(self, api=TwitterConstant.api, twitter_path=TwitterConstant.twitter_path,
                 id_list=TwitterConstant.id_list):
        """
        Constructors
        :param api: twitter_scrapy api connector
        :param twitter_path: path of file twitter_scrapy
        :param id_list: twitter_scrapy id list
        """
        self.api = api
        self.twitter_path = twitter_path
        self.id_list = id_list

    @staticmethod
    def init_data(twitter_path, dir_path, id_path):
        """
        initialize date path
        :param twitter_path: path of file twitter_scrapy
        :param dir_path: path of directory message
        :param id_path: path of file id
        :return:
        """
        if not os.path.exists(twitter_path):
            os.mkdir(twitter_path)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        if not os.path.exists(id_path):
            os.mkdir(id_path)
        return

    @staticmethod
    def get_user_info(name, id_path, api):
        """
        get users information
        :param name: user id
        :param id_path: path of file user id
        :param api: twitter_scrapy api connector
        :return:
        """
        info_path = id_path + 'user_info.txt'
        if os.path.exists(info_path):
            print('%s already exist user information' % name)
            return
        else:
            new_file = open(info_path, 'w')
            new_file.close()
        file = open(info_path, 'r+', encoding='utf-8')
        file.seek(0, 0)
        info = api.get_user(name)
        content = '%s\n%s\n%s\n%s\n%s\n' % (info.id_str, info.screen_name, info.created_at,
                                            info.location, info.description)
        file.write(content)
        file.close()
        print('%s user information done' % name)
        return

    @staticmethod
    def get_id_list(name, id_path, api):
        """
        get friends and followers id list of the target user
        :param name: user id
        :param id_path: path of file user id
        :param api: twitter_scrapy api connector
        :return:
        """
        follower_path = id_path + 'follower_id_list.txt'
        friend_path = id_path + 'friend_id_list.txt'
        if os.path.exists(follower_path):
            os.remove(follower_path)
        follower_file = open(follower_path, 'w')
        follower_file.close()
        friend_file = open(friend_path, 'w')
        friend_file.close()
        followers = api.followers_ids(name)
        friends = api.friends_ids(name)
        file = open(follower_path, 'r+', encoding='utf-8')
        file.seek(0, 0)
        for follower in followers:
            content = str(follower) + '\n'
            file.write(content)
        print('%s user followers id list done' % name)
        file.close()
        file = open(friend_path, 'r+', encoding='utf-8')
        file.seek(0, 0)
        for friend in friends:
            content = str(friend) + '\n'
            file.write(content)
        print('user friends id list done')
        file.close()

    @staticmethod
    def get_follower_info(name, id_path, api):
        """
        get followers information
        Due to the rate limit, this function has to sleep for 15 min every 300 response.
        :param name: user id
        :param id_path: path of file user id
        :param api: twitter_scrapy api connector
        :return:
        """
        print('loading followers information...')
        info_path = id_path + 'user_followers_info.txt'
        if os.path.exists(info_path):
            os.remove(info_path)
        new_file = open(info_path, 'w')
        new_file.close()
        file = open(info_path, 'r+', encoding='utf-8')
        file.seek(0, 0)
        # use cursor to traverse followers information list, get data
        # rate limit: get 300 response, this project has to sleep for 15 min
        for follower in tweepy.Cursor(api.followers, id=name).items():
            content = '%s\t%s\t%s\t%s\t%s\n' % (follower.id_str, follower.screen_name, follower.created_at,
                                                follower.location, follower.description)
            file.write(content)
        print('user followers information done')
        file.close()
        return

    def upgrade_user_data(self):
        twitter_path = self.twitter_path
        dir_path = twitter_path + 'user/'
        id_list = self.id_list
        api = self.api
        # For every id in the id list, get their user information, followers and friends id list.
        for name in id_list:
            print('%s:' % name)
            id_path = dir_path + '%s/' % name
            self.init_data(twitter_path, dir_path, id_path)
            self.get_user_info(name, id_path, api)
            self.get_id_list(name, id_path, api)
            # too much time for running the function
            # self.get_follower_info(name, id_path, api)
            print('%s user data done')
        return


if __name__ == '__main__':
    print('start')
    c = TwitterUser()
    # upgrade data related to users
    c.upgrade_user_data()

