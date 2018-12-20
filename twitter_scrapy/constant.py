import tweepy
import os

class TwitterConstant:
    absolute_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    twitter_path = os.path.join(absolute_path,'data','twitter_scrapy')
    list_path = os.path.dirname(os.path.abspath(__file__)) + '/id_list.txt'
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
    header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
              'accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
              'accept - encodin': 'gzip, deflate, br',
              'accept - language': 'en - US, en;q = 0.9, zh - CN;q = 0.8, zh;q = 0.7'
    }
    post_dir = {'session[username_or_email]': '+8618310200105',
                'session[password]': 'zyf__123'}
    id_list = []
    with open(list_path) as f:
        buf = f.readlines()
    for name in buf:
        id_list.append(name.split('\n')[0])


if __name__ == '__main__':
    # t = TwitterConstant()
    # for name in t.id_list:
    #     print(name)
    print(TwitterConstant.absolute_path)