from selenium import webdriver
from bs4 import BeautifulSoup

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

driver = webdriver.Chrome(r'C:\Users\문세미\Downloads\chromedriver_win32/chromedriver.exe')
# 크롬을 연다. (★chromedriver.exe 의 경로를 제대로 설정해주는 것이 중요함)


driver.get('https://post.naver.com/search/post.nhn?keyword=%EB%B0%B1%EC%A2%85%EC%9B%90+%EB%A7%8C%EB%93%A4%EA%B8%B0')
for page_num in range(1,41) :
    # '더보기'버튼 40번 클릭
    # more_btn > button
    # // *[ @ id = "more_btn"] / button
    btn = driver.find_element_by_xpath('//*[@id="more_btn"]/button')
    btn.click()
    # 로딩 시간이 있으므로 타이밍 맞추기 위해 사용
    driver.implicitly_wait(10)

soup = BeautifulSoup(driver.page_source, 'html.parser')

paik_follow_recipes = soup.select('#_list_container > ul > li')

#  insert 할 데이터 셋트를 만듦
paik_follow_recipe_doc = {
    'image': '',
    'category': '',
    'title': '',
    'posting_day': '',
    'description': '',
    'author': '',
    'url': ''
}
# 109개 밖에 저장이 안되어있음 / 만개의 레시피 등 이미지 arrts없는 것들
# AttributeError: 'NoneType' object has no attribute 'attrs'
for paik_follow_recipe in paik_follow_recipes:
   try:
       author = paik_follow_recipe.select_one('div > div.feed_head > div > div.writer_area > p > span.name > a').text.strip()
       if author == '집밥백선생':
           continue
       print(author)
       image = paik_follow_recipe.select_one('div > div.feed_body > div.image_area > a > img').attrs['src']
       print(image)
       category = '따라하기레시피'
       print(category)
       title = paik_follow_recipe.select_one('div > div.feed_body > div.text_area > a.link_end > strong').text.strip()
       if title == "레시피 모음 best5! 깨알팁만 모아봤어유":
           continue
       if title == "‘골목식당’ 백종원, 홍제동 감자탕집에 요구한 바쿠테 뭐길래?…“바쿠테해도 답 없네”":
           continue
       if title == "혈관 질환 예방 도와주는 계란, 편견의 껍질 깨고 많이 드세요":
           continue
       if title == "제2 백종원·제2 이강인 키우고… 프리랜서맘도 출산 급여 지급":
           continue
       if title == "456수미네 반찬 매콤 진미채볶음 만드는 법,김수미표 초간단 진미채볶음":
           continue
       if title == "아내 소유진 자격증 자랑한 백종원이 돌연 김희철 질투한 사연":
           continue
       if title == "집밥백선생 술빵 만들기.":
           continue
       if title == "수미네반찬 옛날식 매콤한 고추장 감자조림 만드는 법,매콤한 엄마표 수미네감자조림":
           continue
       if title == "화제의 강식당2 '김치밥이 피오씁니다' 만들었씁니다!":
           continue
       if title == "419수미네 반찬 추석 명절 요리 갈비찜 만드는 법,추석 명절 요리 소갈비찜":
           continue
       if title == "출산 후 회복에 좋은 음식,초간단 천연조미료":
           continue
       if title == "살랑이는 가을바람,감성을 더한 한 그릇[오코노미야키덮밥]":
           continue
       if title == "백선생 짜장면 만들기.":
           continue
       if title == "“아니 벌써?” 구독자 많아지더니 벌써 PPL 넣은 유튜버":
           continue
       if title == "집밥백선생 콩나물찌개 만들기.":
           continue
       if title == "집밥백선생 추억의 왕돈가스 만들기":
           continue
       if title == "집밥백선생 고깃집 볶음밥 만들기.":
           continue
       if title == "집밥백선생 만능 간장 만들기.":
           continue
       if title == "집밥백선생 만능간장으로 '초간단 잡채' 만들기":
           continue
       if title == "집밥백선생 양파 캐러멜 카레 만들기.":
           continue
       if title == "백선생 식당식 폭탄 계란찜 만들기":
           continue
       if title == "[백종원의 제주 타운] 포방터시장 연돈이 더본호텔 옆으로 간 까닭 (feat. 골목식당)":
           continue
       print(title)
       posting_day = paik_follow_recipe.select_one('div > div.feed_head > div > div.info_post > time').text.strip()
       print(posting_day)
       description = paik_follow_recipe.select_one('div > div.feed_body > div.text_area > a.link_end > p').text
       print(description)
       pre_url = paik_follow_recipe.select_one('div > div.feed_body > div.text_area > a.link_end').get('href')
       url = 'https://post.naver.com/' + pre_url
       print(url)

       paik_follow_recipe_doc = {
           'image': image,
           'category': category,
           'title': title,
           'posting_day': posting_day,
           'description': description,
           'author': author,
           'url': url
       }

       db.paik_all_recipes.insert_one(paik_follow_recipe_doc)
   except AttributeError :
       continue
