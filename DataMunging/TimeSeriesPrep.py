# Time Series Preparation
# Purpose: To transpose and combine various CSV files in preparation for time series analysis.
# Please direct questions to Tom Tibbett: tptibbett@gmail.com
# Last executed: 07/18/2016

# Data:		This theoretical data assumes 3 years and 2 months of monthly data from Jan 2012 to
#			February 2015.  The client would eventually like to predict Units Sold via 
#			external factors and the Price they're paying/selling the Units for.  All of these
#			are in different CSV files with inconsistent formatting.
# Input: 	Units Sold data file, Externalities data file, Price In and Out data file
#			These can be found for each customer (a store chain) but since 
#			they may have multiple pages, save them to CSV first.
# Output:	pivoted_set.csv
#			customer_merged_data_with_ext.csv
#			ext_sellinout_merged 	======	Final Dataset
# Next:		Utilize TimeSeries.R for forecasting

# Part 1: Transposing Dataset for Time Series.
import pandas as pd
import numpy as np
import datetime
from dateutil.rrule import rrule, MONTHLY
df=pd.read_csv('UnitsSoldData.csv')

df = df.drop(['Rim', 'Region'], axis=1)
print df.head()

pivoted=pd.pivot_table(df, index=['Material'])

# # If you have a promotional calendar, 
# # you can use this and tweak the above code to create a separate Promo dataset.
# # This can later be combined as dummy codes in the R model.

# base = datetime.date(month=1, day=1, year=2012)
# date_list=list(rrule(freq=MONTHLY, count=38, dtstart=base))
# date_list=pd.to_datetime(date_list)
# for i in date_list:
#    df[i]=0
# print df.columns
# print df['Product Line'].value_counts()

# # It's a little hacky, but promo calendars may need to be hardcoded.
# # We use dummy codes here for the time series analysis to indicate
# # if the product line was on sale during that month (yes/no).

# # Promotional Calendar - Mango
# df.loc[df['Product Line']=='Mango', '2012-02-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2012-03-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2012-04-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2012-05-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2012-09-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2012-10-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2012-11-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2012-12-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2013-01-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2013-03-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2013-04-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2013-05-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2013-06-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2013-07-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2013-08-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2013-09-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2013-10-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2013-11-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2013-12-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2014-01-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2014-02-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2014-03-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2014-04-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2014-05-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2014-06-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2014-07-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2014-08-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2014-09-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2014-10-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2014-11-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2014-12-01 00:00:00']=1
# df.loc[df['Product Line']=='Mango', '2015-01-01 00:00:00']=1
# # Promotional Calendar - Pineapple
# df.loc[df['Product Line']=='Pineapple Co.', '2012-05-01 00:00:00']=1
# df.loc[df['Product Line']=='Pineapple Co.', '2012-06-01 00:00:00']=1
# df.loc[df['Product Line']=='Pineapple Co.', '2012-07-01 00:00:00']=1
# df.loc[df['Product Line']=='Pineapple Co.', '2012-08-01 00:00:00']=1
# df.loc[df['Product Line']=='Pineapple Co.', '2012-09-01 00:00:00']=1
# df.loc[df['Product Line']=='Pineapple Co.', '2012-10-01 00:00:00']=1
# df.loc[df['Product Line']=='Pineapple Co.', '2013-03-01 00:00:00']=1
# df.loc[df['Product Line']=='Pineapple Co.', '2013-04-01 00:00:00']=1
# df.loc[df['Product Line']=='Pineapple Co.', '2013-05-01 00:00:00']=1
# df.loc[df['Product Line']=='Pineapple Co.', '2013-06-01 00:00:00']=1
# df.loc[df['Product Line']=='Pineapple Co.', '2013-07-01 00:00:00']=1
# # Promotional Calendar - Crabapple
# df.loc[df['Product Line']=='Crabapples to Apples', '2012-05-01 00:00:00']=1
# df.loc[df['Product Line']=='Crabapples to Apples', '2012-06-01 00:00:00']=1
# df.loc[df['Product Line']=='Crabapples to Apples', '2012-07-01 00:00:00']=1
# df.loc[df['Product Line']=='Crabapples to Apples', '2012-08-01 00:00:00']=1
# df.loc[df['Product Line']=='Crabapples to Apples', '2012-09-01 00:00:00']=1
# df.loc[df['Product Line']=='Crabapples to Apples', '2012-10-01 00:00:00']=1

pivoted=pivoted.transpose() # Transposes data set.
pivoted.reset_index(inplace=True)
pivoted.rename(columns = {'index':'Date'}, inplace = True)
pivoted=pivoted.sort_values(by='Date', ascending=True)
pd.to_datetime(pivoted['Date'], format='%b-%y') # Dates are recognized.
print pivoted
pivoted.to_csv('pivoted_set.csv', index=False) # Save Point

# Part 2: Merging External Factors
df= pd.read_csv('pivoted_set.csv') # Reloading data set from source folder.
df.Date=pd.to_datetime(df.Date, format='%Y-%m-%d')

ext=pd.read_csv('External.csv') # Externalities Dataset
print ext.shape
ext=ext[["Date", "DispInc", "VMT", "ConSent", "LVSAAR", "CommSAAR", "ISRatio", "GasPrice"]] # Only includes what we're interested in.
ext=ext.head(38) # There should not be any data after 38 months; preventing extra rows from CSV.
ext.Date=pd.to_datetime(ext.Date, format='%m/%d/%y') # Converting to datetime here.  Note the different format.

data=pd.merge(df, ext, on='Date', how='left') # Joining externalities dataset to the time series.
data['Date'] =  pd.to_datetime(data['Date'], infer_datetime_format=True)
data=data.sort_values(by='Date', ascending=1) # Sorting by ascending Date for Time Series.
print data

data.to_csv('customer_merged_data_with_ext.csv', index=False) # Save Point

#Part 3: Adding Price In/Price Out
sellin=pd.read_csv('Sellin.csv', header=1) # Sell In Prices Data from Partner: Note that the header skips a line.
sellout=pd.read_csv('Sellout.csv', header=1) # Sell Out Prices Data from Partner

obs=[sellin.iloc[:,0], sellin.iloc[:,10:47]] # Subsetting...
obs2=[sellout.ix[:,0], sellout.ix[:,10:47]]
print obs.head()

sellin.set_index("Material", inplace=True) # Index becomes column Material for transposition 
sellout.set_index("Material", inplace=True)
sellin=sellin.transpose()
sellout=sellout.transpose()

sellin=sellin.reset_index()
sellin.columns = [str(col) + '_in' for col in sellin.columns] # adds '_in' to each column to denote this column deals with Price In
sellin['index_in']= pd.to_datetime(sellin['index_in'], format='%b-%y')
print sellin

sellout=sellout.reset_index()
sellout.columns = [str(col) + '_out' for col in sellout.columns] # See above, but adds '_out'
sellout['index_out']= pd.to_datetime(sellout['index_out'], format='%b-%y')
print sellout

sell=pd.merge(sellin,sellout,left_on='index_in', right_on='index_out', how='left') # Merging Price In and Price Out to each other.
print sell.columns

ext=pd.read_csv('customer_merged_data_with_ext.csv') # Load merged with externalities data set
ext.Date=pd.to_datetime(ext.Date, format='%Y-%m-%d')
print ext.shape

data=pd.merge(ext, sell, left_on='Date', right_on='index_in', how='left')
data['Date'] =  pd.to_datetime(data['Date'], infer_datetime_format=True)
data=data.sort_values(by='Date', ascending=1) # Sorting by ascending Date for Time Series.
print data.shape
data.drop('index_in', axis=1, inplace=True)
data.drop('index_out', axis=1, inplace=True)
print data

data.to_csv('ext_sellinout_merged.csv', index=False) # Final Dataset to be inserted into R code.