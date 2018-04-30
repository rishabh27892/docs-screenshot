# Author: Rishabh Chauhan
# License: BSD
# Location for tests  of FreeNAS new GUI
# Test case count: 18

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


xpaths = { 'navService' : '//*[@id="nav-8"]/div/a[1]',
          'configButton1' : '/html/body/app-root/app-admin-layout/mat-sidenav-container/mat-sidenav-content/div/services/div/div[1]/entity-card/div[1]/div/mat-card[1]/div/div[2]/div[3]/button',
          'configButton2' : '/html/body/app-root/app-admin-layout/mat-sidenav-container/mat-sidenav-content/div/services/div/div[2]/entity-card/div[1]/div/mat-card[1]/div/div[2]/div[3]/button',
          'configButton3' : '/html/body/app-root/app-admin-layout/mat-sidenav-container/mat-sidenav-content/div/services/div/div[3]/entity-card/div[1]/div/mat-card[1]/div/div[2]/div[3]/button',
          'configButton4' : '/html/body/app-root/app-admin-layout/mat-sidenav-container/mat-sidenav-content/div/services/div/div[4]/entity-card/div[1]/div/mat-card[1]/div/div[2]/div[3]/button',
          'configButton5' : '/html/body/app-root/app-admin-layout/mat-sidenav-container/mat-sidenav-content/div/services/div/div[5]/entity-card/div[1]/div/mat-card[1]/div/div[2]/div[3]/button',
          'configButton6' : '/html/body/app-root/app-admin-layout/mat-sidenav-container/mat-sidenav-content/div/services/div/div[6]/entity-card/div[1]/div/mat-card[1]/div/div[2]/div[3]/button',
          'configButton7' : '/html/body/app-root/app-admin-layout/mat-sidenav-container/mat-sidenav-content/div/services/div/div[7]/entity-card/div[1]/div/mat-card[1]/div/div[2]/div[3]/button',
          'configButton8' : '/html/body/app-root/app-admin-layout/mat-sidenav-container/mat-sidenav-content/div/services/div/div[8]/entity-card/div[1]/div/mat-card[1]/div/div[2]/div[3]/button',
          'configButton9' : '/html/body/app-root/app-admin-layout/mat-sidenav-container/mat-sidenav-content/div/services/div/div[9]/entity-card/div[1]/div/mat-card[1]/div/div[2]/div[3]/button',
          'configButton10' : '/html/body/app-root/app-admin-layout/mat-sidenav-container/mat-sidenav-content/div/services/div/div[10]/entity-card/div[1]/div/mat-card[1]/div/div[2]/div[3]/button',
          'configButton11' : '/html/body/app-root/app-admin-layout/mat-sidenav-container/mat-sidenav-content/div/services/div/div[11]/entity-card/div[1]/div/mat-card[1]/div/div[2]/div[3]/button',
          'configButton12' : '/html/body/app-root/app-admin-layout/mat-sidenav-container/mat-sidenav-content/div/services/div/div[12]/entity-card/div[1]/div/mat-card[1]/div/div[2]/div[3]/button',
          'configButton13' : '/html/body/app-root/app-admin-layout/mat-sidenav-container/mat-sidenav-content/div/services/div/div[13]/entity-card/div[1]/div/mat-card[1]/div/div[2]/div[3]/button',
          'configButton14' : '/html/body/app-root/app-admin-layout/mat-sidenav-container/mat-sidenav-content/div/services/div/div[14]/entity-card/div[1]/div/mat-card[1]/div/div[2]/div[3]/button',
          'configButton15' : '/html/body/app-root/app-admin-layout/mat-sidenav-container/mat-sidenav-content/div/services/div/div[15]/entity-card/div[1]/div/mat-card[1]/div/div[2]/div[3]/button',
          'configButton16' : '/html/body/app-root/app-admin-layout/mat-sidenav-container/mat-sidenav-content/div/services/div/div[16]/entity-card/div[1]/div/mat-card[1]/div/div[2]/div[3]/button',
          'configButton17' : '/html/body/app-root/app-admin-layout/mat-sidenav-container/mat-sidenav-content/div/services/div/div[17]/entity-card/div[1]/div/mat-card[1]/div/div[2]/div[3]/button',
         }

class service_test(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        driver.implicitly_wait(30)
        pass


    def test_01_nav_service (self):
        try:
            # click Service Menu
            driver.find_element_by_xpath(xpaths['navService']).click()
            # allowing the button to load
            time.sleep(1)
            # Taking screenshot
            self.screenshot("_")
        except Exception:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            self.screenshot("-e")
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i])
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")

    def test_02_configure_afp(self):
        try:
            print (" configuring afp service")
            time.sleep(2)
            # click on configure button
            driver.find_element_by_xpath(xpaths['configButton1']).click()
            # Taking screenshot
            self.screenshot("_")
        except Exception:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            self.screenshot("-e")
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i])
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")
    def test_03_configure_smb(self):
        try:
            # click Service Menu
            driver.find_element_by_xpath(xpaths['navService']).click()
            # allowing the button to load
            time.sleep(1)
            print (" configuring smb service")
            time.sleep(2)
            # click on configure button
            driver.find_element_by_xpath(xpaths['configButton2']).click()
            # Taking screenshot
            self.screenshot("_")
        except Exception:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            self.screenshot("-e")
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i])
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")
    def test_04_configure_dc(self):
        try:
            # click Service Menu
            driver.find_element_by_xpath(xpaths['navService']).click()
            # allowing the button to load
            time.sleep(1)
            print (" configuring dc service")
            time.sleep(2)
            # click on configure button
            driver.find_element_by_xpath(xpaths['configButton3']).click()
            # Taking screenshot
            self.screenshot("_")
        except Exception:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            self.screenshot("-e")
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i])
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")
    def test_05_configure_dns(self):
        try:
            # click Service Menu
            driver.find_element_by_xpath(xpaths['navService']).click()
            # allowing the button to load
            time.sleep(1)
            print (" configuring dns service")
            time.sleep(2)
            # click on configure button
            driver.find_element_by_xpath(xpaths['configButton4']).click()
            # Taking screenshot
            self.screenshot("_")
        except Exception:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            self.screenshot("-e")
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i])
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")
    def test_06_configure_ftp(self):
        try:
            # click Service Menu
            driver.find_element_by_xpath(xpaths['navService']).click()
            # allowing the button to load
            time.sleep(1)
            print (" configuring ftp service")
            time.sleep(2)
            # click on configure button
            driver.find_element_by_xpath(xpaths['configButton5']).click()
            # Taking screenshot
            self.screenshot("_")
        except Exception:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            self.screenshot("-e")
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i])
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")
    def test_07_configure_iscsi(self):
        try:
            # click Service Menu
            driver.find_element_by_xpath(xpaths['navService']).click()
            # allowing the button to load
            time.sleep(1)
            print (" configuring iscsi service")
            time.sleep(2)
            # click on configure button
            driver.find_element_by_xpath(xpaths['configButton6']).click()
            # Taking screenshot
            self.screenshot("_")
        except Exception:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            self.screenshot("-e")
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i])
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")
    def test_08_configure_lldp(self):
        try:
            print (" configuring lldp service")
            time.sleep(2)
            # click on configure button
            driver.find_element_by_xpath(xpaths['configButton7']).click()
            # Taking screenshot
            self.screenshot("_")
        except Exception:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            self.screenshot("-e")
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i])
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")
    def test_09_configure_netdata(self):
        try:
            # click Service Menu
            driver.find_element_by_xpath(xpaths['navService']).click()
            # allowing the button to load
            time.sleep(1)
            print (" configuring netdata service")
            time.sleep(2)
            # click on configure button
            driver.find_element_by_xpath(xpaths['configButton8']).click()
            # Taking screenshot
            self.screenshot("_")
            if (self.is_element_present(By.XPATH,'//*[contains(text(), "Close")]')):
                driver.find_element_by_xpath('//*[contains(text(), "Close")]').click()
        except Exception:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            self.screenshot("-e")
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i])
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")
    def test_10_configure_nfs(self):
        try:
            # click Service Menu
            driver.find_element_by_xpath(xpaths['navService']).click()
            # allowing the button to load
            time.sleep(1)
            print (" configuring nfs service")
            time.sleep(2)
            # click on configure button
            driver.find_element_by_xpath(xpaths['configButton9']).click()
            # Taking screenshot
            self.screenshot("_")
        except Exception:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            self.screenshot("-e")
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i])
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")
    def test_11_configure_rsync(self):
        try:
            # click Service Menu
            driver.find_element_by_xpath(xpaths['navService']).click()
            # allowing the button to load
            time.sleep(1)
            print (" configuring rsync service")
            time.sleep(2)
            # click on configure button
            driver.find_element_by_xpath(xpaths['configButton10']).click()
            # Taking screenshot
            self.screenshot("_")
        except Exception:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            self.screenshot("-e")
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i])
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")
    def test_12_configure_s3(self):
        try:
            # click Service Menu
            driver.find_element_by_xpath(xpaths['navService']).click()
            # allowing the button to load
            time.sleep(1)
            print (" configuring s3 service")
            time.sleep(2)
            # click on configure button
            driver.find_element_by_xpath(xpaths['configButton11']).click()
            # Taking screenshot
            self.screenshot("_")
        except Exception:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            self.screenshot("-e")
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i])
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")
    def test_13_configure_SMART(self):
        try:
            # click Service Menu
            driver.find_element_by_xpath(xpaths['navService']).click()
            # allowing the button to load
            time.sleep(1)
            print (" configuring S.M.A.R.T service")
            time.sleep(2)
            # click on configure button
            driver.find_element_by_xpath(xpaths['configButton12']).click()
            # Taking screenshot
            self.screenshot("_")
        except Exception:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            self.screenshot("-e")
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i])
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")
    def test_14_configure_snmp(self):
        try:
            # click Service Menu
            driver.find_element_by_xpath(xpaths['navService']).click()
            # allowing the button to load
            time.sleep(1)
            print (" configuring snmp service")
            time.sleep(2)
            # click on configure button
            driver.find_element_by_xpath(xpaths['configButton13']).click()
            # Taking screenshot
            self.screenshot("_")
        except Exception:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            self.screenshot("-e")
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i])
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")
    def test_15_configure_ssh(self):
        try:
            # click Service Menu
            driver.find_element_by_xpath(xpaths['navService']).click()
            # allowing the button to load
            time.sleep(1)
            print (" configuring ssh service")
            time.sleep(2)
            # click on configure button
            driver.find_element_by_xpath(xpaths['configButton14']).click()
            # Taking screenshot
            self.screenshot("_")
        except Exception:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            self.screenshot("-e")
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i])
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")
    def test_16_configure_tftp(self):
        try:
            # click Service Menu
            driver.find_element_by_xpath(xpaths['navService']).click()
            # allowing the button to load
            time.sleep(1)
            print (" configuring tftp service")
            time.sleep(2)
            # click on configure button
            driver.find_element_by_xpath(xpaths['configButton15']).click()
            # Taking screenshot
            self.screenshot("_")
        except Exception:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            self.screenshot("-e")
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i])
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")
    def test_17_configure_ups(self):
        try:
            # click Service Menu
            driver.find_element_by_xpath(xpaths['navService']).click()
            # allowing the button to load
            time.sleep(1)
            print (" configuring ups service")
            time.sleep(2)
            # click on configure button
            driver.find_element_by_xpath(xpaths['configButton16']).click()
            # Taking screenshot
            self.screenshot("_")
        except Exception:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            self.screenshot("-e")
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i])
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")
    def test_02_configure_webdav(self):
        try:
            # click Service Menu
            driver.find_element_by_xpath(xpaths['navService']).click()
            # allowing the button to load
            time.sleep(1)
            print (" configuring webdav service")
            time.sleep(2)
            # click on configure button
            driver.find_element_by_xpath(xpaths['configButton17']).click()
            # Taking screenshot
            self.screenshot("_")
        except Exception:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            self.screenshot("-e")
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i])
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")

        # Next step-- To check if the new user is present in the list via automation


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


def run_service_test(webdriver):
    global driver
    driver = webdriver
    suite = unittest.TestLoader().loadTestsFromTestCase(service_test)
    xmlrunner.XMLTestRunner(output=results_xml, verbosity=2).run(suite)
