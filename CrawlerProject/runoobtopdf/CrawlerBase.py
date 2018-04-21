# -*- coding = UTF-8 -*-

# Created on:  2018年4月16
# Author: Regan_Chai
# E-Mail: regan_chai@163.com

__author__ = 'Regan_Chai'

import os
import re

from urllib.parse import urlparse
import requests


class Crawler(object):
    '''
    爬虫基类
    '''
    ## 初始化
    def __init__(self, name, URL):
        self.name = name;
        self.url = URL;
     
    ## 请求网络响应
    def Request_Net(self, url):
        response = requests.get(url)
    
        return response

    ## 解析URL
    def Parse_URL(self, url):

        url_components = urlparse(url)
        url_path = url_components.path
        url_head = url_components.scheme + "://" + url_components.netloc + url_path[0:url_path.rfind('/') + 1]
        url_domain = url_components.scheme + "://" + url_components.netloc + "/"

        return {'url_head':url_head, 'url_domain':url_domain}


if __name__ == '__main__':
    file_name = "Runoob_Python3_Test"
    start_url = "http://www.runoob.com/python3/python3-tutorial.html"
    Crawler_Test = Crawler(file_name, start_url)
    print(Crawler_Test.Parse_URL(start_url))
  