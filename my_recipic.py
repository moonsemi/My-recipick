from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

app = Flask(__name__)


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


### API 역할을 하는 부분
## 레시피 리스트로 보여주기
# 백종원 공식레시피 API
@app.route('/official_recipes', methods=['GET'])
def official_recipes_view():
    # 서버 내부에서 수행 할 기능 / DB에 저장돼있는 모든 정보 중 '공식레시피' 가져오기
    paik_official = list(db.paik_all_recipes.find({'category': '공식레시피'}, {'_id': 0}))
    return jsonify({'result': 'success', 'paik_official': paik_official})


# 백종원 따라하기레시피 API
@app.route('/follow_recipes', methods=['GET'])
def follow_recipes_view():
    # 서버 내부에서 수행 할 기능 / DB에 저장돼있는 모든 정보 중 '따라하기레시피' 가져오기
    paik_follow = list(db.paik_all_recipes.find({'category': '따라하기레시피'}, {'_id': 0}))
    return jsonify({'result': 'success', 'paik_follow': paik_follow})


##################################### 레시피검색 API ######################################

@app.route('/search_paik_follow', methods=['GET'])
def search_paik_follow_view():
    # title_give로 클라이언트가 준 title을 가져오기
    title_receive = request.args.get('title_give')
    # title의 값이 받은 title과 일치하는 document 찾기 & _id 값은 출력에서 제외하기
    follow_recipe_info = list(db.paik_all_recipes.find({'category': '따라하기레시피', 'title': {'$regex': title_receive}}, {'_id': 0}))
    # info라는 키 값으로 해당하는 레시피 데이터 내려주기
    return jsonify({'result': 'success', 'follow_recipe_info': follow_recipe_info})


@app.route('/search_paik_official', methods=['GET'])
def search_paik_official_view():
    # title_give로 클라이언트가 준 title을 가져오기
    title_receive = request.args.get('title_give')
    # title의 값이 받은 title과 일치하는 document 찾기 & _id 값은 출력에서 제외하기
    official_recipe_info = list(db.paik_all_recipes.find({'category': '공식레시피', 'title': {'$regex': title_receive}}, {'_id': 0}))
    # info라는 키 값으로 해당하는 레시피 데이터 내려주기
    return jsonify({'result': 'success', 'official_recipe_info': official_recipe_info})


##################################### 레시피저장 API ######################################
@app.route('/save_follow_recipe', methods=['POST'])
def save_follow_recipe():
    # 클라이언트로부터 데이터를 받는 부분
    email_receive = request.form['email_give']
    # 요청할 때 함께 줄 데이터
    image_receive = request.form['image_give']
    title_receive = request.form['title_give']
    posting_day_receive = request.form['posting_day_give']
    description_receive = request.form['description_give']
    author_receive = request.form['author_give']
    url_receive = request.form['url_give']

    # 해당 레시피를 score로 업데이트 해주기
    db.save_follow_recipes.insert_one({
        'email': email_receive,
        'image': image_receive,
        'title': title_receive,
        'posting_day': posting_day_receive,
        'description': description_receive,
        'author': author_receive,
        'url': url_receive,
    })

    return jsonify({'result': 'success'})


# 백종원 공식레시피 API
# @app.route('/official_recipes', methods=['POST'])
# def official_recipes_save():
#     # 요청할 때 함께 줄 데이터
#     image_receive = request.form['image_give']
#     title_receive = request.form['title_give']
#     posting_day_receive = request.form['posting_day_give']
#     description_receive = request.form['description_give']
#     author_receive = request.form['author_give']
#     url_receive = request.form['url_give']
#
#     # 서버 내부에서 수행 할 기능 / mongoDB에 넣는 부분
#     paik_official_recipe = {
#         'image': image_receive,
#         'title': title_receive,
#         'posting_day': posting_day_receive,
#         'description': description_receive,
#         'author': author_receive,
#         'url': url_receive
#     }
#     db.paik_official_recipes.insert_one(paik_official_recipe)
#
#     return jsonify({'result': 'success'})
#
#
# # 백종원 따라하기레시피 API
# @app.route('/follow_recipes', methods=['POST'])
# def follow_recipes_save():
#     # 요청할 때 함께 줄 데이터
#     image_receive = request.form['image_give']
#     title_receive = request.form['title_give']
#     posting_day_receive = request.form['posting_day_give']
#     description_receive = request.form['description_give']
#     author_receive = request.form['author_give']
#     url_receive = request.form['url_give']
#
#     # 서버 내부에서 수행 할 기능 / mongoDB에 넣는 부분
#     paik_recipe = {
#         'image': image_receive,
#         'title': title_receive,
#         'posting_day': posting_day_receive,
#         'description': description_receive,
#         'author': author_receive,
#         'url': url_receive
#     }
#     db.paik_recipes.insert_one(paik_recipe)
#
#     return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)
