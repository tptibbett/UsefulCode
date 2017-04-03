##############################################################################
# Internal Consistency Reliability
# Created by Tom Tibbett
# Last Executed: 01/12/2017
##############################################################################
# Clearing the Workspace
rm(list=ls())

#install.packages("irr")
library("irr")
setwd("f:/Dissertation/PCSpipeline/PCSpipeline/Pipeline/ICCData")

# Fluency ####################################################################
sink("../Scripts/Output/ICC/Fluency.txt", append=FALSE, split=FALSE)
lf <- read.csv(file="Fluency_LaurenCoding.csv",head=TRUE,sep=",")
nf <- read.csv(file="Fluency_NaaCoding.csv",head=TRUE,sep=",")
mf <- read.csv(file="Fluency_MadisonCoding.csv", head=TRUE, sep=",")
fluency <- data.frame(cbind(lf$Fluency, nf$Fluency, mf$Fluency))
names(fluency)<- c('Lauren', 'Naa', 'Madison')
agree(fluency, tolerance=1)
icc(fluency, model="twoway", type="agreement")
fluency$Participant<-seq(from=1, to=nrow(fluency), by=1)
sink()

# Flexibility ################################################################
sink("../Scripts/Output/ICC/Flexibility.txt", append=FALSE, split=FALSE)
lf <- read.csv(file="Flexibility_LaurenCoding.csv",head=TRUE,sep=",")
nf <- read.csv(file="Flexibility_NaaCoding.csv",head=TRUE,sep=",")
mf <- read.csv(file="Flexibility_MadisonCoding.csv", head=TRUE, sep=",")
flexibility <- data.frame(cbind(lf$Flexibility, nf$Flexibility, mf$Flexibility))
names(flexibility)<- c('Lauren', 'Naa', 'Madison')
agree(flexibility, tolerance=1)
icc(flexibility, model="twoway", type="agreement")
flexibility$Participant<-seq(from=1, to=nrow(flexibility), by=1)
sink()

# Detail #####################################################################
sink("../Scripts/Output/ICC/Detail.txt", append=FALSE, split=FALSE)
lf <- read.csv(file="Detail_LaurenCoding.csv",head=TRUE,sep=",")
nf <- read.csv(file="Detail_NaaCoding.csv",head=TRUE,sep=",")
mf <- read.csv(file="Detail_MadisonCoding.csv", head=TRUE, sep=",")
detail <- data.frame(cbind(lf$Detail, nf$Detail, mf$Detail))
names(detail)<- c('Lauren', 'Naa', 'Madison')
agree(detail, tolerance=1)
icc(detail, model="twoway", type="agreement")
detail$Participant<-seq(from=1, to=nrow(fluency), by=1)
sink()


