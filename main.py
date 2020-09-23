from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#import os
from PIL import Image
import time
from PIL import Image 
import os
import smtplib
from time import sleep
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from fake_useragent import UserAgent
chrome_options = Options()

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
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
gmail_id="aman765180"
gmail_password ="Neesu@1234"
driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')  # signing in to google through stack overflow
sleep(2)
driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()  # signing in with google
driver.find_element_by_xpath('//input[@type="email"]').send_keys(gmail_id)  # entering the gmail id
driver.find_element_by_xpath('').click()
driver.find_element_by_xpath('//*[@jscontroller="soHxf"]').click()
#sleep(2)
#driver.find_element_by_xpath('//input[@type="password"]').send_keys(gmail_password)  # entering the password
#driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
#sleep(2)
print('Login Successful...!!')
#driver.implicitly_wait(50)
#driver.get('https://meet.google.com/hmk-urey-myq')
#sleep(5)

driver.save_screenshot("image.png")
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
  s.login('aman765180@gmail.com', 'Neesu@1234')
  s.sendmail('aman765180@gmail.com','abhishek7071631646@gmail.com' , msg.as_string())
  s.quit()
  
send_mail()
#time.sleep(3600)
