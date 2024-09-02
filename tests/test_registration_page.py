from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locator_variables import Locators

class TestRegistration():
    def test_registration(self, driver):
        # находим кнопку Войти
        driver.find_element(*Locators.button_login).click()

        # находим ссылку на регистрацию
        driver.find_element(*Locators.link_register).click()

        # создание имени
        driver.find_element(*Locators.input_name).send_keys("Timur")

        # создание логина
        driver.find_element(*Locators.input_email_registration).send_keys(Locators.login)

        # создание пароля
        driver.find_element(*Locators.input_password).send_keys(Locators.password)

        # нажатие на кнопку Зарегистрироваться
        driver.find_element(*Locators.button_register).click()

        # ожидание загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_login_after_registration))

        # проверка, что регистрация успешная
        assert driver.current_url == Locators.url_login






