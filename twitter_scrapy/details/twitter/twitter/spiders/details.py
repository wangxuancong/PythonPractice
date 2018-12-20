# -*- coding: utf-8 -*-
import scrapy
import os
from details.twitter.twitter.messageid import TwitterMessage
from scrapy.http import Request
from scrapy.selector import Selector
import re
from constant import TwitterConstant
from selenium import webdriver
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from pyvirtualdisplay import Display
up_chrome = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
chrome_path = os.path.join(up_chrome,'tools','chromedriver')
import json
from scrapy.http.cookies import CookieJar
import urllib.parse
import time

class DetailsSpider(scrapy.Spider):
    name = 'details'
    allowed_domains = ['twitter_scrapy.com']
    start_urls = ['https://twitter_scrapy.com/']
    domains_url = 'https://twitter_scrapy.com/'

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield Request(url= url,callback=self.parse,dont_filter=True)

    def parse(self, response):
        print('Login success ..........',response.url)
        for user in TwitterMessage().get_twitter_message():
            up_save  = os.path.join(TwitterConstant.twitter_path,'message/')
            file_name  = up_save + '{user}_massage.txt'.format(user=user[0])
            if not os.path.exists(up_save):
                os.makedirs(up_save)
            if not os.path.exists(file_name):
                with open(file_name,'w') as f:
                    f.close()
            for dict in user[1].items():    # user[1] is a dictionary : key message id , value message
                text = dict[1]
                rank = text.split(' ')[0]
                if rank == 'RT':
                    author = re.findall('@(.*):',text.split(' ')[1])[0]
                    url = self.domains_url + author + '/status/' + dict[0]
                else:
                    url = self.domains_url + user[0] + '/status/'+ dict[0]

                yield Request(url= url,dont_filter=True,callback=self.get_details,method='GET',
                              meta={'id':dict[0],'time':user[2].pop(0),'twitter_scrapy':text,'file':file_name})
    def get_details(self,response):

        message_id = response.meta.get('id')
        create_time = response.meta.get('time')
        twitter  = response.meta.get('twitter_scrapy')
        save_file = response.meta.get('file')
        hx = Selector(response)
        js_info = hx.xpath('//div[@class="stream-item-footer"]')
        comments_num = js_info.xpath('.//span[@class="ProfileTweet-action--reply u-hiddenVisually"]//span[@class="ProfileTweet-actionCount"]//@data-tweet-stat-count').extract_first()
        transmit_num = js_info.xpath('.//span[@class="ProfileTweet-action--retweet u-hiddenVisually"]//span[@class="ProfileTweet-actionCount"]//@data-tweet-stat-count').extract_first()
        like_num = js_info.xpath('.//span[@class="ProfileTweet-action--favorite u-hiddenVisually"]//span[@class="ProfileTweet-actionCount"]//@data-tweet-stat-count').extract_first()
        authors_name = hx.xpath('//div[@class="stream-item-header"]//strong[@class="fullname show-popup-with-id u-textTruncate "]/text()').extract()
        authors_ids = hx.xpath('//div[@class="stream-item-header"]//@data-user-id').extract()
        ids = []
        for id in authors_ids:
            ids.append(id.xpath('.//@data-user-id').extract()[1])
        comments = hx.xpath('//div[@class="js-tweet-text-container"]')
        comment_li = []
        all_comment = []
        for comment in comments[1:]:
            text =  comment.xpath('.//p/text()').extract()[0]
            text = ''.join(i for i in text)
            comment_li.append(text)
        for i in range(len(authors_name)):
            message = {}
            message['name'] = authors_name[i]
            message['id'] = authors_ids[i]
            message['comment'] = comment_li[i]
            comment_li.append(message)
        twitter_message = {'message_id':message_id,
                     'create_time':create_time,
                     'twitter_scrapy':twitter,
                     'like_num':like_num,
                     'comments_num':comments_num,
                     'transmit_num':transmit_num,
                     'comment':all_comment}
        save_message  = json.dumps(twitter_message)
        with open(save_file,'r+') as f :
            f.write(save_message)



