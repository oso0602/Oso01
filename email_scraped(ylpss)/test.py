from selenium import webdriver as web
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = web.Chrome('/path/to/chromedriver')
driver.get("https://foodmarketmaker.com/main/mmsearch")
iframe = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(iframe)

wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//section[@id="search-right"]//input[@placeholder="start typing to search"]'))).click()
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//li[.="Bass"]'))).click()

links = wait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//section[@id="search-results"]//a[.//*[name()="svg"]]')))

for link in links:
    print(link.get_attribute('href'))