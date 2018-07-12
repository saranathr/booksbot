import scrapy


class PricingSpider(scrapy.Spider):
    name = "pricing_spider"
    start_urls = ['https://www.bjs.com/sets/year-2016']