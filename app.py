from flask import Flask, render_template, request
import requests
import random
from bs4 import BeautifulSoup
from pprint import pprint 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/artii_input')
def input():
    return render_template('artii_input.html')


@app.route('/artii')
def artii():
    word = request.args.get('artbox')
    
    font_url = 'http://artii.herokuapp.com/fonts_list'
    font = requests.get(font_url).text
    #print(type(font)) #string
    font_list = font.split('\n')
    #print(font_list)

    font_result = random.choice(font_list)
    
    url = f'http://artii.herokuapp.com/make?text={word}&font={font_result}'
    #response에 저장
    response = requests.get(url).text #url에서 텍스트 값만 얻어올것이다

    #print(response) #response 값 알아보기
    return render_template('artii.html', response = response)

@app.route('/dust')  
def dust():
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

    return render_template('dust.html', dust = dust, station = station, dust_rate = dust_rate) #같은 이름으로 쓸 수 있게 dust=dust 작성

@app.route('/getUpdates')
def getUpdates():
    token = "927033695:AAHfEAmklL4ZkN4c85epUiNNgN1ab-Nl1Zc"
    url = f"https://api.telegram.org/bot{token}/getUpdates"

    response = requests.get(url)

    #print(response) #pprint
    return 'finish'

@app.route('/sendMessage')
def sendMessage():
    token = "927033695:AAHfEAmklL4ZkN4c85epUiNNgN1ab-Nl1Zc"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    update_url = f"https://api.telegram.org/bot{token}/getUpdates"
    response = requests.get(update_url).json()

    #print(response.get('result')[1].get('message').get('chat').get('id'))
    #경로찾기

    chat_id = response.get('result')[1].get('message').get('chat').get('id')
    msg = request.args.get('msg') #get을 받아오기 위해 작성
    message = msg

    sendmessage = f'{url}?chat_id={chat_id}&text={message}'

    res = requests.get(sendmessage)


    return 'finish'

@app.route('/input')
def input_msg():
    return render_template('input_msg.html')

@app.route('/telegram', methods=['POST'])
def telegram():
    response = request.get_json()
    #print(response.get('message').get('text')) #채팅 가져오기
    chat_id = response.get('message').get('chat').get('id')
    
    #get message
    res_msg = response.get('message').get('text')
    msg = res_msg

    if res_msg == "로또":
        lotto_num = random.sample(range(1, 46), 6)
        mise = str(lotto_num)
    elif res_msg == "미세먼지":
        api_key = '%2BU7i%2FvDO%2FBK2WCOovaPvXwUflXI1S1EpsklWdXkQUNImJNXCTUtUGsFYZErRRrfYIE0mFSTpvwozaxoQhT5kag%3D%3D'

        url = f"http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=경북&pageNo=1&numOfRows=10&ServiceKey={api_key}&ver=1.3"

        response1 = requests.get(url).text
        #print(response)
        data = BeautifulSoup(response1, 'lxml')
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

    
        mise = f'{station}의 현재 미세먼지 농도는 {dust}{dust_rate}입니다'  


    token = "927033695:AAHfEAmklL4ZkN4c85epUiNNgN1ab-Nl1Zc"
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    #send message
    send_url = f'{url}?chat_id={chat_id}&text={mise}' #res에 담긴 것이 출력됨

    res = requests.get(send_url)

    return '', 200 #200은 성공이라는 뜻



# for Debug mode
if __name__=="__main__":
    app.run(debug=True)
