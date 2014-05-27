# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class CrawlerItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass

class PodcastItem(Item):
    id_podcast = Field()
    name = Field()
    domain = Field()
    url = Field()
    published = Field()
    player = Field()
