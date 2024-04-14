import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By

# Set up the WebDriver (replace with your Chrome driver's path)


options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=/home/alok/.config/google-chrome")
options.add_argument(r"--profile-directory=Profile 7")
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

# # Open ChatGPT
driver.get("https://chat.openai.com")
sleep(5)


# print('----------------------------------- open chatgpt -----------------------------------')

sleep(5)
print('----------------------------------- driver -----------------------------------')
# Find the chatbox 
chatbox = driver.find_elements(By.TAG_NAME, "textarea")
print("got text area")

print('----------------------------------- chatbox -----------------------------------')

chatbox[0].send_keys("Hello, I am a bot!")
chatbox[0].send_keys(Keys.ENTER)

sleep(5)

inputElements = driver.find_elements(By.TAG_NAME, "p")
sleep(5)
results = []
for element in inputElements:
   results.append(element.text)
print(results)