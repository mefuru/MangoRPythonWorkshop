
# Read in data 
filepath = "/Users/mehulmandania/Dropbox/sandbox/PythonRWorkshop/data"
input_file = open(filepath + "/Oxford.txt", 'rb')

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
            data = line.split()
            for field in fields[0:len(fields)]:
                if field==fields[0]:
                    D[field].append(data[0])
                elif field==fields[1]:
                    D[field].append(data[1])
                elif field==fields[2]:
                    D[field].append(data[2])
                elif field==fields[3]:
                    D[field].append(data[3])
                elif field==fields[4]:
                    D[field].append(data[4])
                elif field==fields[5]:
                    D[field].append(data[5])
                elif field==fields[6]:
                    D[field].append(data[6])
                elif field==fields[7]:
                    if len(data) < len(fields):
                        D[field].append("?")
                    else:
                        D[field].append(data[7])

print D['comments']
