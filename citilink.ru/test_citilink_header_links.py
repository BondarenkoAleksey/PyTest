link = "https://www.citilink.ru"

# Логотип
def test_guest_should_see_citilink_ru(browser):
    browser.get(link)
    citilink_ru = browser.find_element_by_css_selector("div.row-start-1.md-col1.col1.Main__max-width.MainHeader__logo-block.js--MainHeader__logo-block > div > div > a").get_attribute("href")
    assert "https://www.citilink.ru/" == citilink_ru, f"Некорректная ссылка - {citilink_ru}"
    # print(citilink_ru)

# +7(863)210-11-44 (г. Ростов-на-Дону)
def test_guest_should_see_tel_74957802002(browser):
    #browser.get(link)
    tel_78632101144 = browser.find_element_by_css_selector("div.row-start-1.md-col4.xs-col3.col2.md-col-start-2.Main__max-width.MainHeader__info-block > div.MainHeader__city-block > div.MainHeader__phone > a").get_attribute("href")
    assert "tel:+78632101144" == tel_78632101144, f"Некорректная ссылка - {tel_78632101144}"
    # print(tel_78632101144)

# Журнал
def test_guest_should_see_journal_citilink_ru(browser):
    #browser.get(link)
    journal_citilink_ru = browser.find_element_by_css_selector("div.MainHeader__menu-block.js--MainHeader__menu-block > div > div > div.MainMenu__link > a:nth-child(1)").get_attribute("href")
    assert "https://journal.citilink.ru/" == journal_citilink_ru, f"Некорректная ссылка - {journal_citilink_ru}"
    # print(journal_citilink_ru)

# Акции
def test_guest_should_see_citilink_ru_actions(browser):
    #browser.get(link)
    citilink_ru_actions = browser.find_element_by_css_selector("div.MainHeader__menu-block.js--MainHeader__menu-block > div > div > div.MainMenu__link > a:nth-child(2)").get_attribute("href")
    assert "https://www.citilink.ru/actions/" == citilink_ru_actions, f"Некорректная ссылка - {citilink_ru_actions}"
    # print(citilink_ru_actions)

# Ситилинк.Бизнес
def test_guest_should_see_citilink_ru_about_corporate(browser):
    #browser.get(link)
    citilink_ru_about_corporate = browser.find_element_by_css_selector("div.MainHeader__menu-block.js--MainHeader__menu-block > div > div > div.MainMenu__link > a:nth-child(3)").get_attribute("href")
    assert "https://www.citilink.ru/about/corporate/" == citilink_ru_about_corporate, f"Некорректная ссылка - {citilink_ru_about_corporate}"
    # print(citilink_ru_about_corporate)

# Доставка
def test_guest_should_see_citilink_ru_about_delivery(browser):
    #browser.get(link)
    citilink_ru_about_delivery = browser.find_element_by_css_selector("div.MainHeader__menu-block.js--MainHeader__menu-block > div > div > div.MainMenu__link > a:nth-child(4)").get_attribute("href")
    assert "https://www.citilink.ru/about/delivery/" == citilink_ru_about_delivery, f"Некорректная ссылка - {citilink_ru_about_delivery}"
    # print(citilink_ru_about_delivery)

# Магазины
def test_guest_should_see_citilink_ru_about_stores(browser):
    #browser.get(link)
    citilink_ru_about_stores = browser.find_element_by_css_selector("div.MainHeader__menu-block.js--MainHeader__menu-block > div > div > div.MainMenu__link > a:nth-child(5)").get_attribute("href")
    assert "https://www.citilink.ru/about/stores/" == citilink_ru_about_stores, f"Некорректная ссылка - {citilink_ru_about_stores}"
    # print(citilink_ru_about_stores)

# Обратная связь
def test_guest_should_see_citilink_ru_feedback_new(browser):
    #browser.get(link)
    citilink_ru_feedback_new = browser.find_element_by_css_selector("div.MainHeader__menu-block.js--MainHeader__menu-block > div > div > div.MainMenu__link > a:nth-child(6)").get_attribute("href")
    assert "https://www.citilink.ru/feedback-new" == citilink_ru_feedback_new, f"Некорректная ссылка - {citilink_ru_feedback_new}"
    # print(citilink_ru_feedback_new)

# Каталог товаров
def test_guest_should_see_citilink_ru_catalog(browser):
    #browser.get(link)
    citilink_ru_catalog = browser.find_element_by_css_selector("div.MainHeader__catalog-block.row-start-1.md-col1 > div.MainHeader__catalog > a").get_attribute("href")
    assert "https://www.citilink.ru/catalog/" == citilink_ru_catalog, f"Некорректная ссылка - {citilink_ru_catalog}"
    # print(citilink_ru_catalog)

# Избранное
def test_guest_should_see_citilink_ru_profile_wishlist(browser):
    #browser.get(link)
    citilink_ru_profile_wishlist = browser.find_element_by_css_selector("div.HeaderMenu__buttons-wrapper > div.HeaderMenu__buttons.HeaderMenu__buttons_wishlist > a").get_attribute("href")
    assert "https://www.citilink.ru/profile/wishlist/" == citilink_ru_profile_wishlist, f"Некорректная ссылка - {citilink_ru_profile_wishlist}"
    # print(citilink_ru_profile_wishlist)

# Сравнение
def test_guest_should_see_citilink_ru_compare(browser):
    #browser.get(link)
    citilink_ru_compare = browser.find_element_by_css_selector("div.HeaderMenu__buttons.HeaderMenu__buttons_compare > div > div > div.DropDown__trigger.js--MouseOverDropdown__trigger > span > a").get_attribute("href")
    assert "https://www.citilink.ru/compare/" == citilink_ru_compare, f"Некорректная ссылка - {citilink_ru_compare}"
    # print(citilink_ru_compare)

# Корзина
def test_guest_should_see_citilink_ru_order(browser):
    # browser.get(link)
    citilink_ru_order = browser.find_element_by_css_selector("div.HeaderMenu.js--HeaderMenuMobile > div.HeaderMenu__buttons-wrapper > div.HeaderMenu__buttons.HeaderMenu__buttons_basket > a").get_attribute("href")
    assert "https://www.citilink.ru/order/" == citilink_ru_order, f"Некорректная ссылка - {citilink_ru_order}"
    # print(citilink_ru_order)