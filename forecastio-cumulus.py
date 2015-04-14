# -*- coding: utf-8 -*-
import forecastio
import datetime
import urllib2
import calendar
from colorama import init
import sys
init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format
import json

api_key = "f71f75cd9e99dbc211c6e48ceaae557c"

home_lat = 47.705936
home_long = -122.320500
time = (2015, 4, 14, 2, 17)
forecast = forecastio.load_forecast(api_key, home_lat, home_long)

# for instances where the wrapper doesn't work:
manualforecast = urllib2.urlopen("https://api.forecast.io/forecast/"
                                 "f71f75cd9e99dbc211c6e48ceaae557c/"
                                 "47.705936,-122.320500")
json_string = manualforecast.read()

parsed_json = json.loads(json_string)


def dt(u):
    """return utc from unix time"""
    return datetime.datetime.utcfromtimestamp(u)


def ut(d):
    """return unix time from utc"""
    return calendar.timegm(d.timetuple())


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
        cprint("(1) Forecast for today \n", 'cyan')
        cprint("(2) Forecast for this week \n", 'cyan')
        cprint("(3) Advanced Queries \n", 'cyan')
        cprint("(4) Quit \n", 'red')

        mainquery = raw_input(">")
        if mainquery == "1":
            one()
        elif mainquery == "2":
            two()
        elif mainquery == "3":
            three()
        elif mainquery.upper() == "X":
            experiment()
        elif mainquery == "4":
            print(chr(27) + "[2J")
            quit()

        else:
            cprint("Not a Query. \n", 'cyan')


def one():
    """Get hourly forecast for the next 24 hrs"""
    hourly = forecast.hourly()
    print hourly.summary
    print ("\n\n\n\n")


def two():
    """Get daily forecast for the next week"""
    daily = forecast.daily()
    print daily.summary
    print ("\n\n\n\n")


def three():
    cprint("Enter Query: \n", 'cyan')
    cprint("(1) Minute Data for the next hour \n", 'cyan')
    cprint("(2) Hourly Data for the next 48 hours \n", 'cyan')
    cprint("(3) Daily Data for the next week  \n", 'cyan')
    cprint("(4) Quit to Main Menu \n", 'red')

    advquery = raw_input(">")
    if advquery == "1":
        newdict = parsed_json['minutely']['data'][0]
    elif advquery == "2":
        newdict = parsed_json['hourly']['data'][0]
    elif advquery == "3":
        newdict = parsed_json['daily']['data'][0]
    elif advquery.upper() == "X":
        pass
    elif advquery == "4":
        print(chr(27) + "[2J")
        main()

    else:
        cprint("Not a Query. \n", 'cyan')

        # jsonfile = forecast.json
    newdict = parsed_json['hourly']['data'][0]
    # for key, value in newdict.values():
    #    print("%s: %s \n" % (key, value))

    for key, value in newdict.items():
        if (key != "icon"):
            cprint("%s: %s \n" % (key, value), 'blue')
    print ("\n\n\n\n\n")


def experiment():
    # jsonfile = forecast.json
    newdict = parsed_json['hourly']['data'][0]
    # for key, value in newdict.values():
    #    print("%s: %s \n" % (key, value))

    for key, value in newdict.items():
        if (key != "icon"):
            cprint("%s: %s \n" % (key, value), 'blue')
    print ("\n\n\n\n\n")

# program flow:
main()
