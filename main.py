
# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get("https://www.daraz.com.bd/bath-body/?page=2&spm=a2a0e.home.cate_4.1.25e84591fd3uEZ")

i=1
comments=[]
link=[]
while 1:
    try:
        name = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div[2]/div'+str([i])+'/div/div/div[1]/div')
        herf=name.find_element_by_css_selector('a').get_attribute('href')
        print(herf)
        i += 1
        link.append(herf)
    except Exception as e:
        break
for i in range(len(link)-1):
    driver.get(link[i])
    x = 1
    while 1:
        try:
            name = driver.find_element_by_xpath('//*[@id="module_product_review"]/div/div[3]/div[1]/div'+str([x]))
            k = name.find_element_by_class_name("content")
            comments.append(k.text)
            print(k.text)
            x += 1
        except Exception as e:
            break


df = pd.DataFrame(comments)
print(df)
df.to_csv('data.csv')
