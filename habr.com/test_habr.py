import time

link = "https://habr.com/ru/all/"

def test_guest_should_see_become_autor_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#app > div > header > div > div > a")

def test_guest_should_see_arrow_down(browser):
    #browser.get(link)
    browser.find_element_by_css_selector('div.tm-dropdown.tm-header__projects > div')

def test_guest_should_see_all_publications_link(browser):
    #browser.get(link)
    browser.find_element_by_css_selector("a.tm-main-menu__item.router-link-exact-active.tm-main-menu__item_active")

def test_guest_should_see_development_link(browser):
    # browser.get(link)
    browser.find_element_by_css_selector("div > div > div > div > nav > a:nth-child(2)")

def test_guest_should_see_administration_link(browser):
    # browser.get(link)
    browser.find_element_by_css_selector("div > div > div > div > nav > a:nth-child(3)")

def test_guest_should_see_design_link(browser):
    # browser.get(link)
    browser.find_element_by_css_selector("div > div > div > div > nav > a:nth-child(4)")

def test_guest_should_see_management_link(browser):
    # browser.get(link)
    browser.find_element_by_css_selector("div > div > div > div > nav > a:nth-child(5)")

def test_guest_should_see_marketing_link(browser):
    # browser.get(link)
    browser.find_element_by_css_selector("div > div > div > div > nav > a:nth-child(6)")

def test_guest_should_see_nauchpop_link(browser):
    # browser.get(link)
    browser.find_element_by_css_selector("div > div > div > div > nav > a:nth-child(7)")

# Все потоки
def test_guest_should_see_articles_link(browser):
    # browser.get(link)
    browser.find_element_by_css_selector("#app > div > div.tm-layout > main > div > div > div > div.tm-page__main.tm-page__main_has-sidebar > div > div.tm-page__top > div.tm-tabs.tm-tabs_page-header > div > span:nth-child(1) > a")

def test_guest_should_see_news_link(browser):
    # browser.get(link)
    browser.find_element_by_css_selector("div.tm-tabs.tm-tabs_page-header > div > span:nth-child(2) > a")

def test_guest_should_see_hubs_link(browser):
    # browser.get(link)
    browser.find_element_by_css_selector("div.tm-tabs.tm-tabs_page-header > div > span:nth-child(3) > a")

def test_guest_should_see_authors_link(browser):
    # browser.get(link)
    browser.find_element_by_css_selector("div.tm-tabs.tm-tabs_page-header > div > span:nth-child(4) > a")

def test_guest_should_see_companies_link(browser):
    # browser.get(link)
    browser.find_element_by_css_selector("div.tm-tabs.tm-tabs_page-header > div > span:nth-child(5) > a")

def test_guest_should_see_setting_the_language_link(browser):
    # browser.get(link)
    browser.find_element_by_css_selector("#app > div > div.tm-footer > div > div > button")

def test_guest_should_see_about_link(browser):
    # browser.get(link)
    browser.find_element_by_css_selector("div.tm-footer > div > div > a:nth-child(5)")

def test_guest_should_see_technical_support_link(browser):
    # browser.get(link)
    browser.find_element_by_css_selector("div.tm-footer > div > div > a:nth-child(6)")

def test_guest_should_see_copyright_habr_link(browser):
    #browser.get(link)
    browser.find_element_by_css_selector("span.tm-copyright__name > a")

#время осмотреться
time.sleep(3)