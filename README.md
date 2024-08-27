# Sprint_5
Кнопка "Войти в аккаунт":
By.XPATH, ".//div/button[text()='Войти в аккаунт']"
Ссылка на регистрацию:
By.XPATH, ".//p/a[text()='Зарегистрироваться']"
Поле для ввода имени:
By.XPATH, ".//form/fieldset[1]/div/div/input"
Поле для ввода логина (email):
By.XPATH, ".//form/fieldset[2]/div/div/input"
Поле для ввода пароля:
By.XPATH, ".//form/fieldset[last()]/div/div/input"
Кнопка "Зарегистрироваться" в форме регистрации:
By.XPATH, ".//form/button[text()='Зарегистрироваться']"
Кнопка "Войти" на странице после регистрации:
By.XPATH, ".//form/button[text()='Войти']"
Проверка на успешную регистрацию (URL):
assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
Поле ввода email (для логина):
By.XPATH, ".//form/fieldset[1]/div/div/input"
Кнопка "Войти" (для логина):
By.XPATH, ".//form/button[text()='Войти']"
Кнопка "Оформить заказ" (для проверки успешного входа):
By.XPATH, ".//div/button[text()='Оформить заказ']"
Ссылка на "Войти" после регистрации:
By.XPATH, ".//p/a[text()='Войти']"
Ссылка на "Восстановить пароль":
By.XPATH, ".//p/a[text()='Восстановить пароль']"
Аккаунт в навигации (для перехода в личный кабинет):
By.XPATH, ".//nav/a"
Поле с email в личном кабинете (для проверки сохраненного email):
By.XPATH, ".//div/ul/li[2]/div/div/input"
Кнопка "Выход" (для выхода из аккаунта):
By.XPATH, ".//nav/ul/li[last()]/button[text()='Выход']"
Кнопка "Войти" после выхода (для проверки, что выход был успешным):
By.XPATH, ".//form/button[text()='Войти']"
Навигационная ссылка для перехода на главный экран (логотип или другой элемент):
By.XPATH, ".//nav/ul/li/a"  # В тесте `test_click_button_constructor_success`
Навигационный элемент для перехода на главный экран:
By.XPATH, ".//nav/div/a"  # В тесте `test_click_logo_success`
Раздел "Булки":
By.XPATH, "html/body/div/div/main/section[1]/div/div[1]"
Раздел "Соусы":
By.XPATH, "html/body/div/div/main/section[1]/div/div[2]"
Раздел "Начинка":
By.XPATH, "html/body/div/div/main/section[1]/div/div[3]"