from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from crawler.items import PodcastItem

import hashlib
import json
import re

class FactSpider(CrawlSpider):

  name = "fact"
  allowed_domains = ['www.factmag.com']
  rules = [Rule(SgmlLinkExtractor(allow=['/fact-mix-']), 'parse_podcast')]

  def get_hash(self, value):
    h = hashlib.new('ripemd160')
    h.update(value)
    return h.hexdigest()

  def start_requests(self):
    for i in range(100):
      yield self.make_requests_from_url("http://www.factmag.com/category/factmixes/page/%d" % i)


  def parse_podcast(self, response):
    sel = Selector(response)
    podcast = PodcastItem()

    meta_data = sel.xpath('//meta[@name="parsely-page"]/@content').extract()[0]
    info = json.loads(meta_data)

    podcast['id_podcast'] = self.get_hash(response.url)
    podcast['name'] = info['title']
    podcast['domain'] = 'fact'
    podcast['url'] = response.url

    to_extract_date = re.compile(r'\d\d\d\d-\d\d-\d\d')
    podcast['published'] = to_extract_date.match(info['pub_date']).group()
    player = ''
    if sel.xpath("//object").extract():
      player = sel.xpath("//object").extract()[0]
    else:
      player = sel.xpath("//iframe").extract()[0]
    podcast['player'] = player
    return podcast
