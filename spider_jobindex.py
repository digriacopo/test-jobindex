import scrapy

class JobindexSpider(scrapy.Spider):
    name = 'jobindex'
    start_urls = [
        'https://www.nets.eu/careers/Pages/Job-openings.aspx?jobId=17562',
    ]
# 1 create an iterable object which generates further links (next page):


# 2 create an iterable object which stores:
# - the links to the job ads
# - the job title
# - the uploaded for the job ads
# - detects the language 

## Xpath to select Apply buttons links
# - apply url
# - the job title
    def parse(self, response):
        #get combination of xpaths for apply links likely to happen within the nodes and keywords
        nodes = ["a", "href"]
        key_words = ["apply", "interest"]
        xpath_base = '//{}[contains(translate(., "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"),"{}")]'
        total_combination = len(nodes) * len(key_words)
        xpath_query = ''
        for i in range(total_combination):
            xpath_query = xpath_base.format(nodes[i % len(nodes)], key_words[i // 2])


        xpath_query = xpath_base.format(nodes[0], key_words[0])
        xpath_query
        for node in response.xpath(''):
            yield {

            }

# response.xpath('//a[contains(translate(., "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"),"apply")] | //button[contains(translate(., "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"),"apply")]').get()


