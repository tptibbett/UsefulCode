#################################################################################################
# SEM Election Data
# Explores what's influencing Life Satisfaction scores
# For questions, contact Tom Tibbett
# Last Run: 12/03/2016
# This was simplified from a project involving the 2016 US Election
# This involves a mediation analysis of decisional procrastination scores + correlation matrix
#################################################################################################

# Clearing environment
rm(list=ls())

#install.packages('lavaan') # Not needed if you've done it once.
library('lavaan')

# My working directory.  You'll have to change it to where your data are stored.
getwd()
setwd("C:/Users/tptibbett/Documents/1 Graduate Psychology/Studies/2015 Proc and Regret/")

# Reads in your full data set.
# Keep in mind that I cannot post the .csv file per DePaul's IRB.
df=read.table("MediationUSDPonly.csv",sep=",",header=TRUE, fill=TRUE)

names(df) <- c("Career", "Community", "Education", "Parenting", "Family", "Finance",
               "Friends", "Health", "Leisure", "Romance", "Spirituality", "Self",
               "Regret", "LS", "DP")

#################################################################
# Simple Mediation Model
#################################################################

# Creating the model
# It's very easy to turn this into a more complicated SEM.
# Simply add more paths!
model <- '
# direct effect
  LS ~ c*DP
# mediator
  Regret ~ a*DP
  LS ~ b*Regret
# indirect effect (a*b)
  ab := a*b
# total effect
  total := c + (a*b)
'

# Creating an equation
fit <- sem(model, test = "bootstrap",
           data=df)

# Giving fit indices and pathway significance results
summary(fit, fit.measures=TRUE, standardized=TRUE)

#################################################################
# Correlation Matrix
#################################################################

library('Hmisc')

mat<-rcorr(as.matrix(df))
P<-data.frame(round(mat$P, 2))
r<-data.frame(round(mat$r, 2))

write.csv(r, file="CorrelationMatrixDVs.csv")
write.csv(P, file="PvaluesDVs.csv")
