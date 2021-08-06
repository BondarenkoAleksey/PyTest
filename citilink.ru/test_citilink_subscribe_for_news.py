import time
from random import randint

link = "https://www.citilink.ru"

def test_guest_add_incorrect_email_bla(browser):
    browser.get(link)
    input_email = browser.find_element_by_css_selector("div.Subscribe__input-block.Subscribe__input-block_email > div > label > input")
    input_email.clear()
    input_email.send_keys("bla")
    time.sleep(randint(1, 2))
    email_error = browser.find_element_by_css_selector("div.InputBox__error-block.Subscribe__input-errors-block > div").text
    assert "Укажите полный адрес электронной почты" != email_error, "Need use correct email"
    time.sleep(5)

def test_guest_add_incorrect_email_whitespace(browser):
    input_email = browser.find_element_by_css_selector("div.Subscribe__input-block.Subscribe__input-block_email > div > label > input")
    input_email.clear()
    input_email.send_keys(" ")
    time.sleep(randint(1, 3))
    email_error = browser.find_element_by_css_selector("div.InputBox__error-block.Subscribe__input-errors-block > div").text
    assert "Используйте английские буквы, цифры и символы" != email_error, "Need use correct email"
    time.sleep(5)

def test_guest_add_incorrect_email_atat(browser):
    input_email = browser.find_element_by_css_selector("div.Subscribe__input-block.Subscribe__input-block_email > div > label > input")
    input_email.clear()
    input_email.send_keys("@@")
    time.sleep(randint(1, 3))
    email_error = browser.find_element_by_css_selector("div.InputBox__error-block.Subscribe__input-errors-block > div").text
    assert "Укажите полный адрес электронной почты" != email_error, "Need use correct email"
    time.sleep(5)

def test_guest_add_incorrect_email_useryandex_dot_ru(browser):
    input_email = browser.find_element_by_css_selector("div.Subscribe__input-block.Subscribe__input-block_email > div > label > input")
    input_email.clear()
    input_email.send_keys("useryandex.ru")
    time.sleep(randint(1, 3))
    email_error = browser.find_element_by_css_selector("div.InputBox__error-block.Subscribe__input-errors-block > div").text
    assert "Укажите полный адрес электронной почты" != email_error, "Need use correct email"
    time.sleep(5)

def test_guest_add_incorrect_user_at_yandexru(browser):
    input_email = browser.find_element_by_css_selector("div.Subscribe__input-block.Subscribe__input-block_email > div > label > input")
    input_email.clear()
    input_email.send_keys("user@yandexru")
    time.sleep(randint(1, 3))
    email_error = browser.find_element_by_css_selector("div.InputBox__error-block.Subscribe__input-errors-block > div").text
    assert "Укажите полный адрес электронной почты" != email_error, "Need use correct email"
    time.sleep(5)

def test_guest_add_incorrect_user_at(browser):
    input_email = browser.find_element_by_css_selector("div.Subscribe__input-block.Subscribe__input-block_email > div > label > input")
    input_email.clear()
    input_email.send_keys("user@")
    time.sleep(randint(1, 3))
    email_error = browser.find_element_by_css_selector("div.InputBox__error-block.Subscribe__input-errors-block > div").text
    assert "Укажите почтовый домен" != email_error, "Need use correct email"
    time.sleep(5)

def test_guest_add_incorrect_email_adress(browser):
    browser.get(link)
    input_email = browser.find_element_by_css_selector("div.Subscribe__input-block.Subscribe__input-block_email > div > label > input")
    input_email.clear()
    input_email.send_keys("bf@!#F.fhj")
    time.sleep(randint(1, 3))
    browser.find_element_by_css_selector("div.InputBox__error-block.Subscribe__input-errors-block > div")
    assert "Недопустимый формат электронной почты" != email_error, "Need use correct email"
    time.sleep(5)

def test_guest_add_incorrect_user_at_yandex_dot_r_whitespace_u(browser):
    input_email = browser.find_element_by_css_selector("div.Subscribe__input-block.Subscribe__input-block_email > div > label > input")
    input_email.clear()
    input_email.send_keys("user@yandex.r u")
    time.sleep(randint(1, 3))
    email_error = browser.find_element_by_css_selector("div.InputBox__error-block.Subscribe__input-errors-block > div").text
    assert "Недопустимый пробел в адресе электронной почты" != email_error, "Need use correct email"
    time.sleep(5)

def test_guest_add_incorrect_email_user_at_yandexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx_dot_ru(browser):
    input_email = browser.find_element_by_css_selector("div.Subscribe__input-block.Subscribe__input-block_email > div > label > input")
    input_email.clear()
    input_email.send_keys("user@yandexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.ru")
    time.sleep(randint(1, 3))
    email_error = browser.find_element_by_css_selector("div.InputBox__error-block.Subscribe__input-errors-block > div").text
    assert "Превышение допустимой длины доменного имени" != email_error, "Need use correct email"
    time.sleep(5)