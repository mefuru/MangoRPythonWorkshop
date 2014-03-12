# Read in data 
# Define a string variable called 'filepath' pointing to the location of the data
print 'Assuming input data files are in current working directory.'
filepath = ""
input_file = open(filepath + "Oxford.txt", 'rb')

# Initialise data structure
# A dictionary of lists, one for each column.
fields = ['year', 'month', 'tmax', 'tmin', 'af', 'rain', 'sun', 'comments']
D = {}
for f in fields:
    D[f] = []

for line in input_file:
    if line.startswith(' '):
        # Line is header or data
        line = line.strip()
        if line.startswith('yyyy'):
            # Line is header, store and add a comment column
            header = line.split() + ['comment']
        elif line.startswith('degC'):
            # Line is units of header, disregard for now
            continue 
        else:
            # Line is data
            data = line.split()
            for idx in range(len(fields)):

                # If line has right number of elements
                if idx < len(data):
                    D[fields[idx]].append(data[idx]) # Append data value
                else:
                    D[fields[idx]].append('?') # Pad with NaN value if not enough elements