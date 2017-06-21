import loginspider


def start_scrape(username, password):
    # create a scrapy spider and call it.
    login_spider = loginspider.LoginSpider(username, password)
    login_spider.start_requests()
    print(password + " " + username)

start_scrape("U15029779", "Etienne@92")
