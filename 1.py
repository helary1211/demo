from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="e:\chromedriver.exe")
driver.get("http://www.baidu.com")
time.sleep(3)
driver.close()