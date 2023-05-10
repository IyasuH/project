import scrapy

# scrapy crawl cements -O cement.json

class CementSpider(scrapy.Spider):
    # name is identifier for the spider 
    # here only scaping for cement
    name = "cements"
    # def start_requests(self):
    #     return super().start_requests()
    # and we are scarping only from jiji.com.et
    start_urls = ["https://jiji.com.et/building-materials?filter_attr_559_type=Cement"]
    def parse(self, response, **kwargs):
        for cement in response.css('div.b-list-advert__gallery__item.js-advert-list-item'):
            yield {
                'price':cement.css('div.qa-advert-price::text').get(),
                'title':cement.css('div.b-advert-title-inner.qa-advert-title.b-advert-title-inner--div::text').get(),
                'desc':cement.css('div.b-list-advert-base__description-text::text').get(),
                # locations are not loading I think it is because they are in ::after(w/c kind of load dynamically after the created with JS)
                'location':cement.css('span.b-list-advert__region__text::text').get()
            }