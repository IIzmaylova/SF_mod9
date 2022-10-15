import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    # ждать все элементы в течение x секунд
    browser.implicitly_wait(12)
    # открыть страницу
    browser.get(link)
    # поиск элемента Цена
    price = browser.find_element(By.XPATH, "//h5[@id='price' and text()='$100']")
    # нажать кнопку book
    button_book = browser.find_element(By.CSS_SELECTOR, '#book')
    button_book.click()
    #считывание элемента x
    x = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = int(x.text)
    # решаем уравнение
    y = calc(x)
    # вставляем решение
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(y)
    # отправляем решение
    submit = browser.find_element(By.CSS_SELECTOR, '#solve')
    submit.click()

    time.sleep(1)

finally:
    time.sleep(20)
    browser.quit()





