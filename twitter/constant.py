from bayes.ailib.constant import Constant
import tweepy


class TwitterConstant:
    absolute_path = Constant.absolute_path
    data_path = absolute_path + 'data/'
    twitter_path = data_path + 'twitter/'
    list_path = absolute_path + 'dataflow/twitter/id_list.txt'
    consumer_key = 'DAg0TYh9D8lYObJbYKmYdZhZL'
    consumer_secret = 'E52C5xeDZYEu1V1dpqHf6ZylBaBT73wbFccWGDyDMtVwJEl24F'
    access_token = '1058184258387271680-9xXH1jUXTBbw6LEiLTeP5hK9yrvmFU'
    access_secret = 'oSxUhLAFZJjcHOwAbjNMiNU5Oz6U0OGGr9b8Yg67NtRLf'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    proxy = '127.0.0.1:42951'
    # wait_on_rate_limit is True: if the client reach rate limit, it will wait for 15 min and restart
    api = tweepy.API(auth, compression=True, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True, proxy=proxy)
    id_list = []
    with open(list_path) as f:
        buf = f.readlines()
    for name in buf:
        id_list.append(name.split('\n')[0])


if __name__ == '__main__':
    t = TwitterConstant()
    for name in t.id_list:
        print(name)
