from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from crawler.items import PodcastItem

class SoleSpider(CrawlSpider):

    name = 'sole'
    allowed_domains = ['thump.vice.com']
    rules = [Rule(SgmlLinkExtractor(allow=['/mixes/mixed']), 'parse_podcast')]
