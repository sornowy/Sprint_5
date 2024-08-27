from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegistration():
    def test_registration(self, driver):
#находим кнопку Войти
        driver.find_element(By.XPATH, ".//div/button[text()='Войти в аккаунт']").click()

#находим ссылку на регистрацию
        driver.find_element(By.XPATH, ".//p/a[text()='Зарегистрироваться']").click()

#создание имени
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input").send_keys("Timur")

#создание логина
        driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input").send_keys("timurkadyrov13129@yandex.ru")

#создание пароля
        driver.find_element(By.XPATH, ".//form/fieldset[last()]/div/div/input").send_keys("123456")

#нажатие на кнопку Войти в форме регистрации
        driver.find_element(By.XPATH, ".//form/button[text()='Зарегистрироваться']").click()

#ожидание загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//form/button[text()='Войти']")))

#проверка что регистрация успешная
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"






