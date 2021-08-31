from selenium.webdriver.common.by import By

link = "https://leadfrog.ru/"

def test_write_to_wa(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    write_wa_button = browser.find_element(By.XPATH, "//span[contains(text(),'Написать в WhatsApp')]")
    browser.execute_script("arguments[0].click();", write_wa_button)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    go_to_wa_chat_button = browser.find_element(By.CSS_SELECTOR, "#action-button")
    browser.execute_script("arguments[0].click();", go_to_wa_chat_button)
    use_wa_web = browser.find_element(By.XPATH, "//a[contains(text(),'используйте WhatsApp Web')]")
    browser.execute_script("arguments[0].click();", use_wa_web)
