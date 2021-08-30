import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://leadfrog.ru/"

def test_take_demo_tour(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    demo_button = browser.find_element(By.XPATH, "//span[contains(text(),'Пройти демо-тур!')]")
    browser.execute_script("arguments[0].click();", demo_button)
    click_list = Select(browser.find_element(By.XPATH, '//*[@id="node32_meta"]/div/div[2]/select'))
    click_list.select_by_value("2")
    go_demo_button = browser.find_element(By.XPATH, "//button[@id='uid26']//span[@class='text'][contains(text(),'Пройти демо-тур')]")
    browser.execute_script("arguments[0].click();", go_demo_button)
    input_name = browser.find_element(By.XPATH, "//div[@id='node35_meta']//input[@type='text']")
    input_name.send_keys("Имя")
    input_phone = browser.find_element(By.XPATH, "//div[@id='node36_meta']//input[@type='text']")
    input_phone.send_keys("+79012345678")
    go_demo_button2 = browser.find_element(By.XPATH, "//button[@id='uid31']")
    browser.execute_script("arguments[0].click();", go_demo_button2)
