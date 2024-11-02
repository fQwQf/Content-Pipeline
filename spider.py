'''
## 爬虫
爬虫负责爬取文章，可以使用python的requests库，也可以使用scrapy框架。  
爬虫需要实现以下功能：  
1. 爬取文章的标题、作者、内容、发布时间等信息。  
2. 将文章保存为json文件，以便后续处理。  
3. 将文章发送至洗稿器，以便进行洗稿。 
'''
import requests
import json
import time
import os
from bs4 import BeautifulSoup


class Spider:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        self.article = ""
    def crawl(self):
        '''
        爬取文章信息
        '''
        try:
            response = requests.get(self.url, headers=self.headers)
            response.encoding = 'utf-8'
            html = response.text
            # 解析html，获取文章信息
            # 为微信公众号
            soup = BeautifulSoup(html, 'html.parser')

            # 提取所有段落
            paragraphs = soup.find_all('p')
            for p in paragraphs:
                self.article += p.text + '\n'

        except Exception as e:
            print('爬取文章失败：', e)
    def save(self):
        '''
        将文章保存为json文件
        '''
        with open('article.json', 'w', encoding='utf-8') as f:
            json.dump(self.article, f, ensure_ascii=False, indent=4)
    def send_to_rewriter(self):
        '''
        将文章发送至洗稿器
        '''
        # TODO
        pass


if __name__ == '__main__':
    url = input('请输入文章链接：')
    spider = Spider(url)
    spider.crawl()
    spider.save()
    spider.send_to_rewriter()