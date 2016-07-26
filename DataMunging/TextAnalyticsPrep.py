# Text Analytics Preparation
# First Created: 6/27/2016
# Purpose: 	Public access data is transformed to conduct Text Analysis in SAP HANA.
#			This ordinarily can be done in Excel, but if people do not have Excel, this
#			comma removal may prove useful.
# Please direct questions to Tom Tibbett: tptibbett@gmail.com
# Last executed: 07/25/2016

# Input: 	Consumer Complaints data, primarily qualitative data.
#			Consumer_Complaints.csv from https://catalog.data.gov/dataset/cgb-consumer-complaints-data
# Output:	ConsCompCommaControl.csv
# Next:		Utilize SAP Predictive Analytics to Data Transfer into SAP: HANA.

# Import essential packages
import pandas as pd
import numpy as np
pd.options.display.max_colwidth=0 # To see full text for long entries.
pd.set_option('chained_assignment',None) # Eliminates chained assignment warning.

print 'Reading the csv file...' # Instructions to get this file are above.
df = pd.read_csv('Consumer_Complaints.csv')
print 'Putting commas in quotes as an escape when re-reading this as a CSV file'
print 'Filtering out junk symbols...'
df.replace({',': '\",\"', #So that calling this from a .CSV will not be confused.
            '/':' ',
            '-':'',
            '\\n':''}, regex=True, inplace=True)
print 'Done!'

# DataFrame Architecture
print 'DataFrame Dimensions.'
print df.shape
print 'Column Names'
print df.columns

# Finding Missing Values
print ''
print 'In the Customer Complaints column, here are the number of missing values.'
print df['Consumer complaint narrative'].isnull().sum()
s=df['Consumer complaint narrative'].astype(str).map(len)

# Identifying lengthy complaints
print 'HANA has a character limit of 5000 for each.  The following entries are too long:'
toolong=pd.DataFrame(s[s>5000]).reset_index()
toolong.columns=['ID', 'Length']
print toolong

# Listing the lengthy complaints
for i in toolong.ID:
    print 'ID number:', i
    print df['Consumer complaint narrative'][i]

# Changing complaints and comparing lengths
for i in toolong.ID:
    old=len(df['Consumer complaint narrative'][i])
    df['Consumer complaint narrative'][i]=df['Consumer complaint narrative'][i].replace(" ...", "")
    print 'ID', i, '\tOld Length:', old, '\tNew Length:', len(df['Consumer complaint narrative'][i])
    print df['Consumer complaint narrative'][i]

# Output Stage
print 'Now printing to your local drive...'
df.to_csv('ConsCompCommaControl.csv', sep=',')
print 'All finished!'