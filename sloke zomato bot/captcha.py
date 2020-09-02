# pip install selenium
# find and install browser version specific webdrivers

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import zipfile
import os

chromedriverPath = "C:\\Users\\Rajdeep\\Desktop\\chromedriver.exe"
pdfDirectory = "C:\\Users\\Rajdeep\\Documents\\Python Code\\sloke zomato bot\\sourcepdfs\\"
downloadsDirectory = "C:\\Users\\Rajdeep\\Downloads\\"
imagesDirectory = "C:\\Users\\Rajdeep\\Documents\\Python Code\\sloke zomato bot\\extractedimages\\"

chrome_options = Options()  
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(executable_path=chromedriverPath)#, options=chrome_options)

driver.get("https://www.google.com/recaptcha/api2/demo")

sleep(4)

driver.find_element(By.XPATH, '//div[@class="recaptcha-checkbox-checkmark"]').click()
    
driver.close()
