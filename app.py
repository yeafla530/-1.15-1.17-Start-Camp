from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')
# 다른 페이지로 가는 루트
@app.route('/ssafy') #route 역할 주소창에 ssafy추가하면 다른경로로 이동
def ssafy():
    return 'SSAFY Hello'

#Dday 계산하는 페이지
from datetime import datetime # 데이터를 적게하기 위해 원하는 데이터만 뽑아옴

@app.route('/dday')
def dday():
    today = datetime.now()
    endday = datetime(2020,5, 29)

    td = endday - today
    dday = f'1학기 종료일 까지 {td.days}일 남았습니다'
    return dday

#html
@app.route('/html')
def html():
    return '<h1> This is HTML h1 tag </h1>'

@app.route('/html_line')
def html_line():
    #여러줄 표시하고 싶을 때 ''' 붙이기
    return '''
    <h1> 여러줄 표시 </h1>
    <ul>
    <li>첫번째</li>
    <li>두번째</li>
    </ul>
    '''
#Variable Rules :url 이용하기
@app.route('/greeting/<string:name>')
def greeting(name):
    # return f'어서오세요. {name}님'
    return render_template('greeting.html', html_name=name)

@app.route('/cube/<int:number>')
def cube(number):
    return f'{number}의 세제곱은 {number**3}' #세제곱 표시

#인원수에 맞게 랜덤하게 메뉴출력
import random
@app.route('/lunch/<int:people>')

def lunch(people):
    menu = ['짜장면','떡볶이','참치김밥','라면','치킨','짬뽕']
    a = random.sample(menu, people) #people개수
    return f'{people}명에게 추천해줄 메뉴는 {a}입니다'

#로또 번호 생성하기

@app.route('/lotto/<string:name>')

def lotto(name):

    number = random.sample(range(1,46), 7)
    return f'{name}님 오늘 로또 사셔야 합니다. 꿈에서 {number}가 떠올랐어요'

@app.route('/movie')

def movie():
    movies = ['조커','기생충', '겨울왕국', '코코', '어벤저스', '기생충']
    return render_template('movie.html', movie_list=movies)


@app.route('/ping')

def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    value = request.args.get('peng') #argument 가있으면 peng을 받아오겠다
    print(value)
    return render_template('pong.html',peng = value)

@app.route('/fake_search')
def f_search():
    return render_template('f_search.html')


@app.route('/god_made_me')
def god():
    return render_template('god_made_me.html')

@app.route('/jjan')
def jjan():
    me = request.args.get('me')
    hobby = ['자전거', '책읽기', '사진찍기', '음악듣기']
    h = random.choice(hobby)
    personallity = ['소심함', '털털함', '화가많음', '급함', '착함']
    p = random.choice(personallity)
    love_luck = ['평생솔로', '10%', '30%', '50%', '바람둥이']
    l = random.choice(love_luck)
    return render_template('jjan.html', me1 = me, h1 = h, p1 = p, l1 = l)


if __name__ == '__main__':
    app.run(debug=True)