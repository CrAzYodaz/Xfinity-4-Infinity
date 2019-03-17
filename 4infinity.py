#!/usr/bin/python
# pip arptable
###  SELENIUM / SPLINTER / AND OTHER JAVA HELPERS ON TOP ###
#  YOU STILL SHOULD INSTALL THEM LOCALLY ON YOUR SYSTEM    #

import time , string, random, sys, subprocess
import socket, signal

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

### DEFINE VARIABLES / pay attention to locations, and if tested, make sure that your using  ###
#   the correct firefox,  so much troubleshooting, i was lazy, thats why, i downloaded a zip   #
#   version, then just extracted it right there in my Downloads folder,  --- DO NOT  use your  #
#   personal daily webrowser!!!  just use any version extract it and give it to the script to  #
#   bypass the captive portal.  once this script is more finalized we all can trust it better  #
#   for now and further beta tests, we just give it to script, let the scriipt connect, then   #
#   then put the scrpt to sleep, cloase browser , clean up cookies and get ready for the next  #
#   call, when the bash has to reset our broken internet.                                      #
################################################################################################

foxbin = "/home/user/Downloads/Firefox54/firefox"  #Just a brand new - NO PROFILES extracted zip from mozilla
#foxbin = "/home/kilroy/Downloads/firefox/firefox-bin"
capabilities = webdriver.DesiredCapabilities().FIREFOX
capabilities["marionette"] = False
binary = FirefoxBinary(foxbin)
RETRIES = 3
delay = 25
lapse = 0
online = False
ecount = 0
url = "https://wifiondemand.xfinity.com/wod/"
#url = "http://1.1.1.1"
#url  = "http://wifi.comcast.com"
#url = "http://firefox.detectportal.com"
### END DEFINE VARIABLES ### CANT WAIT FOR THIS TO WORK !!!       #
# KEEPING THE PREVIOUS 3 THERE FOR TROUBLESHOOTING, i'VE ALWAYS   #
# HAD GOOD LUCK GOING STRAIGHT TO THE 'WOD' these past few months #


#Launch Firefox
driver = webdriver.Firefox(firefox_binary=binary, capabilities=capabilities)

###   FUNCTIONS   ###
#prelimenary vars


with open ("Mac.txt", "r") as myfile:
	spoofed_mac = myfile.read().replace(":","%3A").strip()


ap_mac = ARPTABLE[0]["HW address"].replace(":","%3A").strip()
first_name = "".join(random.choice(string.ascii_lowercase)for i in range(random.randrange(3,7)))
last_name = "".join(random.choice(string.ascii_lowercase)for i in range(random.randrange(5,10)))
email_string = str(random.randrange(1000000000,9999999999)) + "@comcast.com"
zip_code_int = random.randrange(10000,99999)
os = platform.system()
unq_hostname = "".join(random.choice(string.ascii_uppercase + string.ascii_lowercase +
									 string.digits + '-') for i in range(random.randrange(9,15)))


def makerandstr(len):
	letters = string.ascii_letters
	return ''.join(random.choice(letters) for i in range(len))


def randNumString(len):
	letters = list(
		"1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMN")
	return ''.join(random.choice(letters) for i in range(len))


def randNum(len):
	letters = list("1234567890")
	return ''.join(random.choice(letters) for i in range(len))

def waitForClick(id, driver, delay):
	return WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.ID, id)))

driver = webdriver.Firefox()
try:
	driver.get("https://wifiondemand.xfinity.com/wod/")
except:
	print("Uhhh, couldn't connect to the modem, please wait a bit.")
	quit()
delay = 20
try:
	signupButton = WebDriverWait(driver, delay).until(
		EC.presence_of_element_located((By.ID, 'amdocs_signup')))
	# time.sleep(5)
	signupButton.click()
	# plan = driver.find_element_by_id("offersFreeList1")
	plan = WebDriverWait(driver, delay).until(
		EC.presence_of_element_located((By.ID, 'offersFreeList1')))
	plan.click()
	# continueButton = driver.find_element_by_id("continueButton")
	time.sleep(2)
	continueButton = WebDriverWait(driver, delay).until(
		EC.presence_of_element_located((By.ID, 'continueButton')))
	continueButton.click()
	# amdocs_signup is the button

	# driver.select('rateplanid', 'spn')
	#Idk how to select the plan
	#continueButton is the continue button

	time.sleep(5)
	frstNameBox = WebDriverWait(driver, delay).until(
		EC.presence_of_element_located((By.ID, 'registerFirstName')))
	frstNameBox.send_keys(makerandstr(6))
	lstNameBox = WebDriverWait(driver, delay).until(
		EC.presence_of_element_located((By.ID, 'registerLastName')))
	lstNameBox.send_keys(makerandstr(5))
	emailBox = WebDriverWait(driver, delay).until(
		EC.presence_of_element_located((By.ID, 'registerEmail')))
	emailBox.send_keys(randNumString(10) + "@" + randNumString(10) + ".ca")
	zipBox = WebDriverWait(driver, delay).until(
		EC.presence_of_element_located((By.ID, 'registerZipCode')))
	zipBox.send_keys(randNum(5))

	time.sleep(2)
	continueRegistrationButton = WebDriverWait(driver, delay).until(
		EC.presence_of_element_located((By.ID, 'registerContinueButton')))
	continueRegistrationButton.click()
	usePersonalEmailBtn = waitForClick("usePersonalEmail", driver, delay)
	usePersonalEmailBtn.click()
	# comboOption = waitForClick("dk0-combobox", driver, delay)
	# comboOption.click()
	# comboOption = comboOption = waitForClick(
	# 	"dk0-What-was your first car (make and model)?", driver, delay)
	# JUST COMMENTED OUT THIS MIDDLE SECTION, IVE NEVER HAD TO ANSW
	# comboOption.click()
	# secretAnswer = waitForClick("secretAnswer", driver, delay)
	# secretAnswer.send_keys(makerandstr(5))
	ourPassword = randNumString(10) + randNum(3)
	passwordBox = waitForClick("password", driver, delay)
	passwordBox.send_keys(ourPassword)
	passwordRetype = waitForClick("passwordRetype", driver, delay)
	passwordRetype.send_keys(ourPassword)
	time.sleep(2)
	registerBtn = waitForClick("submitButton", driver, delay)
	registerBtn.click()
	finishBtn = waitForClick("orderConfirmationActivatePass", driver, delay)
	finishBtn.click()
	time.sleep(30)
	driver.close()
except TimeoutException:
	print ("Took too long to load the pages :(")
