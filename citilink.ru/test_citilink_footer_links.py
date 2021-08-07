import time
from random import randint

link = "https://www.citilink.ru"

# Журнал
def test_guest_should_see_journal_citilink_ru(browser):
    browser.get(link)
    journal_citilink_ru = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.FooterMenu__menu > div:nth-child(1) > ul:nth-child(1) > li > a").get_attribute("href")
    assert "https://journal.citilink.ru/" == journal_citilink_ru, f"Некорректная ссылка - {journal_citilink_ru}"
    # print(journal_citilink_ru)

# Акции
def test_guest_should_see_citilink_ru_actions(browser):
    #browser.get(link)
    citilink_ru_actions = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.FooterMenu__menu > div:nth-child(1) > ul:nth-child(2) > li > a").get_attribute("href")
    assert "https://www.citilink.ru/actions/" == citilink_ru_actions, f"Некорректная ссылка - {citilink_ru_actions}"
    # print(citilink_ru_actions)

# Информация
def test_guest_should_see_citilink_ru_about(browser):
    # browser.get(link)
    citilink_ru_about = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.FooterMenu__menu > div:nth-child(1) > ul:nth-child(3) > li > ul > li:nth-child(1) > a").get_attribute("href")
    assert "https://www.citilink.ru/about/" == citilink_ru_about, f"Некорректная ссылка - {citilink_ru_about}"
    # print(citilink_ru_about)

# Доставка
def test_guest_should_see_citilink_ru_about_delivery(browser):
    # browser.get(link)
    citilink_ru_about_delivery = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.FooterMenu__menu > div:nth-child(1) > ul:nth-child(3) > li > ul > li:nth-child(2) > a").get_attribute("href")
    assert "https://www.citilink.ru/about/delivery/" == citilink_ru_about_delivery, f"Некорректная ссылка - {citilink_ru_about_delivery}"
    # print(citilink_ru_about_delivery)

# Гарантия
def test_guest_should_see_citilink_ru_about_warranty(browser):
    # browser.get(link)
    citilink_ru_about_warranty = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.FooterMenu__menu > div:nth-child(1) > ul:nth-child(3) > li > ul > li:nth-child(3) > a").get_attribute("href")
    assert "https://www.citilink.ru/about/warranty/" == citilink_ru_about_warranty, f"Некорректная ссылка - {citilink_ru_about_warranty}"
    # print(citilink_ru_about_warranty)

# Кредит и рассрочка
def test_guest_should_see_citilink_ru_about_credit(browser):
    # browser.get(link)
    citilink_ru_about_credit = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.FooterMenu__menu > div:nth-child(1) > ul:nth-child(3) > li > ul > li:nth-child(4) > a").get_attribute("href")
    assert "https://www.citilink.ru/about/credit/" == citilink_ru_about_credit, f"Некорректная ссылка - {citilink_ru_about_credit}"
    # print(citilink_ru_about_credit)

# Сервисные центры
def test_guest_should_see_citilink_ru_warranty_services(browser):
    # browser.get(link)
    citilink_ru_warranty_services = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.FooterMenu__menu > div:nth-child(2) > ul:nth-child(1) > li > a").get_attribute("href")
    assert "https://www.citilink.ru/warranty/services/" == citilink_ru_warranty_services, f"Некорректная ссылка - {citilink_ru_warranty_services}"
    # print(citilink_ru_warranty_services)

# Услуги
def test_guest_should_see_citilink_ru_services(browser):
    # browser.get(link)
    citilink_ru_services = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.FooterMenu__menu > div:nth-child(2) > ul:nth-child(2) > li > a").get_attribute("href")
    assert "https://www.citilink.ru/services/" == citilink_ru_services, f"Некорректная ссылка - {citilink_ru_services}"
    # print(citilink_ru_services)

# Корпоративным клиентам
def test_guest_should_see_citilink_ru_about_corporate(browser):
    # browser.get(link)
    citilink_ru_about_corporate = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.FooterMenu__menu > div:nth-child(2) > ul:nth-child(3) > li > a").get_attribute("href")
    assert "https://www.citilink.ru/about/corporate/" == citilink_ru_about_corporate, f"Некорректная ссылка - {citilink_ru_about_corporate}"
    # print(citilink_ru_about_corporate)

# Обзоры
def test_guest_should_see_citilink_ru_reviews(browser):
    # browser.get(link)
    citilink_ru_reviews = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.FooterMenu__menu > div:nth-child(2) > ul:nth-child(4) > li > a").get_attribute("href")
    assert "https://www.citilink.ru/reviews/" == citilink_ru_reviews, f"Некорректная ссылка - {citilink_ru_reviews}"
    # print(citilink_ru_reviews)

# Барахолка
def test_guest_should_see_citilink_ru_used(browser):
    # browser.get(link)
    citilink_ru_used = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.FooterMenu__menu > div:nth-child(2) > ul:nth-child(5) > li > a").get_attribute("href")
    assert "https://www.citilink.ru/used/" == citilink_ru_used, f"Некорректная ссылка - {citilink_ru_used}"
    # print(citilink_ru_used)

# Форум
def test_guest_should_see_forum_citilink_ru(browser):
    # browser.get(link)
    forum_citilink_ru = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.FooterMenu__menu > div:nth-child(2) > ul:nth-child(6) > li > a").get_attribute("href")
    assert "https://forum.citilink.ru/" == forum_citilink_ru, f"Некорректная ссылка - {forum_citilink_ru}"
    # print(forum_citilink_ru)

# Огонь
def test_guest_should_see_citilink_ru_promo_ogon(browser):
    # browser.get(link)
    citilink_ru_promo_ogon = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.FooterMenu__menu > div:nth-child(2) > ul:nth-child(7) > li > a").get_attribute("href")
    assert "https://www.citilink.ru/promo/ogon/" == citilink_ru_promo_ogon, f"Некорректная ссылка - {citilink_ru_promo_ogon}"
    # print(citilink_ru_promo_ogon)

# Конфигуратор
def test_guest_should_see_citilink_ru_configurator(browser):
    # browser.get(link)
    citilink_ru_configurator = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.FooterMenu__menu > div:nth-child(3) > ul:nth-child(1) > li > a").get_attribute("href")
    assert "https://www.citilink.ru/configurator/" == citilink_ru_configurator, f"Некорректная ссылка - {citilink_ru_configurator}"
    # print(citilink_ru_configurator)

# Подбор расходных материалов
def test_guest_should_see_citilink_ru_supplies(browser):
    # browser.get(link)
    citilink_ru_supplies = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.FooterMenu__menu > div:nth-child(3) > ul:nth-child(2) > li > a").get_attribute("href")
    assert "https://www.citilink.ru/supplies/" == citilink_ru_supplies, f"Некорректная ссылка - {citilink_ru_supplies}"
    # print(citilink_ru_supplies)
    time.sleep(randint(1, 4))

# Ситилинк
def test_guest_should_see_citilink_ru_about_citilink(browser):
    # browser.get(link)
    citilink_ru_about_citilink = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.FooterMenu__menu > div:nth-child(3) > ul:nth-child(3) > li > a").get_attribute("href")
    assert "https://www.citilink.ru/about/citilink/" == citilink_ru_about_citilink, f"Некорректная ссылка - {citilink_ru_about_citilink}"
    # print(citilink_ru_about_citilink)

# Новости
def test_guest_should_see_citilink_ru_news(browser):
    # browser.get(link)
    citilink_ru_news = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.FooterMenu__menu > div:nth-child(3) > ul:nth-child(4) > li > a").get_attribute("href")
    assert "https://www.citilink.ru/news/" == citilink_ru_news, f"Некорректная ссылка - {citilink_ru_news}"
    # print(citilink_ru_news)

# Клуб Ситилинк
def test_guest_should_see_citilink_ru_about_club(browser):
    # browser.get(link)
    citilink_ru_about_club = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.FooterMenu__menu > div:nth-child(3) > ul:nth-child(5) > li > a").get_attribute("href")
    assert "https://www.citilink.ru/about/club/" == citilink_ru_about_club, f"Некорректная ссылка - {citilink_ru_about_club}"
    # print(citilink_ru_about_club)

# Вакансии
def test_guest_should_see_job_citilink_ru(browser):
    # browser.get(link)
    job_citilink_ru = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.FooterMenu__menu > div:nth-child(3) > ul:nth-child(6) > li > a").get_attribute("href")
    assert "http://job.citilink.ru/" == job_citilink_ru, f"Некорректная ссылка - {job_citilink_ru}"
    # print(job_citilink_ru)

# Адреса магазинов
def test_guest_should_see_citilink_ru_about_stores(browser):
    # browser.get(link)
    citilink_ru_about_stores = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.Footer__contact > div.Footer__contacts-wrapper > a").get_attribute("href")
    assert "https://www.citilink.ru/about/stores/" == citilink_ru_about_stores, f"Некорректная ссылка - {citilink_ru_about_stores}"
    # print(citilink_ru_about_stores)

# tel:+74957802002
def test_guest_should_see_tel_74957802002(browser):
    # browser.get(link)
    tel_74957802002 = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.Footer__contact > div.Footer__contacts-wrapper > div > div.MainHeader__phone > a").get_attribute("href")
    assert "tel:+74957802002" == tel_74957802002, f"Некорректная ссылка - {tel_74957802002}"
    # print(tel_74957802002)

# facebook.com/citilink.ru
def test_guest_should_see_facebook_com_citilink_ru(browser):
    # browser.get(link)
    facebook_com_citilink_ru = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.Footer__contact > div.Footer__socials > div > a:nth-child(1)").get_attribute("href")
    assert "https://www.facebook.com/citilink.ru" == facebook_com_citilink_ru, f"Некорректная ссылка - {facebook_com_citilink_ru}"
    # print(facebook_com_citilink_ru)

# instagram.com/citilink_ru
def test_guest_should_see_instagram_com_citilink_ru(browser):
    # browser.get(link)
    instagram_com_citilink_ru = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.Footer__contact > div.Footer__socials > div > a:nth-child(2)").get_attribute("href")
    assert "https://www.instagram.com/citilink_ru/" == instagram_com_citilink_ru, f"Некорректная ссылка - {instagram_com_citilink_ru}"
    # print(instagram_com_citilink_ru)

# youtube.com/user/CitilinkTV
def test_guest_should_see_youtube_com_user_citilinktv(browser):
    # browser.get(link)
    youtube_com_user_citilinktv = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.Footer__contact > div.Footer__socials > div > a:nth-child(3)").get_attribute("href")
    assert "https://www.youtube.com/user/CitilinkTV" == youtube_com_user_citilinktv, f"Некорректная ссылка - {youtube_com_user_citilinktv}"
    # print(youtube_com_user_citilinktv)
    time.sleep(randint(1, 4))

# vk.com/citilink_ru
def test_guest_should_see_vk_com_citilink_ru(browser):
    # browser.get(link)
    vk_com_citilink_ru = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.Footer__contact > div.Footer__socials > div > a:nth-child(4)").get_attribute("href")
    assert "https://vk.com/citilink_ru" == vk_com_citilink_ru, f"Некорректная ссылка - {vk_com_citilink_ru}"
    # print(vk_com_citilink_ru)

# ok.ru/citilink.ru
def test_guest_should_see_ok_ru_citilink_ru(browser):
    # browser.get(link)
    ok_ru_citilink_ru = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.Footer__contact > div.Footer__socials > div > a:nth-child(5)").get_attribute("href")
    assert "https://ok.ru/citilink.ru" == ok_ru_citilink_ru, f"Некорректная ссылка - {ok_ru_citilink_ru}"
    # print(ok_ru_citilink_ru)

# tiktok.com/@citilink.ru
def test_guest_should_see_tiktok_com_at_citilink_ru(browser):
    # browser.get(link)
    tiktok_com_at_citilink_ru = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.Footer__contact > div.Footer__socials > div > a:nth-child(6)").get_attribute("href")
    assert "https://www.tiktok.com/@citilink.ru" == tiktok_com_at_citilink_ru, f"Некорректная ссылка - {tiktok_com_at_citilink_ru}"
    # print(tiktok_com_at_citilink_ru)

# zen.yandex.ru/citilink
def test_guest_should_see_zen_yandex_ru_citilink(browser):
    # browser.get(link)
    zen_yandex_ru_citilink = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.Footer__contact > div.Footer__socials > div > a:nth-child(7)").get_attribute("href")
    assert "https://zen.yandex.ru/citilink" == zen_yandex_ru_citilink, f"Некорректная ссылка - {zen_yandex_ru_citilink}"
    # print(zen_yandex_ru_citilink)

# t.me/citilink_official
def test_guest_should_see_t_me_citilink_official(browser):
    # browser.get(link)
    t_me_citilink_official = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.Footer__contact > div.Footer__socials > div > a:nth-child(8)").get_attribute("href")
    assert "https://t.me/citilink_official" == t_me_citilink_official, f"Некорректная ссылка - {t_me_citilink_official}"
    # print(t_me_citilink_official)

# Политика обработки персональных данных
def test_guest_should_citilink_ru_about_privacy_policy(browser):
    # browser.get(link)
    citilink_ru_about_privacy_policy = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__copyright > div.Footer__citilink > a").get_attribute("href")
    assert "https://www.citilink.ru/about/privacy-policy/" == citilink_ru_about_privacy_policy, f"Некорректная ссылка - {citilink_ru_about_privacy_policy}"
    # print(citilink_ru_about_privacy_policy)

# Ситилинк – зона безопасного сервиса
def test_guest_should_ecomvscovid_ru(browser):
    # browser.get(link)
    ecomvscovid_ru = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.Footer__contact > div:nth-child(5) > div > div > div > div > a:nth-child(1)").get_attribute("href")
    assert "https://ecomvscovid.ru/" == ecomvscovid_ru, f"Некорректная ссылка - {ecomvscovid_ru}"
    # print(ecomvscovid_ru)

# Безопасные способы оплаты
def test_guest_should_citilink_ru_promo_contactless(browser):
    # browser.get(link)
    citilink_ru_promo_contactless = browser.find_element_by_css_selector("footer > div > div > div > div.Footer__body > div.Footer__contact > div:nth-child(5) > div > div > div > div > a:nth-child(2)").get_attribute("href")
    assert "https://www.citilink.ru/promo/contactless/" == citilink_ru_promo_contactless, f"Некорректная ссылка - {citilink_ru_promo_contactless}"
    # print(citilink_ru_promo_contactless)
