from selenium import webdriver
import time

url = "https://newprospect.ru/"
driver = webdriver.Firefox(executable_path ="geckodriver")
# driver = webdriver.Firefox()

try:
    driver.get(url = url)
    time.sleep = 5
    driver.save_screenshot('test.png')

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()