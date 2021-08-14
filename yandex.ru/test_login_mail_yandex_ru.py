import time
from random import randint
from selenium.webdriver.common.by import By
import requests

link = "https://passport.yandex.ru/auth"
link1 = "https://www.google.com/search?q=купить+кофемашину+bork+c804"

# тест входа в почту Яндекс
def test_login_to_mail_yandex_ru(browser):
    browser.get(link) # перейти на страницу логина
    time.sleep(randint(0,3)) # ждать. Можно закомментировать строку. Использовалось для разнообразия времени ожидания (для алгоритмов Яндекса, хотя этого очень мало)
    browser.find_element_by_xpath("//input[@id='passp-field-login']").send_keys("ivashka.ivanofff") # ввести в поле логина свои данные
    time.sleep(randint(0,3)) # ждать. Можно закомментировать строку. Использовалось для разнообразия времени ожидания (для алгоритмов Яндекса, хотя этого очень мало)
    browser.find_element_by_xpath("//button[@id='passp:sign-in']").click() # нажать кнопку "Войти"
    time.sleep(randint(0,3)) # ждать. Можно закомментировать строку. Использовалось для разнообразия времени ожидания (для алгоритмов Яндекса, хотя этого очень мало)
    browser.find_element_by_xpath("//input[@id='passp-field-passwd']").send_keys("wer32Hfrew") # ввести пароль
    browser.find_element_by_xpath("// button[ @ id = 'passp:sign-in']").click() # нажать кнопку "Войти"
    time.sleep(randint(2, 4)) # ждать. Можно закомментировать строку. Использовалось для разнообразия времени ожидания (для алгоритмов Яндекса, хотя этого очень мало)
    current_url = browser.current_url
    if f'https://passport.yandex.ru/profile' in current_url: # если открылась ссылка на профиль
        browser.find_element_by_xpath("//a[@class='user-account user-account_has-ticker_yes user-account_has-accent-letter_yes legouser__current-account i-bem']//img[@class='user-pic__image']").click() # нажать на иконку слева от логина в правом верхнем углу
        browser.find_element_by_xpath("//span[contains(text(),'Почта')]").click() #нажать на пункт меню "Почта"
    elif f'https://mail.yandex.ru' in current_url: # если открылась страница почты
        print("Ok") # Ок