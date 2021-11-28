from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import Select
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
print(file_path)
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    butt = browser.find_element_by_class_name('btn').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    num = browser.find_element_by_id('input_value').text
    ans = browser.find_element_by_id('answer').send_keys(calc(num))
    time.sleep(2)
    butt1 = browser.find_element_by_class_name('btn')
    butt1.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()