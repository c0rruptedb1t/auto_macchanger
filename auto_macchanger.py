#!/usr/bin/python3

'''
auto_macchanger - c0rruptedb1t
'''

import sys, getopt, os, time

timer = float(60)
randommac = int(0) #0 - random, 1 - same type, 2 - any type
burnedin = False
interface = str("wlan0")
count = int(0)
invpass = False

def macloop(rand, burn, intr, tmr):
    generator = str()
    bia = str(" ")
    tmptimr = tmr
    if (rand == 0):
        generator = str("-r")
    if (rand == 1):
        generator = str("-a")
    if (rand == 2):
        generator = str("-A")
    if (burn == True):
        bia = " -b "
    print(intr)
    print(tmr)
    while True:
        os.system("clear")
        print("Changing MAC in " + str(tmptimr) + " seconds...")
        tmptimr -= 1
        if (tmptimr < 0):
            print("Changing MAC Address...")
            os.system("sudo ifconfig " + intr + " down")
            os.system("sudo macchanger " + generator + bia + intr)
            os.system("sudo ifconfig " + intr + " up")
            tmptimr = tmr
            print("Changed MAC Successfully!")
        time.sleep(1)

def install():
    os.system("sudo apt update")
    os.system("sudo apt install macchanger net-tools -y")
    print("If all went right then the script should be ready to go!")

def help():
    print("auto_macchanger.py help")
    print("")
    print("-------------------------")
    print("Basic Arguments:")
    print("-h Displays help dialogue")
    print("-install auto install/setup")
    print("-i <interface>       e.g -i wlan0")
    print("-t <amount of time>  e.g -t 60")
    print("")
    print("Extra Arguments:")
    print("-a uses same kind of MAC             ")
    print("-A uses any type of MAC             ")
    print("-r uses a random MAC                 ")
    print("-b pretends to be a burned-in-address  ")
    print("-------------------------")
    print("")


if (os.name == "nt"):
    print("This program is not designed to run on a Windows System. Use a Linux System instead")
else:
    for i in sys.argv:
        if (i == "-r"):
            randommac = 0
        elif (i == "-i"):
                interface = sys.argv[count+1]
                count += 1
                invpass = True
        elif (i == "-t"):
                timer = float(sys.argv[count])
                count += 1
                invpass = True
        elif (i == "-A"):
            randommac = 2
        elif (i == "-a"):
            randommac = 1
        elif (i == "-b"):
            burnedin = True
        elif (i == "-h"):
                help()
                sys.exit(0)
        elif (i == "-install"):
                install()
                sys.exit(0)
        elif (i == "auto_macchanger.py"):
            print("")
        else:
            if (invpass == False):
                print("Improper Argument: " + str(i))
                help()
                sys.exit(2)
            invpass = False
        count += 1

    print("Using Interface: " + str(interface))
    print("Will change MAC Address every: " + str(timer) + " seconds")
    if (randommac == 0):
        print("Using random MAC Addresses...")
    elif (randommac == 1):
        print("Using MAC Addresses of Same Type...")
    elif (randommac == 2):
        print("Using MAC Addresses of Any Kind...")
    if (burnedin == True):
        print("Pretending to be a burned-in-address")

    macloop(randommac, burnedin, interface, timer)
