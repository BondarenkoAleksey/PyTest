# цель - купить ноутбук-трансформер HP до 120000 руб. Диагональ 15,6". Самовывоз из Донецка.
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

link = "https://www.citilink.ru/catalog/noutbuki/"
TOWN = "Донецк"

def test_click_checkbox_hp(browser):
    browser.get(link)
    element = browser.find_element(By.XPATH, "//span[contains(text(),'HP')]")
    browser.execute_script("arguments[0].click();", element)
    time.sleep(5)
def test_change_price_not_higher_than_120000(browser):
    browser.implicitly_wait(5)
    # browser.get("https://www.citilink.ru/catalog/noutbuki/?f=discount.any%2Crating.any%2Chp&pf=discount.any%2Crating.any")
    element = browser.find_element(By.XPATH, "//div[@class='e9u9wc60 css-1tn5u6r eivtqr80']//input[@name='input-max']")
    element.clear()
    element.send_keys("120000")
    element.send_keys(Keys.ENTER)

def test_click_checkbox_diagonal_15_6(browser):
    # browser.get("https://www.citilink.ru/catalog/noutbuki/?f=discount.any%2Crating.any%2Chp&pf=discount.any%2Crating.any%2Chp&price_max=120000")
    element = browser.find_element(By.XPATH, "//input[@id='10659_315b76d1a3']")
    browser.execute_script("arguments[0].click();", element)

def test_click_checkbox_transformer(browser):
    # browser.get("https://www.citilink.ru/catalog/noutbuki/?f=discount.any%2Crating.any%2Chp%2C10659_315b76d1a3&pf=discount.any%2Crating.any%2Chp&price_max=120000&pprice_max=120000")
    element = browser.find_element(By.XPATH, "//input[@id='6536_3']")
    browser.execute_script("arguments[0].click();", element)

def test_click_selection_by_price(browser):
    # browser.get("https://www.citilink.ru/catalog/noutbuki/?f=discount.any%2Crating.any%2Chp%2C6536_3%2C10659_315b76d1a3&pf=discount.any%2Crating.any%2Chp%2C10659_315b76d1a3&price_max=120000&pprice_max=120000")
    browser.find_element(By.XPATH, "//div[contains(text(),'по цене')]").click()

def test_choosing_delivery_city(browser):
    # browser.get("https://www.citilink.ru/catalog/noutbuki/?f=discount.any%2Crating.any%2Chp%2C6536_3%2C10659_315b76d1a3&pf=discount.any%2Crating.any%2Chp%2C10659_315b76d1a3&price_max=120000&pprice_max=120000&sorting=price_asc")
    browser.implicitly_wait(5)
    browser.find_element(By.XPATH, "//div[1]/div[4]/button").click()
    browser.find_element(By.XPATH, "//input[@placeholder='Введите название города']").send_keys("Донецк")
    browser.find_element(By.XPATH, "//div[contains(@class,'InputSearch js--CitiesSearch__input InputBox_full-width InputBox_has-label')]//button[contains(@type,'submit')]//*[local-name()='svg']").click()
    browser.find_element(By.XPATH, "//span[contains(@class,'CitiesSearch__highlight')][contains(text(),'Донецк')]").click()

def test_select_laptop_from_list(browser):
    # browser.get("https://www.citilink.ru/catalog/noutbuki/?f=discount.any%2Crating.any%2Chp%2C6536_3%2C10659_315b76d1a3&pf=discount.any%2Crating.any%2Chp%2C10659_315b76d1a3&price_max=120000&pprice_max=120000&sorting=price_asc")
    browser.implicitly_wait(5)
    element = browser.find_element(By.XPATH, "//section/div[12]/div[3]/a")
    browser.execute_script("arguments[0].click();", element)

def test_scroll_to_characteristics(browser):
    # browser.get("https://www.citilink.ru/product/noutbuk-hp-envy-x360-15-ed1015ur-15-6-ips-intel-core-i7-1165g7-16gb-51-1443932/")
    element = browser.find_element(By.XPATH, "// a[contains(text(), 'Характеристики')]")
    browser.execute_script("arguments[0].scrollIntoView()", element)
    # browser.execute_script("window.scrollTo(0, 850)")


def test_click_to_all_characteristics_and_scroll(browser):
    browser.implicitly_wait(5)
    # browser.get("https://www.citilink.ru/product/noutbuk-hp-envy-x360-15-ed1015ur-15-6-ips-intel-core-i7-1165g7-16gb-51-1443932/")
    element = browser.find_element(By.XPATH, "// a[contains(text(), 'Характеристики')]")
    browser.execute_script("arguments[0].scrollIntoView()", element)
    element1 = browser.find_element(By.XPATH, '//*[@id="content"]/div[3]/div[1]/div[1]/div/div[2]/div[1]/a')
    browser.execute_script("arguments[0].click();", element1)
    time.sleep(3)
    browser.execute_script("window.scrollTo(0, -850)")

def test_click_to_add_to_cart_and_order_registration(browser):
    browser.implicitly_wait(5)
    # browser.get("https://www.citilink.ru/product/noutbuk-hp-envy-x360-15-ed1015ur-15-6-ips-intel-core-i7-1165g7-16gb-51-1443932/")
    # browser.find_element(By.XPATH, "//div[1]/div[4]/button").click()
    # browser.find_element(By.XPATH, "//input[@placeholder='Введите название города']").send_keys("Донецк")
    # browser.find_element(By.XPATH, "//div[contains(@class,'InputSearch js--CitiesSearch__input InputBox_full-width InputBox_has-label')]//button[contains(@type,'submit')]//*[local-name()='svg']").click()
    # browser.find_element(By.XPATH, "//span[contains(@class,'CitiesSearch__highlight')][contains(text(),'Донецк')]").click()
    element = browser.find_element(By.XPATH, "//span[contains(text(),'В корзину')]")
    browser.execute_script("arguments[0].click();", element)
    browser.find_element(By.XPATH, "//div[contains(@class,'UpsaleBasket__header-link')]//span[contains(@class,'Button__text jsButton__text')][contains(text(),'Перейти в корзину')]").click()
    browser.find_element(By.XPATH, "//span[contains(text(),'Перейти к оформлению')]").click()
    browser.find_element(By.XPATH, "//input[@placeholder='Введите ваше имя']").send_keys("Ivan")
    browser.find_element(By.XPATH, "//input[@placeholder='Введите вашу фамилию']").send_keys("Ivanov")
    browser.find_element(By.XPATH, "//input[@name='phone']").send_keys("+79876543210")
    browser.find_element(By.XPATH, "//input[@name='additionalPhone']").send_keys("+79012345678")
    is_button_of_pickup_active = browser.find_element(By.XPATH, '//*[@id="app-check-out"]/div/div/div/div[1]/div[3]/div/div/div[2]/div/div[1]/div/div/div/div/div/div[1]/button[1]')
    # print(is_button_of_pickup_active.get_attribute("class"))
    if "BinTab_active" not in is_button_of_pickup_active.get_attribute("class"):
        is_button_of_pickup_active.click()
    browser.find_element(By.XPATH, "//textarea[@id='comment']").send_keys("Оплачу на месте картой 'Халва'")
    is_button_in_cash_or_by_card_upon_receipt_active = browser.find_element(By.XPATH, '//*[@id="app-check-out"]/div/div/div/div[1]/div[4]/div/div[2]/div/div/div[1]/div/div[2]/div/label[1]/span[1]')
    # print(is_button_in_cash_or_by_card_upon_receipt_active.get_attribute("class"))
    if "InputBox_checked" not in is_button_in_cash_or_by_card_upon_receipt_active.get_attribute("class"):
        is_button_in_cash_or_by_card_upon_receipt_active.click()

    element = browser.find_element(By.XPATH, "//span[contains(text(),'Оформить заказ')]")
    browser.execute_script("arguments[0].scrollIntoView()", element)
    time.sleep(15) # осмотреться
    browser.find_element(By.XPATH, "//span[contains(text(),'Оформить заказ')]").click()


