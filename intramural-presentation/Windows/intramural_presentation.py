from pymsgbox import prompt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# Load login
driver = webdriver.Chrome()
driver.maximize_window()
url = prompt(title="URL to Presentation",
             text="Enter url for presentation if not doing default presentation for all participants",
             default="https://canvas.vt.edu/courses/36155/assignments/80298")
driver.get(url)

# Wait for user to log in
grades_button = None
while not grades_button:
    try:
        grades_button = driver.find_element_by_class_name("grades")
    except Exception as err:
        sleep(1)
action = webdriver.common.action_chains.ActionChains(driver)

switch = 1
while True:
    switch *= -1
    # Click to either A or B
    action.move_to_element_with_offset(grades_button, 300, 287 + 12*switch)
    action.click()
    action.perform()
    sleep(0.5)
    # Click submit
    action.move_to_element_with_offset(grades_button, 872, 527)
    action.click()
    action.perform()
    sleep(0.5)
