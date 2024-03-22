import scrapy


class TackleworldSpider(scrapy.Spider):
    name = "tackleworld"
    allowed_domains = ["tackleworldadelaide.com.au"]
    start_urls = ["https://tackleworldadelaide.com.au"]
    visited_urls = set()

    def parse(self, response):
        headers = response.xpath('//*[@class="navPages-item"]//a/@href').getall()
        for header in headers:
            yield scrapy.Request(url=header, callback=self.parse_items)
    
    def parse_items(self, response):
        products = response.xpath('//*[@class="product"]')  
        for p in products:
            product_url = p.xpath('//*[@class="card-figure"]//a/@href').get()
            if product_url not in self.visited_urls:
                self.visited_urls.add(product_url)
                yield {
                    "Sku_name": product_url.split('/')[-2],
                    "Price_now": p.xpath('//*[@class="price"]/text()').get(),
                    "Price_was": p.xpath('//*[@class="price price--rrp"]/text()').get(),
                    "Image_url": p.xpath('//*[@class="card-image "]/@src').get(),
                    "Product_url": product_url
                }
            # yield scrapy.Request(url=product_url, callback=self.parse_sku, meta=meta)
            
    # def parse_sku(self, response):
    #     sku = response.xpath('//*[@class="productView-info-value"]/text()').get()
    #     item = response.meta
    #     item['Sku_name'] = sku
    #     item['Product_url'] = response.url  # Assuming the current URL is the product URL
    #     yield item
    