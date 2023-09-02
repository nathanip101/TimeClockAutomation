from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import yaml
import sys

conf = yaml.safe_load(open('secrets.yaml'))
URL = conf['login_details']['url']
BADGE_NUMBER = conf['login_details']['badge_number']
PIN = conf['login_details']['pin']

BADGE_NUMBER_ID= "LogOnEmployeeId"
BADGE_NUMBER_SUBMIT = "//input[@value='Log On To Dashboard']"
PIN_ID = "LogOnEmployeePin"
PIN_SUBMIT = "//input[@value='Log On']"

CLOCK_IN_ID = "//input[@value='Punch In']"
CLOCK_OUT_ID = "//input[@value='Punch Out']"
START_LUNCH_ID = "//input[@value='Start Meal Period]"
END_LUNCH_ID = "//input[@value='End Meal Period]"
CLOCK_SUBMIT = "//input[@value='Continue']"
OK = "//input[@value='Ok']"

ACTION_DICT = {
        "in": CLOCK_IN_ID,
        "out": CLOCK_OUT_ID,
        "hungry": START_LUNCH_ID,
        "full": END_LUNCH_ID
}

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

def log(action):
        driver.get(url=URL)
        
        wait = WebDriverWait(driver, 10)

        badge_number_element = wait.until(EC.presence_of_element_located((By.ID, BADGE_NUMBER_ID)))
        badge_number_element = wait.until(EC.visibility_of_element_located((By.ID, BADGE_NUMBER_ID)))
        badge_number_element = wait.until(EC.element_to_be_clickable((By.ID, BADGE_NUMBER_ID)))
        badge_number_element.send_keys(BADGE_NUMBER)

        badge_submit_element = wait.until(EC.element_to_be_clickable((By.XPATH, BADGE_NUMBER_SUBMIT)))
        badge_submit_element.click()

        action_element = wait.until(EC.presence_of_element_located((By.XPATH, action)))
        action_element = wait.until(EC.visibility_of_element_located((By.XPATH, action)))
        action_element = wait.until(EC.element_to_be_clickable((By.XPATH, action)))
        action_element.click()

        submit_element = wait.until(EC.element_to_be_clickable((By.XPATH, CLOCK_SUBMIT)))
        submit_element.click()

        ok_element = wait.until(EC.element_to_be_clickable((By.XPATH, OK)))
        ok_element.click()

if __name__ == "__main__":
        log(ACTION_DICT.get(sys.argv[1]))