#################################################################################################################
# SEM Election Data
# For questions, contact Tom Tibbett
# Last Run: 12/03/2016
# Purpose: Comparing SEM model fit indices to explore what's influencing Life Satisfaction scores 
#################################################################################################################

# Clearing environment
rm(list=ls())

# install.packages('lavaan') # Not needed if you've done it once.
library('lavaan')

# My working directory.  You'll have to change it to where your data are stored.
getwd()
setwd("C:/Users/Tom/Analyses")

# Reads in your full data set.
# Keep in mind that I cannot post the .csv file per my IRB.
df=read.table("mediationanalyses2.csv",sep=",",header=TRUE, fill=TRUE)

# Create a dataset with just the relevant columns.
mediation <- data.frame(cbind(df$difMF, df$diffreqang, df$diffreqsca, 
                   df$How.surprised.will.you.be.if.Donald.Trump.is.elected.president., 
                   df$How.satisfied.are.you.feeling.with.your.life..all.things.considered.,
                   df$How.frequently.today.did.you.think.about.Donald.Trump.being.elected.president.,
                   df$trump.v.clinton.only, df$How.frequently.today.did.you.feel.this.way.about.Donald.Trump.being.elected.president..angry,
                   df$How.frequently.today.did.you.feel.this.way.about.Donald.Trump.being.elected.president..Scared))

# Makes the column names way more reasonable.
colnames(mediation) <- c( 'difMF', 'diffreqang', 'diffreqsca', 'T1FTSUP', 'T2LS', 
                          'T2EFT', 'Candidates2', 'T2angfreq', 'T2scafreq' )

#################################################################
# Proposed Model
#################################################################

model <- '
# regression pathways
  difMF ~ Candidates2
  T1FTSUP ~ Candidates2
  T2EFT ~ T1FTSUP
  diffreqang ~ T2EFT 
  diffreqsca ~ T2EFT
  T2LS ~ Candidates2 + difMF + diffreqang + diffreqsca
'

# Creating an equation
fit <- sem(model, test = "bootstrap",
           data=mediation)

# Giving fit indices and pathway significance results
summary(fit, fit.measures=TRUE, standardized=TRUE)

# Finished the First Model.

################################################################
# Revised Model
################################################################

model2 <- '
# regression pathways
  difMF ~ Candidates2
  T1FTSUP ~ Candidates2
  T2EFT ~ T1FTSUP
  diffreqang ~ T2EFT 
  diffreqsca ~ T2EFT
  T2LS ~ Candidates2 + difMF 
'

# Creating an equation
fit2 <- sem(model2, test = "bootstrap",
           data=mediation)

# Giving fit indices and pathway significance results
summary(fit2, fit.measures=TRUE, standardized=TRUE)

# Finished the Second Model

################################################################
# Below substitutes the Difference Scores with T2 scores
################################################################

model3 <- '
# regression pathways
  difMF ~ Candidates2
  T1FTSUP ~ Candidates2
  T2EFT ~ T1FTSUP
  T2angfreq ~ T2EFT 
  T2scafreq ~ T2EFT
  T2LS ~ Candidates2 + difMF + T2angfreq + T2scafreq
'

# Creating an equation
fit <- sem(model3, test = "bootstrap",
           data=mediation)

# Giving fit indices and pathway significance results
summary(fit, fit.measures=TRUE, standardized=TRUE)


# Finished the Third Model

################################################################
# Inserting Direct Lines to Difference of Anger and Scared
################################################################

model4 <- '
# regression pathways
difMF ~ Candidates2
T1FTSUP ~ Candidates2
T2EFT ~ T1FTSUP
diffreqang ~ T2EFT + Candidates2 
diffreqsca ~ T2EFT + Candidates2
T2LS ~ Candidates2 + difMF 
'

# Creating an equation
fit <- sem(model4, test = "bootstrap",
           data=mediation)

# Giving fit indices and pathway significance results
summary(fit, fit.measures=TRUE, standardized=TRUE)


# Finished the Fourth Model