import time
link = "http://itcareer.pythonanywhere.com/"

# Проверка названия страницы
def test_ITCareerToday_web_form_text(browser):
    browser.get(link)
    form_text = browser.find_element_by_xpath("//h2[normalize-space()='ITCareerToday web form']").text
    assert form_text == "ITCareerToday web form", f"Text changed - now this text is '{form_text}'"

# Проверка названия поля ввода имени
def test_checking_name_of_name_input_field(browser):
    browser.get(link)
    name_of_name_input_field = browser.find_element_by_xpath("//label[normalize-space()='Name:']").text
    assert name_of_name_input_field == "Name:", f"Name of the input field has changed - now this text is '{name_of_name_input_field}'"

# Проверка текста в поле ввода имени
def test_checking_text_in_name_input_field(browser):
    browser.get(link)
    text_in_name_input_field = browser.find_element_by_xpath("//input[@id='name']").get_attribute('placeholder')
    assert text_in_name_input_field == "Name?", f"Text changed - now this text is '{text_in_name_input_field}'"

# Проверка наличия поля ввода имени
def test_checking_name_input_field(browser):
    browser.get(link)
    type_of_field_of_input_name = browser.find_element_by_xpath("//input[@id='name']").get_attribute('type')
    id_of_field_of_input_name = browser.find_element_by_xpath("//input[@id='name']").get_attribute('id')
    name_of_field_of_input_name = browser.find_element_by_xpath("//input[@id='name']").get_attribute('name')
    assert type_of_field_of_input_name == "text", f"This is probably not a name input field  - type of field of input name '{type_of_field_of_input_name}'"
    assert id_of_field_of_input_name == "name", f"This is probably not a name input field - id of field of input name '{id_of_field_of_input_name}'"
    assert name_of_field_of_input_name == "name", f"This is probably not a name input field - name of field of input name '{name_of_field_of_input_name}'"

# Проверка названия поля ввода фамилии
def test_checking_name_of_surname_input_field(browser):
    browser.get(link)
    name_of_surname_input_field = browser.find_element_by_xpath("//label[normalize-space()='Surame:']").text
    assert name_of_surname_input_field == "Surname:", f"Name of the input field has changed - now this text is '{name_of_surname_input_field}'"

# Проверка текста в поле ввода фамилии
def test_checking_text_in_surname_input_field(browser):
    browser.get(link)
    text_in_surname_input_field = browser.find_element_by_xpath("//input[@id='surname']").get_attribute('placeholder')
    assert text_in_surname_input_field == "Surname?", f"Text changed - now this text is '{text_in_surname_input_field}'"

# Проверка наличия поля ввода фамилии
def test_checking_surname_input_field(browser):
    browser.get(link)
    type_of_field_of_input_surname = browser.find_element_by_xpath("//input[@id='surname']").get_attribute('type')
    id_of_field_of_input_surname = browser.find_element_by_xpath("//input[@id='surname']").get_attribute('id')
    name_of_field_of_input_surname = browser.find_element_by_xpath("//input[@id='surname']").get_attribute('name')
    assert type_of_field_of_input_surname == "text", f"This is probably not a surname input field  - type of field of input surname '{type_of_field_of_input_surname}'"
    assert id_of_field_of_input_surname == "surname", f"This is probably not a surname input field - id of field of input surname '{id_of_field_of_input_surname}'"
    assert name_of_field_of_input_surname == "surname", f"This is probably not a surname input field - name of field of input surname '{name_of_field_of_input_surname}'"

# Проверка названия поля ввода email
def test_checking_name_of_email_input_field(browser):
    browser.get(link)
    name_of_email_input_field = browser.find_element_by_xpath("//label[normalize-space()='Email:']").text
    assert name_of_email_input_field == "Email:", f"Name of the input field has changed - now this text is '{name_of_email_input_field}'"

# Проверка текста в поле ввода email
def test_checking_text_in_email_input_field(browser):
    browser.get(link)
    text_in_email_input_field = browser.find_element_by_xpath("//input[@id='email']").get_attribute('placeholder')
    assert text_in_email_input_field == "Your email address.", f"Text changed - now this text is '{text_in_email_input_field}'"

# Проверка наличия поля ввода email
def test_checking_email_input_field(browser):
    browser.get(link)
    type_of_field_of_input_email = browser.find_element_by_xpath("//input[@id='email']").get_attribute('type')
    id_of_field_of_input_email = browser.find_element_by_xpath("//input[@id='email']").get_attribute('id')
    name_of_field_of_input_email = browser.find_element_by_xpath("//input[@id='email']").get_attribute('name')
    assert type_of_field_of_input_email == "text", f"This is probably not a email input field  - type of field of input email '{type_of_field_of_input_email}'"
    assert id_of_field_of_input_email == "email", f"This is probably not a email input field - id of field of input email '{id_of_field_of_input_email}'"
    assert name_of_field_of_input_email == "email", f"This is probably not a email input field - name of field of input email '{name_of_field_of_input_email}'"

# Проверка названия поля ввода пароля
def test_checking_name_of_password_input_field(browser):
    browser.get(link)
    name_of_password_input_field = browser.find_element_by_xpath("//label[normalize-space()='Password:']").text
    assert name_of_password_input_field == "Password:", f"Name of the input field has changed - now this text is '{name_of_password_input_field}'"

# Проверка текста в поле ввода пароля
def test_checking_text_in_password_input_field(browser):
    browser.get(link)
    text_in_password_input_field = browser.find_element_by_xpath("//input[@id='password']").get_attribute('placeholder')
    assert text_in_password_input_field == "Enter a password.", f"Text changed - now this text is '{text_in_password_input_field}'"

# Проверка наличия поля ввода email
def test_checking_password_input_field(browser):
    browser.get(link)
    type_of_field_of_input_password = browser.find_element_by_xpath("//input[@id='password']").get_attribute('type')
    id_of_field_of_input_password = browser.find_element_by_xpath("//input[@id='password']").get_attribute('id')
    name_of_field_of_input_password = browser.find_element_by_xpath("//input[@id='password']").get_attribute('name')
    assert type_of_field_of_input_password == "password", f"This is probably not a password input field  - type of field of input password '{type_of_field_of_input_password}'"
    assert id_of_field_of_input_password == "password", f"This is probably not a password input field - id of field of input password '{id_of_field_of_input_password}'"
    assert name_of_field_of_input_password == "password", f"This is probably not a password input field - name of field of input password '{name_of_field_of_input_password}'"

# Проверка названия кнопки отправки запроса
def test_checking_button_name(browser):
    browser.get(link)
    button1 = browser.find_element_by_xpath("//button[normalize-space()='Submit']").text
    assert button1 == "Submit", f"Button has a different name - now this text is '{button1}'"

# Проверка наличия кнопки отправки запроса
def test_checking_button_type(browser):
    browser.get(link)
    button1 = browser.find_element_by_xpath("//button[normalize-space()='Submit']").get_attribute("type")
    assert button1 == "submit", f"This is a different button - now this text is '{button1}'"

# Smoke
def test_smoke(browser):
    browser.get(link)
    browser.find_element_by_xpath("//input[@id='name']").send_keys("Aleksey")
    browser.find_element_by_xpath("//input[@id='surname']").send_keys("Bondarenko")
    browser.find_element_by_xpath("//input[@id='email']").send_keys("bonddd@gmail.com")
    browser.find_element_by_xpath("//input[@id='password']").send_keys("123456")
    #время проверить
    time.sleep(5)
    browser.find_element_by_xpath("//button[normalize-space()='Submit']").click()