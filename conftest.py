import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="Choose browser language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")

    options = webdriver.ChromeOptions()

    # У себя я использую Chrome for testing, но для проверки закомментирую реализацию через него
    # options.binary_location = r"D:\Chrome-for-Test-win64\chrome.exe"

    # Реализовал установку языка браузера через аргумент lang
    options.add_argument(f'--lang={language}')


    browser = webdriver.Chrome(service=Service(), options=options)


    yield browser
    print("\nquit browser..")
    browser.quit()
