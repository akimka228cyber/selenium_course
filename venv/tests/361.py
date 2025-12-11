import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest

@pytest.mark.parametrize('link1', ["https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"
                                      ])
def test_reg1(link1):
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.binary_location = r"D:\Chrome-for-Test-win64\chrome.exe"

    driver = webdriver.Chrome(service=Service(), options=options)
    try:
        driver.get(link1)
        time.sleep(3)

        loginButton = driver.find_element(By.ID, "ember496")
        time.sleep(0.5)
        loginButton.click()

        email = driver.find_element(By.ID, "id_login_email")
        email.send_keys("akimhtcnew@gmail.com")
        time.sleep(1)

        passw = driver.find_element(By.ID, "id_login_password")
        passw.send_keys("NfyzNegfz123")
        time.sleep(1)

        butt = driver.find_element(By.CLASS_NAME, "sign-form__btn")
        butt.click()

        time.sleep(3)

        answer = math.log(int(time.time()))

        input2 = driver.find_element(By.CSS_SELECTOR,
                                     "textarea[required][placeholder='Напишите ваш ответ здесь...']")
        time.sleep(1)
        input2.send_keys(answer)

        butts = driver.find_element(By.CLASS_NAME, "submit-submission")
        butts.click()

        time.sleep(1)

        ans = driver.find_element(By.CLASS_NAME, "smart-hints__hint")
        ans_text = ans.text

        assert "Correct!" == ans_text, "Сравниваем тексты"

        time.sleep(2)
        againbutt = driver.find_element(By.CLASS_NAME, "again-btn")
        againbutt.click()
        time.sleep(2)

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        driver.quit()