# Installing
___
In order to install, you need to install selenium via ```pip install selenium``` and install geckodriver. You MUST have Firefox installed.
# Issues
___
* Currently, the program crashes if you are offered a "Special Offer", as this popup blocks the continue button on the rate selection screen.
* Timings are dependent on your hotspot. The last wait is the longest, and most likely to need tweaking.
# How to use
___
* In order to use, you need to randomize your MAC address and reconnect to the XFinity Wifi hotspot. This can be done via my Mac-Automator program.
* Then, once your computer prompts you to do the captive portal login, just run ```python main.py```
