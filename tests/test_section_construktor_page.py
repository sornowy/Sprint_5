from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestSection():
    def test_section_bulki(self, driver):
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

        assert "tab_tab_type_current__2BEPc" in driver.find_element(By.XPATH, "html/body/div/div/main/section[1]/div/div[1]").get_attribute("class")

    def test_section_sous(self, driver):
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

        driver.find_element(By.XPATH, "html/body/div/div/main/section[1]/div/div[2]").click()

        assert "tab_tab_type_current__2BEPc" in driver.find_element(By.XPATH,"html/body/div/div/main/section[1]/div/div[2]").get_attribute("class")

    def test_section_nachinka(self, driver):
        # Нажимаем на кнопку "Войти в аккаунт"
        driver.find_element(By.XPATH, ".//div/button[text()='Войти в аккаунт']").click()

        # Вводим email
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input").send_keys("timurkadyrov13123@yandex.ru")

        # Вводим пароль
        driver.find_element(By.XPATH, ".//form/fieldset[last()]/div/div/input").send_keys("123456")

        # Нажимаем кнопку "Войти"
        driver.find_element(By.XPATH, ".//form/button[text()='Войти']").click()

        # Ожидаем, что кнопка "Оформить заказ" станет видимой
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//div/button[text()='Оформить заказ']")))

        driver.find_element(By.XPATH, "html/body/div/div/main/section[1]/div/div[3]").click()

        assert "tab_tab_type_current__2BEPc" in driver.find_element(By.XPATH, "html/body/div/div/main/section[1]/div/div[2]").get_attribute("class")
