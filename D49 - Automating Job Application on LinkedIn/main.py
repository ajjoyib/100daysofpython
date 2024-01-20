from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from src import *
import time

def abort_application():
    """
    Handle application abortion by closing the modal.
    """
    try:
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()
        time.sleep(2)
        discard_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
        discard_button.click()
    except NoSuchElementException:
        pass

# Set up Chrome options for the webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize the webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Sign in
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[4]/a[1]').click()
time.sleep(1)
driver.find_element(By.ID, "username").send_keys(USERNAME)
driver.find_element(By.ID, "password").send_keys(PASSWORD)
driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()

# Get job listings
time.sleep(3)
all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

# Apply to all listings
for listing in all_listings:
    print("Opening Listing...")
    listing.click()
    time.sleep(2)
    try:
        # Click the apply button
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()

        # Insert phone number if not provided
        time.sleep(2)
        phone = driver.find_element(By.CSS_SELECTOR, "input[id*=phoneNumber]")
        if not phone.text:
            phone.send_keys(PHONE)

        # Check the Submit Button
        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipping.")
            continue
        else:
            # Click the Submit Button
            submit_button.click()

        time.sleep(2)
        # Click Close button
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipping.")

# Quit the webdriver
time.sleep(2)
driver.quit()
