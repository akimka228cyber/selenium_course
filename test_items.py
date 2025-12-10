import time
from selenium.webdriver.common.by import By

# В линке убрал домен языка, чтобы корректно подтягивался язык браузера
link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    time.sleep(30)
    basket_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert basket_button.is_displayed(), "Кнопка корзины не отображается на странице"
