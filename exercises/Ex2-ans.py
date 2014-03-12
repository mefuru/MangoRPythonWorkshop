import urllib2

# Define a string variable called 'filepath' pointing to the location of the data
print 'Assuming input data files are in current working directory.'
filepath = ""
baseurl = 'http://www.metoffice.gov.uk'

# Read in cleaned csv data on weather station information from WeatherStations.txt
inputFile = open(filepath + "WeatherStations.csv", 'rb')

for line in inputFile:
    parts = line.split(',')
    
    # fetch url    
    dataurl = baseurl + parts[0]
    
    # fetch data via url
    dataset = urllib2.urlopen(dataurl)
    
    # fetch name
    station_name = parts[1]

    # write data to disk with a file name = station name
    outputFile = open(filepath + station_name + '.txt', 'wb')
    outputFile.writelines(dataset)
    outputFile.close()