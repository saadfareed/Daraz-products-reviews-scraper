# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get("https://www.daraz.com.bd/bath-body/?page=2&spm=a2a0e.home.cate_4.1.25e84591fd3uEZ")

i=1
comments=[]
label=[]
link=[]
def collect(drive,p):
    x = 1

    while 1:
        try:
            print('collecting')
            name = drive.find_element_by_xpath('//*[@id="module_product_review"]/div/div[3]/div[1]/div' + str([x]))
            k = name.find_element_by_class_name("content")
            if k!=None:
                comments.append(k.text)
                label.append(p)
                print(k.text)
            x += 1
            print(x)
        except Exception as e:
            break
def change_page(driver,p):
    v = 2
    while v <= 5:
        try:
            but = driver.find_element_by_xpath('//*[@id="module_product_qna"]/div[2]/div[2]/div[2]/div/div')
            but.find_element_by_xpath('//button[contains(text(),' + str(v) + ')]').click()
            time.sleep(7)
            collect(driver,p)
            time.sleep(5)
            v = v + 1
        except Exception as e:
            break

while 1:
    try:
        name = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div[2]/div'+str([i])+'/div/div/div[1]/div')
        herf=name.find_element_by_css_selector('a').get_attribute('href')
        print(herf)
        i += 1
        link.append(herf)
    except Exception as e:
        print('finished')
        break
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
for i in range(len(link)-1):
    driver.get(link[i])
    print(link[i])
    time.sleep(10)
    try:
        print('changing for good reviews')
        driver.find_element_by_xpath('//*[@id="module_product_review"]/div/div[2]/div/div[1]').click()
        t = driver.find_element_by_class_name('next-menu-content')
        t.find_element_by_xpath("//li[contains(text(), '5 star')]").click()
        print('changed')
        time.sleep(7)
        collect(driver,1)
        change_page(driver,1)
        print('changing for bad reviews')
        driver.find_element_by_xpath('//*[@id="module_product_review"]/div/div[2]/div/div[1]').click()
        t = driver.find_element_by_class_name('next-menu-content')
        t.find_element_by_xpath("//li[contains(text(), '1 star')]").click()
        print('changed')
        time.sleep(7)
        collect(driver,0)
        change_page(driver,0)
    except:
        None
df = pd.DataFrame({"text":comments,
                         "label":label})
df.to_csv('data.csv', encoding='utf-8')
