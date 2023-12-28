from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EtaxiMain:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'http://185.246.118.41/'

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def open(self):
        """Открытие главной страницы"""
        self.driver.get(self.base_url)

    def wait_for_element(self, by, value, timeout=10):
        """Ожидание загрузки определённого элемента"""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))

    def element_is_visible(self, element):
        """Проверка, что элемент располагается в видимой области экрана"""

        # Вертикальное расстояние от верхней границы элемента до верхней границы видимой области окна
        element_top = element.location['y'] - self.driver.execute_script("return window.scrollY;")

        # Проверка, что верхняя граница элемента видна в видимой области. Значение -10 выбрано для небольшой погрешности,
        # на случай если верх элемента немного выше видимой зоны, но это не плияет на качество отображения
        return -10 <= element_top <= self.driver.execute_script("return window.innerHeight;")

    def click_catalog_link(self):
        """Нажатие на ссылку 'Каталог'"""
        catalog = self.wait_for_element(By.XPATH, '//li[@class="header-nav__item"]/a[contains(@href, "#catalog")]')
        catalog.click()

    def click_footer_catalog_link(self):
        """Нажатие на ссылку 'Каталог' из футера"""
        catalog = self.wait_for_element(By.XPATH, '//li[@class="nav__item-footer"]/a[contains(@href, "#catalog")]')
        catalog.click()

    def catalog_section(self):
        """Поиск блока 'Автомобили нашего таксопарка'"""
        return self.find_element(By.XPATH, '//section[@id="catalog"]')

    def click_rent_link(self):
        """Нажатие на ссылку 'Условия аренды'"""
        rent = self.wait_for_element(By.XPATH, '//li[@class="header-nav__item"]/a[contains(@href, "#rent")]')
        rent.click()

    def click_footer_rent_link(self):
        """Нажатие на ссылку 'Условия аренды' из футера"""
        rent = self.wait_for_element(By.XPATH, '//li[@class="nav__item-footer"]/a[contains(@href, "#rent")]')
        rent.click()

    def rent_section(self):
        """Поиск блока 'Условия аренды'"""
        return self.find_element(By.XPATH, '//section[@id="rent"]')

    def click_reviews_link(self):
        """Нажатие на ссылку 'Отзывы'"""
        reviews = self.wait_for_element(By.XPATH, '//li[@class="header-nav__item"]/a[contains(@href, "#reviews")]')
        reviews.click()

    def click_footer_reviews_link(self):
        """Нажатие на ссылку 'Отзывы' из футера"""
        reviews = self.wait_for_element(By.XPATH, '//li[@class="nav__item-footer"]/a[contains(@href, "#reviews")]')
        reviews.click()

    def reviews_section(self):
        """Поиск блока 'Отзывы'"""
        return self.wait_for_element(By.XPATH, '//section[@id="reviews"]')

    def click_contacts_link(self):
        """Нажатие на ссылку 'Контакты'"""
        contacts = self.wait_for_element(By.XPATH, '//li[@class="header-nav__item"]/a[contains(@href, "/contacts")]')
        contacts.click()

    def click_footer_contacts_link(self):
        """Нажатие на ссылку 'Контакты' из футера"""
        contacts = self.wait_for_element(By.XPATH, '//li[@class="nav__item-footer"]/a[contains(@href, "#contacts")]')
        contacts.click()

    def contacts_section(self):
        """Поиск блока 'Контакты'"""
        return self.wait_for_element(By.XPATH, '//section[@id="contacts"]')

    def click_about_link(self):
        """Нажатие на ссылку 'О нас'"""
        about = self.wait_for_element(By.XPATH, '//li[@class="header-nav__item"]/a[contains(@href, "/about")]')
        about.click()

    def click_footer_about_link(self):
        """Нажатие на ссылку 'О нас' из футера"""
        about = self.wait_for_element(By.XPATH, '//li[@class="nav__item-footer"]/a[contains(@href, "/about")]')
        about.click()

    def get_current_url(self):
        """URL текущей страницы"""
        return self.driver.current_url

    def click_logo(self):
        """Нажатие на логотип"""
        logo = self.wait_for_element(By.XPATH, '//div[@class="header-logo"]')
        logo.click()

    def main_section(self):
        """Главный/первый блок на главной странице"""
        return self.wait_for_element(By.XPATH, '//section[@class="main"]')

    def click_request_button(self):
        """Нажатие на кнопку 'Оставить заявку'"""
        request_button = self.wait_for_element(By.XPATH, '//button[@class="button header-nav__button"]')
        request_button.click()

    def click_rent_button(self):
        """Нажатие на кнопку 'Арендовать'"""
        rent_button = self.wait_for_element(By.XPATH, '//button[@class="button catalog__button" and contains(text(), "Арендовать")]')
        rent_button.click()

    def input_name(self, keyword):
        """Ввести имя"""
        name = self.wait_for_element(By.XPATH, '//input[@id="id_name"]')
        name.clear()
        name.send_keys(keyword)

    def input_phone_number(self, keyword):
        """Ввести номер телефона"""
        phone_number = self.wait_for_element(By.XPATH, '//input[@id="id_phone_number"]')
        phone_number.clear()
        phone_number.send_keys(keyword)

    def click_submit_button(self):
        """Нажатие на кнопку 'Оставить заявку' (отправить данные)"""
        submit_button = self.wait_for_element(By.XPATH, '//button[@class="button application-button" and @type="submit"]')
        submit_button.click()

    def confirmation_message(self):
        """Ожидание сообщения об успешной отправке данных"""
        return self.wait_for_element(By.XPATH, '//*[contains(text(), "заявка принята")]')

    def hint_message(self):
        """Ожидание всплывающей подсказки по заполнению поля"""
        return self.wait_for_element(By.XPATH, '//div[@class="form-error"]')

    def get_input_value(self):
        """Получение значения из поля ИМЯ"""
        input_element = self.find_element(By.XPATH, '//input[@id="id_name"]')
        return input_element.get_attribute('value')

    def uncheck_checkbox(self):
        """Снять галочку с чекбокса 'Согласие на обработку данных'"""
        checkbox = self.wait_for_element(By.XPATH, '//input[@id="confirmation"]')
        if checkbox.is_selected():
            # Чекбокс перекрывается другим элементом поэтому пришлось использовать JavaScript
            self.driver.execute_script("arguments[0].click();", checkbox)

    def request_form(self):
        """Ожидание появления формы отправки запроса"""
        return self.wait_for_element(By.XPATH, '//form[@id="reg-form"]')

    def click_close(self):
        """Нажатие на 'крестик' (закрыть)"""
        close_button = self.wait_for_element(By.XPATH, '//figure[@class="application-close"]')
        close_button.click()
