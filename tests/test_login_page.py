from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLogin:
    def test_login_button_success(self, driver):
        #находим кнопку Войти
        driver.find_element(By.XPATH, ".//div/button[text()='Войти в аккаунт']").click()

        #Вводим email
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input").send_keys("timurkadyrov13123@yandex.ru")

        #Вводим пароль
        driver.find_element(By.XPATH, ".//form/fieldset[last()]/div/div/input").send_keys("123456")

        #Нажимаем кнопку "Войти"
        driver.find_element(By.XPATH, ".//form/button[text()='Войти']").click()

        #ожидание загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div/button[text()='Оформить заказ']")))

        # Проверяем, что URL совпадает с ожидаемым
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_login_personal_account_success(self, driver):
        # Нажимаем на кнопку аккаунта в навигации
        driver.find_element(By.XPATH, ".//nav/a").click()

        # Вводим email
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input").send_keys("timurkadyrov13123@yandex.ru")

        # Вводим пароль
        driver.find_element(By.XPATH, ".//form/fieldset[last()]/div/div/input").send_keys("123456")

        # Нажимаем кнопку "Войти"
        driver.find_element(By.XPATH, ".//form/button[text()='Войти']").click()

        # Ожидаем, что кнопка "Оформить заказ" станет видимой
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div/button[text()='Оформить заказ']")))

        # Проверяем, что URL совпадает с ожидаемым
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_login_form_registration_success(self, driver):
        driver.find_element(By.XPATH, ".//div/button[text()='Войти в аккаунт']").click()

        driver.find_element(By.XPATH, ".//p/a[text()='Зарегистрироваться']").click()

        driver.find_element(By.XPATH, ".//p/a[text()='Войти']").click()

        driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input").send_keys("timurkadyrov13123@yandex.ru")

        driver.find_element(By.XPATH, ".//form/fieldset[last()]/div/div/input").send_keys("123456")

        driver.find_element(By.XPATH, ".//form/button[text()='Войти']").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div/button[text()='Оформить заказ']")))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_login_form_password_recovery_success(self, driver):
        driver.find_element(By.XPATH, ".//div/button[text()='Войти в аккаунт']").click()

        driver.find_element(By.XPATH, ".//p/a[text()='Восстановить пароль']").click()

        driver.find_element(By.XPATH, ".//p/a[text()='Войти']").click()

        driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input").send_keys("timurkadyrov13123@yandex.ru")

        driver.find_element(By.XPATH, ".//form/fieldset[last()]/div/div/input").send_keys("123456")

        driver.find_element(By.XPATH, ".//form/button[text()='Войти']").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div/button[text()='Оформить заказ']")))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"