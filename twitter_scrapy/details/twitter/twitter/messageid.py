import os
twitter_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import sys
sys.path.append(twitter_path)
print(twitter_path)
from constant import TwitterConstant
import tweepy
from selenium import webdriver
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from pyvirtualdisplay import Display
up_chrome = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
chrome_path = os.path.join(up_chrome,'tools','chromedriver')
import time


class TwitterMessage:
    def __init__(self, api=TwitterConstant.api,id_list=TwitterConstant.id_list):
        """
        Constructors
        :param api: twitter_scrapy api connector
        :param id_list: twitter_scrapy id list
        """
        self.api = api
        self.id_list = id_list
        display = Display(visible=0, size=(800, 600))
        display.start()
        self.browser = webdriver.Chrome(executable_path=chrome_path)
        super(TwitterMessage, self).__init__()
        dispatcher.connect(signals.spider_closed)
    def get_twitter_message(self):
        '''
        :return: users twitter_scrapy massage's id
        '''
        api = self.api
        id_list = self.id_list
        for id in id_list:
            print('upgrading message data of %s...' % id)
            id_dic = {}
            time_list = []

            # use cursor to traverse history tweets of the target user, get tweets data
            for status in tweepy.Cursor(api.user_timeline, id=id).items():
                id_dic[status.id_str] = status.text
                time_list.append(status.created_at)
            yield id,id_dic,time_list
    def get_cookies(self):
        self.browser.get('https://twitter_scrapy.com/login')
        time.sleep(3)
        self.browser.find_element_by_xpath(
            '//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input').send_keys(
            TwitterConstant.post_dir['session[username_or_email]'])
        self.browser.find_element_by_xpath(
            '//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input').send_keys(
            TwitterConstant.post_dir['session[password]'])
        self.browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button').click()
        cookies = self.browser.get_cookies()
        cookie = {}
        time.sleep(2)
        for co in cookies:
            cookie[co['name']] = co['value']
        return cookie