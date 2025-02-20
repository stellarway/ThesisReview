# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()
    href = scrapy.Field()
    # date = scrapy.Field()
    writer = scrapy.Field()
    content = scrapy.Field()

    pass


class NewsItem(scrapy.Item):

    title = scrapy.Field()
    href = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()

    pass
