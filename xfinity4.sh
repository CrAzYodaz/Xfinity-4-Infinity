#!/bin/bash

### BEGIN INIT INFO
# Provides:        wifixfinity
# Required-Start:  $network
# Required-Stop:
# Default-Start:   2 3 4 5
# Default-Stop:   0 1 6
# Short-Description: Auto-Connects Xfinity Wifi Public Hotspots
### END INIT INFO

# place these into the crontab for root
# */9 * * * * /usr/local/bin/check_network
# 0 * * * *    service network restart > /dev/null
# exit 0;
#################################################################################
# Script to monitor and restart wireless access point when needed


LOG=/home/user/mylog.log #going to have to have log file somewhere, dont want the screen all blocked up with error messages
SECONDS=1000 # some variable seconds counter string i was thinking about, but kinda redundant
maxPloss=10 #Maximum percent packet loss before a restart of network script below


#getting_started

restart_networking() {
        # Add any commands need to get network back up and running
        sudo service network-manager stop
        sudo service network-manager start
        sleep 3
        sudo nmcli con up xfinitywifi
        sleep 9
        #had a *.py file in here before, then i gave up , found the selenium runner, wich now i am
        #giving up on aswell also,  the goal here the script is to check the internet connection every 5,10,15 or so
        #minutes, I have previously pissed off xfinity so bad they limited their trials to 30mins multiple of times
        #and there also been times i'd get signed on and immediatly they would kick me off .. LOL
        #selenium-side-runner -c "browserName='firefox'" /home/user/Downloads/Firefox54/firefox/test.side
        python Xfinity4.py  ### THIS PY file will loop back to this bash if the runner above dont work.
        #or place for call of python py file if selenium runner dont work will go here
        #and then we would have a infinate loop, just having difficulty now cause i am in and out of ROOT so much
        #that i think even python installs got goofed up, but with the network-manager and nmcli command line calls
        #we gotta run this as sudo --- then of course firefox and chrome give cant run as sudo erors
		sleep 120
		getting_started

        #only needed if your running a wireless ap
        #/etc/init.d/dhcp3-server restart
}

getting_started() {
	sleep 4
	echo "RECHECKING INTERNET...."
	if ! $(host -W5 www.google.com > /dev/null 2>&1); then
		#Make a note in syslog
		logger "wap_check: Network connection is down, restarting network ..."
		restart_networking
	else packet_ping
	exit
fi

}
# First make sure we can resolve google, otherwise 'ping -w' would hang
# Initialize to a value that would force a restart
# (just in case ping gives an error and ploss doesn't get set)
packet_ping() {
	ploss=101
# now ping google for 10 seconds and count packet loss
	echo "IN DEPTH PACKET TEST .... "
	ploss=$(ping -q -w10 www.google.com | grep -o "[0-9]*%" | tr -d %) > /dev/null 2>&1
	if [ "$ploss" -gt "$maxPloss" ]; then
        logger "Packet loss ($ploss%) exceeded $maxPloss, restarting network ..."
        restart_networking
    else
        echo "ONLINE VERIFICATION COMPLETED.... "
        sleep_timer
		exit
fi
}

sleep_timer() {
	secs=$((4 * 60))
while [ $secs -gt 0 ]; do
   echo -ne "  $secs\033[0K\r SECONDS TILL NEXT TEST ..."
   sleep 1
   : $((secs--))
done
getting_started

}

echo " checking current connection"
getting_started

exit
# sothis script runs sorta messy but clean, funny when xfinity kicks your hour, they still leave ya in limbo land connected
# and i hate that, if i fall asleep and well, ya know the drill,  i have actually used this broken script to actually disconect me
# after they have,
