from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/Users/Public/Documents/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/") #open site

#review

driver.execute_script("window.scrollBy(0, 600);")  #scroll
ruby_btn = driver.find_element_by_css_selector(".post-160 h3")
ruby_btn.click()           #open book
reviews_btn = driver.find_element_by_css_selector(".reviews_tab")
reviews_btn.click()   #open reviews
stars = driver.find_element_by_css_selector(".star-5")
stars.click()   # 5 star
otzyv = driver.find_element_by_id("comment")
otzyv.send_keys("Nice book!")   # enter review
name = driver.find_element_by_id("author")
name.send_keys("Anonim")   # enter name
email = driver.find_element_by_id("email")
email.send_keys("anonim@mail.ru")   # enter email
submit_btn = driver.find_element_by_css_selector(".form-submit .submit")
submit_btn.click()   #send review


time.sleep(3)
driver.quit()