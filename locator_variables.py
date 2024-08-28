from selenium.webdriver.common.by import By

class Locators:
    # Кнопки
    button_login = (By.XPATH, ".//div/button[text()='Войти в аккаунт']")
    button_register = (By.XPATH, ".//form/button[text()='Зарегистрироваться']")
    button_login_after_registration = (By.XPATH, ".//form/button[text()='Войти']")
    button_order = (By.XPATH, ".//div/button[text()='Оформить заказ']")
    button_logout = (By.XPATH, "//button[contains(text(), 'Выход')]")

    # Поля ввода
    input_name = (By.XPATH, ".//input[@type='text' and @name='name']")
    input_email_registration = (By.XPATH, ".//input[@type='text' and @name='name' and preceding-sibling::label[text()='Email']]")
    input_email_login = (By.XPATH, ".//input[@type='text' and @name='name' and preceding-sibling::label[text()='Email']]")
    input_password = (By.XPATH, ".//input[@type='password' and @name='Пароль']")

    # Ссылки
    link_register = (By.XPATH, ".//p/a[text()='Зарегистрироваться']")
    link_login_after_registration = (By.XPATH, ".//p/a[text()='Войти']")
    link_password_recovery = (By.XPATH, ".//p/a[text()='Восстановить пароль']")

    # Элементы навигации
    nav_account = (By.XPATH, ".//nav/a")
    nav_home = (By.XPATH, ".//a[contains(@class, 'AppHeader_header__link') and contains(., 'Конструктор')]")  # Конструктор
    nav_home_direct = (By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo')]//a[@href='/']")  # Логотип

    # Поля в личном кабинете
    input_email_personal = (By.XPATH, ".//div/ul/li[2]/div/div/input")

    # Разделы
    section_bulki = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Булки')]")
    section_sous = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Соусы')]")
    section_nachinka = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Начинки')]")

    # Проверки
    url_login = "https://stellarburgers.nomoreparties.site/login"
    url = "https://stellarburgers.nomoreparties.site/"

    # Данные для входа
    login = "timurkadyrov13129@yandex.ru"
    password = "123456"