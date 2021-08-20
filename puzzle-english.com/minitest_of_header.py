import time
from random import randint
from selenium.webdriver.common.by import By

link = "https://puzzle-english.com"

# Логотип и надпись в хедере
def test_logo(browser):
    browser.get(link)
    time.sleep(randint(0,3))
    section_name = "Puzzle English"
    text_check = browser.find_element(By.XPATH,"//img[@alt='Puzzle English']").get_attribute("alt")
    assert text_check == section_name, f'Название раздела "{text_check}"'
    link_check = browser.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/a").get_attribute("href")
    assert link_check == "https://puzzle-english.com/", f'Ссылка на раздел "{section_name}" - {link_check}'

# Кнопка "Вход"
def test_signin(browser):
    browser.get(link)
    time.sleep(randint(0,3))
    section_name = "Вход"
    text_check = browser.find_element(By.XPATH,"//a[contains(text(),'Вход')]").text
    assert text_check == section_name, f'Название раздела "{text_check}"'
    link_check = browser.find_element(By.XPATH,"//a[contains(text(),'Вход')]").get_attribute("href")
    assert link_check == "https://puzzle-english.com/signin", f'Ссылка на раздел "{section_name}" - {link_check}'

# Кнопка "Регистрация"
def test_signup(browser):
    browser.get(link)
    time.sleep(randint(0,3))
    section_name = "Регистрация"
    text_check = browser.find_element(By.XPATH,"//a[contains(text(),'Регистрация')]").text
    assert text_check == section_name, f'Название раздела "{text_check}"'
    link_check = browser.find_element(By.XPATH,"//a[contains(text(),'Регистрация')]").get_attribute("href")
    assert link_check == "https://puzzle-english.com/signin", f'Ссылка на раздел "{section_name}" - {link_check}'
