from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Firefox()


print("Set window size")
browser.set_window_size(1280,960)
browser.get('http://www.baidu.com')

above = browser.find_element_by_link_text("新闻")
ActionChains(browser).move_to_element(above).perform()



#size = browser.find_element_by_id('kw').size
#print(size)

#text = browser.find_element_by_id('cp').text
#print(text)










#browser.find_element_by_id("kw").clear()
#browser.find_element_by_id("kw").send_keys("selenium")
#browser.find_element_by_id("su").click()

time.sleep(6)


browser.close()
