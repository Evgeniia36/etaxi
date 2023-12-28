import time
import pytest
from pages.etaxi_main import EtaxiMain
from selenium.webdriver.common.by import By

def test_send_request_button(chrome_driver, etaxi_main):
    """Нажатие на 'Оставить заявку' открывает форму отправки запроса"""
    etaxi_main.open()
    etaxi_main.click_request_button()

    assert etaxi_main.request_form()

def test_rent_button(chrome_driver, etaxi_main):
    """Нажатие на 'Арендовать' открывает форму отправки запроса"""
    etaxi_main.open()
    etaxi_main.click_rent_button()

    assert etaxi_main.request_form()

def test_successful_send_request(chrome_driver, etaxi_main):
    """Проверка успешной отправки заявки на сервер"""
    etaxi_main.open()
    etaxi_main.click_request_button()
    etaxi_main.input_name('Николай')
    etaxi_main.input_phone_number('+79129786539')
    etaxi_main.click_submit_button()

    # Проверяем, что сообщение об отправке данных появилось на странице
    confirmation = etaxi_main.confirmation_message()

    assert confirmation.is_displayed()

def test_name_yo_simbol(chrome_driver, etaxi_main):
    """Проверка, что поле ИМЯ принимает букву Ё"""
    etaxi_main.open()
    etaxi_main.click_request_button()
    etaxi_main.input_name('Иван Фёдорович Крузенштерн')
    etaxi_main.input_phone_number('+79129786539')
    etaxi_main.click_submit_button()

    # Проверяем, что сообщение об отправке данных появилось на странице
    confirmation = etaxi_main.confirmation_message()

    assert confirmation.is_displayed()

def test_latin_name(chrome_driver, etaxi_main):
    """Проверка, что поле ИМЯ принимает латиницу"""
    etaxi_main.open()
    etaxi_main.click_request_button()
    etaxi_main.input_name('Alina')
    etaxi_main.input_phone_number('+79129786539')
    etaxi_main.click_submit_button()

    # Проверяем, что сообщение об отправке данных появилось на странице
    confirmation = etaxi_main.confirmation_message()

    assert confirmation.is_displayed()

def test_catalog_link(chrome_driver, etaxi_main):
    """Нажатие на ссылку 'Каталог' прокручивает страницу до блока 'Автомобили нашего таксопарка'"""
    etaxi_main.open()
    etaxi_main.click_catalog_link()
    element = etaxi_main.catalog_section()

    assert etaxi_main.element_is_visible(element), "Блок 'Автомобили нашего таксопарка' не отображается на экране"

def test_rent_link(chrome_driver, etaxi_main):
    """Нажатие на ссылку 'Условия аренды' прокручивает страницу до блока 'Условия аренды'"""
    # etaxi_main.open()
    etaxi_main.click_rent_link()
    element = etaxi_main.rent_section()

    assert etaxi_main.element_is_visible(element), "Блок 'Условия аренды' не отображается на экране"

def test_reviews_link(chrome_driver, etaxi_main):
    """Нажатие на ссылку 'Отзывы' прокручивает страницу до блока 'Отзывы'"""
    # etaxi_main.open()
    etaxi_main.click_reviews_link()
    element = etaxi_main.reviews_section()

    assert etaxi_main.element_is_visible(element), "Блок 'Отзывы' не отображается на экране"

def test_contacts_link(chrome_driver, etaxi_main):
    """Нажатие на ссылку 'Контакты' открывает страницу 'Контакты'"""
    # etaxi_main.open()
    etaxi_main.click_contacts_link()

    assert '/contacts' in etaxi_main.get_current_url(), "Станица 'Контакты' не открылась"

def test_about_link(chrome_driver, etaxi_main):
    """Нажатие на ссылку 'О нас' открывает страницу 'О нас'"""
    # etaxi_main.open()
    etaxi_main.click_about_link()

    assert '/about' in etaxi_main.get_current_url(), "Станица 'О нас' не открылась"

def test_logo(chrome_driver, etaxi_main):
    """Нажатие на логотип открывает главную страницу"""
    # etaxi_main.open()
    etaxi_main.click_logo()
    element = etaxi_main.main_section()

    assert etaxi_main.element_is_visible(element), "Что-то не так с главной страницей"

def test_footer_catalog_link(chrome_driver, etaxi_main):
    """Нажатие на ссылку 'Каталог' из футера прокручивает страницу до блока 'Автомобили нашего таксопарка'"""
    # etaxi_main.open()
    etaxi_main.click_footer_catalog_link()
    element = etaxi_main.catalog_section()

    assert etaxi_main.element_is_visible(element), "Блок 'Автомобили нашего таксопарка' не отображается на экране"

def test_footer_rent_link(chrome_driver, etaxi_main):
    """Нажатие на ссылку 'Условия аренды' из футера прокручивает страницу до блока 'Условия аренды'"""
    # etaxi_main.open()
    etaxi_main.click_footer_rent_link()
    element = etaxi_main.rent_section()

    assert etaxi_main.element_is_visible(element), "Блок 'Условия аренды' не отображается на экране"

def test_footer_reviews_link(chrome_driver, etaxi_main):
    """Нажатие на ссылку 'Отзывы' из футера прокручивает страницу до блока 'Отзывы'"""
    # etaxi_main.open()
    etaxi_main.click_footer_reviews_link()
    element = etaxi_main.reviews_section()

    assert etaxi_main.element_is_visible(element), "Блок 'Отзывы' не отображается на экране"

def test_footer_contacts_link(chrome_driver, etaxi_main):
    """Нажатие на ссылку 'Контакты' из футера прокручивает страницу до блока 'Контакты'"""
    # etaxi_main.open()
    etaxi_main.click_footer_contacts_link()
    element = etaxi_main.contacts_section()

    assert etaxi_main.element_is_visible(element), "Блок 'Контакты' не отображается на экране"

def test_footer_about_link(chrome_driver, etaxi_main):
    """Нажатие на ссылку 'О нас' из футера открывает страницу 'О нас'"""
    # etaxi_main.open()
    etaxi_main.click_footer_about_link()

    assert '/about' in etaxi_main.get_current_url(), "Станица 'О нас' не открылась"


# Негативное тестирование формы отправки заявки

def test_empty_name(chrome_driver, etaxi_main):
    """Пустое значение в поле ИМЯ вызывает подсказку по заполнению поля"""
    # etaxi_main.open()
    etaxi_main.click_request_button()
    etaxi_main.input_name('')
    etaxi_main.input_phone_number('+79129786539')
    etaxi_main.click_submit_button()

    # Ожидание появления сообщения
    assert etaxi_main.hint_message(), "Подсказка не появилась"

def test_symbols_name(chrome_driver, etaxi_main):
    """Специальные символы в поле ИМЯ вызывают подсказку по заполнению поля"""
    # etaxi_main.open()
    # etaxi_main.click_request_button()
    etaxi_main.input_name('!;№@')
    etaxi_main.input_phone_number('+79129786539')
    etaxi_main.click_submit_button()

    # Ожидание появления сообщения
    assert etaxi_main.hint_message(), "Подсказка не появилась"

def test_numbers_name(chrome_driver, etaxi_main):
    """Цифры в поле ИМЯ вызывают подсказку по заполнению поля"""
    # etaxi_main.open()
    # etaxi_main.click_request_button()
    etaxi_main.input_name('1')
    etaxi_main.input_phone_number('+79129786539')
    etaxi_main.click_submit_button()

    # Ожидание появления сообщения
    assert etaxi_main.hint_message(), "Подсказка не появилась"

def test_too_long_name(chrome_driver, etaxi_main):
    """Слишком длинное значение в поле ИМЯ автоматически обрезается до 40 символов"""
    # etaxi_main.open()
    # etaxi_main.click_request_button()
    etaxi_main.input_name('Иван Федорович Крузенштерн Иван Федорович')
    input_value = etaxi_main.get_input_value()
    max_length = 40

    assert len(input_value) <= max_length

def test_empty_phone(chrome_driver, etaxi_main):
    """Пустое значение в поле ТЕЛЕФОН вызывает подсказку по заполнению поля"""
    # etaxi_main.open()
    # etaxi_main.click_request_button()
    etaxi_main.input_name('Николай')
    etaxi_main.input_phone_number('')
    etaxi_main.click_submit_button()

    # Ожидание появления сообщения
    assert etaxi_main.hint_message(), "Подсказка не появилась"

def test_symbols_phone(chrome_driver, etaxi_main):
    """Нечисловое значение в поле ТЕЛЕФОН вызывает подсказку по заполнению поля"""
    # etaxi_main.open()
    # etaxi_main.click_request_button()
    etaxi_main.input_name('Николай')
    etaxi_main.input_phone_number('+7912978653g')
    etaxi_main.click_submit_button()

    # Ожидание появления сообщения
    assert etaxi_main.hint_message(), "Подсказка не появилась"

def test_too_long_phone(chrome_driver, etaxi_main):
    """Слишком длинное значение в поле ТЕЛЕФОН вызывает подсказку по заполнению поля"""
    # etaxi_main.open()
    # etaxi_main.click_request_button()
    etaxi_main.input_name('Николай')
    etaxi_main.input_phone_number('+791297865399')
    etaxi_main.click_submit_button()

    # Ожидание появления сообщения
    assert etaxi_main.hint_message(), "Подсказка не появилась"

def test_too_short_phone(chrome_driver, etaxi_main):
    """Слишком короткое значение в поле ТЕЛЕФОН вызывает подсказку по заполнению поля"""
    # etaxi_main.open()
    # etaxi_main.click_request_button()
    etaxi_main.input_name('Николай')
    etaxi_main.input_phone_number('7')
    etaxi_main.click_submit_button()

    # Ожидание появления сообщения
    assert etaxi_main.hint_message(), "Подсказка не появилась"

def test_wrong_format_phone(chrome_driver, etaxi_main):
    """Неверный формат значения в поле ТЕЛЕФОН вызывает подсказку по заполнению поля"""
    # etaxi_main.open()
    # etaxi_main.click_request_button()
    etaxi_main.input_name('Николай')
    etaxi_main.input_phone_number('+49129786539')
    etaxi_main.click_submit_button()

    # Ожидание появления сообщения
    assert etaxi_main.hint_message(), "Подсказка не появилась"

def test_unchecked_checkbox(chrome_driver, etaxi_main):
    """Снятый флаг с чекбокса 'Согласие на обработку данных' вызывает подсказку по заполнению поля"""
    # etaxi_main.open()
    # etaxi_main.click_request_button()
    etaxi_main.input_name('Николай')
    etaxi_main.input_phone_number('+79129786539')
    etaxi_main.uncheck_checkbox()
    etaxi_main.click_submit_button()

    # Ожидание появления сообщения
    assert etaxi_main.hint_message(), "Подсказка не появилась"
