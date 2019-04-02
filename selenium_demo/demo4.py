from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep



driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

above = driver.find_element_by_xpath('//div[@id="u1"]/a[8]')
ActionChains(driver).move_to_element(above).perform()
sleep(1)

driver.find_element_by_link_text("搜索设置").click()
sleep(2)

sel = driver.find_element_by_xpath("//select[@id='nr']")
Select(sel).select_by_value("50")

driver.quit()
