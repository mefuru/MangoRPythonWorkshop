# Exercise 1: Answer
#
# Define a string variable called 'filepath' pointing to the location of the data
print 'Assuming input data files are in current working directory.'
filepath = ""

inputFile = open(filepath + "WeatherStationsRaw.txt", 'rb')
outputFile = open(filepath + "WeatherStations.csv", 'wb')

for line in inputFile:
    # Find the text for the url
    url = line.split('"')[1]
    
    # Find the text for the Weather Name
    x = line.split('>')[1]
    nameDateText = x.split('<')[0]
    nameParts = nameDateText.split()
    nameText = ' '.join(nameParts[:-1])
    
    # Find the text for the date range after the weather name
    dateText = nameParts[-1]

    # Join up the strings, separated by commas
    outputline = ','.join([url, nameText, dateText]) 

    # Write to the output file
    outputFile.write(outputline + '\n')

outputFile.close()