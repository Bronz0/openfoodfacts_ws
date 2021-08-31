import scrapy
import pandas as pd

class ProductsSpider(scrapy.Spider):

    name = 'products'
    df = pd.read_csv('brands_links.csv')
    start_urls = list(df.href)


    def parse(self, response):
        # get brand name
        brand_name = response.xpath('//*[@id="main_column"]/div[2]/h1/text()').get()

        # get products
        search_results = response.xpath('//*[@id="search_results"]')
        products = search_results.css('li')

        # get product name and image url
        for product in products:
            product_image = product.xpath('a/div/img').attrib['src']
            product_name = product.css('span::text').get()
            yield {
                'brand': brand_name,
                'product': product_name,
                'image_url': product_image,
            }
