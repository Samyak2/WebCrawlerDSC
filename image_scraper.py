import scrapy
import urllib.request
import csv

class ImageSpider(scrapy.Spider):
    name = "image_spider"
    wordlist = []
    with open("wordlist.csv", "r") as csvfile:
        readCSV = csv.reader(csvfile)
        for row in readCSV:
            wordlist += row
    count = 0
    search_term = wordlist[count]
    start_urls = ["https://www.pexels.com/search/" + search_term]

    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)

    def parse(self, response):
        print("NOW SEARCHINGGGGGG: " + self.wordlist[ImageSpider.count])
        img_url = ""

        for imagecolumn in response.css(".photos__column"):#response.xpath("//div[@class=\"photos__column\"]"):
            if(not imagecolumn.xpath(".//a[@class=\"js-photo-link photo-item__link\"]")):
                break
            img_url = (imagecolumn.xpath(".//a[@class=\"js-photo-link photo-item__link\"]/img/@data-big-src").extract_first()).split(".jpeg")[0] + ".jpeg"
            yield {
                "image": img_url
            }
            urllib.request.urlretrieve(img_url, "Images/" + self.wordlist[ImageSpider.count] + " " + img_url.split("/")[-1])
        if(self.wordlist[ImageSpider.count]):
            ImageSpider.count += 1
            yield scrapy.Request(response.urljoin(
                "https://www.pexels.com/search/" + self.wordlist[ImageSpider.count]),
                callback=self.parse)
