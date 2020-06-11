# 逆嘶亭之備份

Backup all the articles in https://gnimmm.com/

## Get Started

* Python & Scrapy
* NodeJS

1. change the `start_urls` in `scrape/spiders/gnimmm_spider.py` to the latest articles
2. Install depns needed for Python side
3. Run scrapy to scrap the articles: `scrapy crawl gnimmm`.
4. Line JSON file `gnimmm.jl` will be generated.
5. Run `yarn install` to install depns
6. Run `node index.js` to parse the line JSON file to seperate `*.txt` files under `output`
