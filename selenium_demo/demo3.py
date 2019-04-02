from selenium import webdriver
from time import sleep


driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

sleep(3)

texts = driver.find_elements_by_xpath('//div/h3/a')

for t in texts:
    print(t.text)

driver.quit()
