from selenium.webdriver.support.color import Color
import time
import pytest

link = "https://www.eurekabpo.ru/ru/"
link1 = "https://www.eurekabpo.ru/ru/search/"

# проверка лупы
def test_is_search_present(browser):
    browser.get(link)
    icon = browser.find_element_by_css_selector("td.search-item.nosave > div")
    assert icon, "Element not found"

# проверка цвета кнопки поиска
def test_color_of_button(browser):
    #browser.get(link)
    button = browser.find_element_by_css_selector("form > div.search-button-div > button")
    rgb = button.value_of_css_property('background-color')
    hex = Color.from_string(rgb).hex
    assert "#107bb1" == hex, "Incorrect color of button"
