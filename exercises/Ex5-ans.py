# Exercise 5: Write data to a csv file. 
fields = ['year', 'month', 'tmax', 'tmin', 'af', 'rain', 'sun', 'comments']
n_lines = len(D['year']) 

out_file = open('OxfordData.csv', 'wb')

# Write Header 
out_file.write(','.join(fields) + '\n')

# Write data row by row.
for idx in range(n_lines):
    data2write = []
    for field in fields:
        
        # Clean up NaN elements
        if D[field][idx] == '---':
            D[field][idx] = '?'
        elif '*' in D[field][idx]:
            # Strip away '*' from values
            D[field][idx] = D[field][idx].strip('*')
        
        # List of data to write 
        data2write.append(D[field][idx]) 
    
    # Convert list to a string and write
    data_str = ','.join(data2write)
    out_file.write(data_str + '\n')

out_file.close()