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
# apt-get install git unzip python python-dev python-pip build-essential
W="\033[0m"  # white (normal)
R="\033[31m"  # red
G="\033[32m"  # green
O="\033[33m"  # orange
B="\033[34m"  # blue
P="\033[35m"  # purple
C="\033[36m"  # cyan
GR="\033[37m"  # gray

your_not_sudo() {
clear
    while true; do
        clear
        echo -e "$O $X4I NEEDS to be ran as 'SUDO' to help control your wifi interface's $W [$Bsu$W] \n"
        echo -e "$C Do You wish to restart as $R SUDO? $O Choose By Entering A Number then press'ENTER' $W \n"
        echo -e "$C PLEASE NOTE: running as ROOT damages certain webbrowsers and can mess up dependency $W \n"
        echo -e "$C files needed by this program, SUDO is fine, ROOT is not. (thank you)$W \n"
        echo -e "\t 1] Yes, please call up the script again using root preferences  "
        echo -e "\t 2] NO PLEASE DONT RESTART SCRIPT, place me inside debugging mode right away    "
        echo -e "\t 3] No, Lets $R EXIT $O out of this program.          \n"
        echo  -n""
        read sn
        echo ""
        case $sn in
            1 ) exec sudo -- "$0" "$@";;
            2 ) clear; houston_problem;;
            3 ) clear; break;;
            * ) echo $R "Unknown option. Please choose again" $C ;;
        esac
    done

exit
}
[ "$(whoami)" != "root" ] && your_not_sudo
[ $HOME == "/root" ] && your_not_sudo

# gotta make sure file is ran as sudo - this is mainly for the actual connection and packet pings
# to avoid sudo errors while browser loads, a seperate "sudo -u <username> command is used
# so if you change any of this, make sure to change that aswell

## with ping/packet requests done once every 4 minutes to make sure our connection is alive with google the math USED
## in the script is simple -- 15 x 4minutes makes 60 minutes, but we also know takes a minute to sign up and maybe a
## couple other things. so around 13 ping / packet tests, the script will offer to hang up and re-sign back up
## ITS NOT LIKE WE HAVE TO USE UP ALL 59minutes and 59seconds of our time. -- let the script do its job, and every 52-55
## minutes, we will leave, and not be kicked off, then enter right back making sure to change what we can before so that
## we do not raise a wind storm.
#
# we are basically using this script, to keep full anominity aswell as keeping as much as possible on OUR terms and not
# Xfinity's terms.
MINSL=0 # (minutes left math --- (takes 15 then subtracts how many ping tests we already did)
ML=0 #Minutes Left -- (we take MINSL above and TIMES that * 4) gives us time remaining estimate, we dont neend exact
#     time, we dont need to be kicked of every hour, this script can assure us we leave on our own terms. even if that
#     means we leave a few mins early -- we can re-sign back up while minimizing any "RED FLAG WARNINGS"
CUR_TIME=0  # CURRENT TIME - same as below but without the [:] so the script can do the math
TN=$(date +%I:%M:%S[%p]) #  TIME NOW local time with [HH:MM:SS] #pretty nmae
CON_TIME=0  # CONNECTION TIME - same as below but in raw format so script can do easy math (without the ':')
CT=0 #CONNECTION TIME AKA (when our hour started) pretty name [hh:mm:ss]
### TODO: prolly just take current time, then compare to timezone west of you if they are
# equals, then your hour is up,  seems allot easier and fewer variable strings needed.

X4I=Xfinity-4-Infinity  #  long project names make scripting difficult with 120 character limit per line -- shorten it
XFINITYTRIES="0"   #COUNTING FAILED CONNECTION ATTEMPTS IF ANY
XFINITY4INFINITY="0"   #COUNTING NUMBER OF PING TESTS MADE TO CALCULATE ROUGHLY WHEN HOUR IS UP
MAXPLOSS="40"  # MAXIMUM ALLOWED PACKET LOSS WE WILL ACCEPT BEFORE RESTARTING OUR NETWORK CONECTION AND USING A seperate
#              ACCOUNT. (raised for users that watch netflix and such, the scripts main concern iw when packet loss is
#              at 100% -- meaning Xfinity dropped our internet, but actually left us sitting in LIMBO on the Public
#              Wifi Hotspot) <----- hate that when they do that, and they do, thats how this script was created.
LOGGINGFILE=./X4I.log #going to have to have log file somewhere, dont want the screen all blocked up with
#                                 error messages
SECS="0"  # SECONDS -- used on few of these sleep timers

houston_problem() {
    clear
        while true; do
            clear
            echo -e "$O $X4I $C is preparing to enter DEBUGGING mode [$P DEBUG$C] \n"
            echo -e "   <$C Do You wish to Continue? $O Choose By Entering A Number then '$R ENTER $O' $W> \n"
            echo -e "\t 1] Yes    "
            echo -e "\t 2] No          \n"
            echo  -n""
            read sn
            echo ""
            case $sn in
                1 ) clear; sudo -u user -- sh -c ./debuggertool.py ;;
                2 ) clear; break;;
                * ) echo "Unknown option. Please choose again" ;;
              esac
        done

    exit
    }

hour_aboutup() {
    SECS=$((15))
    clear
    echo -e "  $O $X4I $C Started This 1-hour Xfinity Connection Originally Around $CT . The Time now is  $R $TN  \n"
    echo -e $C " Our Hour is just about up, we will stop this connection a few mins early then sign up with  \n"
    echo -e $B "a differnt $R RANDOMLY $C generated fakeuser \n"
    echo -e $C "This Really CHAPS $O Xfinity's $C hide. to think that we ourselfs, would kick ourself off before they\n"
    echo -e $C "had the chance too, we are just being polite and courteous, like visiting a friends house if we knew \n"
    echo -e $C "our friend got mad if we stayed at their house for over 59 minutes, we would protect that friendship \n"
    echo -e $O "and leave early.  so just think of Xfinity as a stupid friend, we will leave early, all courteous \n"
    echo -e $O "like.. but we will come right back inside after we change some clothes so they think its somebody \n"
    echo -e $O "else .. no-worries $C we will return in just a sec \n "

    echo -e $O "$X4I $R == $C KEEPING OURSELVES IN TOTAL CONTROL \n "
    echo -e " $O PLEASE STAND BY .. \n"
    while [ $SECS -gt 0 ]; do
        echo -ne " $C RESETTING WIFI CONNECTION IN $R $SECS\033[0K\r"
        sleep 1
        : $((SECS--))
    done
    XFINITYTRIES="0"
    XFINITY4INFINITY="0"
    #cur_time=$(date +%I%M%S)
    TN=$(date +%I:%M:%S[%p])
    CT="0"
    print "✔ Success ${TN} ressetting connection on our own terms before being blacklisted" > LOGGINGFILE
    print "✔ Success ${TN} leaving on our own terms -- ${X4I}" > LOGGINGFILE
    restart_networking
}

restart_networking() {
    XFINITY4INFINITY="0"
    # Add any commands need to get network back up and running -- script should only come here if packet ping fails
        clear
        echo -e "."
        echo -e "$O $X4I $C is now preparing this computer for a new WIFI Session "
        ((XFINITYTRIES++))
        sudo service network-manager stop
    # now that we disconected - let us check to see if there was more than 3 failed attempts -- if so -- then time to close up shop and debug ourself's
        if [ "$XFINITYTRIES" -gt 4 ]; then
            print "✖✖ Error -- ${TN} there has been 4 failed connection attempts  " > LOGGINGFILE
            print "✖✖ Error -- ${TN} something needs to be fixxed like mac address or user-agent" > LOGGINGFILE
            houston_problem
        else
        sudo service network-manager start
        sudo service network-manager restart
        # yes i know this duplicate, just making sure system is ready
    sleep 3 # lets actually give the Wifi Interface a chance to load its own magical JOO-JOO before we try and connect
    sudo nmcli con up xfinitywifi #if <xfinitywifi> is named different in your area, or if you dont have this, atleast for this beta release, you should make one first
    #                             # if you've connected to xfinity wifi before, chances are you already have this connection  ## view the <README.WIFI> for more info
    #if ! $(host -w5 www.google.com > /dev/null 2>&1); then
    sleep 3
    con_time=$(date +%I%M) #TODO variable for script math regarding connection time
    CT=$(date +%I:%M:%S[%p]) # pretty name all [:] set for LOGGINGFILE and echo displays regarding connection time
    sleep 1
        #CT=$(date +[%I]:%M:%S[%p])
        #IMPORTANT NOTE
    ###### you need to use SUDO to run this script, this is because SUDO is NEEDED for 'Network-Manager','nmcli' and the 'packet requests' below.... HOWEVER
    ###### firefox, chrome, ect -- DOES NOT LIKE to be ran as SUDO --- so to bypass this, we run this script as SUDO then when its time to
    ###### call the 4infinity.py (python script) we acting as sudo, will call on normal user instead, as the python file is the file that
    ###### brings up the web browser firefox ---
    ######
    ###### I do this with the next UN-COMMENTED line below --- YOU MUST EDIT THIS YOURSELF, TO REFER TO YOUR NON-SUDO USER
    # sudo -u user -- this is a command for root to load a file as USER -- to confuse you more, my username is user -- to simplify this
    # sudo -u <your_normal_username> -- sh -c <python script> ####  change the line below and that will make both worlds happy
    ########### KNOWN ISSUE ######## sudo su, creates error and leaves you stranded in python shell press <CTRL> + <D> to exit that shell
    ########### instead just open up directory where extracted (and after you personally inspected and changed what you needed )
    ########### then when thats done --- sudo ./xfinity4.sh  --- it still runs the ./xfinity4.sh file with root privalages.. but wont carry the root environment
    ########### over to the python shell -- thus making everything happy including firefox and network-manager
    # TODO: Sometimes us country folk, like to watch movies while downloading with JDownloader, IF this is the case, and your near the computer, then a warning like this would be nice"
    # TODO: however, if your away from computer or asleep, then no need to keep running over and over if something is broken"

    # TODO: so eventually will add a choice, with maybe a 15 second default exit if there is no reply"
    #
    # check the connection before we launch browser for nothing we dont have internet yet, so we ping xfinity
    # makes sure we are ready to sign in.
    PLOSS=$(ping -q -w1 172.20.20.20 | grep -o "[0-9]*%" | tr -d %) > /dev/null 2>&1;
    if [ "$PLOSS" -gt 4 ]; then
        echo "[ ✖ Error ${TN} -- Packet loss ${PLOSS} % exceeded ${MAXPLOSS}, restarting network ]" > LOGGINGFILE
        echo "[ ✖ Error ${TN} -- This happened durring initial sign-in to Xfinity ]" > LOGGINGFILE
        restart_networking
    else
        echo -e $C "Be Patient here...  $O We CAN NOT Rush things...."
        echo -e $C " Just kick-back, Relax, and wait till the browser to closes itself without error"
        sudo -u user -- sh -c ./x4i.py  ### MAIN VERSION ### THIS PY file will loop back to this bash untill something breaks README.WIFI
        sleep 20 #give browser chance to close on its own first
        pkill geckodriver && pkill firefox && pkill firefox-bin
        sleep 20 # important to not have your personal browser open because of above line
        # IF YOUR RUNNING A PERSONAL FIREFOX BROWSER -- IT WILL CLOSE ON YOU -- but it is important for SYSTEM
        # memory to close everything this script starts, or you will have memory leaks (not good)
        echo "[ ✔ Success ${TN} -- ${X4I} was able to start your 1 hour Xfinity Session ]" > LOGGINGFILE
        echo "[ ✔ Success ${TN} -- Successful connection time was ${CT} ]" > LOGGINGFILE
        echo "[ ✔ Success ${TN} -- Successful connection time was ${CT} ]"
        getting_started
    fi
fi
}

    ########################################    README.WIFI    ########################################
    # this would be a good file to read about now -- AND LIKE ALWAYS -- personally inspect any script file before running it
    # this is pre-release, but working (atleast on my Debian Stretch) -- everything is broken-up english with side notes everywhere -- NOT FOR ME -- but for you
    # to somewhat follow along before things happen sudo is needed for the network-manager and nmcli command line calls and we CAN'T run firefox as root, so unless somebody
    # emails me a better solution --- this is the only solution I know how -- and did I mention? --- IT WORKS :)
    # solved with "sudo -u <normal_username> -- sh -c <./4infinity.py> " command it lets sudo launch programs as non-sudo user while being in sudo mode
    # while at the same time keeping sudo (root) for reset of network-manager and your wireless device
    # seeming we just re-connected, let us reset the test variable
    # below comment adjustable ontop MAXXFIN default 3 --- we just reconnected once, 3 fails in a row, let us shut script down, so we can fix later, might be bad signal
        # or maybe even a MAC address or USER_AGENT that got banned, we can manually fix this later (that means you fix it) LOL
        # on above statement, if we failed 3 times but connected on 4th, all we have to do is pass 4 ping tests (below) then and if so -- above will be reset to 0 automatically
        # a little harsh, but if we are using this script while at work, or asleep, we dont want to take no chances <README.WIFI> for more info

    #only needed if your running a wireless ap -- this will be added later -- future feature for hostapd


getting_started() {

    if ! $(host -W5 www.google.com > /dev/null 2>&1); then
        #Make a note in syslog
        #print "wap_check: Network connection is down, restarting network ..."
        restart_networking
    else
        ((XFINITY4INFINITY++))
        packet_ping
    exit
fi

}

# First make sure we can resolve google, otherwise 'ping -w' would hang
# Initialize to a value that would force a restart
# (just in case ping gives an error and ploss doesn't get set)
packet_ping() {
    PLOSS=101
    # now ping google for 10 seconds and count packet loss
    TN=$(date +%I:%M:%S[%p])
    MINSL=$((12 - $XFINITY4INFINITY))
    ML=$((5 * $MINSL))
  clear
    echo -e " $O $X4I $C Making XFINITY-WIFI Last $R FOREVER $C and $R EVER $C and $R EVER "
    echo -e "$C NOW PERFORMING A IN-DEPTH CONNECTION / PACKET-LOSS TEST @ $O $TN"
    PLOSS=$(ping -q -w10 www.google.com | grep -o "[0-9]*%" | tr -d %) > /dev/null 2>&1;
    if [ "$PLOSS" -gt "40" ]; then
        LOGGINGFILE "[ ${TN} -- Packet loss ${PLOSS} % exceeded ${MAXPLOSS}, restarting network ]"
        restart_networking
    else
    TN=$(date +%I:%M:%S[%p])
    echo -e $O " $X4I $C ONLINE CONECTION-VERIFICATION COMPLETED @ $R $TN"
    echo -e $C "[..Our Packet-Loss was only ${R} ${PLOSS} % ${O} During This Test $C]"
    echo -e $O "THIS XFINITY-WIFI Session Test Number: $C [ ${R} $XFINITY4INFINITY ${C}PASSED ] "
    sleep_primer
    exit
fi
}

## edit this myself ## work in progress ## if [ "$XFINITY4INFINITY" -gt "$MAXXFIN" ]; then $XFINITYTRIES=0 #Reset failed attempts, if 3 good tests, in row connection is fixxed, adjustable ontop
sleep_primer() {
SECS=$((5 * 60))  #starting the 5min timer before next test (5 x 12 =60mins)-- remember that if you manually adjust
    for((i=1; i<=$SECS; i++)); do
    PL=$(($i / 3))  #simple math 300 secs divided by 3 gives us 100 percent progress bar makes bar releastic time
    X4E=$((300 - $i))  #math to show seconds remain so progress bar moves slower than seconds
    echo "$PL"  #actual percentage according to above math = how much completed of our 5min wait between tests
    sleep 1
    echo "XXX"
    echo "Our Packet-Loss was only ${PLOSS} % During The Last Test"
    echo "✔ Success Previous Online-Session Test Number:[ $XFINITY4INFINITY PASSED ] "
    echo "$X4E Seconds Remain Till Next Test"
    echo "$X4I Making Xfinity Last Forever and Ever.."
    echo "XXX"
    [ $PL -gt 100 ] && break  # break when reach the 100% (or greater
done | dialog --backtitle "Session started at $CT and roughly have $ML Minutes before we gotta reset safely" --title "$X4I 5Minute SLEEP TIMER" --gauge " NEXT $X4I ONLINE VERIFICATION TEST in 5 mins" 9 90 0
if [ 10 -gt "$XFINITY4INFINITY" ]; then
getting_started  #10 x 5 = 50mins plus the first few mins == used to leave early and not get banned or raise flags
else
hour_aboutup  #above math to leave early and reset script for another random sign-up
#TODO: give option to bypass this with variable, so if user wants 1hour only script wont restart and give full 60mins
#TODO: bypass dialog script alltogether to save system resources == good idea at time, does not use that much extra mem
fi
}

sleep_timer() {
    echo -e " $C Main Connection was around $CT, we roughly have $ML Minutes before we gotta reset safely"
    SECS=$((4 * 60))  #starting the 4min timer before next test (4*15=60mins)-- remember that if you manually adjust
    while [ $SECS -gt 0 ]; do
    echo -ne " $C NEXT $O $X4I $C TEST in $P $SECS\033[0K\r"
    sleep 1
    : $((SECS--))
    done
    if [ 12 -gt "$XFINITY4INFINITY" ]; then
    getting_started
else
hour_aboutup
# TODO ### Fix timers as the $XFINITY4INFINITY string is only a estimate still close maybe 6 or so mins early
# almost used this string, but starting at am/pm it shorted me big time
#if [ "$time_left" -gt 9 ]; then
#with 4mins sleep between tests and time_left string was made 4mins ago, thats 8mins + time for tests thats atleast
# 10mins we need and thats pushing it, we dont want to be disconnected inbetween the sleep cycles prolly should raise
# this to -gt 10 making it if we have less than 11mins then lets volunteer a reset -- 7mins instead of 6mins

fi
}

its_time() {
clear
    while true; do
        clear
        echo -e "$O Xfinity-4-Infinity has Failed more than 4 Times in a row [$P?$W] \n"
        echo -e "   <$C Do You wish to Continue $O Choose By Entering A Number $W> \n"
        echo -e "\t 1] Yes    "
        echo -e "\t 2] No          \n"
        echo  -n""
        read sn
        echo ""
        case $sn in
            1 ) clear; getting_started;;
            2 ) clear; break;;
            * ) echo "Unknown option. Please choose again" ;;
          esac
    done

exit
}

echo " checking current connection"
getting_started

# 4 errors in a row happened, final version would have shut down by now, but for debugging purposes, and with network-manager STOPPED we will give
# users a command prompt to exit or continue -- even if away, at work, asleep, no further connection possible until you the user debugs the problems



exit
# so this script is sorta messy but it runs clean, funny when xfinity kicks your hour early, they still leave ya in limbo land connected
# and i hate that, if i fall asleep and well, ya know the drill,  they should just kick ya off, instead of hanging onto you in limbo
# Xfinity-4-Infinity -- the script that puts a stop to all that nonsence
# http://i.imgur.com/iZOtIte.png
