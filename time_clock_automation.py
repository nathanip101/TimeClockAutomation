from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import yaml
import sys

BADGE_NUMBER_ID= "LogOnEmployeeId"
BADGE_NUMBER_SUBMIT_XPATH = "//input[@value='Log On To Dashboard']"
PIN_ID = "LogOnEmployeePin"
PIN_SUBMIT_XPATH = "//input[@value='Log On']"

CLOCK_IN_XPATH = "//input[@value='Punch In']"
CLOCK_OUT_XPATH= "//input[@value='Punch Out']"
START_MEAL_XPATH = "//input[@value='Start Meal Period]"
END_MEAL_XPATH = "//input[@value='End Meal Period]"
CONTINUE_XPATH = "//input[@value='Continue']"
CANCEL_XPATH = "//input[@value='Cancel']"
OK_XPATH = "//input[@value='Ok']"
INIT = "init"

ACTION_DICT = {
    "in": CLOCK_IN_XPATH,
    "out": CLOCK_OUT_XPATH,
    "hungry": START_MEAL_XPATH,
    "full": END_MEAL_XPATH,
}

def create_secret():
    secrets_dict = {"login_details": {}}
    secrets_dict["login_details"]["url"] = input("Enter TCP portal URL: ")
    secrets_dict["login_details"]["badge_number"] = input("Enter TCP badge number: ")
    secrets_dict["login_details"]["pin"] = input("Enter TCP pin: ")
    with open("secrets.yaml", 'w') as file:
        yaml.dump(secrets_dict, file)

def log(action, test=False):
    try: 
        conf = yaml.safe_load(open('secrets.yaml'))
    except IOError:
        print("Error: secrets.yaml file does not exist.\nRun ./clock.sh init to create.")
        exit(-1)

    url = conf['login_details']['url']
    badge_number = conf['login_details']['badge_number']
    pin = conf['login_details']['pin']

    driver = webdriver.Chrome()
    driver.get(url=url)
    
    wait = WebDriverWait(driver, 10)

    badge_number_element = wait.until(EC.presence_of_element_located((By.ID, BADGE_NUMBER_ID)))
    badge_number_element = wait.until(EC.visibility_of_element_located((By.ID, BADGE_NUMBER_ID)))
    badge_number_element = wait.until(EC.element_to_be_clickable((By.ID, BADGE_NUMBER_ID)))
    badge_number_element.send_keys(badge_number)

    badge_submit_element = wait.until(EC.element_to_be_clickable((By.XPATH, BADGE_NUMBER_SUBMIT_XPATH)))
    badge_submit_element.click()

    # TODO Directly inject pin. Currently just selects input box to make pin input faster.
    pin_element = wait.until(EC.presence_of_element_located((By.ID, PIN_ID)))
    pin_element = wait.until(EC.visibility_of_element_located((By.ID, PIN_ID)))
    pin_element = wait.until(EC.element_to_be_clickable((By.ID, PIN_ID)))
    # driver.execute_script("arguments[0].type = 'text';", pin_element)
    pin_element.click()
    # pin_element.send_keys(pin)

    # pin_submit_element = wait.until(EC.element_to_be_clickable((By.XPATH, PIN_SUBMIT_XPATH)))
    # pin_submit_element.click() 

    action_element = wait.until(EC.presence_of_element_located((By.XPATH, action)))
    action_element = wait.until(EC.visibility_of_element_located((By.XPATH, action)))
    action_element = wait.until(EC.element_to_be_clickable((By.XPATH, action)))
    action_element.click()

    if not test:
            continue_element = wait.until(EC.element_to_be_clickable((By.XPATH, CONTINUE_XPATH)))
            continue_element.click()

            ok_element = wait.until(EC.element_to_be_clickable((By.XPATH, OK_XPATH)))
            ok_element.click()

    cancel_element = wait.until(EC.element_to_be_clickable((By.XPATH, CANCEL_XPATH)))
    cancel_element.click()


def main(argv):
    if argv[1] == INIT:
        create_secret()
    elif argv[1] in ACTION_DICT:
        log(ACTION_DICT.get(argv[1]), test=True)
    else:
            exit(-1)


if __name__ == "__main__":
    main(sys.argv)