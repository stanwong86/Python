'''
Use this script to visit webpages by creating a url list and using selenium to loop through.
Requires chromedriver
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException, NoAlertPresentException
import time
import re
import sys
import base64
import csv
import pandas as pd

def get_unmatched_urls():
	with open('flight_data.log', 'r') as f:
		lines = f.readlines()
		lines = list(map(lambda x: re.sub(r".*EntityID': '(.*?)'.*\n", r"https://advertising.amazon.com/dsp/\g<1>/advertisers", x), lines))
		lines = list(set(lines))
		return lines

def get_unmatched_entity_urls(filename):
	with open(filename, 'r') as f:
		lines = f.read().split('\n')
		lines = list(map(lambda entity: f"https://advertising.amazon.com/dsp/{entity}/advertisers", lines))
		return lines

def parse_entity_dnes(filename):
	df = pd.read_excel(filename)
	entities = df['EntityID'].unique().tolist()
	urls = list(map(lambda entity: f"https://advertising.amazon.com/dsp/{entity}/advertisers", entities))
	return urls

def login_to_website():
	if UK_LOGIN:
		landing_page = 'https://advertising.amazon.co.uk/dsp/ENTITY136H24VGYWOIJ/line-items/593236248115953456/edit'
	else:
		landing_page = 'https://advertising.amazon.com/dsp/ENTITY2W3MXDBG96VM7/advertisers/587518818619761650/orders'
	driver.get(landing_page)
	print('Loading Landing Page')

	delay = 3
	try:
	    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'ap_email')))
	    print('Login Page is Ready!')
	except TimeoutException:
	    print("Loading took too much time!")

	wait(3) # Required

	username = driver.find_element_by_id("ap_email")
	username.send_keys(AMAZON_EMAIL)

	username = driver.find_element_by_id("ap_password")
	username.send_keys(AMAZON_PASSWORD)
	username.send_keys(Keys.RETURN)


def wait(seconds):
	print(f'Wait {seconds} seconds')
	time.sleep(seconds)


def loop_through_urls(urls):
	for i, url in enumerate(urls):
		print(f'{i} of {len(urls)}: {url}')
		click_on_url(url)

def click_on_url(url):
	delay = 5
	driver.get(url)
	new_advertiser_button_xpath = '/html/body/div[1]/section/eap-page/main/section[2]/campaign-datatable/section/article/div[1]/eap-split-dropdown/div/span/a'
	try:
	    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, new_advertiser_button_xpath)))
	    print('Found!')
	except TimeoutException:
	    print("Loading took too much time!")

	# time.sleep(15)
	# print('Wait 5 seconds')

def encode_string(text):
	b64_bytes = text.encode('ascii')
	msg_bytes = base64.b64encode(b64_bytes)
	msg = msg_bytes.decode('ascii')
	return msg

def decode_string(text):
	b64_bytes = text.encode('ascii')
	msg_bytes = base64.b64decode(b64_bytes)
	msg = msg_bytes.decode('ascii')
	return msg

# Make sure the URLs above are saved to urls variable
UK_LOGIN = False
AMAZON_EMAIL = 'sywong@amazon.com'
AMAZON_PASSWORD = ''
### CONFIG END ###


# urls = get_unmatched_urls()
# urls = get_unmatched_entity_urls('Agency_unmatched_entities.csv')
urls = parse_entity_dnes('EntityDNE.xlsx')
print('Unique URLs ', len(urls))

driver = webdriver.Chrome('/Users/sywong/chromedriver/chromedriver')

login_to_website()
loop_through_urls(urls)

print('Done')

time.sleep(10)
driver.close()