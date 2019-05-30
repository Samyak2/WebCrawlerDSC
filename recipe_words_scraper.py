import scrapy
import csv

class RecipeSpider(scrapy.Spider):
    name = "recipe_word_spider"
    start_urls = ["https://www.vocabulary.com/lists/331218"]

    def parse(self, response):
        f = csv.writer(open("wordlist.csv", "w"))
        word = ""
        for worddiv in response.css(".entry"):
            word = worddiv.xpath(".//a[@class=\"word dynamictext\"]/text()").extract_first()
            f.writerow([word])
            yield {
                "word": word
            }