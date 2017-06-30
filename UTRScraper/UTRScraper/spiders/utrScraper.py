import scrapy
import time

class UtrScraper(scrapy.Spider):
    name = "UTR"

    start_urls = ['https://universaltennis.com/login/']

    def parse(self, response):
        if "login" in response.url:
            return scrapy.FormRequest.from_response(
                response,
                formdata={'username': 'cmhudson11@gmail.com', 'password': 'Hudson12compsci'},
                callback=self.after_login
            )
        else:
            print response.body


    def after_login(self, response):
        # check login succeed before going on
        next_page_url = "https://universaltennis.com/players/377850"
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))


            
        