# Installing
___
In order to install, you need to install selenium via ```pip install selenium``` and install geckodriver. You MUST have Firefox installed.
# Issues
___
* Currently, the program crashes if you are offered a "Special Offer", as this popup blocks the continue button on the rate selection screen.

                ****** Cr@zYodaz Edit NOTE:  Working on above with new click id, Actually instead of (click on ID) it uses (click on CSS Code ) -- my Selenium IDE firefox plugin recorded it and have it inside the "TEST.SIDE" file.

                ****** As far as the random "POP-UP / Special Offer" think this can be easily solved with quick IF or ELSE...

                **** I have noticed that small pop-up before, even noticed sometimes my recorded SIDE selenium file would not play, this is because they are starting to randomize the click ID's , but Ive read somewhere if worse came to worse, we can look for partial "ID's " instead of looking for complete ID's -- some selenium projects would suffer, but  i think for something like a captive portal that wont be a issue

* Timings are dependent on your hotspot. The last wait is the longest, and most likely to need tweaking.
# How to use
___
* In order to use, you need to randomize your MAC address and reconnect to the XFinity Wifi hotspot. This can be done via my Mac-Automator program.
* Then, once your computer prompts you to do the captive portal login, just run ```python main.py```


              ***** Cr@zYodaz Edit Note:  I really hate it when Xfinity decides my hour is up early and then they leave me idleing still connected to the server but without any IP route --- Future goals will be to combine a simple BASH or BATCH file that can be controlled from command line, that will periodically check every 5, 10, or 15mins to verify everything is still connected and downloading,  IF NOT, then the script will call on admin / root rights to bring the network down, change mac, and maybe a simular KALI / PARROT script to change the hostname aswell,  Finally bringing it all back up again, reconnecting to xfinitywifi , then once again recall the "MAIN.py" file to automatically generate a random new user and  bypassing  the "CAPTIVE PORTAL" for another 30 or 60 mins ,

              again that will be all automatic while at work or sleep, so will also have to put in some saftey variables, like for some reason if connection can not be brought back up after 3 tries 2mins apart, then shut it down
