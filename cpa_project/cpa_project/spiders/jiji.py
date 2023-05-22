import scrapy

class AllMaterialSpider(scrapy.Spider):
    name = "all_materials"
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


class CementSpider(scrapy.Spider):
    name = "cements"
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


class TilesSpider(scrapy.Spider):
    name="tiles"
    start_urls = ["https://jiji.com.et/building-materials?filter_attr_559_type=Tiles"]
    def parse(self, response, **kwargs):
        for tile in response.css('div.b-list-advert__gallery__item.js-advert-list-item'):
            yield {
                'price':tile.css('div.qa-advert-price::text').get(),
                'title':tile.css('div.b-advert-title-inner.qa-advert-title.b-advert-title-inner--div::text').get(),
                'desc':tile.css('div.b-list-advert-base__description-text::text').get(),
                # locations are not loading I think it is because they are in ::after(w/c kind of load dynamically after the created with JS)
                'location':tile.css('span.b-list-advert__region__text::text').get()
            }

class PaintsSpider(scrapy.Spider):
    name="paints"
    start_urls = ["https://jiji.com.et/building-materials?filter_attr_559_type=Paints"]
    def parse(self, response, **kwargs):
        for paint in response.css('div.b-list-advert__gallery__item.js-advert-list-item'):
            yield {
                'price':paint.css('div.qa-advert-price::text').get(),
                'title':paint.css('div.b-advert-title-inner.qa-advert-title.b-advert-title-inner--div::text').get(),
                'desc':paint.css('div.b-list-advert-base__description-text::text').get(),
                # locations are not loading I think it is because they are in ::after(w/c kind of load dynamically after the created with JS)
                'location':paint.css('span.b-list-advert__region__text::text').get()
            }


class BricksSpider(scrapy.Spider):
    name="bricks"
    start_urls = ["https://jiji.com.et/building-materials?filter_attr_559_type=Bricks"]
    def parse(self, response, **kwargs):
        for brick in response.css('div.b-list-advert__gallery__item.js-advert-list-item'):
            yield {
                'price':brick.css('div.qa-advert-price::text').get(),
                'title':brick.css('div.b-advert-title-inner.qa-advert-title.b-advert-title-inner--div::text').get(),
                'desc':brick.css('div.b-list-advert-base__description-text::text').get(),
                # locations are not loading I think it is because they are in ::after(w/c kind of load dynamically after the created with JS)
                'location':brick.css('span.b-list-advert__region__text::text').get()
            }
