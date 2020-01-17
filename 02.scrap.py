import requests

response = requests.get('https://finance.naver.com/').text
#print(response)

from bs4 import BeautifulSoup
data = BeautifulSoup(response, 'html.parser') # 원하는 정보 쉽게 바꾸고

kospi = data.select_one('#content > div.article > div.section2 > div.section_stock_market > div.section_stock > div.kospi_area.group_quot.quot_opn > div.heading_area > a > span > span.num')

print(kospi.text)