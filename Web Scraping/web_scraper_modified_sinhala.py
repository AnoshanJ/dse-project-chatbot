import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

url = 'https://demo.boc.lk/personal-banking/savings-accounts'

r = requests.get(url,headers=headers)

# print(r.status_code)

soup = BeautifulSoup(r.text,'html.parser')

cards = soup.find_all('div',{'class':'product unique'})
titles=[]
links = []
# print(soup.text)
for item in cards:
    title = item.find('h4')
    print(title.text)
    titles.append(title.text)
    link = item.find('a',{'class':'cta flex-button black'})['href']
    print(link)
    links.append(link)
    print()

def get_product_data(url,title):
    driver = webdriver.Chrome()
    driver.get(url)
    print('obtained url')
    #Bypass alert window
    try:
        driver.find_elements(By.CLASS_NAME,'lity-close')[0].click()
    except:
        print("NO Initial Closing alerts")
        pass

    try:
        driver.find_elements(By.CLASS_NAME,'language-switcher')[0].click()
    except:
        print('Language Seems Fine')
        pass

    r_product = requests.get(url,headers=headers)
    product_soup = BeautifulSoup(r_product.text,'html.parser')
    #get main description
    main_desc = product_soup.find('div',{'class':'main-description'}).get_text(separator="\n", strip=True)


    #get expandables
    data = product_soup.find_all('div',{'class':'expand-block'})
    cleaned = {}
    cleaned['TITLE : ']=title.upper()
    cleaned['MAIN DESCRIPTION']=main_desc
    for i in data:
        # soup = BeautifulSoup(i, 'html.parser')
        a_tag = i.find('a', class_='expand-link')
        # if a_tag:
        a_id = a_tag.get('id')

        editor_content = i.find('div', class_='editor-content')
        # if editor_content:
        content = editor_content.get_text(separator="\n", strip=True)
        # print(f"\nContent within editor-content:{a_id}")
        # print(content)   

        # print(main_desc)
        cleaned[a_id.upper()] = content
    return cleaned

collected = []
for i in range(len(links)):
    collected.append(get_product_data(links[i],titles[i]))


with open(f'BOC_Savings_Data_Sinhala.txt','w',encoding="utf-8") as file: 
    for x in range(len(links)):
        for k in collected[x]:
            file.write(k+'\n')
            file.write(collected[x][k]+'\n')
            file.write('\n')

