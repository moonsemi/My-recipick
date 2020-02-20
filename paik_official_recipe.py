from selenium import webdriver
from bs4 import BeautifulSoup

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

driver = webdriver.Chrome(r'C:\Users\문세미\Downloads\chromedriver_win32/chromedriver.exe')
# 크롬을 연다. (★chromedriver.exe 의 경로를 제대로 설정해주는 것이 중요함)


driver.get('https://post.naver.com/my.nhn?memberNo=19357942')
# 조건을 검색해야하는 사이트를 들어간다.

driver.implicitly_wait(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.implicitly_wait(3)
driver.find_element_by_class_name("btn_lst_more").click()
# 레시피 100개까지 추출 / 참고)document.body.scrollHeight : 페이지 세로 길이

soup = BeautifulSoup(driver.page_source, 'html.parser')

paik_official_recipes = soup.select('#_my_list_container > ul.lst_feed > li._cds')

# insert 할 데이터 셋트를 만듦
paik_official_recipes_doc = {
    'image': '',
    'name': '',
    'title': '',
    'posting_day': '',
    'description': '',
    'author': '',
    'url': ''
}

for paik_official_recipe in paik_official_recipes:
    image = paik_official_recipe.select_one('a.link_end img').attrs['src']
    print(image)
    name = paik_official_recipe.select_one('div > div.feed_body > div.text_area > a > strong').text.split()[0]
    print(name)
    title = paik_official_recipe.select_one('div > div.feed_body > div.text_area > a > strong').text.split()[1]
    print(title)
    posting_day = paik_official_recipe.select_one('div > div.feed_head > div > div.info_post > time').text
    print(posting_day)
    # Q : 2020.02.14. -> 2020.02.14 마지막 '.'을 삭제하는 방법
    description = paik_official_recipe.select_one('div > div.feed_body > div.text_area > a > p').text
    print(description)
    author = '집밥백선생 블로그'
    print(author)
    pre_url = paik_official_recipe.select_one('div > div.feed_body > div.text_area > a').get('href')
    url = 'https://post.naver.com/' + pre_url
    print(url)

    paik_official_recipes_doc = {
        'image': image,
        'name': name,
        'title': title,
        'posting_day': posting_day,
        'description': description,
        'author': author,
        'url': url
    }

    db.paik_official_recipes.insert_one(paik_official_recipes_doc)
