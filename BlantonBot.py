#!/bin/bash

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
    #buy_blantons_when_clickable(driver)
    test_when_clickable(driver) #comment this out for production runs
    add_checkout_details(driver)

    input()  # TODO replace with a wait statement
    driver.quit()


def login(driver) -> None:
    user = driver.find_element_by_id("AppUserEmail")
    user.send_keys(env_variables.user_name)
    password = driver.find_element_by_id("AppUserPassword")
    password.send_keys(env_variables.password)
    driver.find_element_by_class_name("submit").click()


def start_order(driver) -> None:
    driver.find_element_by_class_name("btn-primary").click()


def buy_blantons_when_clickable(driver) -> None:
    # retries every 500ms for 600 seconds the button to be clickable
    try:
        element = WebDriverWait(driver, 600).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[5]/div[1]/div/div[4]/button")))
        element.click()
    except TimeoutError as e:
        print(e)
    finally:
        print("element still un-clickable")


def test_when_clickable(driver):
    # test function for buy_blantons_when_clickable; has the same functionality but for a product currently available
    #input()

    try:
        element = WebDriverWait(driver, 600).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/div/div[4]/button")))
        element.click()
    except TimeoutError as e:
        print(e)


def add_checkout_details(driver):
    driver.find_element_by_xpath('//*[@id="cart"]/div/div[1]/div/input').click()
    driver.find_element_by_id("OrderRetailerSelectionChooseRetailer").click()  # Choose Retailer

    # select 'United States'
    dropdown = Select(driver.find_element_by_id("AddressCountryId"))
    dropdown.select_by_visible_text("United States")

    # select 'Kentucky'
    dropdown = Select(driver.find_element_by_id("AddressZoneId6"))
    dropdown.select_by_visible_text("Kentucky")

    # select 'Crescent Springs
    dropdown = Select(driver.find_element_by_id("city"))
    dropdown.select_by_visible_text("Crescent Springs")

    # select 'tobacco'
    dropdown = Select(driver.find_element_by_id("retailer_id"))
    dropdown.select_by_value("3116")

    driver.find_element_by_xpath('//*[@id="select-delivery-form"]/div[4]/input').click()  # Continue
    driver.find_element_by_xpath('//*[@id="SelectSamplesSelectBarrelsForm"]/div[3]/div/div/button').click()  # Schedule a Visit

    schedule_visit(driver)


def schedule_visit(driver):
    # select start date
    # if error, select next date

    week: int = 3
    day: int = 3
    month: int = 0

    while True:
        driver.find_element_by_id('TripDetail5TripDate').click()  # Desired date

        # deal with edge case of january ending on a friday
        if week == 6:
            week = 2

        if day == 6:
            day = 2
            if week == 5:
                if month == 1: # deal with edge case of january ending on a friday
                    week = 6
                else:
                    week = 2
                month += 1
            else:
                week += 1
        else:
            day += 1

        driver.find_element_by_xpath(f'//*[@id="TripDetail5TripDate_table"]/tbody/tr[{week}]/td[{day}]/div').click()

        num_of_people = driver.find_element_by_id("TripDetail5PeopleAttendingTrip")
        num_of_people.clear()
        num_of_people.send_keys("4")

        driver.find_element_by_id("TripDetail5Tour").click()  # i'd like a tour
        driver.find_element_by_id("TripDetail5Lunch").click()  # i'd like lunch

        driver.find_element_by_xpath('//*[@id="TripDetailScheduleDistilleryVisitForm"]/div[4]/input').click()
        if not driver.find_elements_by_id('flashMessage'):
            break


if __name__ == '__main__':
    main()
