from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time

class InstaBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.USERNAME = "memor.first"
        self.PASSWORD = "password"
        self.URL =  "https://www.instagram.com/accounts/login/"

    def login(self):
        self.driver.get(self.URL)

        # Check if the cookie warning is present on the page
        decline_cookies_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]"
        cookie_warning = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, decline_cookies_xpath)))
        if cookie_warning:
            # Dismiss the cookie warning by clicking an element or button
            cookie_warning.click()

        # Locate username and password input fields
        username = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
        password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')))

        # Enter the username and password
        username.send_keys(self.USERNAME)
        password.send_keys(self.PASSWORD)

        password.send_keys(Keys.ENTER)

        time.sleep(4.3)
        # Click "Not now" and ignore Save-login info prompt
        save_login_prompt = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Not now')]")))
        if save_login_prompt:
            save_login_prompt.click()


        time.sleep(3.7)
        # Click "Not now" on notifications prompt
        notifications_prompt = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not now')]")))
        if notifications_prompt:
            notifications_prompt.click()


    # Create an object of the class
instabot001 = InstaBot()
instabot001.login()