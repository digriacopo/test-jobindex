import scrapy
from math import sqrt 

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
        ## get combination of xpaths for apply links likely to happen within the nodes and keywords
        nodes = ["a", "href"] #this should be a dynamic list
        key_words = ["apply", "interest"] #this should be a dynamic list
        xpath_base = '//{}[contains(translate(., "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"),"{}")]'
        total_combination = len(nodes) * len(key_words)

        ## build the key_word series (0, 0, 1, 1)
        key_words_series = []
        counter = 0
        for i in range(total_combination):
            if counter != i // int(sqrt(total_combination)):
                counter += 1
            key_words_series.append(counter)
        
        ## build the xpath query with the combination of nodes and key_words 
        ## then concatenate it in a string with the ' | ' operator
        xpath_query = ''
        for i in range(total_combination):
            xpath_query += xpath_base.format(nodes[i % len(nodes)], key_words[key_words_series[i]]) + " | "

        xpath_query = xpath_query[:-3]

        for node in response.xpath('xpath_query'):
            yield {
                'link': node
            }
