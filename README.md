# 逆嘶亭之備份

## Get Started

* Python & Scrapy
* NodeJS

1. change the `start_urls` in `scrape/spiders/gnimmm_spider.py` to the latest articles
2. Run scrapy to scrap the articles: `./run.sh` or `scrapy crawl gnimmm`.
3. Line JSON file `gnimmm.jl` will be generated.
4. Run `node index.js` to parse the line JSON file to seperate `*.txt` files under `output`
