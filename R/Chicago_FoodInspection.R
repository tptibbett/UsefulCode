# Chicago Food Violations
# Date of Creation: 04/09/2017
# Created by Tom Tibbett
# This program uses data munging techniques on a real world Food Inspection dataset in Chicago
# A small smattering of data exploration, munging, text analysis, visualization, and binary classification
# Includes ggmap, stringr, plyr, MASS, and randomForest packages.

# Clear the Environment
rm(list=ls())

# If you do not have ggmap, install it first!
# install.packages("ggmap")
library ('ggmap')

# This data involves Chicago, IL
map <- get_map(location = 'Chicago, Illinois', maptype="toner-background", source="stamen", zoom=11)

# Working Directory
getwd()
setwd("F:/Python Scripts/UsefulCode/R/SampleData/")

# Formatting
df<-read.csv("Food_Inspections.csv",sep=",",header=TRUE, stringsAsFactors = FALSE, na.strings=c("NA", "", " "))
df$Inspection.Date <-as.Date(df$Inspection.Date, format='%m/%d/%Y')
df$Month <-months.Date(df$Inspection.Date)
df$Year <- format(df$Inspection.Date,'%Y')

# install.packages('plyr')
library('plyr')

# What types of Results and how many were there?
count(df$Results)

# Create a dataset with only passes and fails
passfail <- df[which (df$Results == "Fail" | df$Results == "Pass"),]

# Violation Numbers
passfail$Issues<-regmatches(passfail$Violations, gregexpr('\\(?[0-9,-.]+', passfail$Violations))

# install.packages('stringr')
library('stringr')

# Grabbing Critical Violations based on their format: X-XX-XXX.
passfail$Critical<- str_extract_all(passfail$Issues, '\\d-\\d{2}-\\d{3}')
passfail$NumCrit<-lengths(passfail$Critical)

# Grabbing Violations based on their format: XX.[space]
passfail$ViolNums<- str_extract_all(passfail$Issues, '\\d{1,2}[. ]')
passfail$NumViol<- lengths(passfail$ViolNums)

# Change your dates of interest - I chose 2016
# Keep in mind that subsetting too many points will prevent ggmap from completing the task.
dtlower<- as.Date('2016/12/01', format='%Y/%m/%d') # Make sure the date ACTUALLY exists.
dtupper<- as.Date('2017/01/01', format='%Y/%m/%d')

# Subsetting three points: Passes, Fails with no critical violations, and those with at least one.
f<-passfail[which(passfail$Inspection.Date > dtlower & passfail$Inspection.Date 
                    < dtupper & passfail$Results == 'Fail' & passfail$NumCrit==0), ]
p<-passfail[which(passfail$Inspection.Date > dtlower & passfail$Inspection.Date 
                  < dtupper & passfail$Results == 'Pass'), ]
c<-passfail[which(passfail$Inspection.Date > dtlower & passfail$Inspection.Date 
                  < dtupper & passfail$NumCrit > 0), ]
# Geospatial Plotting
result <- ggmap(map) + 
  geom_point(data=p, aes(x = Longitude, y = Latitude), color="blue", alpha=.6) + 
  geom_point(data=f, aes(x = Longitude, y = Latitude), color="orange", alpha=.8) +
  geom_point(data=c, aes(x = Longitude, y = Latitude), color="red", alpha=.6) +
  labs(x="Longitude", y="Latitude") +
  ggtitle("Food Inspections - December 2016")

# Viewing the Map
result

# Risk as potential predictor
count(passfail$Risk)

# Removing 'ALL' and NA, as they seems suspect
risk<-passfail[which(passfail$Risk!= "All" & passfail$Risk!="NA"),]

# install.packages('MASS')
library("MASS")

# Creating a Contingency Table and Chi-Square on if Risk Assessment predicts Passing/Failing
tbl<- table(risk$Results, risk$Risk, useNA="no")
tbl
chisq.test(tbl)

# Running simple logistic regression
logmod<- glm(as.factor(Results)~Risk+Month+Year, family=binomial(logit), data=risk)
summary(logmod)

# Conducting a Random Forest
# install.packages('randomForest')
library('randomForest')

rfmod<-randomForest(as.factor(risk$Results)~as.factor(risk$Risk)+as.factor(risk$Month)+as.factor(risk$Year), 
                    ntree=500, importance=TRUE, na.action=na.omit)

# Results, Importance, and Plotting
rfmod
importance(rfmod)
varImpPlot(rfmod)