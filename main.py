from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException
import time
#LINK = "https://www.bestbuy.com/site/evga-geforce-rtx-3080-ftw3-ultra-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6436196.p?skuId=6436196"
LINK = "https://www.bestbuy.com/site/hp-spectre-x360-2-in-1-15-6-4k-uhd-touch-screen-laptop-intel-core-i7-16gb-memory-512gb-ssd-32gb-optane-nightfall-black/6428658.p?skuId=6428658"
#LINK = "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149"
ID = int(LINK.split("skuId=")[1])
FIRSTNAME = "Conner"
LASTNAME = "Replogle"
ADDRESS = "32827 Green Bend Ct"
CITY = 'MAGNOLIA'
EMAIL = "connerlreplogle@gmail.com"
PHONENUMBER = "8329042281"
CREDITCARD_NUMBER = "4342 5801 6596 7680"
EXPERATIONMONTH = "01"
EXPERATIONYEAR = '2022'
CSV = 871
print(ID)
chrome_options = Options()
#chrome_options.add_argument("--headless")
service = webdriver.chrome.service.Service(os.path.abspath("chromedriver"))
#service.start()
driver = webdriver.Chrome("chromedriver",options=chrome_options)
driver.get(LINK)
print("at link")
def find_element_by_xpath_Repeat(path):
    while True:
        try:
            buyButton = driver.find_element_by_xpath(path)
            return buyButton
        except NoSuchElementException as e:
            #print(e)
            pass
def click(element):
    while True:
        try:
            element.click()
            break
        except ElementClickInterceptedException as e:
            print(e)
            pass

def Buy():
    print("Buying")
    buyButton = find_element_by_xpath_Repeat(f"//button[@data-sku-id='{ID}']")
    click(buyButton)
    driver.get("https://www.bestbuy.com/checkout/r/fulfillment")
    time.sleep(2)
    try:
        change_shipping = driver.find_element_by_xpath("//a[@class='ispu-card__switch']")
        change_shipping.click()
    except Exception as e:
        print(e)
    Firstname = find_element_by_xpath_Repeat("//input[@id='consolidatedAddresses.ui_address_2.firstName']")
    Firstname.send_keys(FIRSTNAME)
    LastName = find_element_by_xpath_Repeat("//input[@id='consolidatedAddresses.ui_address_2.lastName']")
    LastName.send_keys(LASTNAME)
    address = find_element_by_xpath_Repeat("//input[@id='consolidatedAddresses.ui_address_2.street']")
    address.send_keys(ADDRESS[:-1])
    autocomplete = find_element_by_xpath_Repeat("//div[@id='street-a11y-autocomplete-list-item-0']")
    autocomplete.click()
    email = find_element_by_xpath_Repeat("//input[@id='user.emailAddress']")
    email.send_keys(EMAIL)
    phone = find_element_by_xpath_Repeat("//input[@id='user.phone']")
    phone.send_keys(PHONENUMBER)
    continueButton = find_element_by_xpath_Repeat("//div[@class='button--continue']//button[@class='btn btn-lg btn-block btn-secondary']")
    continueButton.click()
    creditCard = find_element_by_xpath_Repeat("//input[@id='optimized-cc-card-number']")
    creditCard.send_keys(CREDITCARD_NUMBER)
    driver.find_element_by_xpath(f"//select[@name='expiration-month']/option[text()='{EXPERATIONMONTH}']").click()
    driver.find_element_by_xpath(f"//select[@name='expiration-year']/option[text()='{EXPERATIONYEAR}']").click()
    csv = find_element_by_xpath_Repeat("//input[@id='credit-card-cvv']")
    csv.send_keys(CSV)
    PLACE_ORDER = driver.find_element_by_xpath("//button[@data-track='Place your Order - Contact Card']")
    PLACE_ORDER.click()

while True:
    stockStatus = driver.find_element_by_xpath(f"//button[@data-sku-id='{ID}']")
    if stockStatus.text != "Sold Out":
        Buy()
        break
    else:
        print("Sold Out")
        driver.refresh()
    time.sleep(1)