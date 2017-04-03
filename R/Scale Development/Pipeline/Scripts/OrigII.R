###########################################################################
# Originality Coding
# For questions, contact Tom Tibbett
# Last Run: 01/12/2017
###########################################################################
# Clearing the Workspace
rm(list=ls())

# install.packages('dplyr')
library('dplyr')

setwd("f:/Dissertation/PCSpipeline/PCSpipeline/Pipeline/Scripts")
df1 <- read.csv(file="PCS_cleaned_data.csv",head=TRUE,sep=",")
df2 <- read.csv(file="Originality_OnlyValid.csv",head=TRUE,sep=",")
df3 <- read.csv(file="OriginalityCoding_TypeIIedit.csv",head=TRUE,sep=",")

# Originality Type 1: Rated by multiple RAs
i=1
end <- vector("list", length=length(unique(df2$Number)))
while(i <= length(unique(df2$Number))){
  end[i]=mean(df2$Originality.Score[df2$Number== i], na.rm=TRUE)
  i=i + 1}
end <- data.frame(matrix(unlist(end)))

# Removing participant who admitted doing this task
end<-data.frame(end[-30,])
names(end) <- 'Originality'

# Saving Output
sink("Output/Originality/OriginalityTypeI.txt", append=FALSE, split=FALSE)
print('Descriptive Statistics', quote=FALSE)
summary(end$Originality)
print('Standard Deviation', quote=FALSE)
sd(end$Originality)
sink()

# Originality Type 2: Creating a number of categories
dim(df3)
two <- df3[,3:46]

list(names(two))

out=NULL
for (c in names(two)){
  b<-sum(two[c]!="")
  a<-c
  d<-data.frame(a,b)
  out=rbind(out, d)
}
out$c <- out$b/sum(out$b)
print(c(sum(out$b), "ideas"), quote=FALSE)
out<- out[order(-out$b),]

# Creating Originality Points
out$d<-NULL
for (g in 1:length(out$b)){
  if (32 < out$b[g]& out$b[g] < 120){
    out$d[g]=1
  } else if(out$b[g] < 32){
    out$d[g]=2
  } else if(out$b[g]> 120){
    out$d[g]=0
  }
}
names(out)<- c('Category', 'Freq', 'Percent', 'Points')
write.csv(out, file="Output/Originality/Table_Percents.csv", row.names = FALSE)

# Pair coin collector with Column Name Container
two2 <- df3[,1:2]
two2<-two2[which(two2$Idea!=""),]

nope=NULL
for (q in two2$Idea){
  index<- which(two==q, arr.ind=TRUE)
  d<-data.frame(colnames(two)[index[2]])
  nope=rbind(nope, d)
}
orig<-cbind(two2, nope)
names(orig)<-c("Number", "Idea", "Category")

# Pair Column Name Container with Point Bonus
result<-left_join(orig, out, by=c("Category"="Category"))
result$Points[is.na(result$Points)]<- 0

# Originality Score II - Mean Score for each person
j=1
mango <- vector("list", length=length(unique(result$Number)))
while(j <= length(unique(result$Number))){
  mango[j]=mean(result$Points[result$Number== j], na.rm=TRUE)
  j=j + 1}

mango <- data.frame(matrix(unlist(mango)))

# Removing participant who admitted doing this task
mango<-data.frame(mango[-30,])
names(mango) <- 'OriginalityII'

# Merging with the Dataset
df<-cbind(end,mango)
write.csv(df, file="Output/Originality/OrigIIScores.csv", row.names = FALSE)