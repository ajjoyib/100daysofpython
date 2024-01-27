import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

def get_zillow_data():
    # Zillow link
    zillow_link = "https://appbrewery.github.io/Zillow-Clone/"
    response = requests.get(zillow_link)
    response.raise_for_status()
    website_html = response.text

    # Parse HTML using BeautifulSoup
    soup = BeautifulSoup(website_html, "html.parser")

    # Extract links
    link_elements = soup.find_all(name="a", class_="property-card-link")
    links = [element["href"] for element in link_elements]

    # Extract prices
    all_prices_elements = soup.select(".PropertyCardWrapper span")
    prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_prices_elements if "$" in price.text]

    # Extract addresses
    address_elements = soup.find_all(name="address")
    addresses = [address.text.strip().replace("\n", "").replace("|", "") for address in address_elements]

    # Combine three lists into a dictionary
    property_data = [{"address": address, "price": price, "link": link} for address, price, link in zip(addresses, prices, links)]

    return property_data


def fill_survey_form(property_data, survey_link):
    # Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    for data in property_data:
        driver.get(survey_link)

        # Fill out the form
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'))).send_keys(data["address"])
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'))).send_keys(data["price"])
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'))).send_keys(data["link"])
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'))).click()


if __name__ == "__main__":
    survey_link = "https://forms.gle/Mq1x4gLFRWjZ1yWy9"
    property_data = get_zillow_data()
    fill_survey_form(property_data, survey_link)