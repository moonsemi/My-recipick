from selenium import webdriver
from bs4 import BeautifulSoup

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

driver = webdriver.Chrome(r'C:\Users\문세미\Downloads\chromedriver_win32/chromedriver.exe')
# 크롬을 연다. (★chromedriver.exe 의 경로를 제대로 설정해주는 것이 중요함)


driver.get('https://post.naver.com/search/post.nhn?keyword=%EB%B0%B1%EC%A2%85%EC%9B%90+%EB%A7%8C%EB%93%A4%EA%B8%B0')
for page_num in range(1,31) :
    # '더보기'버튼 30번 클릭
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
    author = paik_follow_recipe.select_one('div > div.feed_head > div > div.writer_area > p > span.name > a').text
    if author == '집밥백선생':
        continue
    if author == 'wozm2368':
        continue
    if author == '만개의레시피':
        continue
    print(author)
    no_img = paik_follow_recipe.select_one('div > div.feed_body > div.image_area > a > img').attrs
    if no_img != None :
        image = paik_follow_recipe.select_one('div > div.feed_body > div.image_area > a > img').attrs['src']
    print(image)
    category = '따라하기레시피'
    print(category)
    title = paik_follow_recipe.select_one('div > div.feed_body > div.text_area > a.link_end > strong').text.strip()
    if title == ' 레시피 모음 best5! 깨알팁만 모아봤어유':
        continue
    if title == '주말, 맛있는 백종원 집반찬 만들기':
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
