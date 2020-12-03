#!/bin/bash

from selenium.webdriver import Chrome

# from selenium.webdriver.support.ui import Select
# from requests_html import HTMLSession, AsyncHTMLSession
# import time

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

    # SELECT 'Start an Order'

    # Wait for Blantons to become available

    # Select add to order

    # Select Place Order

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


if __name__ == '__main__':
    main()
