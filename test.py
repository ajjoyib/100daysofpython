from keys import *
import speedtest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PROMISED_DOWN = 95
PROMISED_UP = 100
# CHROME_DRIVER_PATH = "\Users\hamid\Development\chromedriver"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.st = speedtest.Speedtest()

    def get_internet_speed(self):
        """
        Get the internet speed from fast.com
        """
        self.driver.get("https://www.fast.com")  # Open fast.com
        WebDriverWait(self.driver, 200).until(EC.element_to_be_clickable((By.LINK_TEXT, "Show more info"))).click()  # Click on "Show more info"
        download_speed = WebDriverWait(self.driver, 200).until(EC.element_to_be_clickable((By.ID, "speed-value"))).text  # Get download speed
        time.sleep(25)  # Wait for 10 seconds
        upload_speed = WebDriverWait(self.driver, 200).until(EC.element_to_be_clickable((By.ID, "upload-value"))).text  # Get upload speed
        return [download_speed, upload_speed]  # Return a list of download and upload speed
        
  
    def tweet_at_provider(self):
        self.driver.get("https://www.twitter.com")


twitter_bot = InternetSpeedTwitterBot()

# results = twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()