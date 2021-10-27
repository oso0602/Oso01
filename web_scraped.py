import selenium.webdriver.support.select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import  Select
import time
import imaplib
import email
import os
import pandas as pd
browser = webdriver.Chrome('C:\\Users\\oso\\PycharmProjects\\WEB\\chromedriver.exe')
browser.get("https://eclass.ylpss.edu.hk/templates/")
browser.find_element(By.ID,"UserLogin").send_keys("yl_e*425")
browser.find_element(By.ID, "UserPassword").send_keys("yl*0060206")
browser.find_element(By.ID, "login_btn").click()
browser.find_element(By.CLASS_NAME,"indexquickbtn-item").click()
mail=[]
i=1
while True:
    email_body=browser.find_element(By.ID,"html_body_frame")
    for row in email_body.find_elements(By.CSS_SELECTOR,"table table tbody>tr:not(.tabletop)")[6:-2]:
        title=row.find_element(By.CSS_SELECTOR, ".iMailsubject,.iMailsubjectunread").text
        print(title)
        date=row.find_element(By.CSS_SELECTOR,'[nowrap="nowrap"]').text
        print(date)
        mail.append([title, date])
    #while True:
        # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(2)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    page=Select(browser.find_element(By.CSS_SELECTOR,".formtextbox"))
    i+=1
    if f"{i}" in [elem.text for elem in page.options]:
        page.select_by_value(f"{i}")
    else:
        break

email_list=mail
df = pd.DataFrame (email_list, columns = ['email','date'])
df.to_csv("email.csv",index=False)
print(df)











