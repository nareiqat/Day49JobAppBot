import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import os
import random

load_dotenv()

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# email = os.getenv("EMAIL")
# password = os.getenv("PASSWORD")

email = "areiqat2@gmail.com"
password = "Riven123!"

print("email")


def generate_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.54 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.54 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7; rv:89.0) Gecko/20100101 Firefox/89.0",
        # Add more user agents as needed
    ]

    return random.choice(user_agents)


# Example of how to use the generated user agent
user_agent = generate_user_agent()

headers = {
    "User-Agent": user_agent,
    "Accept-Language": "en-US,en;q=0.5",
    # Add more headers as needed
}

chrome_options.add_argument(f"user-agent={headers['User-Agent']}")
chrome_options.add_argument(f"accept-language={headers['Accept-Language']}")

driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=3777006090&f_AL=true&geoId=103644278&keywords=front%20end"
    "%20developer&location=United%20States&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")


time.sleep(5)
sign_in_button = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign_in_button.click()

time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(email)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(password)
password_field.send_keys(Keys.ENTER)

list_of_jobs = driver.find_elements(by=By.CLASS_NAME, value="job-card-container--clickable")
for listing in list_of_jobs:
    print("called")
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".job-s-apply button")
        apply_button.click()
        time.sleep(2)
        next_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if next_button.get_attribute("data-control-name") == "contiune_unify":
            next_button.click()
        else:
            close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element(by=By.XPATH, value="//button[contains(@class, 'artdeco-button')]//*["
                                                                    "contains(., 'Discard')]/..")
            discard_button.click()
            print("Complex application, skipped..")
            continue

        time.sleep(2)
        review_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-button--primary")

        if review_button.get_attribute("data-control-name") == "contiune_unify":
            close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco_modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element(by=By.CLASS_NAME, value="artdeco_modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped..")
            continue
        else:
            review_button.click()
            time.sleep()
            submit_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-button--primary")
            if submit_button.get_attribute("data-control-name") == "submit_unify":
                submit_button.click()
                time.sleep(2)
                close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
                close_button.click()
            else:
                close_button = driver.find_element(by=By.CLASS_NAME,value="artdeco-modal__dismiss")
                close_button.click()
                time.sleep(2)
                discard_button = driver.find_element(by=By.CLASS_NAME, value="artdeco_modal__confirm-dialog-btn")[1]
                discard_button.click()
                print("Complex application, skipped..")
                continue
    except NoSuchElementException:
        print("No application button, skipped")
        continue




