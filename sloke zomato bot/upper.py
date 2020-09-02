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

sleep(3)
count = 0

for pr, pd, pf in os.walk(pdfDirectory):
    for pdf in pf:
        if '.pdf' in pdf:
            pdfFile = pdf

        if pdfFile in downloadsDirectory:
            os.remove(downloadsDirectory + pdfFile[:-4] + '.zip')

        driver.get("https://pdftoimage.com/")
        
        sleep(0.5)

        driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(pdfDirectory + pdfFile)

        sleep(15)

        driver.find_element(By.XPATH, '//div[@class="plupload_file_button"]').click()

        sleep(10)

        zip_ref = zipfile.ZipFile(downloadsDirectory + pdfFile[:-4] + ".zip", 'r')
        zip_ref.extractall(imagesDirectory)

        files = []
        for r, d, f in os.walk(imagesDirectory):
            for file in f:
                if '.jpg' in file:
                    files.append(file)

        for file in files:
            print(file)
            driver.get("https://www.onlineocr.net/")

            sleep(10)
            
            driver.find_element(By.XPATH, '//input[@id="fileupload"]').send_keys(imagesDirectory + file)

            sleep(5)

            driver.find_element(By.XPATH, '//option[@value="Microsoft Excel (xlsx)"]').click()
            driver.find_element(By.XPATH, '//input[@value="CONVERT"]').click()

            sleep(15)

            driver.find_element(By.XPATH, '//a[@id="MainContent_lnkBtnDownloadOutput"]').click()

        os.remove(downloadsDirectory + pdfFile[:-4] + '.zip')
        
driver.close()
