import scrapy

class JobindexSpider(scrapy.Spider):
    name = 'jobindex'
    start_urls = [
        'https://www.jobindex.dk/jobsoegning/it/virksomhedssystemer/storkoebenhavn'
    ]

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = 'joblist_page-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

## Xpath to select Apply buttons links
## //a[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),"apply")] | //button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),"apply")] 