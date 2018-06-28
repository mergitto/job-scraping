# -*- coding: utf-8 -*-
import scrapy


class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['https://chiebukuro.yahoo.co.jp/tag/tags.php?page=1&tag=%E5%B0%B1%E6%B4%BB']
    start_urls = ['http://https://chiebukuro.yahoo.co.jp/tag/tags.php?page=1&tag=%E5%B0%B1%E6%B4%BB/']

    def parse(self, response):
        pass
