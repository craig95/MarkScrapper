from scrapy.crawler import CrawlerProcess
import loginspider


def start_scrape():
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(loginspider.LoginSpider)
    process.start()

start_scrape()
