# -*- coding = UTF-8 -*-

# Created on:  2018年4月16
# Author: Regan_Chai
# E-Mail: regan_chai@163.com

__author__ = 'regan_chai@163.com'

import os
import re
import time

from bs4 import BeautifulSoup
import pdfkit
import click

from CrawlerBase import Crawler

import logging
logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


class MyCrawler(Crawler):
    """
    自定义爬虫类
    """
    def __init__(self, name, URL):
        super().__init__(name, URL)

    def Parse_URL_Menu(self):
        """
        解析目录结构,获取所有URL目录列表
        :yield: url生成器
        """
        logging.info('parsing url menu...')
        try:
            soup = BeautifulSoup(super().Request_Net(self.url).content, "html.parser")
            menu_tag = soup.find(class_="design")

            for a in menu_tag.find_all("a"):
                href = str(a.get('href'))
                result = href.find('/')
                if result == -1:
                    url = super().Parse_URL(self.url).get('url_head', 'invalid url_head of key') + href
                else:
                    url = super().Parse_URL(self.url).get('url_domain', 'invalid url_domain of key') + href
                yield url

        except Exception as e:
            logging.exception(e)


    def Parse_URL_Body(self, every_url, html_name):
        """
        解析URL，返回HTML内容
        :param every_url:解析的url
        :param html_name: 保存的html文件名
        :return: html
        """
        logging.info('parsing url body...')
        html_template = """
            <!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="UTF-8">
                </head>
                <body>
                    {content}
                </body>
            </html>
            """
        try:
            soup = BeautifulSoup(super().Request_Net(every_url).content, 'html.parser')
            # 正文
            body = soup.find_all(class_="article-intro")
            # 标题
            title = soup.find_all('h1')[1].get_text()

            h = str(body)
            html = h[1:-1]
            html = html_template.format(content = html)
            html = html.encode("utf-8")
            with open(html_name, 'wb') as f:
                f.write(html)
            return html_name

        except Exception as e:
            logging.exception(e)


    def Save_To_File(self, htmls, file_name):
        """
        把所有html文件保存到pdf文件
        :param htmls:  html文件列表
        :param file_name: pdf文件名
        :return:
        """
        logging.info('save as file of pdf format...')
        option_template = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'custom-header': [('Accept-Encoding', 'gzip')],
            'cookie': [('cookie-name1', 'cookie-value1'),('cookie-name2', 'cookie-value2'),],
            'outline-depth': 10,
        }
        pdfkit.from_file(htmls, file_name, options = option_template)

    def Run(self):
        logging.info('start crawler...')
        start = time.time()

        file_name = u"%s.pdf" % self.name
        htmls = [self.Parse_URL_Body(url, str(index) + ".html") for index, url in enumerate(self.Parse_URL_Menu())]
        self.Save_To_File(htmls, file_name)

        for html in htmls:
            os.remove(html)

        total_time = time.time() - start
        print(u"总共耗时：%f 秒" % total_time)

if __name__ == '__main__':
    Name = "Runoob_Python3_Test"
    URL = "http://www.runoob.com/python3/python3-tutorial.html"
    Crawler_Test = MyCrawler(Name, URL)
