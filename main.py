from selenium import webdriver
import os
from PIL import Image

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
driver.get("https://www.google.com/")
driver.get_screenshot_as_file("screenshot.png")
driver.implicitly_wait(50)

image.show() 

driver.get_screenshot_as_file("screenshot.png")
image = Image.open("image.png") 


print(driver.page_source)

