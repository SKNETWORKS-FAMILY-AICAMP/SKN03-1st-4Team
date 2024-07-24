from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()
url = "https://www.hyundai.com/kr/ko/e/customer/center/faq"
driver.get(url)
driver.implicitly_wait(5)

data = []

driver.execute_script("window.scrollTo(0, 1100)")
time.sleep(1)

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


    
driver.quit()

df = pd.DataFrame(data)
df.to_csv('현대_차량구매_QnA.csv', index=False, encoding='utf-8-sig')
