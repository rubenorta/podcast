from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from crawler.items import PodcastItem
import hashlib

class ViceSpider(CrawlSpider):

    name = 'vice'
    allowed_domains = ['thump.vice.com']
    rules = [Rule(SgmlLinkExtractor(allow=['/mixes/mixed']), 'parse_podcast')]

    def get_hash(self, value):
        h = hashlib.new('ripemd160')
        h.update(value)
        return h.hexdigest()

    def start_requests(self):
        for i in range(20):
            yield self.make_requests_from_url("http://thump.vice.com/mixes/page/%d" % i)

    def parse_podcast(self, response):
        sel = Selector(response)
        podcast = PodcastItem()

        podcast['id_podcast'] = self.get_hash(response.url)
        podcast['name'] = sel.xpath("//h1/text()").extract()
        podcast['domain'] = 'vice'
        podcast['url'] = response.url
        podcast['published'] = sel.xpath("//div[@class='story_meta']").re('\w{3} \d+ \d{4}')
        podcast['player'] = sel.xpath("//iframe").extract()[1]
        return podcast

