# !/usr/bin/env python
# Author: Rishabh Chauhan
# License: BSD
# Location for tests  of FreeNAS new GUI
# Test case count: 1

from source import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

#error handling/screenshotsave
import sys
import traceback
import os
cwd = str(os.getcwd())

import time
import unittest
import xmlrunner
import random
try:
    import unittest2 as unittest
except ImportError:
    import unittest

xpaths = {'usernameTxtBox': '/html/body/app-root/app-auth-layout/app-signin/div/div/mat-card/mat-card-content/div[1]/form/div[1]/mat-input-container/div/div[1]/div/input',
          'passwordTxtBox': '/html/body/app-root/app-auth-layout/app-signin/div/div/mat-card/mat-card-content/div[1]/form/div[2]/mat-input-container/div/div[1]/div/input',
          'submitButton': '/html/body/app-root/app-auth-layout/app-signin/div/div/mat-card/mat-card-content/div[1]/form/button'
          }


class login_test(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        driver.get(ui_url)

    def test_01_login(self):
        try:
            print ("loging in FreeNAS new webui- woot woot")
            # enter username in the username textbox
            driver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()
            driver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)
            # enter password in the password textbox
            driver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)
            # click
            driver.find_element_by_xpath(xpaths['submitButton']).click()
            self.screenshot("_")
        except Exception:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            self.screenshot("-e")
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i])
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")


    # method to test if an element is present
    def is_element_present(self, how, what):
        """
        Helper method to confirm the presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        try: driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True

    def screenshot(self, count):
        test_method_name = self._testMethodName
        time.sleep(1)
        text_path = os.path.dirname(os.path.realpath(__file__))
        filename = str(__file__)
        filename = filename[:-3]
        final_file = filename.replace(text_path + "/", '')
        print ("Taking screenshot for " + final_file + "-" + test_method_name)
        driver.save_screenshot(cwd + "/screenshot/"  + "screenshot-" + final_file + "-" + test_method_name + ".png")

    def error_check(self):
        if self.is_element_present(By.XPATH, '//*[contains(text(), "Close")]'):
            if self.is_element_present(By.XPATH,'/html/body/div[5]/div[2]/div/mat-dialog-container/error-dialog/h1'):
                ui_element=driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/mat-dialog-container/error-dialog/h1')
                error_element=ui_element.text
                print (error_element)
            driver.find_element_by_xpath('//*[contains(text(), "Close")]').click()
            print ("rdd error closed")


    @classmethod
    def tearDownClass(inst):
        pass

def run_login_test(webdriver, ip):
    global driver
    driver = webdriver
    global ui_url
    ui_url = "http://%s/ui" % ip
    suite = unittest.TestLoader().loadTestsFromTestCase(login_test)
    xmlrunner.XMLTestRunner(output=results_xml, verbosity=2).run(suite)
