import re

from scrapy import Selector
from ezpymysql import Connection
from downloader import downloader

db = Connection(
    'localhost',
    'spider_advance',
    'root',
    '1qaz2wsx!!!!'
)

def sina_news():
    url = 'https://news.sina.com.cn/'
    s, html, lost_url_found_dongys_z = downloader(url)
    all_urls = set(re.findall('''(https:\S+\/\d{4}-\d{2}-\d{2}\/\S+.shtml)''', html))
    for detail_url in all_urls:
        detail_s, detail_html, detail_lost_url_found_dongys_z = downloader(detail_url)
        sl_html = Selector(text=detail_html)
        title = sl_html.xpath('//h1[@class="main-title"]/text() | //h2/text()').extract_first()
        if title:
            detail_url = detail_url
            item = {
                'title': title,
                'url': detail_url
            }
            db.table_insert(table_name='spider_advance', item=item)

if __name__ == '__main__':
    sina_news()