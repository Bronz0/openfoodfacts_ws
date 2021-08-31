import scrapy


class BrandsSpider(scrapy.Spider):
    name = 'brands'

    start_urls = ['https://dz-fr.openfoodfacts.org/marques']

    def parse(self, response):
        table = response.xpath('//*[@id="tagstable"]')
        brands = table.xpath('tbody/tr/td/a')
        for brand in brands:
            yield {
                'name': brand.css('a::text').get(),
                'href': 'https://dz-fr.openfoodfacts.org'+brand.css('a::attr(href)').get()
            }
