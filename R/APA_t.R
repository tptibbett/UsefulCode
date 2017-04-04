####################################################################################################
# t-Tests in APA style
# Created by Tom Tibbett
# Created: 04/04/2017
# Purpose: Practice running a simple t-test and creating a function to convert output to APA style
####################################################################################################

# Clear the Environment
rm(list=ls())

# Working Directory
getwd()
setwd("SampleData/")

# Read the CSV file
dat<-read.csv('ProcDemo.csv', stringsAsFactors = TRUE, strip.white=TRUE, na.strings= "")

# t-test: Gender
report1 <- t.test(AIP~Sex, data=dat)

# Creating a simple helper function
apa.t<- function(x){
  t<-round(as.numeric(x[1]), digits=2) # obtained t-value
  df<-round(as.numeric(x[2]), digits=2) # df
  p<-round(as.numeric(x[3]), digits=2) # p-value
  apa<-print(paste0("t(",df,")=",t,",p=", p, sep=""))
  resp<-{if (p < .05) cat("There was a significant difference between the two groups.") 
    else cat("There was no significant difference between groups.\n")}
  m<-x["estimate"]
  return(m)
}

apa.t(report1)