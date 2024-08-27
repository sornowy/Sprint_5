from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestClick():
    def test_click_button_constructor_success(self, driver):
        # Нажимаем на кнопку "Войти в аккаунт"
        driver.find_element(By.XPATH, ".//div/button[text()='Войти в аккаунт']").click()

        # Вводим email
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input").send_keys("timurkadyrov13123@yandex.ru")

        # Вводим пароль
        driver.find_element(By.XPATH, ".//form/fieldset[last()]/div/div/input").send_keys("123456")

        # Нажимаем кнопку "Войти"
        driver.find_element(By.XPATH, ".//form/button[text()='Войти']").click()

        # Ожидаем, что кнопка "Оформить заказ" станет видимой
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div/button[text()='Оформить заказ']")))

        driver.find_element(By.XPATH, ".//nav/a").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div/ul/li[2]/div/div/input")))

        driver.find_element(By.XPATH, ".//nav/ul/li/a").click()

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_click_logo_success(self, driver):
        # Нажимаем на кнопку "Войти в аккаунт"
        driver.find_element(By.XPATH, ".//div/button[text()='Войти в аккаунт']").click()

        # Вводим email
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input").send_keys("timurkadyrov13123@yandex.ru")

        # Вводим пароль
        driver.find_element(By.XPATH, ".//form/fieldset[last()]/div/div/input").send_keys("123456")

        # Нажимаем кнопку "Войти"
        driver.find_element(By.XPATH, ".//form/button[text()='Войти']").click()

        # Ожидаем, что кнопка "Оформить заказ" станет видимой
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div/button[text()='Оформить заказ']")))

        driver.find_element(By.XPATH, ".//nav/a").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div/ul/li[2]/div/div/input")))

        driver.find_element(By.XPATH, ".//nav/div/a").click()

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
