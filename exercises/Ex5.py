
# NOTE: You will need to already have constructed the dictionary D in memory.

# Write data to a csv file. 
fields = ['year', 'month', 'tmax', 'tmin', 'af', 'rain', 'sun', 'comments']
n_lines = len(D['year']) 

out_file = open('OxfordData.csv', 'wb')

# Write Header 
#
#

# Write data row by row.
for idx in range(n_lines):
    data2write = []
    for field in fields:
        D[field][idx] = D[field][idx].replace("*","")
        print D[field][idx]
        if D[field][idx] == '---':
            D[field][idx] = '?'
        # Clean up NaN elements
        #
        #
        # Remove '*' from values
        #
        #
        #
        #

        # List of data to write 
        data2write.append(D[field][idx]) 
    
    # Convert list to a string and write
    data_str = ','.join(data2write)
    out_file.write(data_str + '\n')

out_file.close()
