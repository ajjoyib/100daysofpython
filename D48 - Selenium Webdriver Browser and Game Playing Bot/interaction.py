from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
url = "https://en.wikipedia.org/wiki/Main_Page" 
driver.get(url)

num_of_articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(num_of_articles.text)

driver.quit()
