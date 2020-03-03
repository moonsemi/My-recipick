from selenium import webdriver
from bs4 import BeautifulSoup
from pymongo import MongoClient
import time

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

# driver = webdriver.Chrome('C:\Users\문세미\Desktop\sparta\python_project_test\venv\Scripts\python.exe') #세미's webdriver 경로
driver = webdriver.Chrome('/Users/cho/Downloads/chromedriver') #원행's webdriver 경로
# 크롬을 연다. (★chromedriver.exe 의 경로를 제대로 설정해주는 것이 중요함)


url = 'https://post.naver.com/my/series/detail.nhn?seriesNo=472832&memberNo=3669297'
driver.get(url)

SCROLL_PAUSE_TIME = 0.5
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
for cnt in range(1, 4):
	driver.find_element_by_xpath('//*[@id="more_btn"]/button').click()

	# btn 클릭후 스크롤 하단으로 내리기 반복
	while True:
		# Scroll down to bottom
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

		# Wait to load page
		time.sleep(SCROLL_PAUSE_TIME)

		# Calculate new scroll height and compare with last scroll height
		new_height = driver.execute_script("return document.body.scrollHeight")
		if new_height == last_height:
			break
		last_height = new_height
		soup = BeautifulSoup(driver.page_source, 'html.parser')
		soomis_official_recipes = soup.select('#el_list_container > ul > ul > li ')

for soomis_official_recipe in soomis_official_recipes:
	soomis_official_recipe_doc = {
		'author': '',
		'description': '',
		'image': '',
		'category': '',
		'posting_day': '',
		'title': 'title',
		'url': url
	}
	print(cnt_up)

	# 레시피와 관련없는 post 제외
	title = soomis_official_recipe.select_one('div.spot_post_name').text.strip()
	if title == "바로, 오늘! 수미네 괌특집 2탄 공개방송 현장을 공개합니다!":
		continue
	if title == "[오늘] 9월 5일 (수) '수미네' 방송 안내":
		continue
	if title == "<수미네 반찬> 레시피북 예약판매 소식":
		continue
	if title == "'수미네' 스승의 날 특집":
		continue
	if title == "'수미네' 어버이날 특집":
		continue
	print(title)


	image = str(soomis_official_recipe.select_one('img').attrs['src'])
	print(image)


	category = '공식레시피'
	print(category)

	posting_day = str(soomis_official_recipe.select_one('a > p').text.split()[0])
	print(posting_day)

	description = '수미네반찬 공식 레시피'
	print(description)

	author = '수미네반찬 블로그'
	print(author)

	pre_url = soomis_official_recipe.select_one('a.spot_post_area').get('href')
	url = 'https://post.naver.com' + pre_url
	print(url)


	soomis_official_recipe_doc = {
		'author': author,
		'description': description,
		'image': image,
		'category': category,
		'posting_day': posting_day,
		'title': title,
		'url': url
	}



        #db에 뽑은 data 저장
	# db.soomi_all_recipes.insert_one(soomis_official_recipe_doc) #저장할때만 활성화 시키기
	# db.soomis_official_recipes.insert_one(soomis_official_recipe_doc)
driver.close()

