# -*- coding: utf-8 -*-
import urllib2
import json
from colorama import init
import sys
init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format


def currentweather():

    state = raw_input("Enter State:\n>")
    city = raw_input("Enter City:\n>")
    try:
        f = urllib2.urlopen('http://api.wunderground.com/api/19e8ddc94141aec0/'
                            'geolookup/conditions/q/'
                            + state + '/' + city + '.json')
        json_string = f.read()
        parsed_json = json.loads(json_string)
        location = parsed_json['location']['city']
        temp_f = parsed_json['current_observation']['temp_f']
        print "Current temperature in %s is: %s \n\n" % (location, temp_f)
        f.close()
    except KeyError:
        cprint("Failed to find location. Please try again.", 'cyan', 'on_red')
        currentweather()


def historyweather():
    state = raw_input("Enter State:\n>")
    city = raw_input("Enter City:\n>")
    yearfrom = raw_input("Enter Start Year:\n>")
    monthfrom = raw_input("Enter Start Month (number):\n>")
    dayfrom = raw_input("Enter Start Day:\n>")
    yearto = raw_input("Enter End Year:\n>")
    monthto = raw_input("Enter End Month (number):\n>")
    dayto = raw_input("Enter End Day:\n>")

    if len(dayto) < 2:
        dayto = "0" + dayto
    if len(dayfrom) < 2:
        dayfrom = "0" + dayfrom
    if len(monthto) < 2:
        monthto = "0" + monthto
    if len(monthfrom) < 2:
        monthfrom = "0" + monthfrom

    timefrom = int(yearfrom + monthfrom + dayfrom)
    timeto = int(yearto + monthto + dayto)

    if (timeto - timefrom) > 30:
        print ("Please select a shorter time range")
        historyweather()
    else:
        try:
            historybject = urllib2.urlopen('http://api.wunderground.com/api/'
                                           '19e8ddc94141aec0/history_'
                                           + yearfrom + monthfrom + dayfrom
                                           + '/q/' + state + '/' + city
                                           + '.json')
            json_string = historybject.read()
            parsed_json = json.loads(json_string)
            # location = parsed_json['location']['city']
            timestamp = parsed_json["history"]['date']['pretty']
            print(json_string)
            print timestamp
            historybject.close()
        except KeyError:
            cprint("Failed to find location. Please try again.", 'cyan',
                   'on_red')
            historyweather()


def forecast3():

    state = raw_input("Enter State:\n>")
    city = raw_input("Enter City:\n>")
    try:
        f = urllib2.urlopen('http://api.wunderground.com/api/19e8ddc94141aec0/'
                            'forecast10day/q/'
                            + state + '/' + city + '.json')
        json_string = f.read()
        parsed_json = json.loads(json_string)
        for datadicts in parsed_json['forecast']["simpleforecast"]["forecastday"]:
            for key, value in datadicts.items():
                if (key != "icon_url") and (key != "icon") and (key != "pop"):
                    print("%s: %s \n \n" % (key, value))
        # print(parsed_json)
        f.close()
    except KeyError:
        cprint("Failed to find location. Please try again.", 'cyan', 'on_red')
        currentweather()


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
        cprint("(1) Current Weather \n", 'cyan')
        cprint("(2) Historical Weather Query \n", 'cyan')
        cprint("(3) 10 Day Forecast \n", 'cyan')
        cprint("(4) Quit \n", 'red')

        mainquery = raw_input(">")
        if mainquery == "1":
            currentweather()
        elif mainquery == "2":
            historyweather()
        elif mainquery == "3":
            forecast3()
        # elif mainquery.upper() == "X":
        #     experiment()
        elif mainquery == "4":
            print(chr(27) + "[2J")
            quit()

        else:
            cprint("Not a Query. \n", 'cyan')

# program flow:
main()
