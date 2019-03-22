# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class MinzuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class MinzuItemLoader(ItemLoader):
    default_input_processor = TakeFirst()

class MinzuItem(scrapy.Item):

    name = scrapy.Field()
    type = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
