import os
import re
import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import requests


# Get the absolute path of the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Set up the download directory within the current directory
download_dir = os.path.join(script_dir, "downloads")

# Create the downloads directory if it doesn't exist
os.makedirs(download_dir, exist_ok=True)

# Set up the WebDriver
driver_path = os.path.join(script_dir, "chromedriver")
chrome_binary_path = "/usr/bin/google-chrome"

chrome_options = ChromeOptions()
chrome_options.binary_location = chrome_binary_path
chrome_options.add_argument("--no-sandbox")
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
})

service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
print("WebDriver initialized.")

# Visit the website
driver.get('https://bilue.com.au')
print("Website loaded.")

# Wait and click on the Contact banner
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="webpage"]/div[3]/div[1]/div/div[2]/a'))
).click()
print("Clicked on Contact banner.")

greeting_text_xpath = '//*[@id="webpage"]/main/section[1]/div/div/div/h2/strong'
greeting_text_name = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, greeting_text_xpath))
).text

email_text_xpath = '//*[@id="w-node-a1641327-6a9b-164b-f9f3-9e53a8bd3695-d4602f49"]/div[2]/p[2]'
email_text_name = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, email_text_xpath))
).text

telephone_text_xpath = '//*[@id="w-node-a1641327-6a9b-164b-f9f3-9e53a8bd3695-d4602f49"]/div[1]/p[2]'
telephone_text_name = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, telephone_text_xpath))
).text

print("print greetings: "+greeting_text_name)
print("print email: "+email_text_name)
print("print telephone: "+telephone_text_name)
driver.quit()
exit()


