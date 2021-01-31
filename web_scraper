# A program to log onto McGill's Minerva portal and notify you when a class has room available for you to register.
# Originally programmed for a particular finance class

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from time import sleep
from datetime import datetime
import Email

browser = webdriver.Firefox(executable_path='/Users/a_saussier/Documents/geckodriver')


def seats_checker(username, password):

    # Open browser @ minerva
    browser.get('https://horizon.mcgill.ca/fr-PBAN1/twbkwbis.P_WWWLogin')

    sleep(5)

    # find username field, send username key
    username_elem = browser.find_element_by_xpath('//*[@id="UserID"]')
    username_elem.send_keys(username)

    # Find password field, send password key
    password_elem = browser.find_element_by_xpath('//*[@id="PIN"]')
    password_elem.send_keys(password)

    # click on connexion button
    password_elem.submit()
    # Time for the webpage to load
    sleep(7)

    seats_remaining = 0
    while int(seats_remaining) == 0:
        sleep(10)

        main_menu_elem = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/span/map/table/tbody/tr[1]/td/table/tbody/tr/td[1]/a').click()

        sleep(5)
        # Access student menu
        student_menu_elem = browser.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[2]/td[2]/a').click()
        sleep(10)

        # Access class registration menu
        class_registration_elem = browser.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[2]/td[2]/a').click()
        sleep(10)

        # Access class browser
        class_browser_elem = browser.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[2]/td[2]/a').click()
        sleep(10)

        # Click on winter 2021 semester
        winter_elem = browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr/td/select').click()

        
        wait(browser, 5).until(EC.visibility_of_element_located(
            (By.XPATH,'/html/body/div[3]/form/table/tbody/tr/td/select/option[3]'))).click()

        submit_term_elem = browser.find_element_by_xpath('/html/body/div[3]/form/input[3]').click()
        sleep(10)

        # Click on Finance Subject
        subject_elem = browser.find_element_by_xpath('/html/body/div[3]/form/table[1]/tbody/tr/td[2]/select/option[115]'
                                                     ).click()
        click_course_search_elem = browser.find_element_by_xpath('/html/body/div[3]/form/input[17]').click()
        sleep(10)
        # View sections of FINE 446 Behavioural finance
        class_elem = browser.find_element_by_xpath('/html/body/div[3]/table[2]/tbody/tr[12]/td[3]/form/input[30]'
                                                   ).click()

        sleep(10)

        # If there are seats remaining, send me an email
        seats_remaining = browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[3]/td[13]').text
        print(str(datetime.now()) + ' - SeatsRemaining = ' + seats_remaining)
        sleep(10)

        # Go back to main menu to be able to start scraping loop again

    return int(seats_remaining)

username = input("Username: ")
password = input("Password: ")
available_seats = seats_checker(username, password)

print('Quick! Go register, there are ' + str(available_seats) + 'seats remaining!')


Email.send_email('Your Email here', 'Your subject',
                 'Someone dropped the class and there is availability. Go register ASAP!')

worksheet_elem = browser.find_element_by_xpath('/html/body/div[3]/form/input[8]').click()
sleep(5)

# CRN of Behavioral: 16577
crn_case_elem = browser.find_element_by_xpath('//*[@id="crn_id1"]')
crn_case_elem.send_keys('16577')
submit_changes_elem = browser.find_element_by_xpath('/html/body/div[3]/form/input[19]').click()






