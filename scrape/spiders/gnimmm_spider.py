import scrapy

class GnimmmSpider(scrapy.Spider):
    name = "gnimmm"
    start_urls = [
        'https://gnimmm.com/2020/05/25/fagara/',
    ]

    def get_content(self, response):
        contents = response.css('.post > div.entry-content > p::text').getall()
        result = ' '.join(contents)
        if not result:
            contents = response.css('.post > div.entry-content > p > span::text').getall()
            result = ' '.join(contents)
        return result

    def parse(self, response):
        yield {
            'datetime': response.css('.post > header > div > a.posted-on > time.entry-date.published::attr(datetime)').get(),
            'title': response.css('.post > header > h1 > span::text').get(),
            'text': self.get_content(response),
            'url': response.url
        }
        next_page = response.css('#main > nav > div > div > a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)