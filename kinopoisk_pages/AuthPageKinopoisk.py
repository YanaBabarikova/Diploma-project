from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import allure


class Auth:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @allure.step(
        "Переходим на сайт Кинопоиск. Авторизуемся на сайте. Ожидаем возвращения на главную страницу. Логин - {login}, пароль - {password}."
    )
    def user_auth(self, login: str, password: str):
        """Данный метод позволяет пользователю авторизоваться
        на сайте, используя полученные входные данные.

        Args:
            login (str): адрес электронной почты.
            password (str): пароль.
        """
        with allure.step(
            "Если появляется капча нажимаем или продолжаем следующие шаги."
        ):
            try:
                self._driver.find_element(
                    By.CSS_SELECTOR, ".CheckboxCaptcha-Button"
                ).click()
            except NoSuchElementException:
                pass

        with allure.step("Нажимать кнопку 'Войти'"):
            self._driver.find_element(
                By.CSS_SELECTOR, ".styles_loginButton__LWZQp"
            ).click()

        with allure.step("Ввести адрес электронной почты (логин)."):
            self._driver.find_element(By.CSS_SELECTOR, "#passp-field-login").send_keys(
                login
            )

        with allure.step(
            "Нажать кнопку 'Войти', на странице ввода логина пользователя."
        ):
            self._driver.find_element(
                By.CSS_SELECTOR, ".passp-button.passp-sign-in-button"
            ).click()

        with allure.step("Ввести пароль"):
            self._driver.find_element(By.CSS_SELECTOR, "#passp-field-passwd").send_keys(
                password
            )

        with allure.step(
            "Нажать кнопку 'Войти', на странице ввода пароля пользователя."
        ):
            self._driver.find_element(
                By.CSS_SELECTOR, ".passp-button.passp-sign-in-button"
            ).click()

        with allure.step("Ожидаем возвращения на главную страницу сайта."):
            WebDriverWait(self._driver, 5).until(
                EC.url_contains("https://www.kinopoisk.ru/")
            )