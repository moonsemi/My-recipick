from selenium import webdriver
from bs4 import BeautifulSoup

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

driver = webdriver.Chrome(r'C:\Users\문세미\Downloads\chromedriver_win32/chromedriver.exe')
# 크롬을 연다. (★chromedriver.exe 의 경로를 제대로 설정해주는 것이 중요함)


driver.get('https://search.naver.com/')
driver.find_element_by_id("query").send_keys("백종원 레시피")
driver.find_element_by_id("search_btn").click()
driver.find_element_by_class_name("go_more").click()
for page in range(1, 10):
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    paik_recipes = soup.select('#main_pack > div.blog.section._blogBase._prs_blg > ul > li')

    #  insert 할 데이터 셋트를 만듦
    paik_recipe_doc = {
        'image': '',
        'name': '',
        'title': '',
        'posting_day': '',
        'description': '',
        'author': '',
        'url': ''
    }

    for paik_recipe in paik_recipes:
        image = paik_recipe.select_one('img.sh_blog_thumbnail').attrs['src']
        print(image)
        name = '백종원'
        print(name)
        title = paik_recipe.select_one('dl > dt > a').text
        print(title)
        posting_day = paik_recipe.select_one('dl > dd.txt_inline').text
        print(posting_day)
        # Q : 2020.02.14. -> 2020.02.14 마지막 '.'을 삭제하는 방법
        description = paik_recipe.select_one('dl > dd.sh_blog_passage').text
        print(description)
        # sp_blog_1 > dl > dd.txt_block > span > a:nth-child(1)
        author = paik_recipe.select_one('dl > dd.txt_block > span > a.txt84').text
        print(author)
        # sp_blog_1 > dl > dd.txt_block > span > a.url
        url = paik_recipe.select_one('dl > dd.txt_block > span > a.url').get('href')
        print(url)

        paik_recipe_doc = {
            'image': image,
            'name': name,
            'title': title,
            'posting_day': posting_day,
            'description': description,
            'author': author,
            'url': url
        }

        db.paik_recipes.insert_one(paik_recipe_doc)
    # // *[ @ id = "main_pack"] / div[4] / a[1]
    driver.find_element_by_xpath('// *[ @ id = "main_pack"] / div[4] / a[%s]' % page).click()