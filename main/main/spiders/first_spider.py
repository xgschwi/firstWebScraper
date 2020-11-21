import scrapy

class FirstSpider(scrapy.Spider):
    name = "first"
    
    def start_request(self):
        urls = ["https://blog.scrapinghub.com/"]





