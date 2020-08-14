from selenium import webdriver
#import os
from PIL import Image
import time
from PIL import Image 
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from fake_useragent import UserAgent

options = Options()
ua = UserAgent()
userAgent = ua.random
print(userAgent)
options.add_argument(f'user-agent={userAgent}')
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
web = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

web.maximize_window()
web.get("https://web.whatsapp.com/")
web.implicitly_wait(50)
web.save_screenshot("image.png")
image = Image.open("image.png") 

  
# Showing the iamge 
image.show() 
def send_mail():
  img_data = open('image.png', 'rb').read()
  msg = MIMEMultipart()
  msg['Subject'] = 'subject'
  msg['From'] = 'aman765180@gmail.com'
  msg['To'] = 'abhishek7071631646@gmail.com'
  text = MIMEText("test")
  msg.attach(text)
  image = MIMEImage(img_data,'png')
  msg.attach(image)
  s = smtplib.SMTP('smtp.gmail.com',587)
  s.ehlo()
  s.starttls()
  s.ehlo()
  s.login('aman765180@gmail.com', 'Neesu@123')
  s.sendmail('aman765180@gmail.com','abhishek7071631646@gmail.com' , msg.as_string())
  s.quit()
  
send_mail()
#time.sleep(3600)
