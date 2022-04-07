#!/usr/bin/python

# # CSV_Analyze.py

import sys
import csv

def dataSizeName(numBytes: int):
    kilobyte = 1024
    megabyte = kilobyte*1024
    gigabyte = megabyte * 1024
    terabyte = gigabyte * 1024

    if numBytes < kilobyte:
        return '{} bytes'.format(numBytes)
    if numBytes < megabyte:
        decVal = numBytes / kilobyte
        return '{:0.2f} K'.format(decVal)
    if numBytes < gigabyte:
        decVal = numBytes / megabyte
        return '{:0.2f} MB'.format(decVal)
    if numBytes < terabyte:
        decVal = numBytes / gigabyte
        return '{:0.2f} GB'.format(decVal)
    else:
        return 'An error occured formatting the nmber {}.'.format(numBytes)

fileName = sys.argv[1]

print('Analyzing ', fileName)
# Open the filename specified on the command line
file = open(fileName)
csvreader = csv.reader(file)

# Extract thefield names
header = []
header = next(csvreader)

# print('Headers', str(header))

# Create an array to hold the largest data size for each field.
dataSize = []

rowCount = 0
for row in csvreader:
    numFields = len(row)
    # print('numFields = ', numFields)
    
    for x in range(0, numFields):
        # print('x is ', x)
        dataField = row[x]
        if rowCount == 0:
            # This is the first row of data. Store the field size
            dataSize.insert(x, len(dataField))
            # print('x is ZERO')
        else:
            # print('x = ', x)
            # Compare the length of this field to the current largest length
            if(dataSize[x] < len(dataField)):
                # New field is larger! Record it
                # print('replacing field ', x, ' old val = ', dataSize[x], ' with new value ', len(dataField))
                dataSize[x] = len(dataField)
            # else:
                # print('NOT replacing field ', x, ' old val = ', dataSize[x], ' with new value ', len(dataField))
    rowCount += 1
file.close()

# Display our findings
print('Field                    Size')
print('=======================  ==========')
for x in range(0, len(header)):
    print(header[x].ljust(24), dataSizeName(dataSize[x]))
