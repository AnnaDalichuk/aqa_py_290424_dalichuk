# EXplicit for EXpected
# IMplicit for IMaginary
from selenium.webdriver.common.by import By

def test_example_with_implicit_wait(driver):
    driver.implicitly_wait(10) # Чекати не більше 10 секунд
    driver.get("https://www.example.com")
    # Знаходимо елемент на сторінці
    heading = driver.find_element(By.TAG_NAME, "h1")
    # Перевіряємо, чи вірний текст заголовку
    assert heading.text == "Example Domain"
