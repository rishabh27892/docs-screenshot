# Author: Rishabh Chauhan
# License: BSD
# Location for tests  of FreeNAS new GUI
# Test case count: 3

from source import *
from selenium.webdriver.common.keys import Keys
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

xpaths = { 'navNetwork' : '//*[@id="nav-4"]/div/a[1]',
           'submenuNetworkconfig' : '//*[@id="4-0"]',
           'nameserver1' : '//*[@id="gc_nameserver1"]/mat-input-container/div/div[1]/div/input',
           'nameserver2' : '//*[@id="gc_nameserver2"]/mat-input-container/div/div[1]/div/input',
           'buttonSave' : '//*[@id="save_button"]'
         }


class conf_network_test(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        driver.implicitly_wait(30)
        pass

    # Test navigation Account>Users>Hover>New User and enter username,fullname,password,confirmation and wait till user is  visibile in the list
    def test_01_nav_net_conf(self):
        try:
            # Navigating to System>Update page
            a = driver.find_element_by_xpath(xpaths['navNetwork'])
            a.click()
            # allowing page to load by giving explicit time(in seconds)
            time.sleep(1)
            # Click on the Update submenu
            driver.find_element_by_xpath(xpaths['submenuNetworkconfig']).click()
            # cancelling the tour
            if self.is_element_present(By.XPATH,"/html/body/div[6]/div[1]/button"):
                driver.find_element_by_xpath("/html/body/div[6]/div[1]/button").click()
            # Taking screenshot
            self.screenshot("_")
        except Exception:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            self.screenshot("-e")
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i])
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")

    def test_02_close_network_tab(self):
        try:
            # Close the System Tab
            driver.find_element_by_xpath(xpaths['navNetwork']).click()
            time.sleep(2)
            # Taking screenshot
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

    def error_check_sys(self):
        if (self.is_element_present(By.XPATH, "/html/body/div[5]/div[4]/div/mat-dialog-container/error-dialog/h1")):
            driver.find_element_by_xpath("//*[contains(text(), 'Close')]").click()

    def screenshot(self, count):
        test_method_name = self._testMethodName
        time.sleep(1)
        text_path = os.path.dirname(os.path.realpath(__file__))
        filename = str(__file__)
        filename = filename[:-3]
        final_file = filename.replace(text_path + "/", '')
        print ("Taking screenshot for " + final_file + "-" + test_method_name)
        driver.save_screenshot(cwd + "/screenshot/"  + "screenshot-" + final_file + "-" + test_method_name + ".png")


    @classmethod
    def tearDownClass(inst):
        pass

def run_conf_network_test(webdriver):
    global driver
    driver = webdriver
    suite = unittest.TestLoader().loadTestsFromTestCase(conf_network_test)
    xmlrunner.XMLTestRunner(output=results_xml, verbosity=2).run(suite)
