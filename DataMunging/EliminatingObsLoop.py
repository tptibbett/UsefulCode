# Eliminating Observations on Separate files
# Date of Creation: 07/25/2016
# Created by Tom Tibbett
# Purpose: Eliminate observations amongst several files simultaneously.

# Importing relevant libraries
import numpy as np
import pandas as pd
import glob
import os

filelist= [] # Blank lists we'll reference later.
nonext=[]

# Change directories to the relevant ones.
my_dir = "C:\Users\I856176\Documents\Python Scripts\IAPS"
output = "C:\Users\I856176\Documents\Python Scripts\IAPS\Output"
os.chdir( my_dir )

# Creating lists for the loop to reference.
for files in glob.glob("*.dat"):
    fileName, fileExtension = os.path.splitext(files)
    nonext.append(fileName) #filename without extension
    filelist.append(files) #filename with extension

excl=[3, 25, 26, 33, 36, 44, 45, 46, 52, 54, 72, 82, 86, 87, 88, 90, 91, 92, 93, 97] # Picture Numbers to be excluded
print 'Observations to be removed:'
print excl, '\n'
excl[:] = [x - 2 for x in excl] # Correcting for Python's indexing

print 'Now Writing to Output Folder...'
for i in filelist:
    data=pd.read_csv(i, header=None, sep='\s+')
    data=data.sort_values(9, ascending=True).reset_index(drop='index') # Sorting so that this is easier.
    data=data.drop(data[9][excl]) # Drops the pictures we do not want.
    #Printing to another folder because we do not want the files overriden.
    #Ideally, this should be an empty folder beforehand.
    data.to_csv(str(output) + str("\\") + i, header=None, index=False, sep='\t') 
    print i, '\t\tWritten'
print 'Complete!'