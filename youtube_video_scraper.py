import scrapy

class YouTubeSpider(scrapy.Spider):
    name = "youtube_spider"
    search_term = "video"
    start_urls = ["https://www.youtube.com/results?search_query=" + search_term]
    
    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], callback=self.parse, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36"})

    def parse(self, response):
        video_urls = response.xpath("//h3//a/@href").extract()
        video_urls = ["https://www.youtube.com" + i for i in video_urls]
        print(video_urls)
