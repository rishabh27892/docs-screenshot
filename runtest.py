# !/usr/bin/env python
# Author: Rishabh Chauhan
# License: BSD
# Location for tests  of FreeNAS new GUI
# Test case count: 1

import sys
import getopt
from subprocess import call
from os import path
# when running for jenkins user driver, and when running on  an ubuntu system user driverU, because of  capabilities

#from driver import webDriver
#from driverU import webDriver
# Importing test
# from autoflush import autoflush
from login import run_login_test
# from guide import run_guide_test
from acc_group import run_create_group_test
from acc_user import run_create_user_test
from net_conf import run_conf_network_test
from service import run_service_test
from sys_update import run_check_update_test
from sys_email import run_conf_email_test
from sys_advanced import run_conf_sysadvance_test
from guide import run_view_guide_test
from acc_edit import run_edit_test
from acc_delete import run_delete_test
from theme import run_change_theme_test
from logout import run_logout_test
import sys
sys.stdout.flush()

argument = sys.argv

UsageMSG = """
Usage for %s:

Mandatory Commands:

--ip <0.0.0.0>            - IP of the machine targeted

Optional Commands:

--test-name <test_name>    - name of tests targeted
                            [account, system, guide, service, theme]

--driver <d_v>             - version of the driver
                             [U]

""" % argument[0]

# if have no argument stop
if len(argument) == 1:
    print(UsageMSG)
    exit()

# list of argument that should be use.
optionlist = ["ip=", "test-name=", "driver="]
testlist = ["account", "network", "system", "guide", "service", "theme"]
versionlist = ["U"]
# look if all the argument are there.
try:
    myopts, args = getopt.getopt(argument[1:], 'it', optionlist)
except getopt.GetoptError as e:
    print(str(e))
    print(UsageMSG)
    sys.exit(1)

for output, arg in myopts:
    if output == '--ip':
        ip = arg
    if output == "--test-name":
        test_name = arg
    if output == "--driver":
        driver_v = arg

try:
    ip
except NameError:
    print("Option '--ip' is missing")
    print(UsageMSG)
    sys.exit(1)

try:
    driver_v
except NameError:
    from driver import webDriver
    print ("Running jenkin/truos driver")

else:
    if (driver_v == "U"):
        from driverU import webDriver
        print ("Running Ubuntu driver")


global runDriver
runDriver = webDriver()
# turning on the autoflush to display result
# autoflush(True)
# Starting the test and genewratinf result
run_login_test(runDriver, ip)
# run_guide_test(runDriver)

try:
    test_name
except NameError:
    print ("Running: All Tests")
    run_create_user_test(runDriver)
    run_create_group_test(runDriver)
    run_conf_network_test(runDriver)
    run_check_update_test(runDriver)
    run_conf_email_test(runDriver)
    run_conf_sysadvance_test(runDriver)
    run_service_test(runDriver)
    run_view_guide_test(runDriver)
    run_edit_test(runDriver)
    run_delete_test(runDriver)
    run_change_theme_test(runDriver)
else:
    if (test_name == "account"):
        print ("Running: Accounts Test")
        run_create_user_test(runDriver)
        run_create_group_test(runDriver)
        run_edit_test(runDriver)
        run_delete_test(runDriver)
    elif (test_name == "network"):
        run_conf_network_test(runDriver)
    elif (test_name == "system"):
        run_check_update_test(runDriver)
        run_conf_email_test(runDriver)
        run_conf_sysadvance_test(runDriver)
    elif (test_name == "service"):
        print ("Running: Guide Tests")
        run_service_test(runDriver)
    elif (test_name == "guide"):
        print ("Running: Guide Tests")
        run_view_guide_test(runDriver)
    elif (test_name == "theme"):
        print ("Running: Theme Tests")
        run_change_theme_test(runDriver)

run_logout_test(runDriver)
# turning off autoflush, the default mode
# autoflush(False)
# Example test run
# run_creat_nameofthetest(runDriver)

# cleaning up files
if path.exists('driver.pyc'):
    call(["rm", "*.pyc"])

if path.exists('geckodriver.log'):
    call(["rm", "geckodriver.log"])

if path.exists('__pycache__'):
    call(["rm", "-r", "__pycache__"])

if path.isdir('.cache'):
    call(["rm", "-r", ".cache"])
