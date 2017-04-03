##################################################################
# Correlations
# For questions, contact Tom Tibbett
# Last Run: 01/12/2017
##################################################################
# Clearing the Workspace
rm(list=ls())

setwd("f:/Dissertation/PCSpipeline/PCSpipeline/Pipeline/Scripts")
df1 <- read.csv(file="Flexibility_OnlyValid.csv",head=TRUE,sep=",")
df2 <- read.csv(file="Detail_OnlyValid.csv",head=TRUE,sep=",")
df3 <- read.csv(file="PCS_cleaned_data.csv", head=TRUE, sep=",")
df4 <- read.csv(file="Output/Originality/OrigIIScores.csv",head=TRUE,sep=",")

# Completed Data Set
df <- data.frame(cbind(df3, df1$Fluency, df1$Flexibility, 
                       df2$Detail, df2$Detail.Idea, df4))

##################################################################
#Correlation Matrix
#install.packages('Hmisc')
library('Hmisc')

mat<-rcorr(as.matrix(df[,187:length(names(df))]))
P<-round(mat$P, 2)
r<-data.frame(round(mat$r, 2))

write.csv(r, file="Output/Correlations/CorrMatrix.csv")
write.csv(P, file="Output/Correlations/CorrPvalues.csv")
write.csv(df, file="PCS_final.csv", row.names=FALSE)
