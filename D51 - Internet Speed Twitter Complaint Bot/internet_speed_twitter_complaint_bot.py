import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PROMISED_DOWN = 95
PROMISED_UP = 100

class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def get_internet_speed(self):
        """
        Get the internet speed from fast.com
        """
        max_attempts = 5
        for attempt in range(1, max_attempts + 1):
            print(f"Attempting to get internet speed (Attempt {attempt}/{max_attempts})...")
            try:
                self.driver.get("https://www.fast.com")  # Open fast.com
                WebDriverWait(self.driver, 200).until(EC.element_to_be_clickable((By.LINK_TEXT, "Show more info"))).click()  # Click on "Show more info"
                download_speed = WebDriverWait(self.driver, 200).until(EC.element_to_be_clickable((By.ID, "speed-value"))).text  # Get download speed
                time.sleep(25)  # Wait for 10 seconds
                upload_speed = WebDriverWait(self.driver, 200).until(EC.element_to_be_clickable((By.ID, "upload-value"))).text  # Get upload speed
                return [download_speed, upload_speed]  # Return a list of download and upload speed
            except Exception as e:
                print(f"Error getting internet speed: {e}")
                if attempt < max_attempts:
                    print("Retrying...")
                    continue
                else:
                    print("Max attempts reached. Unable to get internet speed.")
                    return None

    def tweet_at_provider(self, data):
        self.driver.get("https://twitter.com/i/flow/login")
        self._login_to_twitter()

        # Make a tweet
        self._compose_tweet(data)
        self._post_tweet()

    def _login_to_twitter(self):
        # Enter the login details
        email_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')))
        email_input.send_keys("EMAIL")
        email_input.send_keys(Keys.ENTER)
        password_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')))
        password_input.send_keys("PASSWORD")
        password_input.send_keys(Keys.ENTER)

    def _compose_tweet(self, data):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div'))).click()
        tweet_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')))
        message = f"Hey Internet Provider, why is my internet speed is {data[0]}mbp down/{data[1]}mbs up when I pay for {PROMISED_DOWN}mbp down/{PROMISED_UP}mbs up?"
        tweet_input.send_keys(message)

    def _post_tweet(self):
        # Posting...
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/div/div/div/div/div[3]/div/div[2]/div/span/span').click()

if __name__ == "__main__":
    twitter_bot = InternetSpeedTwitterBot()
    results = twitter_bot.get_internet_speed()

    if results:
        twitter_bot.tweet_at_provider(results)
    else:
        print("Speed test failed. Unable to retrieve internet speed.")