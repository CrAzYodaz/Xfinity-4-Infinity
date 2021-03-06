from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import string
import random
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


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
	driver.get("http://captive.apple.com/hotspot-detect.html")
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
	comboOption = waitForClick("dk0-combobox", driver, delay)
	comboOption.click()
	comboOption = comboOption = waitForClick(
		"dk0-What-was your first car (make and model)?", driver, delay)

	comboOption.click()
	secretAnswer = waitForClick("secretAnswer", driver, delay)
	secretAnswer.send_keys(makerandstr(5))
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
	time.sleep(15)
	driver.close()
except TimeoutException:
	print ("Took too long to load the pages :(")
