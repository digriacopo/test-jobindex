import scrapy

class JobindexSpider(scrapy.Spider):
    name = 'jobindex'

    def start_requests(self):
        urls = [
            'https://www.jobindex.dk/jobsoegning/it/virksomhedssystemer/storkoebenhavn',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = 'joblist_page-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


