# -*- coding: utf-8 -*-
from scrapy.http import Request
from douban.items import DoubanItem
from urllib import parse
import scrapy
import http.cookiejar as cookielib
import  re
class CommentSpider(scrapy.Spider):
    name = 'comment'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/26826398/comments?start=0&limit=20&sort=new_score&status=P']
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'}
    cookie  ={'_pk_id.100001.4cf6': 'a44d245d5fc9e224.1503625001.1.1503625021.1503625001.', '_pk_ses.100001.4cf6': '*', '__utma': '30149280.18560900.1503625001.1503625001.1503625001.1', '__utmb': '30149280.0.10.1503625001', '__utmc': '30149280', '__utmz': '30149280.1503625001.1.1.utmcsr', 'bid': 'DAUCzU8hISQ', 'ps': 'y', 'ue': '"645015745@qq.com"', 'dbcl2': '"165819933:kUF4uWSW8Kk"', 'ck': 'WDdY', 'push_noty_num': '0', 'push_doumail_num': '0'}
    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], headers=self.headers, cookies=self.cookie)  # 这里带着cookie发出请求
    # def is_login(self,response):
    #     self.initialized()
    #is_login(self)
    # def after_login(self, response):
    #     print('after login')
    #     #print(response.body)
    #     yield Request(url=response.url, callback=self.parse)
        # def parse_article(self, response):
    #     item = DoubanItem()
    #     yield item

    def parse(self, response):
        print(response.body)
        for sel in response.css("#comments .comment-item"):
            item=DoubanItem()
            item['pinglun']=sel.css(".comment p::text")[0].extract()
            print(item)
            yield item

        # 提取下一页并交给scrapy进行下载
        next_url = response.css("#paginator a:nth-child(3)::attr(href)")[0].extract()
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

