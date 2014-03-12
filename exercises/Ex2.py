import urllib2

# Define a string variable called 'filepath' pointing to the location of the data
filepath = '/Users/mehulmandania/Dropbox/sandbox/PythonRWorkshop/data/WeatherStations.csv'
baseurl = 'http://www.metoffice.gov.uk'
savefilepath = '/Users/mehulmandania/Dropbox/sandbox/PythonRWorkshop/data'

# Read in cleaned csv data on weather station information from WeatherStations.txt
inputFile = open(filepath, 'rb')

# For each line in the cleaned file, 
# 		get url
#       get name 
#       get data via url
#		write data to disk with a file name = station name
for line in inputFile:
    data1 = line.split(",")
    url =  baseurl + data1[0]
    data = urllib2.urlopen(url)
    lines = data.readlines()
    print lines
    filename =  "/" + data1[1] + ".txt"
    outputFile = open(savefilepath + filename, 'wb')
    outputFile.writelines(lines)
    outputFile.close()
