from selenium import webdriver
import time


driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

# 获得百度搜索窗口句柄
search_windows = driver.current_window_handle

time.sleep(2)

#driver.find_element_by_link_text('登录').click() #error
#driver.find_element_by_name('tj_login')
#某些情况元素的visibility为hidden或者display属性为none，我们在页面看不到但是实际是存在页面的一些元素，这时候用 #is_displayed（） 来判断
#elem =  driver.find_element_by_name('tj_login')

driver.find_element_by_xpath('//div[@id="u1"]/a[7]').click()

time.sleep(2)

driver.find_element_by_link_text("立即注册").click()

time.sleep(2)
# 获得当前所有打开的窗口的句柄
all_handles = driver.window_handles

for handle in all_handles:
    if handle != search_windows:
        print("now register window")
        driver.find_element_by_name('userName').send_keys('username121312')
	#is not reachable by keyboard
        driver.find_element_by_name('password').send_keys('password23124')
        time.sleep(3)

driver.close()
