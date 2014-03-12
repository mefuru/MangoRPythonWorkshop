# Exercise 1: Ex1.py

# Define a string variable called 'filepath' pointing to the location of the data
# filepath = ''
#

filepath = '/Users/mehulmandania/Dropbox/sandbox/PythonRWorkshop/data'

inputFile = open(filepath + "/WeatherStationsRaw.txt", 'rb')
outputFile = open(filepath + "/WeatherStations.csv", 'wb')

for line in inputFile:
    # Find the text for the url
    # 
    #
    url = line.split("\"")[1]
        
    # Find the text for the seather station name
    #
    #  
    station = line.split(">")[1:]
    station = station[0].split()
    station1 = station[0:len(station)-1]
    station1 = " ".join(station1)
    
    
    # Find the text for the date range after the weather name
    #
    #
    dateRange = station[len(station)-1].split("<")[0]    

    # Join up the strings, separated by commas
    #
    #
    
    join = ",".join([url, station1, dateRange])
    print(join)
    # Write to the output file
    #
    #
    outputFile.write(join + "\n")
        
outputFile.close()
