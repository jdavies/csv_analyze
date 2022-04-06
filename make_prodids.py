#!/usr/bin/python

import sys

fileName = 'prodids.txt'
numIDs = int(sys.argv[1])

if len(sys.argv) != 2:
    print('Incorrect number of command line parameters!')
    print('Example Usage:')
    print('python make_prodids.py 75')
    sys.exit()

print('Creating ', numIDs, ' IDs')
with open(fileName, 'w') as out:
    for x in range(1,numIDs+1):
        prodid = 'L-' + str(x)
        out.write('{}\n'.format(prodid))

    out.close()
print("Done!")