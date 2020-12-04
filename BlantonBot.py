#!/bin/bash

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import env_variables

'''
This program opens the Blanton's website to add a product to a cart once it become available.
'''


def main() -> None:
    base_url = 'https://app.singlebarrelselect.com/'
    driver = Chrome()
    driver.get(base_url)

    login(driver)
    start_order(driver)
    buy_when_clickable(driver)

    input()

    driver.quit()


def login(driver) -> None:
    user = driver.find_element_by_id("AppUserEmail")
    user.send_keys(env_variables.user_name)
    password = driver.find_element_by_id("AppUserPassword")
    password.send_keys(env_variables.password)
    driver.find_element_by_class_name("submit").click()


def start_order(driver) -> None:
    driver.find_element_by_class_name("btn-primary").click()


def buy_when_clickable(driver) -> None:
    # retries every 500ms for 600 seconds the button to be clickable
    try:
        element = WebDriverWait(driver, 600).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[5]/div[1]/div/div[4]/button")))
        element.click()
    except TimeoutError as e:
        print(e)
    finally:
        print("element still unclickable")


if __name__ == '__main__':
    main()
