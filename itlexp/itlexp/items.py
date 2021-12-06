# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ItlexpItem(scrapy.Item):
    # define the fields for your item here like:
    Country = scrapy.Field()
    Gold = scrapy.Field()
    Silver = scrapy.Field()
    Bronze = scrapy.Field()
    Total = scrapy.Field()
