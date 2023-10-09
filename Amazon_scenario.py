import time
import re

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys

options = webdriver.ChromeOptions()
options.add_argument("--disable-cache")
driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://www.amazon.com")

SEARCH_FIELD = ('xpath', "//input[@id='twotabsearchtextbox']")
FIND_BUTTON = ('xpath', "//input[@id= 'nav-search-submit-button']")
SEARCH_RESULTS_SECTION = ('xpath', "//div[@class = 'a-section a-spacing-base']")
QUANTITY_DROPDOWN = ('xpath', "//select[@id = 'quantity']")
ADD_TO_CART = ('xpath', "//input[@id='add-to-cart-button']")
CART_BUTTON = ('xpath', "//a[@id = 'nav-cart']")
ELEMENT_PRICE = ('xpath', "//p[@class = 'a-spacing-mini']")
TOTAL_PRICE = ('xpath', "//span[@id = 'sc-subtotal-amount-activecart']")
TOTAL_QUANTITY = ('xpath', "//span[@id = 'sc-subtotal-label-activecart']")
QUANTITY_DROPDOWN_ON_CART = ('xpath', "(//select[@id = 'quantity'])[2]")

def find_hat_for_men():
    search_field = driver.find_element(*SEARCH_FIELD)
    search_field.send_keys("hats for men")
    find_button = driver.find_element(*FIND_BUTTON)
    find_button.click()
    search_results_section = driver.find_elements(*SEARCH_RESULTS_SECTION)
    search_results_section[0].click()
    quantity_dropdown = Select(driver.find_element(*QUANTITY_DROPDOWN))
    quantity_dropdown.select_by_value("2")
    add_to_cart = driver.find_element(*ADD_TO_CART)
    add_to_cart.click()
    cart_button = driver.find_element(*CART_BUTTON)
    cart_button.click()

def find_hat_for_women():
    search_field = driver.find_element(*SEARCH_FIELD)
    search_field.send_keys("hats for women")
    find_button = driver.find_element(*FIND_BUTTON)
    find_button.click()
    search_results_section = driver.find_elements(*SEARCH_RESULTS_SECTION)
    search_results_section[0].click()
    add_to_cart = driver.find_element(*ADD_TO_CART)
    add_to_cart.click()
    cart_button = driver.find_element(*CART_BUTTON)
    cart_button.click()

def assert_correct_price_and_quantity():
    element_price = driver.find_elements(*ELEMENT_PRICE)
    total_price = driver.find_element(*TOTAL_PRICE)
    total_quantity = driver.find_element(*TOTAL_QUANTITY)
    assert total_quantity.text == "Subtotal (3 items):"
    assert total_price.text == " $57.97"

def change_quantity():
    quantity_dropdown = Select(driver.find_element(*QUANTITY_DROPDOWN_ON_CART))
    total_price = driver.find_element(*TOTAL_PRICE)
    total_quantity = driver.find_element(*TOTAL_QUANTITY)
    quantity_dropdown.select_by_index(1)
    assert total_quantity.text == "Subtotal (2 items):"
    assert total_price.text == " $37.98"

find_hat_for_men()
find_hat_for_women()
assert_correct_price_and_quantity()
change_quantity()