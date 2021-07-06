# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
op=webdriver.ChromeOptions()
op.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument('--headless')
op.add_argument('--no-sandbox')
op.add_argument('--disable-dev-sh-usage')
#from webdriver_manager.firefox import GeckoDriverManager
driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=op)
#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

##driver.get("https://www.daraz.com.bd/bath-body/?page=2&spm=a2a0e.home.cate_4.1.25e84591fd3uEZ")
list_link=[
    "https://www.daraz.com.bd/cereal/?page=1&spm=a2a0e.home.cate_6_2.2.107a12f7jJBzfg",
    "https://www.daraz.com.bd/cereal/?page=2&spm=a2a0e.home.cate_6_2.2.107a12f7jJBzfg",
    "https://www.daraz.com.bd/cereal/?page=3&spm=a2a0e.home.cate_6_2.2.107a12f7jJBzfg",
    "https://www.daraz.com.bd/cereal/?page=4&spm=a2a0e.home.cate_6_2.2.107a12f7jJBzfg",
    "https://www.daraz.com.bd/cereal/?page=5&spm=a2a0e.home.cate_6_2.2.107a12f7jJBzfg",
    "https://www.daraz.com.bd/cereal/?page=6&spm=a2a0e.home.cate_6_2.2.107a12f7jJBzfg",
    "https://www.daraz.com.bd/cereal/?page=7&spm=a2a0e.home.cate_6_2.2.107a12f7jJBzfg",
    "https://www.daraz.com.bd/mother-baby/?spm=a2a0e.searchlistcategory.cate_5.1.6d4158dfpM1n6k",
    "https://www.daraz.com.bd/mother-baby/?page=2&spm=a2a0e.searchlistcategory.cate_5.1.6d4158dfpM1n6k",
    "https://www.daraz.com.bd/mother-baby/?page=3&spm=a2a0e.searchlistcategory.cate_5.1.6d4158dfpM1n6k",
    "https://www.daraz.com.bd/mother-baby/?page=4&spm=a2a0e.searchlistcategory.cate_5.1.6d4158dfpM1n6k",
    "https://www.daraz.com.bd/mother-baby/?page=5&spm=a2a0e.searchlistcategory.cate_5.1.6d4158dfpM1n6k",
    "https://www.daraz.com.bd/mother-baby/?page=6&spm=a2a0e.searchlistcategory.cate_5.1.6d4158dfpM1n6k",
    "https://www.daraz.com.bd/mother-baby/?page=7&spm=a2a0e.searchlistcategory.cate_5.1.6d4158dfpM1n6k",
    "https://www.daraz.com.bd/mother-baby/?page=8&spm=a2a0e.searchlistcategory.cate_5.1.6d4158dfpM1n6k",
    "https://www.daraz.com.bd/mother-baby/?page=9&spm=a2a0e.searchlistcategory.cate_5.1.6d4158dfpM1n6k",
    "https://www.daraz.com.bd/mother-baby/?page=10&spm=a2a0e.searchlistcategory.cate_5.1.6d4158dfpM1n6k",
    "https://www.daraz.com.bd/mother-baby/?page=11&spm=a2a0e.searchlistcategory.cate_5.1.6d4158dfpM1n6k",
    "https://www.daraz.com.bd/mother-baby/?page=12&spm=a2a0e.searchlistcategory.cate_5.1.6d4158dfpM1n6k"
]
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
for i in range(len(list_link)):
    driver.get(list_link[i])
    time.sleep(10)
    i=1
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
        driver.find_element_by_xpath('//*[@id="module_product_review"]/div/div[2]/div/div[1]').click()
        t = driver.find_element_by_class_name('next-menu-content')
        t.find_element_by_xpath("//li[contains(text(), '5 star')]").click()
        time.sleep(7)
        collect(driver,1)
        change_page(driver,1)
        driver.find_element_by_xpath('//*[@id="module_product_review"]/div/div[2]/div/div[1]').click()
        t = driver.find_element_by_class_name('next-menu-content')
        t.find_element_by_xpath("//li[contains(text(), '1 star')]").click()
        time.sleep(7)
        collect(driver,0)
        change_page(driver,0)
    except:
        None
df = pd.DataFrame({"text":comments,
                         "label":label})
df.drop_duplicates(subset ="text",
                     keep = False, inplace = True)
# drop all rows with any NaN and NaT values
df= df.dropna()
df.to_csv('data1.csv', encoding='utf-8')
