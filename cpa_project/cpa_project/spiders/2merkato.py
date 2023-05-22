import scrapy

class ConcreteWorkSpider(scrapy.Spider):
    name='concrete_works'
    start_urls=["https://con.2merkato.com/prices/cat/2"]
    def parse(self, response, **kwargs):
        for row in response.xpath('//*[@class="table table-sm table-hover mt-3"]//tbody//tr'):
            yield {
                'Name':row.xpath('td[1]//text()').extract_first(),
                'Price':row.xpath('td[2]//text()').extract_first(),
                'Date':row.xpath('td[5]//text()').extract_first(),
            }

class MasonryWorkSpider(scrapy.Spider):
    name='masnory_works'
    start_urls=["https://con.2merkato.com/prices/cat/3"]
    def parse(self, response, **kwargs):
        for row in response.xpath('//*[@class="table table-sm table-hover mt-3"]//tbody//tr'):
            yield {
                'Name':row.xpath('td[1]//text()').extract_first(),
                'Price':row.xpath('td[2]//text()').extract_first(),
                'Date':row.xpath('td[5]//text()').extract_first(),
            }

class BlockWorkSpider(scrapy.Spider):
    name='block_works'
    start_urls=["https://con.2merkato.com/prices/cat/4"]
    def parse(self, response, **kwargs):
        for row in response.xpath('//*[@class="table table-sm table-hover mt-3"]//tbody//tr'):
            yield {
                'Name':row.xpath('td[1]//text()').extract_first(),
                'Price':row.xpath('td[2]//text()').extract_first(),
                'Date':row.xpath('td[5]//text()').extract_first(),
            }

class CarpentryJoinerySpider(scrapy.Spider):
    name="carpentry_joinery"
    start_urls=["https://con.2merkato.com/prices/cat/5"]
    def parse(self, response, **kwargs):
        for row in response.xpath('//*[@class="table table-sm table-hover mt-3"]//tbody//tr'):
            yield {
                'Name':row.xpath('td[1]//text()').extract_first(),
                'Price':row.xpath('td[2]//text()').extract_first(),
                'Date':row.xpath('td[5]//text()').extract_first(),
            }

class RoofingSpider(scrapy.Spider):
    name="roofing"
    start_urls=["https://con.2merkato.com/prices/cat/6"]
    def parse(self, response, **kwargs):
        for row in response.xpath('//*[@class="table table-sm table-hover mt-3"]//tbody//tr'):
            yield {
                'Name':row.xpath('td[1]//text()').extract_first(),
                'Price':row.xpath('td[2]//text()').extract_first(),
                'Date':row.xpath('td[5]//text()').extract_first(),
            }

class MetalWorksSpider(scrapy.Spider):
    name="metal_works"
    start_urls=["https://con.2merkato.com/prices/cat/7"]
    def parse(self, response, **kwargs):
        for row in response.xpath('//*[@class="table table-sm table-hover mt-3"]//tbody//tr'):
            yield {
                'Name':row.xpath('td[1]//text()').extract_first(),
                'Price':row.xpath('td[2]//text()').extract_first(),
                'Date':row.xpath('td[5]//text()').extract_first(),
            }

class FinishingSpider(scrapy.Spider):
    name="finishing"
    start_urls=["https://con.2merkato.com/prices/cat/8"]
    def parse(self, response, **kwargs):
        for row in response.xpath('//*[@class="table table-sm table-hover mt-3"]//tbody//tr'):
            yield {
                'Name':row.xpath('td[1]//text()').extract_first(),
                'Price':row.xpath('td[2]//text()').extract_first(),
                'Date':row.xpath('td[5]//text()').extract_first(),
            }


class GlazingSpider(scrapy.Spider):
    name="glazing"
    start_urls=["https://con.2merkato.com/prices/cat/9"]
    def parse(self, response, **kwargs):
        for row in response.xpath('//*[@class="table table-sm table-hover mt-3"]//tbody//tr'):
            yield {
                'Name':row.xpath('td[1]//text()').extract_first(),
                'Price':row.xpath('td[2]//text()').extract_first(),
                'Date':row.xpath('td[5]//text()').extract_first(),
            }

class PaintingSpider(scrapy.Spider):
    name="painting"
    start_urls=["https://con.2merkato.com/prices/cat/10"]
    def parse(self, response, **kwargs):
        for row in response.xpath('//*[@class="table table-sm table-hover mt-3"]//tbody//tr'):
            yield {
                'Name':row.xpath('td[1]//text()').extract_first(),
                'Price':row.xpath('td[2]//text()').extract_first(),
                'Date':row.xpath('td[5]//text()').extract_first(),
            }

class ElectricalSpider(scrapy.Spider):
    name="electrical"
    start_urls=["https://con.2merkato.com/prices/cat/11"]
    def parse(self, response, **kwargs):
        for row in response.xpath('//*[@class="table table-sm table-hover mt-3"]//tbody//tr'):
            yield {
                'Name':row.xpath('td[1]//text()').extract_first(),
                'Price':row.xpath('td[2]//text()').extract_first(),
                'Date':row.xpath('td[5]//text()').extract_first(),
            }

class SanitarySpider(scrapy.Spider):
    name="sanitary"
    start_urls=["https://con.2merkato.com/prices/cat/12"]
    def parse(self, response, **kwargs):
        for row in response.xpath('//*[@class="table table-sm table-hover mt-3"]//tbody//tr'):
            yield {
                'Name':row.xpath('td[1]//text()').extract_first(),
                'Price':row.xpath('td[2]//text()').extract_first(),
                'Date':row.xpath('td[5]//text()').extract_first(),
            }
