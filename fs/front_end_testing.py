# Privacy is central FS's business model
# CC #'s, social security numbers, etc


# Navigate to fruitshop, goto checkout, fill out the cc # field. 
# Validate this flow works
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


base_url = 'https://fruitshoppe.firebaseapp.com/'
market_class_locator = 'cta-go-market'
dragonfruit_css_locator = '.fruit-dragonfruit .cta-add-to-cart'
checkout_class_locator = 'cta-go-checkout'
cc_num_input_id_locator = 'credit_card_number'
purchase_btn_class_locator = 'cta-checkout'

cart_class_locator = 'cart'

driver = webdriver.Firefox()
driver.get(base_url)
# goto market page
driver.find_element_by_class_name(market_class_locator).click()
# todo assert market page

# add item to cart
time.sleep(3)
driver.find_element_by_css_selector(dragonfruit_css_locator).click()

# goto cart
driver.find_element_by_class_name(cart_class_locator).click()
time.sleep(3)

# goto checkout
driver.find_element_by_class_name(checkout_class_locator).click()

# type fake cc num and hit purchase
time.sleep(3)
driver.find_element_by_id(cc_num_input_id_locator).send_keys('sa tuna 37')
driver.find_element_by_class_name(purchase_btn_class_locator).click()


time.sleep(5)
driver.close()