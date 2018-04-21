# -*- coding = UTF-8 -*-

# Created on:  2018年4月20
# Author: Regan_Chai
# E-Mail: regan_chai@163.com

__author__ = 'Regan_Chai'

from CrawlerBase import Crawler
from MyCrawler import MyCrawler

def RunoobToPdf():
    file_name = "Runoob_Python3"
    html_url = "http://www.runoob.com/python3/python3-tutorial.html"
    crawler = MyCrawler(file_name, html_url)
    crawler.Run()

if __name__ == '__main__':
    RunoobToPdf()
