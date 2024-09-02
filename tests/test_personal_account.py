from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locator_variables import Locators

class TestPersonlAccount():
    def test_open_personal_account_success(self, driver):
        # Нажимаем на кнопку "Войти в аккаунт"
        driver.find_element(*Locators.button_login).click()

        # Вводим email
        driver.find_element(*Locators.input_email_login).send_keys(Locators.login)

        email_remeber = driver.find_element(*Locators.input_email_login).get_attribute("value")

        # Вводим пароль
        driver.find_element(*Locators.input_password).send_keys(Locators.password)

        # Нажимаем кнопку "Войти"
        driver.find_element(*Locators.button_login_after_registration).click()

        # Ожидаем, что кнопка "Оформить заказ" станет видимой
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_order))

        driver.find_element(*Locators.nav_account).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.input_email_personal))

        email_personal_account = driver.find_element(*Locators.input_email_personal).get_attribute("value")

        assert email_remeber == email_personal_account