from selenium import webdriver

# Keep Chrome open after program finishes
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

URL = "https://www.amazon.com/Walter-Isaacson-Biography-Geniuses-Benjamin/dp/1982130423/?_encoding=UTF8&pd_rd_w=wvttL&content-id=amzn1.sym.9119971c-28e7-426d-b1df-798ac36bb5cd%3Aamzn1.symc.e5c80209-769f-4ade-a325-2eaec14b8e0e&pf_rd_p=9119971c-28e7-426d-b1df-798ac36bb5cd&pf_rd_r=MFBPG2N7Q99HG7WQC370&pd_rd_wg=XgSvy&pd_rd_r=a167295c-f8a3-4fcf-928c-c258b8f68c38&ref_=pd_gw_ci_mcx_mr_hp_atf_m"
driver = webdriver.Chrome
driver.get(URL)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_condition as EC 

element = WebDriverWait(driver, 20). until(
    EC.present_of_element_located((By.CLASS_NAME, "a-offset"))
)

price_dollar = driver.find_element(By.CLASS_NAME, "a-offset")
print(price_dollar.text)
# Closes the browser
driver.quit()



from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.amazon.com/Walter-Isaacson-Biography-Geniuses-Benjamin/dp/1982130423/?_encoding=UTF8&pd_rd_w=wvttL&content-id=amzn1.sym.9119971c-28e7-426d-b1df-798ac36bb5cd%3Aamzn1.symc.e5c80209-769f-4ade-a325-2eaec14b8e0e&pf_rd_p=9119971c-28e7-426d-b1df-798ac36bb5cd&pf_rd_r=MFBPG2N7Q99HG7WQC370&pd_rd_wg=XgSvy&pd_rd_r=a167295c-f8a3-4fcf-928c-c258b8f68c38&ref_=pd_gw_ci_mcx_mr_hp_atf_m"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)


print(driver.find_element(By.XPATH, '//*[@id="corePrice_feature_div"]/div/div/span[1]/span[2]').text)

driver.quit()