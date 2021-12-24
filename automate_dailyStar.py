from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('https://www.thedailystar.net/')
driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element_by_link_text('e-paper').click()

for i in range(5):
    driver.execute_script ("window.scrollTo(0,100);")
    time.sleep(3)
    driver.execute_script ("window.scrollTo(0,200);")
    time.sleep(3)
    driver.execute_script ("window.scrollTo(0,300);")
    time.sleep(3)
    #tab controller---
    windows_before  = driver.current_window_handle
    full = driver.find_element_by_id('lblFulView')
    full.click()
    windows_after = driver.window_handles
    new_window = [x for x in windows_after if x != windows_before][0]
    driver.switch_to.window(new_window)
    for i in range(3):
        driver.execute_script ("window.scrollTo(0,150);")
        time.sleep(3)
        driver.execute_script ("window.scrollTo(0,300);")
        time.sleep(3)
        driver.execute_script ("window.scrollTo(0,400);")
        time.sleep(3)
        driver.execute_script ("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(3)
        # driver.execute_script("")
        lastfull = driver.find_element_by_xpath('//*[@id="nextArticle"]/i')
        if full==lastfull:
            break
        lastfull.click()
        full = lastfull
        
    driver.close()
    driver.switch_to.window(windows_before)
    driver.find_element_by_xpath('//*[@id="nextPage"]/i').click()
#---


