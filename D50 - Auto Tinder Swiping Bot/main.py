from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time
import random

# Credentials
EMAIL = "hamidullo287@gmail.com"
PASSWORD = "f@c3800K_@uth"

# Optional - to make sure that chrome stays opened
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
URL = "https://tinder.com"
driver.get(URL)

# Accept cookies
allow_cookies_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="q-1145712231"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')))
allow_cookies_button.click()

# Locate the login button
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="q-1145712231"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')))
login_button.click()
time.sleep(1)
facebook_login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div')))
facebook_login_button.click()

# Login to facebook
time.sleep(1)
# Get the current window handle
main_window = driver.window_handles[0]

# Switch to the new window
new_window = driver.window_handles[1]
driver.switch_to.window(new_window)

email_input = driver.find_element(By.XPATH, '//*[@id="email"]')
email_input.send_keys(EMAIL)
password_input = driver.find_element(By.XPATH, '//*[@id="pass"]')
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)

# After logging in, switch back to the main window
driver.switch_to.window(main_window)

# Wait for the "Allow Location" button to be clickable
allow_location_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="q-924371795"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')))
allow_location_button.click()

# Wait for the "Disable Notifications" button to be clickable
notifications_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="q-924371795"]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')))
notifications_button.click()

# Click on the dislike button for 10 times
time.sleep(5)
for n in range(10):
    try: 
        print("Disliking profile")
        driver.find_element(By.XPATH, '//body').send_keys(Keys.ARROW_LEFT)
        time.sleep(random.uniform(1, 2)) # Add a random delay between 1 and 2 seconds

    except ElementClickInterceptedException:
        match_popup = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".isAMatch a")))
        match_popup.click()


driver.quit()