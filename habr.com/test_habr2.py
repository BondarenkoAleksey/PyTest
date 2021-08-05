import time
from random import randint

link = "https://habr.com/ru/all/page"

# проверка страниц с 1 по 50
# number = 1
# def test_guest_should_see_1_50_pages(browser):
#     for number in range (1,51):
#         browser.get(link + str(number))
#         time.sleep(randint(1,3))

#проверка -1 страницы
def test_guest_should_see_minus1_page(browser):
    browser.get(link + str(-1))
    time.sleep(randint(1,3))
    page404 = browser.find_element_by_tag_name("h1").text
    assert "Страница не найдена" != page404, "Page not found"

#проверка 0 страницы
def test_guest_should_see_0_page(browser):
    browser.get(link + str(0))
    time.sleep(randint(1, 3))
    page404 = browser.find_element_by_tag_name("h1").text
    assert "Страница не найдена" != page404, "Page not found"

#проверка 1 страницы
def test_guest_should_see_1_page(browser):
    browser.get(link + str(1))
    time.sleep(randint(1, 3))
    page404 = browser.find_element_by_tag_name("h1").text
    assert "Страница не найдена" != page404, "Page not found"

#проверка 25 страницы
def test_guest_should_see_25_page(browser):
    browser.get(link + str(25))
    time.sleep(randint(1, 3))
    page404 = browser.find_element_by_tag_name("h1").text
    assert "Страница не найдена" != page404, "Page not found"

#проверка 49 страницы
def test_guest_should_see_49_page(browser):
    browser.get(link + str(49))
    time.sleep(randint(1, 3))
    page404 = browser.find_element_by_tag_name("h1").text
    assert "Страница не найдена" != page404, "Page not found"

#проверка 50 страницы
def test_guest_should_see_50_page(browser):
    browser.get(link + str(50))
    time.sleep(randint(1, 3))
    page404 = browser.find_element_by_tag_name("h1").text
    assert "Страница не найдена" != page404, "Page not found"

#проверка 51 страницы
def test_guest_should_see_51_page(browser):
    browser.get(link + str(51))
    time.sleep(randint(1, 3))
    page4041 = browser.find_element_by_css_selector("div.tm-articles-subpage > div > div > div > span").text
    assert "К сожалению, здесь пока нет ни одной публикации" != page4041, "Page not found"
