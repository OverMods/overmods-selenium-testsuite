from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
link = 'http://localhost/overmods/'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

time.sleep(3)
browser.find_element(By.CSS_SELECTOR, '.login span').click()

login_form = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'overmodsLogin_username')))
login_form.send_keys('Magic')

password_input = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'overmodsLogin_password')))
password_input.send_keys('kolpol9080')
time.sleep(5)
password_input.send_keys(Keys.RETURN)

time.sleep(10)
browser.quit()