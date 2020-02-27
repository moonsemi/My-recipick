from selenium import webdriver
from bs4 import BeautifulSoup

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

driver = webdriver.Chrome(r'C:\Users\문세미\Downloads\chromedriver_win32/chromedriver.exe')
# 크롬을 연다. (★chromedriver.exe 의 경로를 제대로 설정해주는 것이 중요함)


driver.get('https://post.naver.com/search/post.nhn?keyword=%EB%B0%B1%EC%A2%85%EC%9B%90+%EB%A7%8C%EB%93%A4%EA%B8%B0')
for page_num in range(1,11) :
    # '더보기'버튼 2 클릭
    # more_btn > button
    # // *[ @ id = "more_btn"] / button
    btn = driver.find_element_by_xpath('//*[@id="more_btn"]/button')
    btn.click()
    # 로딩 시간이 있으므로 타이밍 맞추기 위해 사용
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
    # if author ==  '집밥백선생' :
    #     continue
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
