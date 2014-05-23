from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from crawler.items import PodcastItem

class ViceSpider(CrawlSpider):

    def start_requests(self):
        for i in range(12):
            yield self.make_requests_from_url("http://thump.vice.com/mixes/page/%d" % i)

    name = 'vice'
    allowed_domains = ['thump.vice.com']
    rules = [Rule(SgmlLinkExtractor(allow=['/mixes/mixed']), 'parse_torrent')]

    def parse_torrent(self, response):
        sel = Selector(response)
        podcast = PodcastItem()
        podcast['url'] = response.url
        podcast['published'] = sel.xpath("//div[@class='story_meta']").re('\w{3} \d+ \d{4}')
        podcast['name'] = sel.xpath("//h1/text()").extract()
        podcast['player'] = sel.xpath("//iframe").extract()[2]

        return podcast
