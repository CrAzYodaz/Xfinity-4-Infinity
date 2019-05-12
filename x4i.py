#!/usr/bin/python
# coding=utf-8
# pip install python_arptable
# pip install selenium
#  SELENIUM / SPLINTER / AND OTHER JAVA HELPERS ON TOP ###
#  YOU STILL SHOULD INSTALL THEM LOCALLY ON YOUR SYSTEM    #
# you obviously need python installed (v2.7) tested
# and you need to install Selenium if not already -- use the 'pip install selenium'
# if you dont already have it

import socket, signal, platform, sys, random, string, time
from selenium import webdriver
# from python_arptable import ARPTABLE # to be used in future releases for automatic MAC Spoofing
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC

#   DEFINE VARIABLES / pay attention to locations, and if tested, make sure that your using  ###
#   the correct firefox with your geckodriver so much troubleshooting, thats why, i used a zip #
#   version, then just extracted it right there in my Downloads folder,  --- DO NOT  use your  #
#   personal daily webrowser!!!  just use any version extract it and give it to the script to  #
#   bypass the captive portal.  once this script is more finalized we all can trust it better  #
#   for now and further beta tests, we just give it to script, let the scriipt connect, then   #
#   then put the scrpt to sleep, cloase browser , clean up cookies and get ready for the next  #
#   call, when the bash has to reset our broken internet.                                      #
# ############################################################################################ #
# LAST EDITED BECAUSE OF XFINITY CHANGES -- April 17th 2019
#https://hg.mozilla.org/releases/mozilla-release/rev/896611703c2b8f04f596ebcb09e612b7ab06eea3
# prelimenary vars

# Randomly create password -- NO, YOU WILL NOT need this, unless you must, but it would be easier just to recreate login by starting over
# This is just to set things up, so Xfinity thinks we actually care
from typing import Union

xfi_pass = "".join(random.choice(string.ascii_uppercase + string.ascii_lowercase +
                             string.digits + '-') for i in range(random.randrange(9,12)))  # type: Union[str, unicode]
# first we give small list of 150+ names have script randomly pick one for us
first_name = random.choice(open('frstnm.txt').readlines())
# we do same for last names -- small list of 250+ names having script pick one for us
last_name = random.choice(open('lstnm.txt').readlines())
# now that we have randomly chosen a first and last name combination, we can combine them for over 2500 differnt
# possible combinations for signing up down below, as well as randomly making a realistic looking email
# but first let us randomize a few email servers that are popular
emailser = ["gmail", "hotmail", "mail", "ymail", "zoho", "outlook", "gmx", "protonmail"]
emailserver = str(random.choice(emailser)) # now lets put it all together
email_string = first_name + last_name + str(random.randrange(10000, 99999)) + "@" + emailserver + ".com"
# are you keeping track? even if repeated name used, the email is different, just like in real life there is more than one
# bill edwards or tom jones on this planet, random string at end of email keeps us unique
# TODO: add more ways to randomize the above process to keep duplicates from happening

# finally we randomly select a zip code in the US
zip_code_int = random.randrange(10000, 99999)

# now all variables for new user are set, we get ready to load the default xfinity page, let page assign you according
# your own computer and new mac address
#url_wifiondemand="https://wifiondemand.xfinity.com/wod" --- default page, but edited it out because conflict with
#                  hostapd and was rederecting me to gstatic"
url_wifiondemand2 = "https://wifiondemand.xfinity.com/wod/#registerCustomer"
url_wifiondemand = "http://www.distrowatch.com" # seems to force sign-in page- my dns servers are 8.8.8.8,8.8.4.4 so
#                   make sure your using googles dns servers if this dont work.
# set-up some basic profile, disable any fancy readers, or un-needed javascripts for faster loading
#  TIP -- if edited, keep the useragent preference, sorta like spoofing your MAC Address, the useragent can spoof your
#         browser so once xfinity decides to ban a certain useragent (yes it has happened to me) well you just change
#         the string and onward you go -- Xfinity-4-Infinity
options = Options();
options.add_argument("--headless")
driver_key = "headless"
firefox_options = Options()
firefox_options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)
#uaList = [line[:-1] for line in open('uafirefox.txt')]
#open('uafirefox.txt').close()
#ua = random.choice(uaList)

# ua = random.choice(open('uafirefox.txt').readlines())
profile = webdriver.FirefoxProfile()  # type: FirefoxProfile
profile.set_preference("privacy.resistFingerprinting", True) #firefox 57+
profile.set_preference("webgl.disabled", True) #firefox 57+
profile.set_preference("browser.cache.disk.enable", False)
profile.set_preference("browser.cache.memory.enable", False)
profile.set_preference("browser.cache.offline.enable", False)
profile.set_preference("network.http.use-cache", False)
profile.set_preference("reader.parse-on-load.enabled", False)
profile.set_preference("permissions.default.stylesheet", 2);
profile.set_preference("HardwareAcceleration", False)
profile.set_preference("permissions.default.image", 2);
profile.set_preference("network.captive-portal-service.enabled", False)
profile.set_preference('app.update.auto', False)
profile.set_preference('app.update.enabled', False)
profile.set_preference('app.update.silent', False)
profile.set_preference("javascript.enabled", False)
profile.set_preference("places.history.enabled", False)
profile.set_preference("privacy.clearOnShutdown.offlineApps", True)
profile.set_preference("privacy.clearOnShutdown.passwords", True)
profile.set_preference("privacy.clearOnShutdown.siteSettings", True)
profile.set_preference("privacy.sanitize.sanitizeOnShutdown", True)
profile.set_preference("signon.rememberSignons", False)
profile.set_preference("network.cookie.lifetimePolicy", 2)
profile.set_preference("network.dns.disablePrefetch", True)
profile.set_preference("network.http.sendRefererHeader", 0)
#profile.set_preference("general.useragent.override", ua)
profile.set_preference("general.useragent.override", "'Mozilla/5.0 (Android 6.0.1; Mobile; rv:65.0) Gecko/65.0 Firefox/65.0'")
# NOTE -- changing the USER_AGENT prior to launching firefox is prefered, there are many xpi addons that will do this
#         for you. HOWEVER using this method actually works better. even spoofing the user_agent inside of the firefox
#         < about:support > page
# TODO: to have this script further randomize this project by selecting one automatically for us.
driver = webdriver.Firefox(profile)  # type: WebDriver
#path1 = 'C:\\Program Files (x86)\\Mozilla Firefox\\geckodriver.exe'
#path2 = 'C:\\Program Files\\Mozilla Firefox\\geckodriver.exe'
#try:
#    dr= webdriver.Firefox(executable_path = path1,firefox_profile = profile )
#except:
#    dr= webdriver.Firefox(executable_path = path2,firefox_profile = profile )
#return dr,uaList
#return ualist

wait = WebDriverWait(driver, 300)

# THE ALPHA PAGES

# ### THIS IS A PRE-RELEASE -- UNSTABLE -- TO MAKE THIS WORK YOU MUST SPOOF YOUR MAC ADDRESS PRIOR TO CONNECTION
# -- YOU NEED TO SPOOF YOUR MAC Address, Macchanger, or something, before you make connection
# otherwise Xfinity will black-list you.  once these two pages load up, then any further pages will AUTOMATICALLY include
# your SPOOFED MAC ADDRESS (sorta like --
# https://wifiondemand.xfinity.com/wod/landing?c=n&macId=1e%3Adb%3A04 (cut off) a=ho&bn=st22&location=Outdoor&apMacId=00%3A0d%3(cut off)
### super long address ---- THIS WAS THE EASIEST WAY I Knew of to load Xfinity from scratch with your spoofed mac - was with these 2 default pages prior to page 1
#
# I ADDED SLEEP TIMERS, TO SPOOF XFINITY TIMERS, TO MAKE IT LOOK MORE HUMAN -- loads slower - BUT - fewer errors
# if you get secure connection failed errors, try to refresh that page, and or / try to raise timers up a bit
################ REMEMBER -- EVERY LOCATION IS DIFFERENT -- THIS PYTHON SCRIPT IS ONLY A GENERAL TEMPLATE
# http://i.imgur.com/iZOtIte.png
#     driver.get(url_wifiondemand2)
#
def second_part():
    wait = WebDriverWait(driver, 300)
    first_name_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='First Name']")))
    last_name_box = driver.find_element_by_xpath("//input[@placeholder='Last Name']")
    email_box = driver.find_element_by_xpath("//input[@placeholder='Email']")
    zip_code_box = driver.find_element_by_xpath("//input[@placeholder='Zip Code']")
    first_name_box.send_keys(first_name)
    last_name_box.send_keys(last_name)
    email_box.send_keys(email_string)
    zip_code_box.send_keys(zip_code_int)
    zip_code_box.send_keys(Keys.TAB)
    time.sleep(4)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Continue')]"))).click()
    time.sleep(2)
    username = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='usePersonalEmail']")))
    password = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']")))
    password_retype = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='passwordRetype']")))
    third_submit = wait.until(EC.element_to_be_clickable((By.ID, "submitButton")))
    username.send_keys(Keys.ENTER)
    password.send_keys(xfi_pass + "$")
    password_retype.send_keys(xfi_pass + "$")
    third_submit.send_keys(Keys.ENTER)
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.ID, "_orderConfirmationActivatePass"))).click()
    time.sleep(10)
    time.sleep(10)
    driver.quit()
# TODO: proper close of python so not to waiste memory usage --
# closes the webbrowser then returns to the script previously running
#PROCNAME = "geckodriver" # or chromedriver or IEDriverServer
#for proc in psutil.process_iter():
    # check whether the process name matches
#    if proc.name() == PROCNAME:
#        proc.kill()

""" ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  MAIN: ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ """
#Xfinity kept randomizing that offer to upgrade, splitting up this py file to see if fixes it better
# VERY FRUSTRATING DEBUG -- LETS HOPE THIS WORKS -- COMPLETE REMAKE OF PYTHON FILE
#
# python starts here, then runs until that offer to upgrade is supposed to show, we dont really care if its there or not
# just have the script not crash or error, just continue so browser can close properly
# test
#driver.install_addon('/home/user/Xfinity_4_Infinity/selenium_ide-3.5.8-fx.xpi')
time.sleep(3)
driver.get(url_wifiondemand)
#time.sleep(3)
#wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='errorPageActionButton']"))).click()
time.sleep(3)
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Get Started')]"))).click()

# THE FIRST PAGE -- The page where you actually start setting up your free one hour trial of xfinitywifi
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@id='offersFreeList1']/li/label/input"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='continueButton']"))).click()
###### offer to upgrade free with paid costing you money ## Xfinity's last=ditch effort to get your wallet
### NOT ALL AREAS use this, it is a extra click to convince you to pay, if your area freezes around here, then
### comment it out --- THIS BELONGS IN FIRST PAGE
driver.implicitly_wait(3) #lowering timers because the element should already be there if not, skip and move on
time.sleep(3)
# WE KNOW THIS ELEMENT IS NOT ALWAYS THERE, THIS IS THE RANDOM UPGRADE OFFER ELEMENT, SO IF ITS NOT THERE, THEN WE
# DONT CARE, LET THE SCRIPT HANDLE THE ELEMENT ITSELF. THIS IS A FRUSTRATING DEBUG but it is working now :)
wait = WebDriverWait(driver, 3)
try:
    elemm = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'No,')]")))
    elemm.click()
    pass
    second_part()
except (NoSuchElementException, AssertionError, WebDriverException):
    print "Xfinity did not ask us to upgrade our free trial"
    pass
    second_part()
finally:
    driver.quit()
