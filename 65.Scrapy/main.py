from scrapy import cmdline
cmdline.execute('scrapy crawl douban_spider -o test.json'.split())
