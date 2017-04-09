##############################################################################################################
# K-Nearest Neighbor (KNN)
# Date of Creation: 04/09/2017
# Created by Tom Tibbett
# This script conducts KNN on the Iris sample data set.  It also includes simple ways to explore/visualize data
# Libraries include psych, ggvis, class, and gmodels.
##############################################################################################################
# Data Exploration
##############################################################################################################
# Clear the Environment
rm(list=ls())

# Working Directory
getwd()
setwd("F:/Python Scripts/UsefulCode/R/SampleData/")

# install.packages('psych')
library('psych')

# Getting an idea of structure
head(iris)
str(iris)
summary(iris)
describe(iris)
describeBy(iris, iris$Species)

# install.packages('ggvis')
library('ggvis')

# Plotting- separating by flower species and reviewing the overall pattern
## Sepal
iris %>% ggvis(~Sepal.Length, ~Sepal.Width, fill = ~Species) %>% layer_points()

## Petal
iris %>% ggvis(~Petal.Length, ~Petal.Width, fill = ~Species) %>% layer_points()


# install.packages("class") # Library for KNN
library("class")

# Creating a normalization function just in case there are high ranges that do not overlap
normalize <- function(n) {
  num <- n - min(n)
  denom <- max(n) - min(n)
  return (num/denom)
}

# Not a need for this data set to normalize, but in case we need it for others...
iris_n <- as.data.frame(lapply(iris[1:4], normalize))
describe(iris_n) # Note the min and max
describeBy(iris_n, iris$Species)

##############################################################################################################
# Machine Learning
##############################################################################################################
# Preparation
set.seed(1234)

# Splitting into a train and test set with proportional split
t.split <- sample(2, nrow(iris), replace=TRUE, prob=c(.67, .33))
iris.train <- iris[t.split==1, 1:4] # There are four variables to be split in iris
iris.test <- iris[t.split==2, 1:4]
iris.trainLabels <- iris[t.split==1, 5] # Storing the class labels for Species
iris.testLabels <- iris[t.split==2, 5]

# Building a classifier
iris_p <-knn(train=iris.train, test=iris.test, cl = iris.trainLabels, k=3)
match <- iris_p==iris.testLabels # How often do they match?
df_m<-data.frame(iris_p, iris.testLabels, match)
m<-mean(df_m$match)

# Contingency Tables
# install.packages('gmodels')
library('gmodels')

CrossTable(x = iris.testLabels, y = iris_p, prop.chisq=TRUE)

cat("This model classifies at", round(m*100, digits=2), 
    "percent accuracy, compared to random chance:", 
    round(1/length(unique(iris.testLabels))*100, digits=2), "percent"
    )