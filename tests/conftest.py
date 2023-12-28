import pytest
from selenium import webdriver
from pages.etaxi_main import EtaxiMain

@pytest.fixture(scope='session')
def chrome_driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument('executable_path=utils\\chromedriver.exe')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver

@pytest.fixture(scope='function')
def etaxi_main(chrome_driver):
    # Создаем экземпляр класса EtaxiMain
    return EtaxiMain(chrome_driver)

@pytest.fixture(scope='function')
def etaxi_contacts(chrome_driver):
    # Создаем экземпляр класса EtaxiContacts
    return EtaxiContacts(chrome_driver)

@pytest.fixture(scope='function')
def etaxi_about(chrome_driver):
    # Создаем экземпляр класса EtaxiAbout
    return EtaxiAbout(chrome_driver)
