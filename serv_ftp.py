# Author: Rishabh Chauhan
# License: BSD
# Location for tests  of FreeNAS new GUI
# Test case count: 4

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

xpaths = { 'navService': '//*[@id="nav-8"]/div/a[1]',
           'turnoffConfirm': '//*[contains(text(), "OK")]'
         }

class conf_ftp_test(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        driver.implicitly_wait(30)
        pass

    def test_01_turnon_ftp (self):
        try:
            print (" turning on the ftp service")
            # Click Service Menu
            driver.find_element_by_xpath(xpaths['navService']).click()
            # check if the Service page is opens
            time.sleep(1)
            # get the ui element
            ui_element=driver.find_element_by_xpath('//*[@id="breadcrumb-bar"]/ul/li/a')
            # get the weather data
            page_data=ui_element.text
            print ("the Page now is: " + page_data)
            # assert response
            self.assertTrue("Services" in page_data)
            self.status_change("5", "start")
            #ftp test takes almost 6 min to turn on and display
            time.sleep(7)
            # Taking screenshot
            self.screenshot("_")
        except Exception:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            self.screenshot("-e")
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i])
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")

    def test_02_turnoff_ftp (self):
        try:
            print (" turning off the ftp service")
            time.sleep(2)
            self.status_change("5", "stop")
            # Taking screenshot
            self.screenshot("_")
        except Exception:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            self.screenshot("-e")
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i])
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")

    #method to test if an element is present
    def is_element_present(self, how, what):
        """
        Helper method to confirm the presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        try: driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True


    def status_change(self, which, to):
        print ("executing the status change function with input " + which + " + " + to)
        # get the ui element
        ui_element_status=driver.find_element_by_xpath('/html/body/app-root/app-admin-layout/mat-sidenav-container/mat-sidenav-content/div/services/div/div[' + str(which) + ']/entity-card/div[1]/div/mat-card[1]/div/div[2]/div[1]/mat-chip')
        # get the status data
        status_data=ui_element_status.text
        buttonToggle = driver.find_element_by_xpath('/html/body/app-root/app-admin-layout/mat-sidenav-container/mat-sidenav-content/div/services/div/div[' + str(which) + ']/entity-card/div[1]/div/mat-card[1]/div/div[2]/div[1]/button')
        if to == "start":
            if status_data == "STOPPED":
                # Click on the toggle button
                buttonToggle.click()
                time.sleep(1)
                print ("status has now changed to running")
            else:
                print ("the status is already " + status_data)
        elif to == "stop":
            if status_data == "RUNNING":
                #Click on the toggle button
                buttonToggle.click()
                time.sleep(1)
                # re-confirming if the turning off the service
                if self.is_element_present(By.XPATH,xpaths['turnoffConfirm']):
                    driver.find_element_by_xpath(xpaths['turnoffConfirm']).click()
            else:
                print ("the status is already" + status_data)


    def status_check(self, which):
        ui_element_status=driver.find_element_by_xpath('/html/body/app-root/app-admin-layout/mat-sidenav-container/mat-sidenav-content/div/services/div/div[' + str(which) + ']/entity-card/div[1]/div/mat-card[1]/div/div[2]/div[1]/mat-chip')
        # get the status data
        status_data=ui_element_status.text
        print ("current status is: " + status_data)

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

def run_conf_ftp_test(webdriver):
    global driver
    driver = webdriver
    suite = unittest.TestLoader().loadTestsFromTestCase(conf_ftp_test)
    xmlrunner.XMLTestRunner(output=results_xml, verbosity=2).run(suite)
