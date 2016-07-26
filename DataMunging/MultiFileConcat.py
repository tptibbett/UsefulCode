# Multiple File Concatenation
# Date of Creation: 07/25/2016
# Created by Tom Tibbett
# Purpose: Union all files of a certain type in one working directory.

import os # to make things non-specific to OS.
import numpy as np            
import pandas as pd
import glob 

# Remember, this is specifically for files that have the same columns.  They need to all be in the same folder.
path = r'C:\\Users\\I856176\\Documents\\Python Scripts\\IAPS\\Output'

# Be very careful! If you don't have your output in a different place, it will concatenate with the other files if you run this alone!
output= r'C:\\Users\\I856176\\Documents\\Python Scripts\\IAPS\\Output\\IAPSimages.csv'
all_files = glob.glob(os.path.join(path, "*.dat")) # Selects all .dat files in this path.  Make sure you want to concat all .dat files!

# Concatenates all files into one pandas DataFrame.
df = pd.concat(pd.read_csv(f, header=None, 
                           index_col=False, usecols=[0,1,2,3,4,5,6,7,8,9], sep='\t',
                          names=['Col_1', 'Col_2', 'Col_3', 'Col_4', 'Col_5', 'Col_6', 'Col_7', 'Col_8', 'Col_9', 'IAPSPic']) 
               for f in all_files) 

# What does our data set look like?
print len(all_files), 'files to be concatenated, with', len(df)/len(all_files), 'observations per file.\n'
print 'Preview...\n'
print df.head(9)
print '\nDataFrame Dimensions:'
df.shape

# Printing amalgamated file to a singular CSV file.
df.to_csv(output, index=False, header=False)