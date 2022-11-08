#!pip install selenium
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

#크롬 브라우저 띄우기(크롬 버전확인 후 다운로드)
browser = webdriver.Chrome('C:/chromedriver.exe')
browser.maximize_window()
url = "https://www.daangn.com/"
browser.get(url)
browser.implicitly_wait(2)

# 검색창에 아이폰을 입력 -> 아이템은 list로 for문을 만들어주면 됨
itemName = '아이폰'
xpath_text = '//*[@id="gnb-root"]/div/div/div/div/span[1]/span/input'
browser.find_element(By.XPATH, xpath_text).send_keys(itemName)
browser.find_element(By.XPATH, xpath_text).send_keys(Keys.ENTER)

#최대 페이지 : 834개 / 최대 상품 개수 : 834 * 12 = 10,008
#몇 주기로 돌리는지에 따라서 상품의 data가 많이 늘어날것으로 판단됨
no_page = 200
for _ in range(no_page):
    xpath_more = '//*[@id="result"]/div[1]/div[2]'
    browser.find_element(By.XPATH, xpath_more).click()
    time.sleep(1)

#클릭해서 6개 데이터를 가져오는시간:2초
#time.sleep(no_page*2)

items = browser.find_elements(By.CSS_SELECTOR, '.flea-market-article.flat-card')

#csv파일 생성, 컬럼 설정
f = open(r"data/" + itemName + ".csv", 'w', encoding='CP949', newline='')
csvWriter = csv.writer(f)
csvWriter.writerow(['no_product', 'nm_product', 'dt_upload', 'nm_region', 'no_price', 'dc_product_link', 'dc_main_image_link'])

#datatable 생성후 저장하려고 했으나, 통신에 오류가 생긴 row는 삭제하기로 판단
for item in items:
    try:
        dc_product_link = item.find_element(By.CSS_SELECTOR, '.flea-market-article.flat-card > a').get_attribute('href')
        #article index의 길이를 모름;
        no_product = dc_product_link[33:]
        dc_main_image_link = item.find_element(By.CSS_SELECTOR, '.card-photo > img').get_attribute('src')
        dt_upload = dc_main_image_link[52:58]
        nm_product = item.find_element(By.CSS_SELECTOR, '.article-title-content').text
        nm_region = item.find_element(By.CSS_SELECTOR, '.article-region-name').text
        no_price = item.find_element(By.CSS_SELECTOR, '.article-price').text

        csvWriter.writerow([no_product, nm_product, dt_upload, nm_region, no_price, dc_product_link, dc_main_image_link])

    except:
        link = item.find_element(By.CSS_SELECTOR, '.flea-market-article.flat-card > a').get_attribute('href')
        no_index = link[8:]
        print('error page(index no):', no_index)

f.close()



