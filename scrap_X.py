# pip install selenium pandas openpyxl

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

from dotenv import load_dotenv
load_dotenv()

import os
import openpyxl

options = Options()
# disable save password popup
prefs = {"credentials_enable_service": False,
         "profile.password_manager_enabled": False}
options.add_experimental_option("prefs", prefs)
# end

options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("window_size=1280,800")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-save-password-bubble")


def save_to_excel(data, filename):
    if os.path.exists(filename):
        df_existing = pd.read_excel(filename, engine='openpyxl')
        df_new = pd.DataFrame(data, columns=["Tweets"])
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        df_combined.to_excel(filename, index=False, engine='openpyxl')
    else:
        df = pd.DataFrame(data, columns=["Tweets"])
        df.to_excel(filename, index=False, engine='openpyxl')


# open chrome
driver = webdriver.Chrome(options=options)
driver.get('chrome://settings/')
driver.execute_script('chrome.settingsPrivate.setDefaultZoom(.8);')
driver.get("https://x.com")
driver.maximize_window()
time.sleep(3)

# log in
driver.find_element(By.XPATH,
                    "//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[3]/a/div/span/span").click()
time.sleep(3)

x_username = os.environ["x_username"]
username = driver.find_element(By.XPATH,
                               "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div["
                               "2]/div/div/div/div[4]/label/div/div[2]/div/input")
username.send_keys(x_username)

next_button = driver.find_element(By.XPATH,
                                  "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div["
                                  "2]/div/div/div/button[2]/div")
next_button.click()

# input password
time.sleep(3)

pwd_text = os.environ["password"]
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys(pwd_text)

log_in = driver.find_element(By.XPATH, "//span[contains(text(),'Log in')]")
log_in.click()

# close X button
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='layers']/div/div[1]/div/div/div/button").click()

# close cookies button
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div[2]/button[2]/div").click()

hashtags_keywords = [ "bitcoin BTC"]
# hashtags_keywords.reverse()
# hashtags_keywords = [ "eur", "ngn"]
# hashtags_keywords = ['$eth ethereum']
# hashtags_keywords = ['$btc bitcoin']
language = " lang:en"  # language filter

# list to save into
unique_texts = []
seen_texts = set()

# enter search button
time.sleep(2)

for hashtag in hashtags_keywords:

    driver.get("https://x.com/explore")
    time.sleep(7)
    search = driver.find_element(By.XPATH,
                                 "//input[@placeholder='Search']")
    search.send_keys(hashtag + language)
    search.send_keys(Keys.ENTER)

    time.sleep(4)

    actions = ActionChains(driver)

    previous_num_unique = 0
    while True:
        # Scroll 10 times
        for _ in range(10):
            actions.send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(3)  # Giving the page some time to load new content

        # Fetch tweet data
        t_data = driver.find_elements(By.XPATH, ".//div[@data-testid='tweetText']")

        # Store in set
        for i in t_data:
            try:
                tweet_text = i.text
                if tweet_text not in seen_texts:
                    unique_texts.append(tweet_text)
                    seen_texts.add(tweet_text)
            except StaleElementReferenceException:
                # If a stale element exception occurs, break out of the loop
                # and re-fetch the tweets
                break

        if len(unique_texts) == previous_num_unique:
            break

        previous_num_unique = len(unique_texts)

        # for text in unique_texts:
        #     print(text)

        print(len(unique_texts))
        # Save the tweets to the Excel file after processing each hashtag
    save_to_excel(list(unique_texts), "Data/Testv1/tweet_Dec_2024_{}.xlsx".format(hashtag))
