# запуск - pytest -v -s path\to\file\test_leadfrog_ru_feedback_button_and_popup.py

import time
from selenium.webdriver.common.by import By

link = "https://leadfrog.ru/"

# проверка pop-up "Обратной связи"
def test_feedback_pop_up(browser):
    # неявное ожидание подгрузки элементов
    browser.implicitly_wait(5)

    # переход на страницу https://leadfrog.ru/
    browser.get(link)

    # поиск кнопки "Обратная связь", иначе появится ошибка "NoSuchElementException" или "InvalidSelectorException"
    feedback_button = browser.find_element(By.XPATH, "//button[@id='uid11']//span[contains(text(),'Обратная связь')]")
    # проверка, что кнопка "Обратная связь" называется "Обратная связь", иначе ошибка
    assert feedback_button.text == "Обратная связь", f"Ошибка наименования кнопки 'Обратная связь', название кнопки - '{feedback_button.text}'"
    # клик по кнопке "Обратная связь"
    browser.execute_script("arguments[0].click();", feedback_button)

    # поиск pop-up'а. При его отсутствии появится ошибка "NoSuchElementException" или "InvalidSelectorException"
    browser.find_element(By.CLASS_NAME, "modal-content")

    # поиск первой строки pop-up'а "У вас есть вопросы?", иначе появится ошибка "NoSuchElementException"
    text_popup_feedback1 = browser.find_element(By.XPATH, '//*[@id="node11_meta"]/div/div/div/div[1]/div/div/div/div/p[1]/span')
    # проверка, что в первой строке написана фраза "У вас есть вопросы?", иначе ошибка
    assert text_popup_feedback1.text == "У вас есть вопросы?", f"Ошибка в первой строке текста поп-апа 'Обратная связь', текст первой строки - '{text_popup_feedback1.text}'"

    # поиск второй строки pop-up'а "Оставьте свои контакты и мы свяжемся с вами!", иначе появится ошибка "NoSuchElementException"
    text_popup_feedback2 = browser.find_element(By.XPATH, '//*[@id="node11_meta"]/div/div/div/div[1]/div/div/div/div/p[2]/span')
    # проверка, что во второй строке написана фраза "Оставьте свои контакты и мы свяжемся с вами!", иначе ошибка
    assert text_popup_feedback2.text == "Оставьте свои контакты и мы свяжемся с вами!", f"Ошибка во второй строке текста поп-апа 'Обратная связь', текст второй строки - '{text_popup_feedback2.text}'"

    # поиск посказки (слова "Имя") в поле ввода имени, иначе появится ошибка "NoSuchElementException"
    hint_text_in_input_name_popup_feedback = browser.find_element(By.XPATH, '//*[@id="node13_meta"]/div/div[1]')
    # проверка, что в поле ввода имени находится подсказка "Имя"
    assert hint_text_in_input_name_popup_feedback.text == "Имя", f"Ошибка в названии подсказки поля ввода имени поп-апа 'Обратная связь', название подсказки - '{hint_text_in_input_name_popup_feedback.text}'"

    # поиск посказки (слова "Телефон *") в поле ввода телефона, иначе появится ошибка "NoSuchElementException"
    hint_text_in_input_phone_popup_feedback = browser.find_element(By.XPATH, '//*[@id="node14_meta"]/div/div[1]')
    # проверка, что в поле ввода телефона находится подсказка "Телефон *"
    assert hint_text_in_input_phone_popup_feedback.text == "Телефон *", f"Ошибка в названии подсказки поля ввода телефона поп-апа 'Обратная связь', название подсказки - '{hint_text_in_input_phone_popup_feedback.text}'"

    # поиск поля ввода имени. При его отсутствии появится ошибка "NoSuchElementException"
    input_name_popup_feedback = browser.find_element(By.CSS_SELECTOR, "#node13_meta > div > div.input > input")
    # проверка, что это поле ввода имени "autocomplete" = "name"
    assert input_name_popup_feedback.get_attribute('autocomplete') == "name", f"Ошибка в значении атрибута 'autocomplete' поля ввода имени поп-апа 'Обратная связь', значение атрибута - '{input_name_popup_feedback.get_attribute('autocomplete')}'. Необходимо проверить верстку"

    # поиск поля ввода телефона. При его отсутствии появится ошибка "NoSuchElementException"
    input_name_popup_feedback2 = browser.find_element(By.CSS_SELECTOR, "#node14_meta > div > div.input > input")
    # проверка, что это поле ввода телефона "autocomplete" = "tel"
    assert input_name_popup_feedback2.get_attribute('autocomplete') == "tel", f"Ошибка в значении атрибута 'autocomplete' поля ввода телефона поп-апа 'Обратная связь', значение атрибута - '{input_name_popup_feedback.get_attribute('autocomplete')}'. Необходимо проверить верстку"

    # поиск кнопки "Отправить", иначе появится ошибка "NoSuchElementException" или "InvalidSelectorException"
    send_button = browser.find_element(By.XPATH, "//button[@id='uid18']")
    # проверка, что кнопка "Отправить" называется "Отправить", иначе ошибка
    assert send_button.text == "Отправить", f"Ошибка наименования кнопки 'Отправить', название кнопки - '{send_button.text}'"
    # клик по кнопке "Отправить"
    browser.execute_script("arguments[0].click();", send_button)
    # осмотреться
    time.sleep(10)
