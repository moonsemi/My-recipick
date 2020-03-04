from selenium import webdriver
from bs4 import BeautifulSoup
from pymongo import MongoClient
import time


client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

driver = webdriver.Chrome('/Users/cho/Downloads/chromedriver') #원행's webdriver 경로
# 크롬을 연다. (★chromedriver.exe 의 경로를 제대로 설정해주는 것이 중요함)

url = 'https://post.naver.com/search/post.nhn?keyword=%EC%88%98%EB%AF%B8%EB%84%A4%EB%B0%98%EC%B0%AC+%EB%A0%88%EC%8B%9C%ED%94%BC+'
driver.get(url)

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
for cnt in range(0, 42):
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
		soomis_follow_recipes = soup.select('#_list_container > ul > li')

soomis_follow_recipe_doc = {
		'author': '',
		'description': '',
		'image': '',
		'category': '',
		'posting_day': '',
		'title': 'title',
		'url': url
	}

# 하나 더 만들어보자
for soomis_follow_recipe in soomis_follow_recipes:
    title = soomis_follow_recipe.select_one('div > div.feed_body > div.text_area > a.link_end > strong').text.strip()
    # 따라하기 레시피와 관련없는 post 제외
    if title == "'수미네 반찬' 할배특집 오징어초무침-김치콩나물국밥 레시피는?":
        continue
    if title == "'수미네 반찬' 할배특집 오징어초무침-김치콩나물국밥 레시피는?.":
        continue
    if title == "[공유] 엄마가 해주는 그 맛 <수미네반찬 닭볶음탕 레시피>":
        continue
    if title == "예스24 주목신간 수미네반찬  예스맘의 선택":
        continue
    if title == "예스24 요리책 구매_수미네반찬 도마 굿즈까지:)":
        continue
    if title == "[이슈Q] '수미네 반찬' 묵은지등갈비찜, '만물상' 레시피와 차이점은?":
        continue
    if title == "수미네반찬 47회 48회 재방송 무료 다시보기 레시피 무료보기":
        continue
    if title == "오늘의 레시피 - 두부두루치기":
        continue
    if title == "예스24 요리책 구매_ 수미네반찬 도마 굿즈까지:)":
        continue
    if title == "+ 11월주목도서 _ 수미네 반찬 레시피북 & 퇴근길 인문학 수업":
        continue
    if title == "[공유] 김수미표 고구마순갈치조림 수미네 반찬 레시피":
        continue
    if title == "오늘의 레시피 - 묵은지쌈밥":
        continue
    if title == "[공유] [Recipe of the Day] #4. 수미네반찬'소라비빔국수' 레시피":
        continue
    if title == "오늘의 레시피 - 수미네반찬 오징어전":
        continue
    if title == "수미네반찬 책 사고 예스24굿즈 미피 윷놀이사은품 받아써효":
        continue
    if title == "[공유] 수미네반찬 레시피 호박볶음, 간단한 반찬 만들기":
        continue
    if title == "+ 예스24도서 _ 엄마요리책,레시피북,쿡북!! 수미네반찬 도마받기!":
        continue
    if title == "[공유] ​수미네 반찬 묵은지볶음, 묵은지찜 레시피 밥도둑 인정!":
        continue
    if title == "김수미 대파김치 수미네반찬 대파김치 초간단 레시피!.":
        continue
    if title == "[공유] 저녁메뉴 고민 왜해? 수미네반찬 오징어볶음 양념장부터 황금레시피":
        continue
    if title == "레시피북 YES24굿즈와 함께 요리책으로 집밥해먹기 도전!":
        continue
    if title == "수미네반찬 책사고 디즈니굿즈도 득템!":
        continue
    if title == "수미네반찬":
        continue
    if title == "[공유] [이슈Q] '수미네 반찬' VS 김가연 멸치볶음 레시피 차이점은? 백종원표 멸치볶음도 '눈길'":
        continue
    if title == "예스24 주목신간 수미네반찬 예스맘의 선택":
        continue
    if title == "수미네반찬 책 사고 2월예스24굿즈 페코 틴케이스 받고~!!":
        continue
    if title == "예스24 요리책 구입하고 10월 예스베리굿즈 수미네반찬 도마 득템":
        continue
    if title == "[공유] '수미네 반찬' 닭볶음탕·멸치볶음·육전 레시피 공개… 미카엘 표 '치킨 키예프'는?":
        continue
    if title == "예스24에서 수미네반찬 책사고 굿즈로 마블지갑까지 겟!":
        continue
    if title == "예스24 수미네 반찬 책 고르고 귀여운 미피램프 득템♩":
        continue
    if title == "오늘의 레시피 - 애호박찌개":
        continue
    if title == "예스24 디즈니굿즈, 수미네반찬 구입하니 딱!":
        continue
    if title == "오늘의 레시피 - 대피김치":
        continue
    if title == "예스24굿즈 마블지갑 사은품으로 받을 수 있어요":
        continue
    if title == "요리책 사고 예스24굿즈 도마 득템":
        continue
    if title == "예스24 레시피북 사고 수미네반찬 도마 받음♬":
        continue
    if title == "레시피북 사고 수미네반찬 도마 받아요":
        continue
    if title == "+ 예스맘이 선택한 요리책 _ 수미네반찬2, 에어프라이어 레시피100 맛있게 요리하자!!":
        continue
    if title == "오늘의 레시피 - 옛날돈가스":
        continue
    if title == "오늘의 레시피 - 간장감자조림":
        continue
    if title == "예스24굿즈 수미네반찬 도마 요리책과 같이 겟~!":
        continue
    if title == "오늘의 레시피 - 애호박찌개":
        continue
    if title == "예스24 디즈니굿즈 , 수미네반찬 구입하니 딱!":
        continue
    if title == "오늘의 레시피 - 대파김치":
        continue
    if title == "예스24굿즈 마블지갑 사은품으로 받을 수 있어요":
        continue
    if title == "요리책 사고 예스24굿즈 도마 득템":
        continue
    if title == "레시피북 사고 수미네반찬 도마 받아요":
        continue
    if title == "예스24 집밥 레시피북 구입하고 받은 수미네반찬 도마 좋네":
        continue
    if title == "여보~정숙네 이거야 이거!":
        continue
    if title == "'수미네 반찬' 김수미표 코다리 조림 레시피는?":
        continue
    if title == "'수미네 반찬' 박준금 극찬한 김수미표 감자범벅에 오이냉국까지 완벽 조합은":
        continue
    if title == "[이슈Q] '수미네 반찬' 김수미표 김장김치는 남다르다? 생새우까지 들어간 레시피 공개":
        continue
    if title == "'수미네 반찬' 닭갈비 레시피, '집밥 백선생' 백종원과 비교하니? 오징어장조림 눈길":
        continue
    if title == "'수미네 반찬' 도미머리조림·돼지고기 두루치기 레시피 공개":
        continue
    if title == "[이슈Q] '수미네 반찬' VS 김가연 멸치볶음 레시피 차이점? 백종원표 멸치볶음 '눈길'":
        continue
    if title == "[이슈Q] '수미네 반찬' 시래기 꽁치조림·꼬막무침, '만물상' 매콤 고등어구이 레시피":
        continue
    if title == "'수미네 반찬' 김수미표 간장게장 레시피 공개":
        continue
    if title == "[이슈Q] '수미네 반찬' 고추장찌개, '집밥 백선생' 레시피와 비교해보니...고기 먼저?":
        continue
    if title == "'수미네 반찬' 닭볶음탕·멸치볶음·육전 레시피 공개… 미카엘 표 '치킨 키예프'는?":
        continue
    if title == "'수미네 반찬', '매콤 낙지볶음'·'조개탕'·'애호박 부추전' 레시피 공개":
        continue
    if title == "'수미네 반찬' 병어조림·떡잡채 레시피 공개":
        continue
    if title == "'수미네 반찬' 김수미, 강된장·소고기 고추장 볶음·풀치조림 레시피 공개":
        continue
    if title == "[이슈Q] '수미네 반찬' VS '만물상' 동태탕 레시피 차이점은? 새해 첫 레시피 눈길":
        continue
    if title == "'수미네 반찬', 떡갈비·도라지오징어 초무침·오이냉국 레시피 공개… 비프슬라이더 눈길":
        continue
    if title == "'수미네 반찬' 소꼬리찜·떡국 레시피는? 백종원 레시피와 비교해보니":
        continue
    if title == "'수미네 반찬' 레시피는? 여름맞이 막김치·양배추오이김치·가지김치·오이소박이·열무얼갈이김치":
        continue
    if title == "'수미네 반찬' 시청자 군침 돌게한 '묵은지 볶음'·'갑오징어 순대'·'간장게장' 레시피?":
        continue
    if title == "[TV본색] '알토란' 나박김치·'수미네 반찬' 찜닭·'만물상' 멸치볶음 레시피 인기":
        continue
    if title == "'수미네 반찬' 서울 불고기·묵은지고등어조림·계란장조림, '수미표' 레시피 공개":
        continue
    if title == "[이슈Q] '수미네 반찬' 알탕, 백종원 레시피로 활용 가능? '집밥 백선생'과 다른 점은":
        continue
    if title == "[이슈Q] '수미네 반찬' 갓김치, 두부조림 레시피 전수...'만물상' 두부조림과 차이점?":
        continue
    if title == "[이슈Q] '수미네 반찬' 전어회무침·대구뽈찜·꼬막무침, 미세먼지 예방에 좋은 미나리 요리":
        continue
    if title == "'수미네 반찬' 대파김치·'스페인하숙' 차승원 된장찌개·제육볶음… 스타들의 황금 레시피":
        continue
    if title == "'수미네 반찬' 황태해장국, 한마리 닭찜, 무생채 레시피 공개…김수미만의 비법은?":
        continue
    if title == "[이슈Q] '수미네 반찬' 한우등심 버섯전골 VS '만물상' 밀푀유나베 레시피 공개":
        continue
    if title == "'수미네 반찬' 초복 맞이 이색 레시피 공개… 아귀찜·전복간장찜·전복내장 영양밥은?":
        continue
    if title == "'수미네 반찬' 양념게장·묵은지 부대찌개…인도식 '감자 피클'은?":
        continue
    if title == "'수미네 반찬'에 열광하는 시청자들… '집밥 백선생' 열풍이 생각나는 이유는?":
        continue
    if title == "'수미네 반찬' 추석 명절 음식 갈비찜 레시피? 백종원 레시피와 비교해보니":
        continue
    if title == "[이슈Q] '수미네 반찬' 굴전, 백종원 레시피와 다른 점은? 피칸잔멸치볶음·떡볶이까지":
        continue
    if title == "[이슈Q] 김수미·백종원소고기 떡국 끓이는 법...기해년 첫날 해돋이와 함께 폭풍 흡입?":
        continue
    if title == "[베스트셀러 순위] 11월 2주차 이국종 교수 '골든아워' 1주만에 다시 1위 등극":
        continue
    if title == "[공유] [이슈Q] '수미네 반찬' 묵은지등갈비찜, '만물상' 레시피와 차이점은?":
        continue
    if title == "‘수미네 반찬’ 김수미, 유채 재래 된장찌개 레시피는?…제철에 꿀맛":
        continue
    if title == "‘수미네 반찬’ 감자채전, 재료에 햄 들어간다?…‘레시피 뭐길래’":
        continue
    if title == "김수미, 떡국 맛있게 끓이는법…'수미네 반찬'서 멸치육수로 만든 떡국 레시피 공개":
        continue
    if title == "‘수미네 반찬’ 초간단 애호박국수 레시피 공개…골든차일드 보민의 최셰프 따라잡기":
        continue
    if title == "\"이걸 어떻게 해야\"…'수미네반찬' 골든차일드 보민, 대형사고에 일동 '당황'":
        continue
    if title == "‘수미네 반찬’ 김수미표 돼지김치볶음 레시피는?…밥반찬으로 딱":
        continue
    if title == "‘수미네 반찬’ 김수미가 따라 한 골든차일드 보민의 ‘쭈굴미’":
        continue
    if title == "'수미네 반찬' 골든차일드 보민-최현석 셰프, 훈훈 브로맨스 선보여…'두부두루치기 도전'":
        continue
    if title == "황광희, 전문 요리프로→‘수미네 반찬’ 우왕좌왕…“여긴 전쟁터다”":
        continue
    if title == "‘수미네 반찬’ 김수미 레시피, 과메기조림-김치콩나물국밥 만드는 법은":
        continue
    if title == "\"보민이는 전의 달인\"…'수미네 반찬' 송훈 셰프, 마전 수업 中 골든차일드 보민 칭찬":
        continue
    if title == "‘수미네 반찬’ 김수미 레시피, 김장철 배추김치 담그는 법? '배추 절이기부터 김치소까지'":
        continue
    if title == "‘수미네 반찬’ 할배 특집 2탄, 초간단 ‘오이무침’ 레시피…입맛이 도는 맛":
        continue
    if title == "[★픽] ‘수미네 반찬’ 박준금이 그리워한 김수미표 감자범벅-오이냉국 레시피는?":
        continue
    if title == "‘수미네 반찬’ 김수미-여경래 레시피, 순대볶음부터 간짜장-가지전 초간단 레시피는 무엇?":
        continue
    if title == "‘수미네 반찬’ 송가인, ‘쫄면러버’ 입맛 저격…“최현석 100점 만점에 100점”":
        continue
    if title == "‘수미네 반찬’ 김수미표 갑오징어볶음-오이무침-한치물회 레시피 공개…‘만드는 법은?’":
        continue
    if title == "[★픽] ‘수미네 반찬’ 군부대 방문한 최현석, 등갈비 묵은지 김치찌개 선보여":
        continue
    if title == "‘수미네 반찬’ 초복 맞이 김수미표 보양 PICK 가지전 레시피 눈길":
        continue
    if title == "‘수미네 반찬’, 간장두부튀김-통명란계란말이-차돌된장찌개 레시피는?":
        continue
    if title == "‘수미네 반찬’ 임현식-김용건-전인권, 영보이된 이유는?…나이 궁금증↑":
        continue
    if title == "[★픽] ‘수미네 반찬’ 김수미, 손맛 그대로 전수한 ‘열무비빔국수’…레드벨벳 출연":
        continue
    if title == "‘수미네 반찬’ 김수미 레시피, 두부전골-청포묵김무침-오징어꽈리고추볶음 만드는 법은?":
        continue
    if title == "‘수미네 반찬’ 김수미표 완자궁중떡볶이-상추쫄면 레시피는?…비주얼부터 대박":
        continue
    if title == "‘수미네 반찬’ 김수미 레시피, 여름보양식 ‘민어매운탕’-‘민어조림’ 만드는 법은?":
        continue
    if title == "‘수미네 반찬’ 김수미 표 가지전 레시피는? 양념 잘 배기 위해 ‘칼집’이 포인트":
        continue
    if title == "[★픽] ‘수미네 반찬’ 김수미표 우럭매운탕 레시피는?…맛의 비법은 ‘수제비+새우젓’":
        continue
    if title == "“골든차일드 다 가르치고 싶다”…최보민, 전체 출연 제안에 ‘활짝 미소’":
        continue
    if title == "[★픽]‘수미네 반찬’ 최현석 셰프, 초간단 ‘우럭타르타르’ 레시피 공개…허세 필살기":
        continue
    if title == "골든차일드 보민, 김수미 사랑 독차지…요리 못해도 괜찮은 뽀스래기":
        continue
    if title == "'수미네 반찬' 김수미표 마전 레시피는? '밀가루 반죽과 10:4 비율 유지'":
        continue
    if title == "‘수미네 반찬’ 김수미 레시피, 순대볶음-오징어전-알배기배추물김치 만드는 법은?":
        continue
    if title == "[★픽] ‘수미네 반찬’ 김수미, 군부대 장병 위한 150분 깻잎김치 만들기":
        continue
    if title == "‘수미네 반찬’ 소시지김치볶음 레시피는? 아이들 반찬으로 딱":
        continue
    if title == "11월 4주 종합 베스트셀러 발표... 금주 1위??":
        continue
    if title == "2월 3주 종합 베스트셀러를 발표...1위는??":
        continue
    if title == "11월 2주 종합 베스트셀러 발표...1위는?":
        continue
    if title == "12월 4주 종합 베스트셀러 발표... 1위는?":
        continue
    if title == "11월 5주 종합 베스트셀러 발표... 1위는??":
        continue
    if title == "11월 3주 종합 베스트셀러 발표... 1위는??":
        continue
    if title == "3월 4주 종합 베스트셀러 발표... 1위는??":
        continue
    if title == "3월 5주 종합 베스트셀러 발표...1위는??":
        continue
    if title == "맛있는 요리를 금방 해내는 요리책들":
        continue
    if title == "YES24굿즈 핸디선풍기! 에어프라이어 홈베이킹 수미네반찬":
        continue
    if title == "수미네 반찬 레시피북 구매하고 예스베리굿즈 득템":
        continue
    if title == "10월예스24굿즈 수미네반찬 레시피북 사고 도마받고":
        continue
    if title == "수미네반찬 레시피북 사고 예스24굿즈 받았어요":
        continue
    if title == "예스베리굿즈 수미네반찬 이벤트!":
        continue
    if title == "예스24 요리책 구입시 10월예스24굿즈 수미네반찬 도마 사은품":
        continue
    if title == "요리책,엄마책 주문하고 예스24굿즈 수미네반찬 나무도마 받았어요~":
        continue
    if title == "수미네반찬 2 책 사고 예스24굿즈 받고!":
        continue
    if title == "예스24굿즈 백종원 집밥 레시피북 사고 도마 겟!":
        continue
    if title == "예스24굿즈 이번엔 수미네반찬 도마 ♬":
        continue
    if title == "요리책 700만이 뽑은 인생반찬 120 보고 예스24굿즈 도마 받고!":
        continue
    if title == "수미네반찬 백희나 신작 책 고르고 4월예스24굿즈 받으세요":
        continue
    if title == "예스베리굿즈 미피보냉백 너무예뻐 w.수미네반찬":
        continue
    if title == "이달의 주목신간 수미네반찬을 만나요 예스24":
        continue
    if title == "수미네반찬2 사고 주방장갑이 따라오는 예스24굿즈":
        continue
    if title == "수미네반찬책 ~ 사고 예스24에서 사은품 받기":
        continue
    if title == "예스24굿즈 , 백종원이 추천하는 집밥메뉴 구매하고 도마까지 득템했어요!":
        continue
    if title == "예스24에서 레시피북 사고 수미네반찬 도마 받기!":
        continue
    if title == "[교육뉴스] 실무형 인재 양성의 요람, 정화예술대학교 외식산업학부":
        continue
    if title == "캐릭터 말고 나, 대사 말고 내 이야기를 담았다! 배우가 쓴 책 5":
        continue
    if title == "키워드로 보는10년간의 '올해의 책'(2019년 올해의 책은?!)":
        continue
    if title == "예스24에서 요리책사고 수미네반찬 도마에서 요리하고":
        continue
    if title == "예스24에서 수미네반찬 사고 주방장갑 득템!":
        continue
    if title == "마블 엔드게임, 끝나지 않은 예스24의 푸짐한 예스24사은품, 수미네 반찬2사고 받았지요.":
        continue
    if title == "예스24창립20주년 수미네반찬 주방장갑 겟":
        continue
    if title == "예스24에서 백종원 레시피북 사고 수미네반찬 도마 받았어요":
        continue
    if title == "예스24 4월사은품 수미네반찬책 사고 우드트레이주방장갑 라벨스티커 득템":
        continue
    if title == "레시피북 사고 도마 사은품으로 받았어요!!":
        continue
    if title == "예스24 요리책 레시피북 구매 다양한 요리 책 보며 만들기":
        continue
    if title == "음식 하나로 초대박 난 연예인 사업가들은 누구?":
        continue
    if title == "레시피북 소문난반찬가게, 반찬이필요없는밥요리 그리고 수미네반찬 도마까지 득템":
        continue
    if title == "<수미네 반찬> 김수미의 고집이 만들어가는 감동":
        continue
    if title == "‘수미네 반찬’ 골든차일드 최보민, “좋은 선배님들과 함께해서 행복했다”":
        continue
    if title == "":
        continue

    # 공식 레시피 제외
    if title == "'수미네' 낙삼새전골&과메기조림&김치콩나물국밥":
        continue
    if title == "'수미네' 닭곰탕&총각무지짐&오징어순대":
        continue
    if title == "'수미네' 두부두루치기&겨울냉이강된장&애호박국수":
        continue
    if title == "'수미네' 섭국&단호박해물찜&파김치주물럭덮밥":
        continue
    if title == "<수미네 반찬> 레시피북 예약판매 소식":
        continue
    if title == "'수미네' 고추장고구마볶음&차돌버섯불고기&박대탕":
        continue
    if title == "'수미네' 우삼겹공심채볶음&노가리볶음&통오징어찌개":
        continue
    if title == "'수미네' 시금치김치&볼락매운탕&유채재래된장찌개":
        continue
    if title == "'수미네' 뚝불달래&황태구이&비빔만두":
        continue
    if title == "'수미네' 간장 게장 & 보리새우 아욱국 만들기":
        continue
    if title == "'수미네' 불꼬막무침&삼겹살묵은지말이찜&전복죽":
        continue
    if title == "'수미네' 우럭 매운탕 & 감자범벅 & 한치 물회 레시피":
        continue
    if title == "오늘 부터! 수미네 반찬 본방사수 이벤트":
        continue
    if title == "'수미네' 묵은지 볶음 & 묵은지 목살찜 만들기":
        continue
    if title == "'수미네' 묵은지 부대찌개 & 감자전 & 양념게장 만들기":
        continue
    if title == "'수미네' 말린조갯살볶음&매생이굴국&비빔당면":
        continue
    if title == "'수미네' 닭볶음탕 & 여리고추 멸치볶음 만들기":
        continue
    if title == "'수미네' 차돌박이된장찌개 & 통명란계란말이 & 간장두부튀김":
        continue
    if title == "'수미네' 한우등심 버섯전골 & 연근조림 & 고추장찌개 만들기":
        continue
    if title == "'수미네' 황태해장국 & 다시마 간장 닭찜 만들기":
        continue
    if title == "'수미네' 배추김치 만들기":
        continue
    if title == "'수미네' 소고기장조림 & 홍합 미역국 만들기":
        continue
    if title == "'수미네' 새뱅이 무 찌개 & 무말랭이무침 & 유부초밥 만들기":
        continue
    if title == "'수미네' 대구 뽈찜 & 해물 파전 & 소고기 무나물 만들기":
        continue
    if title == "'수미네' 시래기 꽁치 조림 & 꼬막 무침 & 어묵 조림 만들기":
        continue
    if title == "'수미네' 육개장 & 얼갈이열무 된장찜 & 박대 조림 만들기":
        continue
    if title == "'수미네' 옛날 돈가스 & 수프 & 고추종 마늘종 무침":
        continue
    if title == "'수미네' 잔치국수 & 나물 무침 &고추장 주물럭":
        continue
    if title == "'수미네' 우렁 된장찌개 & 오징어 볶음 & 더덕 구이 만들기":
        continue
    if title == "'수미네' 순대 볶음 & 양파,모듬 장아찌 & 아욱죽":
        continue
    if title == "'수미네' 갈비탕 & 완자궁중떡볶이 & 상추쫄면":
        continue
    if title == "[오늘] 9월 5일 (수) '수미네' 방송 안내":
        continue
    if title == "'수미네' 조기매운탕 & 오징어 장조림 & 수미네 닭갈비":
        continue
    if title == "'수미네' 묵밥 & 도토리묵전 & 갑오징어 볶음":
        continue
    if title == "'수미네' 도다리쑥국 & 달래전 & 바지락 칼제비":
        continue
    if title == "'수미네' 고사리 굴비 조림 & 연근전 만들기":
        continue
    if title == "'수미네' 꽃게 미더덕찜 & 카레 & 김밥":
        continue
    if title == "'수미네' 녹두전 & 세발낙지두부찌개 & 김치수제비":
        continue
    if title == "'수미네' 다됐어돼지김치찌개 & 두부고구마순조림 & 김치샌드위치":
        continue
    if title == "'수미네' 누룽지 오리백숙 & 가지전 & 열무비빔국수":
        continue
    if title == "'수미네' 머위 들깨무침+머위 쌈밥 & 얼갈이 된장국 + 묵은지 김치 짜글이":
        continue
    if title == "'수미네' 바지락순두부찌개 & 감자채볶음 만들기":
        continue
    if title == "'수미네' 떡갈비 & 오징어 도라지 초무침 만들기":
        continue
    if title == "바로, 오늘! 수미네 괌특집 2탄 공개방송 현장을 공개합니다!":
        continue
    if title == "'수미네' 서울 불고기 & 묵은지 고등어조림 만들기":
        continue
    if title == "'수미네' 묵은지 비지찌개 & 임연수어 조림 & 나박김치":
        continue
    if title == "'수미네' 닭칼국수 & 메밀전병 & 오이고추김치":
        continue
    if title == "'수미네' LA갈비찜 & 취나물 & 만두 만들기":
        continue
    if title == "'수미네' 멸치찌개 & 유채 겉절이 김치 & 콩나물 잡채":
        continue
    if title == "'수미네' 재첩국 & 씀바귀,방풍나물 튀김 & 매운 돼지갈비찜":
        continue
    if title == "'수미네' 주꾸미볶음 & 황태채무침 & 시래기된장국 만들기":
        continue
    if title == "'수미네' 냉이 된장국 & 톳 두부 무침 & 주꾸미 샤부샤부 만들기":
        continue
    if title == "'수미네' 전어회 무침 & 소고기우엉조림 만들기":
        continue
    if title == "'수미네' 병어 조림 & 전주식 콩나물탕 만들기":
        continue
    if title == "'수미네' 김수미표 알탕 & 진미채 볶음 만들기":
        continue
    if title == "'수미네' 오이소박이 & 열무김치 만들기":
        continue
    if title == "'수미네' 참소라 강된장 & 풀치 조림 만들기":
        continue
    if title == "'수미네' 낙지볶음 & 조개탕 만들기":
        continue
    if title == "'수미네' 아귀찜 & 전복내장 영양밥 만들기":
        continue
    if title == "'수미네' 코다리조림 & 검은콩국수 만들기":
        continue
    if title == "'수미네' 문어장조림&시래기청국장&부추꾸미":
        continue
    if title == "'수미네' 오징어초무침&밀푀유전골&해초무침3종세트":
        continue
    if title == "'수미네' 고추장고구마볶음 & 차돌버섯불고기 & 박대탕":
        continue
    print(title)


    image = str(soomis_follow_recipe.select_one('div > div.feed_body > div.image_area > a.link_end > img ').attrs['src'])
    print(image)


    category = '따라하기 레시피'
    print(category)


    posting_day = str(soomis_follow_recipe.select_one('div.feed_head > div > div.info_post > time').text.split()[0])
    print(posting_day)


    description = soomis_follow_recipe.select_one('div.feed_body > div.text_area > a.link_end > p').text
    print(description)


    author = soomis_follow_recipe.select_one('div.feed_head > div > div.writer_area > p.writer > span.name > a').text
    print(author)


    pre_url = soomis_follow_recipe.select_one('div.feed_body > div.text_area > a.link_end').get('href')
    url = 'https://post.naver.com' + pre_url
    print(url)


    soomis_follow_recipe_doc = {
        'author': author,
        'description': description,
        'image': image,
        'category': category,
        'posting_day': posting_day,
        'title': title,
        'url': url
    }

    db.soomi_all_recipes.insert_one(soomis_follow_recipe_doc) #저장할때만 활성화 시키기
    # db.soomis_follow_recipes.insert_one(soomis_follow_recipe_doc) #저장할때만 활성화 시키기
driver.close()

