import scrapy

class YouTubeSpider(scrapy.Spider):
    name = "youtube_spider" #spider name
    search_term = "video"
    start_urls = ["https://www.youtube.com/results?search_query=" + search_term] #url to scrape
    
    #to set user agent (so that they don't block us for using scrapy and so that it youtube thinks we are using a normal browser)
    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], callback=self.parse, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36"})

    def parse(self, response):
        #get video links and print
        video_urls = response.xpath("//h3//a/@href").extract()
        video_urls = ["https://www.youtube.com" + i for i in video_urls] #add base url to each link (because the links we got are relative)
        print(video_urls)
