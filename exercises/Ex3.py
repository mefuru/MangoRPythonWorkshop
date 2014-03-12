# Exercise 3: Ex3.py

import sys
import urllib2
 
arg1 = sys.argv[1] # First positional argument
arb2 = sys.argv[2] # Second positional argument

baseurl = 'http://www.metoffice.gov.uk'


# Read in cleaned csv data on weather station information from WeatherStations.txt

# Find the url ending for the station name specified with arg1

# Fetch data via web 

# Write to the output location specified with arg2 