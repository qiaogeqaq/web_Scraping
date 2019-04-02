import requests
import bs4


url = "http://tower.im/roadmap"

response = requests.get(url)

status_code = response.status_code 

content = bs4.BeautifulSoup(response.content.decode("utf-8"),"lxml")
element = content.find_all('tr')


print(status_code)
print(element)

