#To run this spider execute the following command in this directory: scrapy runspider loginspider.py
import scrapy
from scrapy.shell import inspect_response


class LoginSpider(scrapy.Spider):
    name = 'login-spider'
    login_url = 'https://www1.up.ac.za'
    start_urls = [login_url]
    login_user = ""
    login_pass = ""

    def print_p(self, response):
        print("\033[94mPrinting <p> elements\033[0m")
        #Print body
        print(response.text)

    def parse(self, response):
        print("\033[92mIN PARSE\033[0m")
        request_id = response.css('input[name="request_id"]::attr(value)').extract_first()
        data = {
            'userid_placeholder': self.login_user,
            'foilautofill': '',
            'password': self.login_pass,
            'request_id': request_id,
            'username': self.login_user[1:]
        }
        yield scrapy.FormRequest(url='https://www1.up.ac.za/oam/server/auth_cred_submit', formdata=data,
                                 callback=self.print_p)

