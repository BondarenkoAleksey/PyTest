import time
from random import randint
from selenium.webdriver.common.by import By

link = "https://software-testing.ru"

# Раздел "На главную"
def test_home_page(browser):
    browser.get(link)
    time.sleep(randint(0,3))
    section_name = "На главную"
    text_check = browser.find_element_by_xpath("//div[2]/div/ul/li[1]/a/span").text
    assert text_check == section_name, f'Название раздела "{text_check}"'
    link_check = browser.find_element(By.CSS_SELECTOR,"a[href='https://software-testing.ru/']").get_attribute("href")
    assert link_check == "https://software-testing.ru/", f'Ссылка на раздел "{section_name}" - {link_check}'

# Раздел "Новости"
def test_news(browser):
    #browser.get(link)
    #time.sleep(randint(0,3))
    section_name = "Новости"
    text_check = browser.find_element_by_xpath("//div[2]/div[1]/ul[1]/li[2]/a[1]/span[1]").text
    assert text_check == section_name, f'Название раздела "{text_check}"'
    link_check = browser.find_element(By.CSS_SELECTOR,"a[href='/news']").get_attribute("href")
    assert link_check == "https://software-testing.ru/news", f'Ссылка на раздел "{section_name}" - {link_check}'

# Раздел "Блоги о тестировании"
def test_blogs_about_testing(browser):
    # browser.get(link)
    # time.sleep(randint(0, 3))
    section_name = "Блоги о тестировании"
    text_check = browser.find_element_by_xpath("//div[2]/div/ul/li[3]/a/span").text
    assert text_check == section_name, f'Название раздела "{text_check}"'
    link_check = browser.find_element(By.CSS_SELECTOR, "a[href='/blogs']").get_attribute("href")
    assert link_check == "https://software-testing.ru/blogs", f'Ссылка на раздел "{section_name}" - {link_check}'

    # Раздел "События"
def test_events(browser):
    # browser.get(link)
    # time.sleep(randint(0, 3))
    section_name = "События"
    text_check = browser.find_element_by_xpath("//div[2]/div/ul/li[4]/a/span").text
    assert text_check == section_name, f'Название раздела "{text_check}"'
    link_check = browser.find_element(By.CSS_SELECTOR, "a[href='/events']").get_attribute("href")
    assert link_check == "https://software-testing.ru/events", f'Ссылка на раздел "{section_name}" - {link_check}'

# Раздел "Библиотека"
def test_library(browser):
    # browser.get(link)
    # time.sleep(randint(0, 3))
    section_name = "Библиотека"
    text_check = browser.find_element_by_xpath("//div[2]/div/ul/li[5]/a/span").text
    assert text_check == section_name, f'Название раздела "{text_check}"'
    link_check = browser.find_element(By.CSS_SELECTOR, "a[href='/library']").get_attribute("href")
    assert link_check == "https://software-testing.ru/library", f'Ссылка на раздел "{section_name}" - {link_check}'

# Раздел "Литература"
def test_books(browser):
    # browser.get(link)
    # time.sleep(randint(0, 3))
    section_name = "Литература"
    text_check = browser.find_element_by_xpath("//div[2]/div/ul/li[6]/a/span").text
    assert text_check == section_name, f'Название раздела "{text_check}"'
    link_check = browser.find_element(By.CSS_SELECTOR, "a[href='/books']").get_attribute("href")
    assert link_check == "https://software-testing.ru/books", f'Ссылка на раздел "{section_name}" - {link_check}'

# Раздел "Рассылка по тестированию"
def test_maillist(browser):
    # browser.get(link)
    # time.sleep(randint(0, 3))
    section_name = "Рассылка по тестированию"
    text_check = browser.find_element_by_xpath("//div[2]/div/ul/li[7]/a/span").text
    assert text_check == section_name, f'Название раздела "{text_check}"'
    link_check = browser.find_element(By.CSS_SELECTOR, "a[href='/maillist']").get_attribute("href")
    assert link_check == "https://software-testing.ru/maillist", f'Ссылка на раздел "{section_name}" - {link_check}'

# Раздел "О проекте"
def test_about(browser):
    # browser.get(link)
    # time.sleep(randint(0, 3))
    section_name = "О проекте"
    text_check = browser.find_element_by_xpath("//div[2]/div/ul/li[8]/a/span").text
    assert text_check == section_name, f'Название раздела "{text_check}"'
    link_check = browser.find_element(By.CSS_SELECTOR, "a[href='/about']").get_attribute("href")
    assert link_check == "https://software-testing.ru/about", f'Ссылка на раздел "{section_name}" - {link_check}'
