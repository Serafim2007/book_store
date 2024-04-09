from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#driver = webdriver.chrome()


service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
# registration

driver.get("https://practice.automationtesting.in/") #open site
akk = driver.find_element_by_link_text("My Account")
akk.click()   # account click
email = driver.find_element_by_id("reg_email")
email.send_keys("anonim@mail.ru")   # enter email
pass_reg = driver.find_element_by_id("reg_password")
pass_reg.send_keys("D0$mvbrk@$$ybw@")   # enter pass
reg_btn = driver.find_element_by_name("register")
reg_btn.click()   # register

# login

driver.get("https://practice.automationtesting.in/") #open site
akk = driver.find_element_by_link_text("My Account")
akk.click()   # account click
email = driver.find_element_by_id("username")
email.send_keys("anonim@mail.ru")   # enter email
pass_enter = driver.find_element_by_id("password")
pass_enter.send_keys("D0$mvbrk@$$ybw@")   # enter pass
log_btn = driver.find_element_by_name("login")
log_btn.click()   # login
logout = driver.find_element_by_css_selector('.woocommerce-MyAccount-navigation :nth-child(6) a')
logout_if = logout.text
assert logout_if == 'Logout'  #check logout


time.sleep(3)
driver.quit()