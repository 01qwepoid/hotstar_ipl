from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common import action_chains
#import time
#import bs4
#import requests
#import webbrowser
#from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
#import pandas as pd

#while(1):
url = "https://www.hotstar.com/sports/cricket/vivo-ipl-2018/mumbai-indians-vs-kolkata-knight-riders-m186538/live-streaming/2001706016"
driver = webdriver.Chrome() #opens chrome
driver.get(url) #opens the url

#driver.find_element_by_xpath("[@id='my_video_1']/div[4]/button[1]").click()
ActionChains(driver).key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB).perform()
#//button[@title='Play Video']
#	time.sleep(275)
	
#driver.set_page_load_timeout(30) #if not loaded, closes after the given time
#assert 'Google' in driver.title #check if right page is loaded
#driver.close()

