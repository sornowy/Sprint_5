from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locator_variables import Locators

class TestSection():
    def test_section_bulki(self, driver):
        # Нажимаем на кнопку "Войти в аккаунт"
        driver.find_element(*Locators.button_login).click()

        # Вводим email
        driver.find_element(*Locators.input_email_login).send_keys(Locators.login)

        # Вводим пароль
        driver.find_element(*Locators.input_password).send_keys(Locators.password)

        # Нажимаем кнопку "Войти"
        driver.find_element(*Locators.button_login_after_registration).click()

        # Ожидаем, что кнопка "Оформить заказ" станет видимой
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_order))

        section_bulki_element = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.section_bulki))

        assert "tab_tab_type_current__2BEPc" in section_bulki_element.get_attribute("class")

    def test_section_sous(self, driver):
        # Нажимаем на кнопку "Войти в аккаунт"
        driver.find_element(*Locators.button_login).click()

        # Вводим email
        driver.find_element(*Locators.input_email_login).send_keys(Locators.login)

        # Вводим пароль
        driver.find_element(*Locators.input_password).send_keys(Locators.password)

        # Нажимаем кнопку "Войти"
        driver.find_element(*Locators.button_login_after_registration).click()

        # Ожидаем, что кнопка "Оформить заказ" станет видимой
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_order))

        driver.find_element(*Locators.section_sous).click()

        section_sous_element = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.section_sous))

        assert "tab_tab_type_current__2BEPc" in section_sous_element.get_attribute("class")

    def test_section_nachinka(self, driver):
        # Нажимаем на кнопку "Войти в аккаунт"
        driver.find_element(*Locators.button_login).click()

        # Вводим email
        driver.find_element(*Locators.input_email_login).send_keys(Locators.login)

        # Вводим пароль
        driver.find_element(*Locators.input_password).send_keys(Locators.password)

        # Нажимаем кнопку "Войти"
        driver.find_element(*Locators.button_login_after_registration).click()

        # Ожидаем, что кнопка "Оформить заказ" станет видимой
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_order))

        driver.find_element(*Locators.section_nachinka).click()

        section_nachinka_element = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.section_nachinka))

        assert "tab_tab_type_current__2BEPc" in section_nachinka_element.get_attribute("class")
