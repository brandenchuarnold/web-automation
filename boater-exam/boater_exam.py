from pymsgbox import password as prompt_password, prompt as prompt_username
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = prompt_username(text='Enter email address', title='User Email Address')
password = prompt_password(text='Enter your password', title='User Password', mask='*')

# Website logon page
driver = webdriver.Firefox()
driver.get("https://cde.boaterexam.com/logon")
time.sleep(1)

# Input username
input_username = driver.find_element_by_id("UserName")
input_username.send_keys(username)
# Input password
input_password = driver.find_element_by_id("Password")
input_password.send_keys(password)
# Press Enter
input_password.send_keys(Keys.ENTER)
time.sleep(1)

# Press "Study the next Chapter"
input_next_chapter = driver.find_element_by_id("ctl01_MainContent_Button-Study")
input_next_chapter.click()
time.sleep(1)

base_url = 'http://cde.boaterexam.com/washington/study'
quiz_url = 'http://cde.boaterexam.com/washington/dashboard'

try:
    while True:
        # Next page url
        next_url = base_url + str(driver.execute_script('return GetNextPageUrl()'))
        # Number of seconds in this chapter
        num_seconds = int(driver.execute_script('return GetTimeRemaining()'))
        time.sleep(num_seconds + 1)
        # Gets the next page
        driver.get(next_url)
except Exception as err:
    # Next page is now the home page
    driver.get(quiz_url)
    # Click "Start Quiz"
    quiz_button = driver.find_element_by_id("Button-TakeQuiz")
    quiz_button.click()
