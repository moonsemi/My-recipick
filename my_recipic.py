from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
from random import random
import random
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

# 김수미 공식레시피 API
@app.route('/s_official_recipes', methods=['GET'])
def official_recipes_view():
    # 서버 내부에서 수행 할 기능 / DB에 저장돼있는 모든 정보 중 '공식레시피' 가져오기
    soomis_official = list(db.soomi_all_recipes.find({'category':'공식레시피'}, {'_id': 0}))
    return jsonify({'result': 'success', 'soomis_official': soomis_official})

# 백종원 따라하기레시피 API
@app.route('/follow_recipes', methods=['GET'])
def follow_recipes_view():
    # 서버 내부에서 수행 할 기능 / DB에 저장돼있는 모든 정보 중 '따라하기레시피' 가져오기
    paik_follow = list(db.paik_all_recipes.find({'category': '따라하기레시피'}, {'_id': 0}))
    return jsonify({'result': 'success', 'paik_follow': paik_follow})

# 김수미 따라하기레시피 API
@app.route('/s_follow_recipes', methods=['GET'])
def follow_recipes_view():
    # 서버 내부에서 수행 할 기능 / DB에 저장돼있는 모든 정보 중 '따라하기레시피' 가져오기
    soomis_follow = list(db.soomi_all_recipes.find({'category':'따라하기 레시피'}, {'_id': 0}))
    return jsonify({'result': 'success', 'soomis_follow': soomis_follow})
##################################### 레시피검색 API ######################################
# 백종원 따라하기 레시피 검색 api
@app.route('/search_paik_follow', methods=['GET'])
def search_paik_follow_view():
    # title_give로 클라이언트가 준 title을 가져오기
    title_receive = request.args.get('title_give')
    # title의 값이 받은 title과 일치하는 document 찾기 & _id 값은 출력에서 제외하기
    follow_recipe_info = list(
        db.paik_all_recipes.find({'category': '따라하기레시피', 'title': {'$regex': title_receive}}, {'_id': 0}))
    # info라는 키 값으로 해당하는 레시피 데이터 내려주기
    return jsonify({'result': 'success', 'follow_recipe_info': follow_recipe_info})

# 김수미 따라하기 레시피 검색 api
@app.route('/search_soomi_follow', methods=['GET'])
def search_soomi_follow_view():
    # title_give로 클라이언트가 준 title을 가져오기
    title_receive = request.args.get('recipe_title_give')
    # title의 값이 받은 title과 일치하는 document 찾기 & _id 값은 출력에서 제외하기
    soomis_follow_info = list(db.soomi_all_recipes.find({'category':'따라하기 레시피','title':{'$regex':title_receive}}, {'_id': 0}))
    # info라는 키 값으로 해당하는 레시피 데이터 내려주기
    return jsonify({'result': 'success', 'soomis_follow_info': soomis_follow_info})

# 백종원 공식레시피 검색 api
@app.route('/search_paik_official', methods=['GET'])
def search_paik_official_view():
    # title_give로 클라이언트가 준 title을 가져오기
    title_receive = request.args.get('title_give')
    # title의 값이 받은 title과 일치하는 document 찾기 & _id 값은 출력에서 제외하기
    official_recipe_info = list(
        db.paik_all_recipes.find({'category': '공식레시피', 'title': {'$regex': title_receive}}, {'_id': 0}))
    # info라는 키 값으로 해당하는 레시피 데이터 내려주기
    return jsonify({'result': 'success', 'official_recipe_info': official_recipe_info})

# 김수미 공식레시피 검색 api
@app.route('/search_soomi_official', methods=['GET'])
def search_soomi_official_view():
    # title_give로 클라이언트가 준 title을 가져오기
    title_receive = request.args.get('recipe_title_give')
    # title의 값이 받은 title과 일치하는 document 찾기 & _id 값은 출력에서 제외하기
    soomis_official_info = list(db.soomi_all_recipes.find({'category':'공식레시피','title':{'$regex':title_receive}}, {'_id': 0}))
    # info라는 키 값으로 해당하는 레시피 데이터 내려주기
    return jsonify({'result': 'success', 'soomis_official_info': soomis_official_info})

##################################### 레시피저장 API ######################################
@app.route('/save_paik_recipe', methods=['POST'])
def save_paik_recipe():
    # 클라이언트로부터 데이터를 받는 부분
    email_receive = request.form['email_give']
    url_receive = request.form['url_give']
    # 사용자가 저장한 레시피의 url 파라미터를 'paik_all_recipes' db에서 조회한 후 카테고리 값 뽑기
    paik_recipes_info = db.paik_all_recipes.find_one({'url': url_receive}, {'_id': 0})['category']
    print(paik_recipes_info)

    if paik_recipes_info == '따라하기레시피' :
        db.save_paik_follow.insert_one({
            'email': email_receive,
            'url': url_receive,
        })
    else:
        db.save_paik_official.insert_one({
            'email': email_receive,
            'url': url_receive,
        })
    # '공식레시피'이면 'save_paik_official' db에 저장되고, '따라하기레시피'이면 'save_paik_follow' db에 저장
    # !!!!!!!!!!!!!!!!!!!!!!!!!!! 코드리뷰  !!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!! 유저가 저장하려는 레시피가 이미 저장되어 있다면 중복저장하지 말기 !!!!!!!!
    return jsonify({'result': 'success'})


##################################### 나의레시피 조회 API ######################################
@app.route('/myrecipes_official_view', methods=['GET'])
def myrecipes_official_view():
    # email_give로 클라이언트가 준 email을 가져오기
    email_receive = request.args.get('email_give')
    # print(email_receive)
    # email의 값이 받은 email과 일치하는 document 찾기 & _id 값은 출력에서 제외하기
    myrecipes_official_user_info = list(db.save_paik_official.find({'email': email_receive}, {'_id': 0}))
    print(myrecipes_official_user_info)
    for email_receive in myrecipes_official_user_info :
        print(email_receive)
        target_url = email_receive['url']
        print(target_url)
    myrecipes_official_info = list(db.paik_all_recipes.find({'url': target_url},{'_id': 0}))
    print(myrecipes_official_info)
    for target_url in myrecipes_official_info :
        print(target_url)
        return jsonify({'result': 'success', 'myrecipes_official_info': myrecipes_official_info})

# @app.route('/myrecipes_follow_view', methods=['GET'])
# def myrecipes_follow_view():
#     # email_give로 클라이언트가 준 email을 가져오기
#     email_receive = request.args.get('email_give')
#     # print(email_receive)
#     # email의 값이 받은 email과 일치하는 document 찾기 & _id 값은 출력에서 제외하기
#     myrecipes_follow_url_info = list(db.save_paik_follow.find({'email': email_receive}, {'_id': 0}))
#     # print(myrecipes_official_url_info)
#     for email in myrecipes_follow_url_info:
#         # print(email['url'])
#         target_url = email['url']
#         # print(target_url)
#         # if target_url ==
#         # ㄴ 코드리뷰 !!!!!!!!!!!!!!!!! 레시피url이 중복이면 하나의 url만 보여주기 !!!!!!!!!!!!!!!!! 코드리뷰
#
#         myrecipes_follow_info = list(db.paik_all_recipes.find({'url': target_url}, {'_id': 0}))
#         # print(myrecipes_official_info)
#         return jsonify({'result': 'success', 'myrecipes_follow_info': myrecipes_follow_info})

##################################### 레시피 랜덤 뿌리기 API #####################################
#김수미 레시피 title 랜덤으로 뿌리기
@app.route('/paik_rand_follow_recipes', methods=['GET'])
def random_recipes():
    # paik_all_recipes 10번 돌면서 recipe 축적
    for repeat in range(10):
        # 백종원의 공식 레시피 400개에서 title만 꺼내온다
        random_recipe = list(db.paik_all_recipes.find({'category':'공식레시피'}, {'_id': 0}))
        paik_random_recipe = (random.sample(random_recipe, 40)) #max = 80개씩 뿌릴수 있음

    return jsonify({'result': 'success', 'paik_random_recipe': paik_random_recipe})

##################################### 레시피 정렬해서 뿌리기 API #####################################
# 사용시에만 활성화 해주세요
# @app.route('/s_show_recipes', methods=['GET'])
# def show_listing():
#     title_show = list(db.paik_all_recipes.find({'category':'공식레시피'}, {'_id': 0}))
#     print(soomis_show)
#     return jsonify({'result': 'success', 'title_show': title_show})

if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)
