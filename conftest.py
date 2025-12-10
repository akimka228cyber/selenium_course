import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose browser language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")



    options = webdriver.ChromeOptions()
    options.add_argument(f'--lang={language}')
    options.binary_location = r"D:\Chrome-for-Test-win64\chrome.exe"

    browser = webdriver.Chrome(service=Service(), options=options)


    yield browser
    print("\nquit browser..")
    browser.quit()
