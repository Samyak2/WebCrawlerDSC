import scrapy
import os
import subprocess

class YouTubeSpider(scrapy.Spider):
    name = "youtube_spider" #spider name
    # search_term = "video"
    def __init__(self, search_term):
        self.search_term = search_term
        self.start_urls = ["https://www.youtube.com/results?search_query=" + self.search_term] #url to scrape
    
    #to set user agent (so that they don't block us for using scrapy and so that it youtube thinks we are using a normal browser)
    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], callback=self.parse, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36"})

    def parse(self, response):
        #get video links and print
        video_urls = response.xpath("//h3//a/@href").extract()
        video_urls = ["https://www.youtube.com" + i for i in video_urls if "watch" in i] #add base url to each link (because the links we got are relative)
        for video_url in video_urls:
            print(video_url)

def runYouTubeSpider(search_term):
    # os.system("scrapy runspider youtube_video_scraper.py --nolog -a search_term=" + search_term)
    op = subprocess.check_output("scrapy runspider youtube_video_scraper.py --nolog -a search_term=" + search_term, shell=True, universal_newlines=True)
    op = op.split("\n")
    print(op)
    return op

if __name__ == "__main__":
    runYouTubeSpider("pewdiepie")