import tweepy
import os
from bayes.dataflow.twitter.constant import TwitterConstant
import pandas as pd
import numpy as np
import json
import time
from bayes.dataflow.twitter.read_kol import Get_DF


class TwitterStatus:
    def __init__(self, api=TwitterConstant.api, twitter_path=TwitterConstant.twitter_path,
                 id_list=TwitterConstant.id_list):
        """
       Constructors
       :param api: twitter api connector
       :param twitter_path:  path of file twitter
       :param id_list: twitter id list
       """
        self.api = api
        self.twitter_path = twitter_path
        self.id_list = id_list

    def check_dir(self, file):
        '''
        :param file: check file dir is exist
        :return: none
        '''
        if not os.path.exists(file):
            os.makedirs(file)

    def check_user(self, name) :
        '''
        check if name is the kol
        :param name: user in id_list
        :return:
        '''
        kol = Get_DF.get_df()['Twitter']
        if name in kol:
            return 'kol'
        else:
            return 'general'

    def author_status(self):
        '''
        get user specified information and users status information
        '''
        extractor = self.api
        for name in self.id_list:
            create_time = []
            text_len = []
            source = []
            retweet_count = []
            favorite_count = []
            text = []
            status_id = []
            file_dir = self.twitter_path + 'message'
            self.check_dir(file_dir)
            write_file = os.path.join(file_dir, name + '.csv')
            position = self.check_user(name)
            for status in tweepy.Cursor(extractor.user_timeline, id=name).items():
                create_time.append(str(status.created_at))
                text_len.append(len(status.text))
                source.append(status.source)
                retweet_count.append(status.retweet_count)
                favorite_count.append(status.favorite_count)
                text.append(status.text)
                status_id.append(status.id_str)

            df = pd.DataFrame()
            df['rank'] = [position for _ in range(len(create_time))]
            df['user'] = [name for _ in range(len(create_time))]
            df['status_id'] = status_id
            df['status'] = text
            df['create_time'] = create_time
            df['status_len'] = text_len
            df['source'] = source
            df['retweet_count'] = retweet_count
            df['favorite_count'] = favorite_count
            df.to_csv(write_file, index=False)
            return df

    def user_info(self):
        '''
        get user information , fans id , friends id
        '''
        api = self.api
        id_list = self.id_list
        for name in id_list:
            dir_path = os.path.join(self.twitter_path, 'user', name)
            self.check_dir(dir_path)
            fans_friends = os.path.join(dir_path, '%s.csv' % name)
            user_info = os.path.join(dir_path, 'user_info.csv')
            info = api.get_user(name)
            position = self.check_user(name)
            user = pd.DataFrame([[position,info.id_str, info.screen_name, info.created_at, info.location,
                                  info.description, info.followers_count, info.friends_count,
                                  info.listed_count, info.favourites_count, info.statuses_count, info.lang]],
                                columns=['rank','id_str',
                                         'screen_name', 'create_at', 'location', 'description', 'followers_count',
                                         'friends_count', 'listed_count',
                                         'favourites_count', 'statuses_count', 'lang'])
            user.to_csv(user_info, index=False)
            followers_info = api.followers_ids(name)
            friends_info = api.friends_ids(name)
            friends_new = friends_info + [None for _ in range(len(followers_info) - len(friends_info))]
            author = [name for _ in range(len(followers_info))]
            social = pd.DataFrame()
            social['author'] = author
            social['followers'] = followers_info
            social['friends'] = friends_new
            social.to_csv(fans_friends, index=False)
            return social

    def get_follower_info(self):
        """
        get followers information
        Due to the rate limit, this function has to sleep for 15 min every 300 response.
        """
        print('loading followers information...')

        for name in self.id_list:
            info_path = os.path.join(self.twitter_path, 'user', name, 'user_followers_info.csv')
            id_str = []
            screen_name = []
            create_at = []
            location = []
            description = []
            position = self.check_user(name)
            for follower in tweepy.Cursor(self.api.followers, id=name).items():
                id_str.append(follower.id_str)
                screen_name.append(follower.screen_name)
                create_at.append(follower.created_at)
                location.append(follower.location)
                description.append(follower.description)
            df = pd.DataFrame()
            df['rank'] = [position for _ in range(len(id_str))]
            df['author'] = [name for _ in range(len(id_str))]
            df['id_str'] = id_str
            df['screen_name'] = screen_name
            df['create_at'] = create_at
            df['location'] = location
            df['description'] = description
            df.to_csv(info_path, index=False)
        return df

    def get_twitter_favorite(self):
        twitter_path = self.twitter_path
        dir_path = twitter_path + 'favorite'
        self.check_dir(dir_path)
        api = self.api
        id_list = self.id_list
        for name in id_list:
            file_path = os.path.join(dir_path, '%s.csv' % name)
            create_time = []
            text_len = []
            source = []
            retweet_count = []
            favorite_count = []
            text = []
            status_id = []
            for status in tweepy.Cursor(api.favorites, id=name).items():
                create_time.append(str(status.created_at))
                text_len.append(len(status.text))
                source.append(status.source)
                retweet_count.append(status.retweet_count)
                favorite_count.append(status.favorite_count)
                text.append(status.text)
                status_id.append(status.id_str)
            df = pd.DataFrame()
            df['user'] = [name for _ in range(len(create_time))]
            df['status_id'] = status_id
            df['status'] = text
            df['create_time'] = create_time
            df['status_len'] = text_len
            df['source'] = source
            df['retweet_count'] = retweet_count
            df['favorite_count'] = favorite_count
            df.to_csv(file_path, index=False)
            return df

    def main(self):
        self.user_info()
        self.author_status()
        self.get_twitter_favorite()


if __name__ == '__main__':
    twitte = TwitterStatus()
    twitte.main()
