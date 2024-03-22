from scrapy.exceptions import CloseSpider
import scrapy


class SurfboardempireSpider(scrapy.Spider):
    name = "surfboardempire"
    allowed_domains = ["www.surfboardempire.com.au"]
    start_urls = ["https://www.surfboardempire.com.au/products.json?page=1"]
    handle_httpstatus_list = [404]
    page_number = 1

    custom_settings = {
        'DUPEFILTER_CLASS': 'scrapy.dupefilters.RFPDupeFilter',
    }

    def parse(self, response):
        json_data = response.json()

        if json_data['products'] == []:
            raise CloseSpider('No more products to scrape')

        for product in json_data['products']:
            yield {
                'Sku_name': product['handle'],
                'Product_id': product['id'],
                'Brand': product['vendor'],
                'Product_url': f"https://surfboardempire.com.au/products/{product['handle']}"
            }
            
        self.page_number += 1
        next_page = f"https://www.surfboardempire.com.au/products.json?page={self.page_number}"
        yield response.follow(next_page, callback=self.parse)
