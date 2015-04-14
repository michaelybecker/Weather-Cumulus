# -*- coding: utf-8 -*-
import urllib2
import json
from colorama import init
import sys
init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format


def main():
    """main program window"""
    print(chr(27) + "[2J")
    print ("\n\n\n\n\n\n\n\n\n")
    cprint(figlet_format('CUMULUS', font='basic'), 'cyan',
           attrs=['bold'])
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    cprint("Welcome to CUMULUS. \n", 'cyan')

    while True:
        cprint("Enter Query: \n", 'cyan')
        mainquery = raw_input(">")
        if mainquery == "current weather":
            currentweather()
        elif mainquery == "quit":
            quit()
        elif mainquery == "weather history":
            historyweather()
        else:
            cprint("Not a Query. \n", 'cyan')

# program flow:
main()
