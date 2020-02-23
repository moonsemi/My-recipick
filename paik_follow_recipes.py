from selenium import webdriver
from bs4 import BeautifulSoup

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

driver = webdriver.Chrome(r'C:\Users\문세미\Downloads\chromedriver_win32/chromedriver.exe')
# 크롬을 연다. (★chromedriver.exe 의 경로를 제대로 설정해주는 것이 중요함)

driver.get('https://post.naver.com/search/post.nhn?keyword=%EB%B0%B1%EC%A2%85%EC%9B%90+%EB%A0%88%EC%8B%9C%ED%94%BC')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.implicitly_wait(3)
driver.find_element_by_css_selector("#more_btn > button").click()
driver.implicitly_wait(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.implicitly_wait(3)

soup = BeautifulSoup(driver.page_source, 'html.parser')

paik_follow_recipes = soup.select('#el_list_container > ul > li')

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

for paik_follow_recipe in paik_follow_recipes:
    image = paik_follow_recipe.select_one('div > div.feed_body > div.image_area > a > img').attrs['src']
    print(image)
    category = '따라하기레시피'
    print(category)
    title = paik_follow_recipe.select_one('div > div.feed_body > div.text_area > a.link_end > strong').text.strip()
    print(title)
    posting_day = paik_follow_recipe.select_one('div > div.feed_head > div > div.info_post > time').text.strip()
    print(posting_day)
    description = paik_follow_recipe.select_one('div > div.feed_body > div.text_area > a.link_end > p').text
    print(description)
    author = paik_follow_recipe.select_one('div > div.feed_head > div > div.writer_area > p > span.name > a').text
    print(author)
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
