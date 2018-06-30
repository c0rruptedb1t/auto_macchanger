# auto_macchanger
A Script that automates changing your MAC Address after a certain amount of time, this can be used for getting around Captive Portals that assign a limited amount of data per device

## This script is made for Linux

## _Installation:_

Automatic
> $auto_macchanger.py -install

Manual
> $sudo sudo apt-get update;apt-get install net-tools macchanger -y

## _Usage:_
Examples:
> ./auto_macchanger.py -i wlan0 -t 120 -r

> ./auto_macchanger.py -A -b -i wlan0 

> ./auto_macchanger.py (default arguments: -i wlan0, -t 60, -r)
-------------------------
#### Basic Arguments:

>-h Displays help dialogue

>-install auto install/setup

>-i <interface>       e.g -i wlan0

>-t <amount of time>  e.g -t 60

#### Extra Arguments:

>-a uses same kind of MAC         

>-A uses any type of MAC   

>-r uses a random MAC          

>-b pretends to be a burned-in-address

-------------------------

