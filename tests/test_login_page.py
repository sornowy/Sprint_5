from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locator_variables import Locators

class TestLogin:
    def test_login_button_success(self, driver):
        # находим кнопку Войти
        driver.find_element(*Locators.button_login).click()

        # Вводим email
        driver.find_element(*Locators.input_email_login).send_keys(Locators.login)

        # Вводим пароль
        driver.find_element(*Locators.input_password).send_keys(Locators.password)

        # Нажимаем кнопку "Войти"
        driver.find_element(*Locators.button_login_after_registration).click()

        # ожидание загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_order))

        # Проверяем, что URL совпадает с ожидаемым
        assert driver.current_url == Locators.url

    def test_login_personal_account_success(self, driver):
        # Нажимаем на кнопку аккаунта в навигации
        driver.find_element(*Locators.nav_account).click()

        # Вводим email
        driver.find_element(*Locators.input_email_login).send_keys(Locators.login)

        # Вводим пароль
        driver.find_element(*Locators.input_password).send_keys(Locators.password)

        # Нажимаем кнопку "Войти"
        driver.find_element(*Locators.button_login_after_registration).click()

        # Ожидаем, что кнопка "Оформить заказ" станет видимой
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_order))

        # Проверяем, что URL совпадает с ожидаемым
        assert driver.current_url == Locators.url

    def test_login_form_registration_success(self, driver):
        driver.find_element(*Locators.button_login).click()

        driver.find_element(*Locators.link_register).click()

        driver.find_element(*Locators.link_login_after_registration).click()

        driver.find_element(*Locators.input_email_login).send_keys(Locators.login)

        driver.find_element(*Locators.input_password).send_keys(Locators.password)

        driver.find_element(*Locators.button_login_after_registration).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_order))

        assert driver.current_url == Locators.url

    def test_login_form_password_recovery_success(self, driver):
        driver.find_element(*Locators.button_login).click()

        driver.find_element(*Locators.link_password_recovery).click()

        driver.find_element(*Locators.link_login_after_registration).click()

        driver.find_element(*Locators.input_email_login).send_keys(Locators.login)

        driver.find_element(*Locators.input_password).send_keys(Locators.password)

        driver.find_element(*Locators.button_login_after_registration).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_order))

        assert driver.current_url == Locators.url