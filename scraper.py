import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ["http://brickset.com/sets/year-2016"]
    
    def parse(self, response):
        SET_SELECTOR = ".set"
        for brickset in response.css(SET_SELECTOR):
            NAME_SELECTOR = "h1 ::text"
            yield {
                "name": (brickset.css(".meta").css(NAME_SELECTOR)).extract()[1],
                "pieces": brickset.xpath(".//div[@class=\"meta\"]/div[@class=\"col\"]/dl[dt/text()=\"Pieces\"]/dd/a/text()").extract_first(),
                "minifigs": brickset.xpath(".//div[@class=\"meta\"]/div[@class=\"col\"]/dl[dt/text()=\"Minifigs\"]/dd[2]/a/text()").extract_first(),
                "image": brickset.xpath("//img/@src").extract_first()
            }
        
        next_page = response.css(".next a ::attr(href)").extract_first()
        if(next_page):
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
