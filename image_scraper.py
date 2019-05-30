import scrapy
import urllib.request
import csv

class ImageSpider(scrapy.Spider):
    name = "image_spider"
    search_term = "butter"
    start_urls = ["https://www.pexels.com/search/" + search_term]

    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)

    def parse(self, response):
        img_url = ""
        for imagecolumn in response.css(".photos__column"):#response.xpath("//div[@class=\"photos__column\"]"):
            img_url = (imagecolumn.xpath(".//a[@class=\"js-photo-link photo-item__link\"]/img/@data-big-src").extract_first()).split(".jpeg")[0] + ".jpeg"
            yield {
                "image": img_url
            }
            urllib.request.urlretrieve(img_url, img_url.split("/")[-1])
