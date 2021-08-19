import time
from random import randint
from selenium.webdriver.common.by import By

link = "https://software-testing.ru"

# Вкладка "Портал"
def test_portal(browser):
    browser.get(link)
    time.sleep(randint(0,3))
    section_name = "Портал"
    text_check = browser.find_element(By.CSS_SELECTOR,"li>a>span.tpparenttitle").text
    assert text_check == section_name, f'Название раздела "{text_check}"'
    link_check = browser.find_element(By.CSS_SELECTOR,"#tp-cssmenu > li.tpmenuid1.tptopmenu > a").get_attribute("href")
    assert link_check == "http://software-testing.ru/", f'Ссылка на раздел "{section_name}" - {link_check}'

# Вкладка "Форум"
def test_forum(browser):
    # browser.get(link)
    # time.sleep(randint(0,3))
    section_name = "Форум"
    text_check = browser.find_element_by_xpath('//*[@id="tp-cssmenu"]/li[2]/a/span').text
    assert text_check == section_name, f'Название раздела "{text_check}"'
    link_check = browser.find_element(By.CSS_SELECTOR,"#tp-cssmenu > li.tpmenuid2.tptopmenu > a").get_attribute("href")
    assert link_check == "https://www.software-testing.ru/forum/", f'Ссылка на раздел "{section_name}" - {link_check}'

# Вкладка "Тренинги"
def test_edu(browser):
    # browser.get(link)
    # time.sleep(randint(0,3))
    section_name = "Тренинги"
    text_check = browser.find_element_by_xpath("//span[contains(text(),'Тренинги')]").text
    assert text_check == section_name, f'Название раздела "{text_check}"'
    link_check = browser.find_element(By.CSS_SELECTOR,"#tp-cssmenu > li.tpmenuid3.tptopmenu > a").get_attribute("href")
    assert link_check == "https://www.software-testing.ru/edu/", f'Ссылка на раздел "{section_name}" - {link_check}'
