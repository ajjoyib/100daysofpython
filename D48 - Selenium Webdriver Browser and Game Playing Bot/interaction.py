from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

url = "https://www.linkedin.com/login"
email = "hamidullo287@gmail.com"
password = "20@lfraganuS04"

driver = webdriver.Chrome(chrome_options)
driver.get(url)

email_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")

# email_input.send_keys(email, Keys.TAB)
email_input.send_keys(email)
password_input.send_keys(password, Keys.ENTER)



