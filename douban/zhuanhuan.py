# -*- coding: utf-8 -*-

class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict

if __name__ == "__main__":
    cookie = '_pk_id.100001.4cf6=a44d245d5fc9e224.1503625001.1.1503625021.1503625001.; _pk_ses.100001.4cf6=*; __utma=223695111.1708174838.1503625001.1503625001.1503625001.1; __utmb=223695111.0.10.1503625001; __utmc=223695111; __utmz=223695111.1503625001.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); bid=DAUCzU8hISQ; ps=y; ue="645015745@qq.com"; dbcl2="165819933:kUF4uWSW8Kk"; ck=WDdY; push_noty_num=0; push_doumail_num=0; __utma=30149280.18560900.1503625001.1503625001.1503625001.1; __utmb=30149280.0.10.1503625001; __utmc=30149280; __utmz=30149280.1503625001.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'
    trans = transCookie(cookie)
    print(trans.stringToDict())
