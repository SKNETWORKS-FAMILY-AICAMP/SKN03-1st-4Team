import time 
import csv
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver import Keys, ActionChains
import pyperclip 
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = "https://www.kia.com/"
driver.get(url)

# FAQ 페이지로 이동
driver.get('https://www.kia.com/kr/customer-service/center/faq')

# 특정 요소가 로드될 때까지 기다리기
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'cmp-accordion__title')))

# 페이지 소스 가져오기
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 원하는 요소 찾기
title_list = soup.find_all("span", class_="cmp-accordion__title")
for title in title_list:
    print(title.text)

content_list=soup.find_all("div", class_="container responsivegrid")
for content in content_list:
    print(content.text)

# CSV 파일로 저장
with open('kia_faq_top10.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['질의제목', '질의내용'])
    
    for title, content in zip(title_list, content_list):
        writer.writerow([title.text.strip(), content.text.strip()])

# 웹 드라이버 종료
driver.quit()