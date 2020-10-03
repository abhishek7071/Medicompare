from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#import os
#driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from PIL import Image
from bs4 import BeautifulSoup
import time
from PIL import Image 
import os
import smtplib
from time import sleep
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
chrome_options = Options()

options = Options()
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
#chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"')
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
gmail_id="aman765180@gmail.com"
gmail_name="attendance"
gmail_pass="Neesu@12345"
#driver.get('https://globalpage-prod.webex.com/signin?surl=https%3A%2F%2Fsignin.webex.com%2Fcollabs%2Fauth%3Fservice%3Dit%26from%3Dhostmeeting%26TrackID%3D%26hbxref%3D%26goid%3Dhost-meeting')
#time.sleep(8)

#driver.find_element_by_xpath('//*[@id="smartJoinButton"]').click()
#time.sleep(5)
#driver.find_element_by_xpath('//input[@type="text"]').send_keys(gmail_id)
#time.sleep(5)
#driver.find_element_by_xpath("//span[contains(.,'Next')]").click()
#driver.find_element_by_xpath('').click()
#time.sleep(4)
#driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys(gmail_pass)
#time.sleep(3)
#driver.find_element_by_xpath('//span[contains(.,"Next")]').click()
#time.Sleep(5)
#driver.execute_script("window.open('');")
#driver.switch_to.window(driver.window_handles[1])
#driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
#driver.get('https://meetingsapac49.webex.com/webappng/sites/meetingsapac49/meeting/download/ec5004db3c532924b8b2875860bfa864?launchApp=true&correlationId=84877e51-f66a-4210-bdcd-46fc1af77683')
#driver.find_element_by_xpath('//*[@id="smartJoinButton"]').click()
#time.sleep(5)
#print(driver.page_source)
#f=open("a.txt","w+")
#f.write(driver.page_source)
#driver.find_element_by_xpath("//button[@title='Join meeting']").click()
#time.sleep(3)
#driver.get('https://globalpage-prod.webex.com/signin?surl=https%3A%2F%2Fsignin.webex.com%2Fcollabs%2Fauth%3F')
#time.sleep(3)
#driver.find_element_by_xpath('//*[@id="smartJoinButton"]').click()
#driver.find_element_by_xpath('//input[@type="text"]').send_keys(gmail_id)
#time.sleep(3)
#driver.find_element_by_xpath('//button[@class="el-button next el-button--primary"]').click()
#time.sleep(3)
#driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')  # signing in to google through stack overflow
#sleep(2)
#driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()  # signing in with google
#time.sleep(3)
#driver.find_element_by_xpath('//input[@type="email"]').send_keys(gmail_id)  # entering the gmail id
#time.sleep(5)
#driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
#sleep(5)
#driver.find_element_by_xpath('//input[@type="password"]').send_keys(gmail_pass)
#driver.find_element_by_xpath('//input[@type="password"]').send_keys(gmail_pass)
# entering the password
#driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
#time.sleep(8)
#driver.save_screenshot("imageo.png")
#driver.get("https://meet.google.com/usm-foaw-dgu")
driver.get("https://meetingsapac49.webex.com/meet/pr1653564050")
time.sleep(2)
#pyautogui.click(100, 100)
#elems = driver.find_elements_by_xpath("//a[@href]")
#for elem in elems:
#  print(elem.get_attribute("href"))
driver.find_element_by_xpath('//*[@id="smartJoinButton"]').click()
time.sleep(2)
#print( (driver.page_source).encode('utf-8') )
#print(driver.page_source)
#driver.switch_to.frame(driver.find_element_by_id("pb_i"))
driver.switch_to.frame("pbui_iframe")
#time.sleep(3)
driver.find_element_by_xpath('//input[@type="text"]').send_keys(gmail_name)
driver.find_element_by_xpath("//input[@placeholder='Email address']").send_keys(gmail_id)
driver.find_element_by_xpath("//button[@title='Next']").click()
time.sleep(3)
driver.find_element_by_xpath("//button[@title='Got it']").click()
time.sleep(2)

#f.write(driver.page_source)

#WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@id='pb_iframecontainer' and @name='TargetContent']")))

driver.find_element_by_xpath('//*[@id="interstitial_join_btn"]').click()
time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html)
for my_tag in soup.find_all(class_="styles-user-name-gpTpQ"):
  print(my_tag.text)
attend=my_tag.text
#price=soup.find_all("div" , {"class":"styles-user-name-"}).text
#print(price)
#tree=driver.find_elements_by_xpath("//*[@id='meetsimple']")
#print(tree.text) 
#or i in tree:
#   print(i.text)simple
#//div[contains(@class, ' plist-userListView-2b_DW')
#div[contains(@class,'plist-userListView-2b_DW')]#f = open("a.txt", "w+")
#//div[contains(@class,'plist-userListView-2b_DW')]simple
f= open("a.txt","w+")
f.write(attend)

#wait = WebDriverWait(driver, 20)
#wait.until(EC.presence_of_element_located((By.ID, "identifierNext"))).click()
#driver.find_element_by_xpath(

#input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierNext"]/span/span')))
#input.click()
#time.sleep(3)
#driver.find_element_by_xpath('//*[@id="next"]').click()
#sleep(2)
#driver.find_element_by_xpath('//input[@type="submit"]').send_keys(gmail_password)  # entering the password
#time.sleep(3)
#driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
#sleep(2)
#print('Login Successful...!!')
#driver.implicitly_wait(50)
#driver.get('https://meet.google.com/tou-bpxg-tvh')
#time.sleep(5)

driver.save_screenshot("image.png")
#image = Image.open("image.png") 

  
# Showing the iamge 
#mage.show() 
def send_mail():
  img_data = open('image.png','rb').read()
  msg = MIMEMultipart()
  msg['Subject'] = 'subject'
  msg['From'] = 'aman765180@gmail.com'
  msg['To'] = 'abhishek7071631646@gmail.com'
  filename = "a.txt"
  f = open(filename)
  attachment = MIMEText(f.read())
  attachment.add_header('Content-Disposition', 'attachment', filename=filename)           
  msg.attach(attachment)
  text = MIMEText("test")
  msg.attach(text)
  image = MIMEImage(img_data,'png')
  msg.attach(image)
  s = smtplib.SMTP('smtp.gmail.com',587)
  s.ehlo()
  s.starttls()
  s.ehlo()
  s.login('aman765180@gmail.com', 'Neesu@12345')
  s.sendmail('aman765180@gmail.com','abhishek7071631646@gmail.com' , msg.as_string())
  s.quit()
  
send_mail()
#time.sleep(3600)
