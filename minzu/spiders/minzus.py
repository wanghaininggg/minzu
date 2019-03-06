# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
from scrapy.http import Request
from minzu.items import MinzuItem, MinzuItemLoader

class MinzusSpider(scrapy.Spider):
    name = 'minzus'
    allowed_domains = ['minzu56.net']
    start_urls = ['http://minzu56.net/']

    def parse(self, response):
        urls = response.css("#menu dl dd a")
        for minzuUrl in urls:
            post_url = minzuUrl.css("::attr(href)").extract_first()
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse2)

    def parse2(self, response):
        urls = response.css("#subnav p a")
        for mzurl in urls:
            post_url =  mzurl.css("::attr(href)").extract_first()
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse3)

    def parse3(self, response):
        urls = response.css(".leftwrap ul li a")
        for mzurl in urls:
            post_url = mzurl.css("::attr(href)").extract_first()
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parseDetail)
        next_url = response.xpath("//*[@id='page']/li/a[text()='下一页']/@href").extract_first()
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse3)

    def parseDetail(self, response):

       content = response.xpath("//div[5]/p/text()").extract()
       text1 = []
       for str in content:
          text1.append(str)
       content = ''.join(text1)

       item_loader = MinzuItemLoader(item=MinzuItem(), response=response)
       item_loader.add_xpath("title","//h1/text()")
       item_loader.add_value("content", [content])
       minzu_item = item_loader.load_item()
       yield minzu_item





