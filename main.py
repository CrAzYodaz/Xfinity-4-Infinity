from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import string
import random
import time


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


driver = webdriver.Firefox()
driver.get("http://captive.apple.com/hotspot-detect.html")
signupButton = driver.find_element_by_id("amdocs_signup")
signupButton.click()
time.sleep(3)
plan = driver.find_element_by_id("offersFreeList1")
plan.click()
continueButton = driver.find_element_by_id("continueButton")
continueButton.click()
# amdocs_signup is the button

# driver.select('rateplanid', 'spn')
#Idk how to select the plan
#continueButton is the continue button

time.sleep(5)
frstNameBox = driver.find_element_by_id("registerFirstName")
frstNameBox.send_keys(makerandstr(6))
lstNameBox = driver.find_element_by_id("registerLastName")
lstNameBox.send_keys(makerandstr(5))
emailBox = driver.find_element_by_id("registerEmail")
emailBox.send_keys(randNumString(10) + "@" + randNumString(10) + ".ca")
zipBox = driver.find_element_by_id("registerZipCode")
zipBox.send_keys(randNum(5))
time.sleep(2)
continueRegistrationButton = driver.find_element_by_id(
	"registerContinueButton")
continueRegistrationButton.click()

#registerFirstName
#registerLastName
#registerEmail
#registerZipCode
#usePersonalEmail
time.sleep(3)
usePersonalEmailBtn = driver.find_element_by_id("usePersonalEmail")
usePersonalEmailBtn.click()
comboOption = driver.find_element_by_id("dk0-combobox")
comboOption.click()
comboOption = driver.find_element_by_id(
	"dk0-What-was your first car (make and model)?")
comboOption.click()
secretAnswer = driver.find_element_by_id("secretAnswer")
secretAnswer.send_keys(makerandstr(5))
ourPassword = randNumString(10) + randNum(3)
passwordBox = driver.find_element_by_id("password")
passwordBox.send_keys(ourPassword)
passwordRetype = driver.find_element_by_id("passwordRetype")
passwordRetype.send_keys(ourPassword)
time.sleep(2)
registerBtn = driver.find_element_by_id("submitButton")
registerBtn.click()
time.sleep(10)
finishBtn = driver.find_element_by_id("orderConfirmationActivatePass")
finishBtn.click()
time.sleep(10)
driver.close()
