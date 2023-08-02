from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path='C:/Users/Public/Documents/chromedriver.exe')
driver.maximize_window()
Wait = WebDriverWait(driver, 10)
#login

driver.get("https://practice.automationtesting.in/") #open site
# akk = driver.find_element_by_link_text("My Account")
# akk.click()   # account click
# email = driver.find_element_by_id("username")
# email.send_keys("anonim@mail.ru")   # enter email
# pass_enter = driver.find_element_by_id("password")
# pass_enter.send_keys("D0$mvbrk@$$ybw@")   # enter pass
# reg_btn = driver.find_element_by_name("login")
# reg_btn.click()   # login

#open book

shop = driver.find_element_by_link_text("Shop")
shop.click()   # shop click
# html5 = driver.find_element_by_css_selector(".post-181 h3")
# html5.click()   # book click
# header = driver.find_element_by_css_selector('.post-181 h1')
# book_name = header.text
# assert book_name == 'HTML5 Forms'  #check header

# #html
#
# html = driver.find_element_by_link_text("HTML")
# html.click()   # html click
# count_book = driver.find_elements_by_css_selector('.products .product')
# count = len(count_book)
# assert count == 3  #check count

##sorting

# def_sel = driver.find_element_by_css_selector("[value=menu_order]")
# def_chk = def_sel.get_attribute('selected')
# assert def_chk == 'true'         #default check
# sort = driver.find_element_by_css_selector('[class=orderby]')
# select_sort = Select(sort)
# select_sort.select_by_index(5)      #sort up to down
# sort = driver.find_element_by_css_selector('[class=orderby]')   #selector
# def_sel_2 = driver.find_element_by_css_selector("[value=price-desc]")
# def_chk_2 = def_sel_2.get_attribute('selected')
# assert def_chk_2 == 'true'         #up to down check

##skidka

# android= driver.find_element_by_css_selector(".post-169 h3")
# android.click()   # book click
# old_price = driver.find_element_by_css_selector('.price del')
# new_price = driver.find_element_by_css_selector('.price ins')   #find price
# assert old_price.text == '₹600.00'
# assert new_price.text == '₹450.00'    #chk price
# book_wait = Wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.images a'))) #wait book
# book_android = driver.find_element_by_css_selector('.images a')
# book_android.click()              #oblojka
# close_wait = Wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class=pp_close]'))) #wait close
# book_close = driver.find_element_by_css_selector('[class=pp_close]')
# book_close.click()              #close book

##price

# add_cart = driver.find_element_by_css_selector('[data-product_id="182"]')
# add_cart.click()   # add book
# time.sleep(2)
# item_book = driver.find_element_by_css_selector('span.cartcontents')
# prise_book = driver.find_element_by_css_selector('span.amount')
# assert item_book.text == '1 Item'
# assert prise_book.text == '₹180.00'    #chk basket
# basket = driver.find_element_by_id('wpmenucartli')
# basket.click()              #open basket
# #chk total
# price_subtotal = Wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.cart-subtotal span.amount'),'₹180.00'))
# price_total = Wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.order-total span.amount'),'₹183.60'))

##basket

# driver.execute_script("window.scrollBy(0, 300);")
# add_cart = driver.find_element_by_css_selector('[data-product_id="182"]')
# add_cart.click()   # add html5
# time.sleep(3)
# add_cart = driver.find_element_by_css_selector('[data-product_id="180"]')
# add_cart.click()   # add js
# time.sleep(2)
# basket = driver.find_element_by_id('wpmenucartli')
# basket.click()              #open basket
# time.sleep(3)
# remove_book = driver.find_element_by_css_selector('.cart_item:nth-child(1) .remove')
# remove_book.click()   # remove first
# time.sleep(3)
# undo_remove = driver.find_element_by_link_text('Undo?')
# undo_remove.click()   # undo remove
# field = driver.find_element_by_css_selector('.cart_item:nth-child(1) .text')
# field.clear()
# field.send_keys('3')  # 3 book add
# upd_bask = driver.find_element_by_name('update_cart')
# upd_bask.click()      #upd basket
# time.sleep(3)
# count_book = driver.find_element_by_css_selector('.cart_item:nth-child(1) .text')
# assert count_book.get_attribute('value') == '3'    #chk count
# appl_coupon = driver.find_element_by_name('apply_coupon')
# appl_coupon.click()      #apply coupon
# time.sleep(2)
# coup_err = driver.find_element_by_css_selector('.woocommerce-error li')
# assert coup_err.text == 'Please enter a coupon code.'

##bying

driver.execute_script("window.scrollBy(0, 300);")   #scroll
add_cart = driver.find_element_by_css_selector('[data-product_id="182"]')
add_cart.click()   # add html5
time.sleep(3)
basket = driver.find_element_by_id('wpmenucartli')
basket.click()    #open basket
proceed_wait = Wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.wc-proceed-to-checkout a')))  # wait proceed
proceed = driver.find_element_by_link_text('PROCEED TO CHECKOUT')
proceed.click()   #	Proceed to Checkout click
# enter fields
fields_wait = Wait.until(EC.element_to_be_clickable((By.ID, 'billing_first_name')))  # wait fields
f_name = driver.find_element_by_id('billing_first_name')
f_name.send_keys('Stive')
l_name = driver.find_element_by_id('billing_last_name')
l_name.send_keys('Bushemi')
mail = driver.find_element_by_id('billing_email')
mail.send_keys('anonim@mail.ru')
phone = driver.find_element_by_id('billing_phone')
phone.send_keys('9876543210')
address = driver.find_element_by_id('billing_address_1')
address.send_keys('Los-Angeles')
country = driver.find_element_by_css_selector('.country_select .select2-arrow')
country.click()
country_enter = driver.find_element_by_id('s2id_autogen1_search')
country_enter.send_keys('United States')
country_click = driver.find_element_by_css_selector(':nth-child(1).select2-match')
country_click.click()
city = driver.find_element_by_id('billing_city')
city.send_keys('HollyWood')
state = driver.find_element_by_css_selector('.state_select .select2-arrow')
state.click()
state_enter = driver.find_element_by_id('s2id_autogen2_search')
state_enter.send_keys('California')
state_click = driver.find_element_by_css_selector(':nth-child(1).select2-match')
state_click.click()
state_enter = driver.find_element_by_id('billing_postcode')
state_enter.send_keys('90027')

driver.execute_script("window.scrollBy(0, 600);")   #scroll
time.sleep(2)
payment = driver.find_element_by_id('payment_method_cheque')
payment.click()     # Check payment
order = driver.find_element_by_id('place_order')
order.click()     # Plase order
thanks_need = 'Thank you. Your order has been received.'
thanks = Wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.woocommerce p:nth-child(1)'),thanks_need))
payment_method = Wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.method strong'),'Check Payments'))
time.sleep(3)
driver.quit()