#!/usr/bin/python

# CSV_Analyze.py

import sys
import os.path
import csv

# Global variables

header = []
maxFieldSize = []

def data_size_name(numBytes: int):
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

def process_file(fileName: str):
    global maxFieldSize
    # Open the filename specified on the command line
    file = open(fileName)

    csvreader = csv.reader(file)

    # Skip over the field names
    next(csvreader)

    rowCount = 0
    for row in csvreader:
        numFields = len(row)
        
        for x in range(0, numFields):
            dataField = row[x]
            if rowCount == 0:
                # This is the first row of data. Store the field size
                maxFieldSize.insert(x, len(dataField))
            else:
                # Compare the length of this field to the current largest length
                try:
                    if(maxFieldSize[x] < len(dataField)):
                        # New field is larger! Record it
                        maxFieldSize[x] = len(dataField)
                    break
                except IndexError:
                    print("index error where x = ", x, " where rowCount == ", rowCount)
        rowCount += 1
    file.close()


def process_directory(dirName: str):
    # Open the directory and readand process each file it contains.
    global header

    curFileIndex = 0
    for fileName in os.listdir(dirName):
        if fileName.endswith(".csv"):
            print("Processing: ", os.path.join(dirName, fileName))
            if curFileIndex == 0:
                # We are processing the first file. Extract the headers.
                # Open the filename specified on the command line
                file = open(dirName + "/" + fileName)
                csvreader = csv.reader(file)

                # Extract thefield names
                header = next(csvreader)
                file.close

            process_file(dirName + "/" + fileName)
            # Move to the next file
            curFileIndex += 1 





# Main Program Body
fileName = sys.argv[1]

print('Analyzing ', fileName)

if os.path.isfile(fileName):
    print(fileName, ' is a file')
    process_file(fileName)

if os.path.isdir(fileName):
    print(fileName, ' is a directory')
    process_directory(fileName)

# Display our findings
print('Field                    Size')
print('=======================  ==========')
for x in range(0, len(header)):
    print(header[x].ljust(24), maxFieldSize[x])
