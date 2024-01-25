from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

USERNAME = "memor.first"
PASSWORD = "password"
URL =  "https://www.instagram.com/accounts/login/"


driver.get(URL)

# Locate username and password fields
username_field = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
password_field = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')))

# Enter username and password
username_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)

# Close pop-ups
login_info_saver = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]")
login_info_saver.click()

time.sleep(5)

notifications = driver.find_element(By.XPATH, "//button[contains(text(), 'Not now')]")
notifications.click()