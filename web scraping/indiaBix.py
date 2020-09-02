from lxml import html
import requests
page = requests.get('https://www.indiabix.com/online-test/aptitude-test/4')
tree = html.fromstring(page.content)
answers = tree.xpath('//span[@class="ib-dgray ib-bold"]/text()')

for i in answers:
    print(i)