print 'This is the Kawee Help Program, using past trials to determine future cell values'
print 'Questions should be directed to Tom Tibbett'
print 'Created November 1st, 2015'

print 'Importing Relevant Libraries'

import pandas as pd
import numpy as np

print 'Importing Data...'

# What is your file named?  Make sure it is in the same folder as this Python script.
name = '47TwoStage_DevalP1en.dat'

# What do you want it to be called?  It will output in the same folder as the Python script.
txtout='47TwoStage_DevalP1en.txt'

print 'Success.'

print 'Converting to Pandas...'

df= pd.read_csv(name, delim_whitespace=True, header=None, names=None)

print 'Creating Column Names for Possible Debugging...'

df.columns= ['RT', 'Resp', 'CurrentState', 'PointsGold', 'PointsSilver', 'TrialType']

print 'Separating Two Trial Types via Sort...'
df['Index']=df.index
df=df.sort_values(['TrialType', 'Index'])

df=df[['RT', 'Resp', 'CurrentState', 'PointsGold', 'PointsSilver', 'TrialType']]
Silver=df[df.TrialType==0]
Silver=Silver[['RT','Resp', 'CurrentState', 'PointsSilver', 'TrialType']]
Gold=df[df.TrialType==1]
Gold=Gold[['RT','Resp', 'CurrentState', 'PointsGold', 'TrialType']]

print 'Correcting Coding Issues...'
Gold['PointsSilver']=0
Silver['PointsGold']=0
Silver=Silver.reset_index(drop='index')
Gold=Gold.reset_index(drop='index')

print 'Part I: Silver Trials'
print 'Creating Reward on Future Trial'
Silver['Reward']=0
count=0
while (count<49):
    if Silver.PointsSilver.ix[count]==100:
        Silver.Reward[count+1]=1
    else: 
        Silver.Reward[count+1]=-1
    count=count+1
print Silver

print 'Designating if Common or Rare'
Silver['Transition']=0
count=0
while (count<50):
    if Silver.Resp.ix[count]==1 and Silver.CurrentState.ix[count]==1:
        Silver.Transition[count]=1
    elif Silver.Resp.ix[count]==1 and Silver.CurrentState.ix[count]==0:
        Silver.Transition[count]=-1
    elif Silver.Resp.ix[count]==2 and Silver.CurrentState.ix[count]==0:
        Silver.Transition[count]=1
    elif Silver.Resp.ix[count]==2 and Silver.CurrentState.ix[count]==1:
        Silver.Transition[count]=-1
    else: Silver.Transition[count]=0
    count=count+1

print 'Noting if they Changed'
Silver['Stay']=1
count=2
while (count<50):
    if Silver.Resp.ix[count]==Silver.Resp.ix[count-1]:
        Silver.Stay.ix[count]=1
    else: 
        Silver.Stay.ix[count]=-1
    count=count+1

print 'Removing first trial'
Silver=Silver.ix[1:]
print 'Final Silver Dataset'
print Silver


print 'Part II: Gold Trials'
print 'Creating Reward on Future Trial'
Gold['Reward']=0
count=0
while (count<49):
    if Gold.PointsGold.ix[count]==100:
        Gold.Reward[count+1]=1
    else: 
        Gold.Reward[count+1]=-1
    count=count+1

print 'Designating if Common or Rare'
Gold['Transition']=0
count=0
while (count<50):
    if Gold.Resp.ix[count]==1 and Gold.CurrentState.ix[count]==1:
        Gold.Transition[count]=1
    elif Gold.Resp.ix[count]==1 and Gold.CurrentState.ix[count]==0:
        Gold.Transition[count]=-1
    elif Gold.Resp.ix[count]==2 and Gold.CurrentState.ix[count]==0:
        Gold.Transition[count]=1
    elif Gold.Resp.ix[count]==2 and Gold.CurrentState.ix[count]==1:
        Gold.Transition[count]=-1
    else: Gold.Transition[count]=0
    count=count+1

print 'Noting if they Changed'
Gold['Stay']=1
count=2
while (count<50):
    if Gold.Resp.ix[count]==Gold.Resp.ix[count-1]:
        Gold.Stay.ix[count]=1
    else: 
        Gold.Stay.ix[count]=-1
    count=count+1

print 'Removing first trial'
Gold=Gold.ix[1:]
print Gold

print 'Part III: Recombining Silver and Gold trials'
Full=[Silver, Gold]
final=pd.concat(Full)
final=final[['Stay','Reward', 'Transition', 'TrialType', 'PointsSilver', 'PointsGold', 'CurrentState', 'Resp', 'RT']]
print 'The Final Dataset for this Participant'
print final

final.to_csv(txtout, header=False, index=False, sep='\t')
print 'File creation complete!  Check if it is there!'