import scrapy

class AllMaterialSpider(scrapy.Spider):
    # name is identifier for the spider 
    # here only scaping for all_materials
    name = "all_materials"
    # def start_requests(self):
    #     return super().start_requests()
    # and we are scarping only from jiji.com.et
    start_urls = ["https://jiji.com.et/building-materials"]
    def parse(self, response, **kwargs):
        for materail in response.css('div.b-list-advert__gallery__item.js-advert-list-item'):
            yield {
                'price':materail.css('div.qa-advert-price::text').get(),
                'title':materail.css('div.b-advert-title-inner.qa-advert-title.b-advert-title-inner--div::text').get(),
                'desc':materail.css('div.b-list-advert-base__description-text::text').get(),
                # locations are not loading I think it is because they are in ::after(w/c kind of load dynamically after the created with JS)
                'location':materail.css('span.b-list-advert__region__text::text').get()
            }