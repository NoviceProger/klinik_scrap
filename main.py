import time, random

# # 1 requests
# url = "https://www.barmer-kliniksuche.de/suche/suchergebnis.php?searchdata%5Bplzort%5D=Berlin&searchdata%5Blocation%5D=6701%7CAGS&searchdata%5Bmaxdistance%5D=bundesweit&searchcontrol%5Border%5D=distance&searchcontrol%5Blimit_offset%5D=50&searchcontrol%5Blimit_num%5D=50"
ortkode = "52074"
text_url = f"https://www.barmer-kliniksuche.de/suche/suchergebnis.php?searchcontrol%5Border%5D=distance&searchdata%5Bautocomplete%5D=&searchdata%5Bplzort%5D={ortkode}&searchdata%5Blocation%5D=&searchdata%5Bmaxdistance%5D=0"
# headers = {
# 	"Accept":"*/*",
# 	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
# }
#
# k = 1
# req = requests.get(url, headers=headers)
# time.sleep(5)
# source_html = req.text

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time
# import pyautogui	#pip install PyAutoGUI

options = Options()
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
# options.add_argument('user-agent={0}'.format(user_agent))
# accept_language = "en-US,en;q=0.9"
# options.add_argument('accept-language={0}'.format(accept_language))
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36")
# options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path="D:/My_PyCharm/Programs for python/Chromedriver/chromedriver.exe",
						  options=options
)
wait = WebDriverWait(driver, 20)
# action = ActionChains(driver)
hhh = driver.get(text_url)
time.sleep(5)
source_html = driver.page_source
#
# # запис в ХТМЛ-файл
# with open(f"HTML/index1.html", 'w', encoding='utf-8') as file:
# 	file.write(source_html)
# # for i in range(4):
# # 	# pyautogui.moveRel(100, 0, duration=0.25)
# # 	pyautogui.moveRel(0, 100, duration=0.25)
# # 	# pyautogui.moveRel(-100, 0, duration=0.25)
# # 	pyautogui.moveRel(0, -100, duration=0.25)
# # find_button = '//*[@id="maincontent"]/main/div/div[3]/div[3]/nav/ul/li[3]/button'
# # driver.find_element(By.XPATH, find_button).click()
# # time.sleep(random.randint(2, 5))
#
driver.close()

from bs4 import BeautifulSoup
import json

result = []
# HTMLFile = open(f"HTML/index1.html", "r", encoding='utf-8')
# Reading the file
# index = HTMLFile.read()
soup = BeautifulSoup(source_html, 'lxml')
# 5 пошук потрібних значень
# soup = BeautifulSoup(index, 'lxml')
url_fin = soup.find('tbody', id='search_result_table_body')
url_next = url_fin.find_all('tr')
# print(url_next)
# rep = 0
for item_list in url_next:
	# rep += 1
	# print(rep)
	# items_icons = item_list.find('small', class_='hospital-icons')
	items = item_list.find_all('div')
	# print(items)
	# for item in items:
		# item_text = item.find_all('div', class_='main-link').find('a').text.strip()
		# if item_text == "":
		# 	print('Pusto')
		# 	continue
		# else:
		# 	print(item_text)
		# find_url = item.find('div', class_='main-link').find('a').get('href')
		# print(find_url)
		# if str(find_url).startswith('http'):
		# item_url = find_url
		# else:
		# 	item_url = f"https://www.bringfido.com{find_url}"
		# item_url = item.find('a',class_='propertyTile__priceLink')#.get('href')
		# print(item_url)
		# print(f"name: {item_text} url: https://www.bringfido.com{item_url}")
		# item_policy = item.find_all('div')
		# print(item)
		# print(item_policy)
		# print(item1.text.strip())
		# if item_policy:
	policy1 = items[0].text.strip()
	find_url = items[1].find('a').get('href')
	policy2 = items[1].text.strip()
	policy3 = items[2].text.strip()
	print(f"link {find_url}| {policy1}|  name {policy2}| adress {policy3}")
		# else:
		# 	policy1 = 'None'
		# 	policy2 = 'None'
		# 	policy3 = 'None'
			# print(item_text)
		# item_location = item.find('div', class_='propertyTile__locationRow').find('a',
		# 																class_='propertyTile__location').text.strip()
		# location = str(item_location).split(',')
		# item_id = re.search('\d{4,7}',item.find(class_='propertyTile__overlay').get('id'))
		# result.append(
		# 	{
		# 		# 'type': url_item['type'],
		# 		# 'name': item_text,
		# 		# 'url': item_url,
		# 		'policy1': policy1,
		# 		'policy2': policy2,
		# 		'policy3': policy3,
		# 		# 'city': location[0],
		# 		# 'state': location[1]
		# 	}
		# )

#
# 	# find_button = '//*[@id="body"]/div[4]/div[2]/div[1]/div[1]/main/div/div[1]/div[3]/a'
# 	# # '//*[@id="resultsList"]/amp-list-load-more[1]/button'
# 	# web.find_element(By.XPATH, find_button).click()
# 	# time.sleep(random.randint(2, 5))

	# 6 запис у файл JSON
# with open(f"D:\Path\result.json", 'w', encoding='utf-8') as file:
# 	json.dump(result, file, indent=4, ensure_ascii=False)
