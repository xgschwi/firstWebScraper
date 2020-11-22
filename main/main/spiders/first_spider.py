import scrapy

class FirstSpider(scrapy.Spider):
    name = "first"
    
    def start_request(self):
        urls = ["https://blog.scrapinghub.com/"]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self,response):
        page = response.url.split("/")[-2]
        filename = f'first-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')






