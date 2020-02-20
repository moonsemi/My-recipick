from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

app = Flask(__name__)


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


## API 역할을 하는 부분
# 백종원 공식레시피 API
@app.route('/official_recipes', methods=['GET'])
def official_recipes_view():
    # 서버 내부에서 수행 할 기능 / DB에 저장돼있는 모든 정보를 가져오기
    paik_official = list(db.paik_official_recipes.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'paik_official': paik_official})


# 백종원 따라하기레시피 API
@app.route('/follow_recipes', methods=['GET'])
def follow_recipes_view():
    # 서버 내부에서 수행 할 기능 / DB에 저장돼있는 모든 정보를 가져오기
    paik_follow = list(db.paik_recipes.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'paik_follow': paik_follow})


# 백종원 공식레시피 API
@app.route('/official_recipes', methods=['POST'])
def official_recipes_save():
    # 요청할 때 함께 줄 데이터
    image_receive = request.form['image_give']
    title_receive = request.form['title_give']
    posting_day_receive = request.form['posting_day_give']
    description_receive = request.form['description_give']
    author_receive = request.form['author_give']
    url_receive = request.form['url_give']

    # 서버 내부에서 수행 할 기능 / mongoDB에 넣는 부분
    paik_official_recipe = {
        'image': image_receive,
        'title': title_receive,
        'posting_day': posting_day_receive,
        'description': description_receive,
        'author': author_receive,
        'url': url_receive
    }
    db.paik_official_recipes.insert_one(paik_official_recipe)

    return jsonify({'result': 'success'})


# 백종원 따라하기레시피 API
@app.route('/follow_recipes', methods=['POST'])
def follow_recipes_save():
    # 요청할 때 함께 줄 데이터
    image_receive = request.form['image_give']
    title_receive = request.form['title_give']
    posting_day_receive = request.form['posting_day_give']
    description_receive = request.form['description_give']
    author_receive = request.form['author_give']
    url_receive = request.form['url_give']

    # 서버 내부에서 수행 할 기능 / mongoDB에 넣는 부분
    paik_recipe = {
        'image': image_receive,
        'title': title_receive,
        'posting_day': posting_day_receive,
        'description': description_receive,
        'author': author_receive,
        'url': url_receive
    }
    db.paik_recipes.insert_one(paik_recipe)

    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)

