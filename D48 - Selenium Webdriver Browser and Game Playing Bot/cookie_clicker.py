from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open browser with detached mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the cookie clicker game
url = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(url)

# Get the cookie element
cookie = driver.find_element(By.ID, "cookie")

# Get upgrade item IDs
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
items_id = [item.get_attribute("id") for item in items]

# Set time limits
timeout = time.time() + 5
five_min = time.time() + 60 * 5  # 5 minutes

while True:
    # Click the cookie
    cookie.click()

    # Check every 5 seconds
    if time.time() > timeout:
        # Get upgrade prices
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = [int(price.text.split("-")[1].strip().replace(",", ""))
                       for price in all_prices if price.text != ""]

        # Create a dictionary of store items and prices
        cookie_upgrade = {item_prices[n]: items_id[n] for n in range(len(item_prices))}

        # Get current cookie count
        cookie_count = int(driver.find_element(By.ID, "money").text.replace(",", ""))

        # Find affordable upgrades
        affordable_upgrades = {cost: id for cost, id in cookie_upgrade.items() if cookie_count > cost}

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
        driver.find_element(By.ID, to_purchase_id).click()

        # Set the next check time
        timeout = time.time() + 5

    # After 5 minutes, stop the bot and print cookies per second count
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break
