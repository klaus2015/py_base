from scrapy import cmdline

cmdline.execute('scrapy crawl maoyan3 -o maoyan.json'.split())

# 流程:items,爬虫,pipeline,settings