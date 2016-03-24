import pandas as pd
import numpy as np

# What is your file named?  Make sure it is in the same folder as this Python script.
name = '47TwoStage_DevalP1en.dat'

# What do you want it to be called?  It will output in the same folder as the Python script.
txtout='47TwoStage_DevalP1en.txt'

df= pd.read_csv(name, delim_whitespace=True, header=None, names=None)

df.columns= ['RT', 'Resp', 'CurrentState', 'PointsGold', 'PointsSilver', 'TrialType']

df['Index']=df.index
df=df.sort_values(['TrialType', 'Index'])

df=df[['RT', 'Resp', 'CurrentState', 'PointsGold', 'PointsSilver', 'TrialType']]
Silver=df[df.TrialType==0]
Silver=Silver[['RT','Resp', 'CurrentState', 'PointsSilver', 'TrialType']]
Gold=df[df.TrialType==1]
Gold=Gold[['RT','Resp', 'CurrentState', 'PointsGold', 'TrialType']]
Gold['PointsSilver']=0
Silver['PointsGold']=0
Silver=Silver.reset_index(drop='index')
Gold=Gold.reset_index(drop='index')
print Silver

# Removing Non-Response Trials - Silver
before = len(Silver)
print "Silver Data"
print len(Silver)
Silver=Silver[Silver.Resp != -1]
after = len(Silver)
print "Participant Number of Trials:"
print len(Silver)
print "Non-Response Trials:"
print before - after
Silver['Reward']=0
Silver=Silver.reset_index(drop='index')

# Removing Non-Response Trials - Gold
before = len(Gold)
print "Gold Data"
print len(Gold)
Gold=Gold[Gold.Resp != -1]
after = len(Gold)
print "Participant Number of Trials:"
print len(Gold)
print "Non-Response Trials:"
print before - after
Gold['Reward']=0
Gold=Gold.reset_index(drop='index')

count=0
while (count<len(Silver)):
    if Silver.PointsSilver.ix[count]==100:
        Silver.Reward[count+1]=1
    else: 
        Silver.Reward[count+1]=-1
    count=count+1
Silver=Silver.reset_index(drop='index')
print Silver

Silver['Transition']=0
count=0
while (count<len(Silver)):
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
Silver

Silver['Stay']=1
count=2
while (count<len(Silver)):
    if Silver.Resp.ix[count]==Silver.Resp.ix[count-1]:
        Silver.Stay.ix[count]=1
    else: 
        Silver.Stay.ix[count]=-1
    count=count+1

Silver=Silver.ix[1:]
print Silver

Gold['Reward']=0
count=0
while (count<len(Gold)):
    if Gold.PointsGold.ix[count]==100:
        Gold.Reward[count+1]=1
    else: 
        Gold.Reward[count+1]=-1
    count=count+1

Gold['Transition']=0
count=0
while (count<len(Gold)):
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

Gold['Stay']=1
count=2
while (count<len(Gold)):
    if Gold.Resp.ix[count]==Gold.Resp.ix[count-1]:
        Gold.Stay.ix[count]=1
    else: 
        Gold.Stay.ix[count]=-1
    count=count+1

Gold=Gold.ix[1:]
print Gold

Full=[Silver, Gold]
final=pd.concat(Full)
final=final[['Stay','Reward', 'Transition', 'TrialType', 'PointsSilver', 'PointsGold', 'CurrentState', 'Resp', 'RT']]
print final

final.to_csv(txtout, header=False, index=False, sep='\t')

print "File creation complete"