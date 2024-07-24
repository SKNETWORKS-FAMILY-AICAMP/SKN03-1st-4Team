from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import os
# 구글 드라이버를 통해 오픈 - 현대 자동차 QnA
driver = webdriver.Chrome()
url = "https://www.hyundai.com/kr/ko/e/customer/center/faq"
driver.get(url)
driver.implicitly_wait(5)
######################################################################################################################3
# 저장할 빈 데이터 생성 -> 차량구매
data = []
# 스크롤 위치 조정
driver.execute_script("window.scrollTo(0, 1100)")
time.sleep(1)
# 추출할 데이터 반복 크롤링 (동적 페이지에 적용)
for i in range(1, 11):
    try:
        driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{i}]/button/div'.format(i=i)).click()
    except:
        break
    title = driver.find_element(By.XPATH,'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{i}]/button/div'.format(i=i)).text
    text = driver.find_element(By.XPATH,'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{i}]/div/div'.format(i=i)).text
    data.append({'title':title, 'text':text})
    pixel = 1100+i*60
    driver.execute_script("window.scrollTo(0, {pixel})".format(pixel=pixel))
    time.sleep(0.2)

# 추출할 데이터 csv 저장
df = pd.DataFrame(data)
try:
    df.to_csv('./csvsource/hyundai/현대_차량구매_QnA.csv', index=False, encoding='utf-8-sig')
except:
    os.mkdir('csvsource')
    os.mkdir('csvsource/hyundai')
######################################################################################################################3

# 저장할 빈 데이터 생성 -> 차량정비
data = []
# 스크롤 위치 조정
driver.execute_script("window.scrollTo(0, 900)")
time.sleep(1)
# 메뉴 클릭(선택) - 차량 정비
driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[1]/div[1]/ul/li[2]/button').click()
# 추출할 데이터 반복 크롤링 (동적 페이지에 적용)
for i in range(1, 11):
    try:
        driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{i}]/button/div'.format(i=i)).click()
    except:
        break
    title = driver.find_element(By.XPATH,'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{i}]/button/div'.format(i=i)).text
    text = driver.find_element(By.XPATH,'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{i}]/div/div'.format(i=i)).text
    data.append({'title':title, 'text':text})
    pixel = 1100+i*86
    driver.execute_script("window.scrollTo(0, {pixel})".format(pixel=pixel))
    time.sleep(0.37)

# 추출할 데이터 csv 저장
df = pd.DataFrame(data)
df.to_csv('./csvsource/hyundai/현대_차량정비_QnA.csv', index=False, encoding='utf-8-sig')
######################################################################################################################3
# 저장할 빈 데이터 생성 -> 홈페이지
data = []
# 스크롤 위치 조정
driver.execute_script("window.scrollTo(0, 900)")
time.sleep(1)
# 메뉴 클릭(선택) - 홈페이지
driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[1]/div[1]/ul/li[3]/button').click()
# 추출할 데이터 반복 크롤링 (동적 페이지에 적용)
for i in range(1, 11):
    try:
        driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{i}]/button/div'.format(i=i)).click()
    except:
        break
    title = driver.find_element(By.XPATH,'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{i}]/button/div'.format(i=i)).text
    text = driver.find_element(By.XPATH,'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{i}]/div/div'.format(i=i)).text
    data.append({'title':title, 'text':text})
    pixel = 1100+i*60
    driver.execute_script("window.scrollTo(0, {pixel})".format(pixel=pixel))
    time.sleep(0.2)

# 추출할 데이터 csv 저장
df = pd.DataFrame(data)
df.to_csv('./csvsource/hyundai/현대_홈페이지_QnA.csv', index=False, encoding='utf-8-sig')

######################################################################################################################3
# 저장할 빈 데이터 생성 -> 블루맴버스
data = []
# 스크롤 위치 조정
driver.execute_script("window.scrollTo(0, 900)")
time.sleep(1)
# 메뉴 클릭(선택) - 블루맴버스
driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[1]/div[1]/ul/li[4]/button').click()
# 추출할 데이터 반복 크롤링 (동적 페이지에 적용)
for i in range(1, 11):
    try:
        driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{i}]/button/div'.format(i=i)).click()
    except:
        break
    title = driver.find_element(By.XPATH,'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{i}]/button/div'.format(i=i)).text
    text = driver.find_element(By.XPATH,'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{i}]/div/div'.format(i=i)).text
    data.append({'title':title, 'text':text})
    pixel = 1100+i*60
    driver.execute_script("window.scrollTo(0, {pixel})".format(pixel=pixel))
    time.sleep(0.2)

# 추출할 데이터 csv 저장
df = pd.DataFrame(data)
df.to_csv('./csvsource/hyundai/현대_블루맴버스_QnA.csv', index=False, encoding='utf-8-sig')  

######################################################################################################################3
# 저장할 빈 데이터 생성 -> 모젠서비스
data = []
# 스크롤 위치 조정
driver.execute_script("window.scrollTo(0, 900)")
time.sleep(1)
# 메뉴 클릭(선택) - 모젠서비스
driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[1]/div[1]/ul/li[5]/button').click()
# 추출할 데이터 반복 크롤링 (동적 페이지에 적용)
for i in range(1, 11):
    try:
        driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{i}]/button/div'.format(i=i)).click()
    except:
        break
    title = driver.find_element(By.XPATH,'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{i}]/button/div'.format(i=i)).text
    text = driver.find_element(By.XPATH,'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{i}]/div/div'.format(i=i)).text
    data.append({'title':title, 'text':text})
    pixel = 1100+i*60
    driver.execute_script("window.scrollTo(0, {pixel})".format(pixel=pixel))
    time.sleep(0.2)

# 추출할 데이터 csv 저장
df = pd.DataFrame(data)
df.to_csv('./csvsource/hyundai/현대_모젠서비스_QnA.csv', index=False, encoding='utf-8-sig')  

######################################################################################################################3
# 저장할 빈 데이터 생성 -> 블루링크
data = []
# 스크롤 위치 조정
driver.execute_script("window.scrollTo(0, 900)")
time.sleep(1)
# 메뉴 클릭(선택) - 블루링크
driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[1]/div[1]/ul/li[6]/button').click()
# 추출할 데이터 반복 크롤링 (동적 페이지에 적용)
for i in range(1, 11):
    try:
        driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{i}]/button/div'.format(i=i)).click()
    except:
        break
    title = driver.find_element(By.XPATH,'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{i}]/button/div'.format(i=i)).text
    text = driver.find_element(By.XPATH,'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{i}]/div/div'.format(i=i)).text
    data.append({'title':title, 'text':text})
    pixel = 1100+i*60
    driver.execute_script("window.scrollTo(0, {pixel})".format(pixel=pixel))
    time.sleep(0.2)

# 추출할 데이터 csv 저장
df = pd.DataFrame(data)
df.to_csv('./csvsource/hyundai/현대_블루링크_QnA.csv', index=False, encoding='utf-8-sig')  

######################################################################################################################3
# 저장할 빈 데이터 생성 -> 현대디지털키
data = []
# 스크롤 위치 조정
driver.execute_script("window.scrollTo(0, 900)")
time.sleep(1)
# 메뉴 클릭(선택) - 현대디지털키
driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[1]/div[1]/ul/li[7]/button').click()
# 추출할 데이터 반복 크롤링 (동적 페이지에 적용)
for i in range(1, 11):
    try:
        driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{i}]/button/div'.format(i=i)).click()
    except:
        break
    title = driver.find_element(By.XPATH,'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{i}]/button/div'.format(i=i)).text
    text = driver.find_element(By.XPATH,'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{i}]/div/div'.format(i=i)).text
    data.append({'title':title, 'text':text})
    pixel = 1100+i*90
    driver.execute_script("window.scrollTo(0, {pixel})".format(pixel=pixel))
    time.sleep(0.35)

# 추출할 데이터 csv 저장
df = pd.DataFrame(data)
df.to_csv('./csvsource/hyundai/현대_현대디지털키_QnA.csv', index=False, encoding='utf-8-sig')  

driver.quit()
