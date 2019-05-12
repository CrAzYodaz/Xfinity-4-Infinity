#!/usr/bin/python
# pip arptable
###  SELENIUM / SPLINTER / AND OTHER JAVA HELPERS ON TOP ###
#  YOU STILL SHOULD INSTALL THEM LOCALLY ON YOUR SYSTEM    #

#!/usr/bin/python
###########################################################################
# pip install selenium
#
# you obviously need python installed (v2.7) tested
# and you need to install Selenium if not already -- use the 'pip install selenium'
# if you dont already have it

from selenium import webdriver
# from python_arptable import ARPTABLE # to be used in future releases for automatic MAC Spoofing
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import socket, platform, sys, random, string, time

### DEFINE VARIABLES / pay attention to locations, and if tested, make sure that your using  ###
#   the correct firefox with your geckodriver so much troubleshooting, thats why, i used a zip #
#   version, then just extracted it right there in my Downloads folder,  --- DO NOT  use your  #
#   personal daily webrowser!!!  just use any version extract it and give it to the script to  #
#   bypass the captive portal.  once this script is more finalized we all can trust it better  #
#   for now and further beta tests, we just give it to script, let the scriipt connect, then   #
#   then put the scrpt to sleep, cloase browser , clean up cookies and get ready for the next  #
#   call, when the bash has to reset our broken internet.                                      #
################################################################################################

# prelimenary vars
# I commented out the 'first_name" and 'last_name' -- replaced them with 17 seperate random names
# just feels more authentic having actual names instead of just random charactors that did not even spell anything
#### 17 should be enough, if you would rather use random characters then un-comment, xfinity goes more by email then
# by name anyways -- future releases will actually read them from seperate txt file for more choices

# Randomly create password -- NO, YOU WILL NOT need this, unless you must, but it would be easier just to recreate login by starting over
# This is just to set things up, so Xfinity thinks we actually care
xfi_pass = "".join(random.choice(string.ascii_uppercase + string.ascii_lowercase +
									 string.digits + '-') for i in range(random.randrange(9,12)))

firstn = ["Timothy", "Richard", "Markus", "Susan", "Brenda", "Mary", "George", "Fred", "Jose", "Patricia", "Anna", "Barbara", "Michael", "Joseph", "Thomas", "Michelle", "Tina", "Bertha"]
first_name = str(random.choice(firstn))
# first_name = "".join(random.choice(string.ascii_lowercase) for i in range(random.randrange(7, 17)))
lastn = ["Smith", "Jones", "Lopez", "Thompson", "Sanchez", "Wilkerson", "Peterson", "Ortega", "Adams", "Sanderson", "Owens", "Reynolds", "McDonald", "Littleton", "Simpson", "Zander", "Gates"]
last_name = str(random.choice(lastn))
# last_name = "".join(random.choice(string.ascii_lowercase) for i in range(random.randrange(6, 17)))
email_string = first_name + last_name + str(random.randrange(1000000000, 9999999999)) + "@gmail.com"
zip_code_int = random.randrange(10000, 99999)

# Load default xfinity page, let page assign you according to your macchanger and user_agents
url_wifiondemand = "about:support"

# set-up some basic profile, disable any fancy readers, or un-needed javascripts for faster loading
## TIP -- if edited, keep the useragent preference, sorta like spoofing your MAC Address, the useragent can spoof your browser so once xfinity
#         decides to ban a certain useragent (yes it has happened to me) well you just change the string and onward you go -- Xfinity-4-Infinity
profile = webdriver.FirefoxProfile()  # type: FirefoxProfile
profile.set_preference("reader.parse-on-load.enabled", False)
profile.set_preference("permissions.default.stylesheet", 2);
profile.set_preference("permissions.default.image", 2);
profile.set_preference("javascript.enabled", False);
profile.set_preference("general.useragent.override","'Mozilla/5.0 (Android 6.0.1; Mobile; rv:65.0) Gecko/65.0 Firefox/65.0'")
driver = webdriver.Firefox(profile)  # type: WebDriver
wait = WebDriverWait(driver, 300)

# THE ALPHA PAGES

# ### THIS IS A PRE-RELEASE -- UNSTABLE -- TO MAKE THIS WORK YOU MUST SPOOF YOUR MAC ADDRESS PRIOR TO CONNECTION
# -- YOU NEED TO SPOOF YOUR MAC Address, Macchanger, or something, before you make connection
# otherwise Xfinity will black-list you.  once these two pages load up, then any further pages will AUTOMATICALLY include

# if you get secure connection failed errors, try to refresh that page, and or / try to raise timers up a bit
################ REMEMBER -- EVERY LOCATION IS DIFFERENT -- THIS PYTHON SCRIPT IS ONLY A GENERAL TEMPLATE
# http://i.imgur.com/iZOtIte.png

driver.get(url_wifiondemand)
