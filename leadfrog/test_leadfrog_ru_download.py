import time

from selenium.webdriver.common.by import By

link = "https://leadfrog.ru/"

def test_download_iphone(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    download_button = browser.find_element(By.XPATH, "//a[@id='uid8']//span[@class='text'][contains(text(),'Скачать')]")
    browser.execute_script("arguments[0].click();", download_button)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    app_store = browser.find_element(By.XPATH, "//a[@id='uid6']//img")
    browser.execute_script("arguments[0].click();", app_store)
    # time.sleep(5)

def test_download_android(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    download_button = browser.find_element(By.XPATH, "//a[@id='uid8']//span[@class='text'][contains(text(),'Скачать')]")
    browser.execute_script("arguments[0].click();", download_button)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    google_store = browser.find_element(By.XPATH, "//a[@id='uid7']//img")
    browser.execute_script("arguments[0].click();", google_store)
    # time.sleep(5)

def test_download_not_google_play(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    download_button = browser.find_element(By.XPATH, "//a[@id='uid8']//span[@class='text'][contains(text(),'Скачать')]")
    browser.execute_script("arguments[0].click();", download_button)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    google_store = browser.find_element(By.XPATH, "//a[contains(text(),'ссылке')]")
    browser.execute_script("arguments[0].click();", google_store)
    # time.sleep(5)