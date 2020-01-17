import requests
from bs4 import BeautifulSoup

api_key = '%2BU7i%2FvDO%2FBK2WCOovaPvXwUflXI1S1EpsklWdXkQUNImJNXCTUtUGsFYZErRRrfYIE0mFSTpvwozaxoQhT5kag%3D%3D'

url = f"http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=경북&pageNo=1&numOfRows=10&ServiceKey={api_key}&ver=1.3"

response = requests.get(url).text
#print(response)
data = BeautifulSoup(response, 'lxml')
#print(data('item'[4]))
location = data('item')[4]
#print(location.pm10value.text) #text만 출력
dust = int(location.pm10value.text) #숫자로 미세먼지 수치 변경됨
station = location.stationname.text

if dust > 150: 
    dust_rate = "매우나쁨"
elif 80 < dust <= 150:
    dust_rate = "나쁨"
elif 30 < dust <=80:
    dust_rate = "보통"
else:
    dust_rate = "좋음"

print(f'{station}의 미세먼지 농도는 {dust} {dust_rate}입니다.')
