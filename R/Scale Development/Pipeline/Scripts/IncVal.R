##################################################################################
# Incremental Validity
# For questions, contact Tom Tibbett
# Last Run: 01/12/2017
##################################################################################
# Clearing the Workspace
rm(list=ls())

setwd("f:/Dissertation/PCSpipeline/PCSpipeline/Pipeline/Scripts")
datavar <- read.csv("PCS_final.csv")

##################Personality Variability Measures################################


print("##############################################")
print("Personality Variability Measures", quote=FALSE)
print("Fluency", quote=FALSE)
print("##############################################")

onePred <-lm(df1.Fluency ~ SelfPlu_Total, datavar)
twoPred <-lm(df1.Fluency ~ SelfPlu_Total + SMS_XB_Total, datavar)
threePred<-lm(df1.Fluency ~ SelfPlu_Total + SMS_XB_Total + PCSTotal, datavar)

summary(onePred)
summary(twoPred)
summary(threePred)

anova(onePred, twoPred, threePred)

print("##############################################")
print("Personality Variability Measures", quote=FALSE)
print("Flexibility", quote=FALSE)
print("##############################################")

onePred <-lm(df1.Flexibility ~ SelfPlu_Total, datavar)
twoPred <-lm(df1.Flexibility ~ SelfPlu_Total + SMS_XB_Total, datavar)
threePred<-lm(df1.Flexibility ~ SelfPlu_Total + SMS_XB_Total + PCSTotal, datavar)

summary(onePred)
summary(twoPred)
summary(threePred)

anova(onePred, twoPred, threePred)

print("##############################################")
print("Personality Variability Measures", quote=FALSE)
print("Originality - Subjective", quote=FALSE)
print("##############################################")

onePred <-lm(Originality ~ SelfPlu_Total, datavar)
twoPred <-lm(Originality ~ SelfPlu_Total + SMS_XB_Total, datavar)
threePred<-lm(Originality ~ SelfPlu_Total + SMS_XB_Total + PCSTotal, datavar)

summary(onePred)
summary(twoPred)
summary(threePred)

anova(onePred, twoPred, threePred)

print("##############################################")
print("Personality Variability Measures", quote=FALSE)
print("Originality - Frequency", quote=FALSE)
print("##############################################")

onePred <-lm(OriginalityII ~ SelfPlu_Total, datavar)
twoPred <-lm(OriginalityII ~ SelfPlu_Total + SMS_XB_Total, datavar)
threePred<-lm(OriginalityII ~ SelfPlu_Total + SMS_XB_Total + PCSTotal, datavar)

summary(onePred)
summary(twoPred)
summary(threePred)

anova(onePred, twoPred, threePred)

print("##############################################")
print("Personality Variability Measures", quote=FALSE)
print("Detail", quote=FALSE)
print("##############################################")

onePred <-lm(df2.Detail ~ SelfPlu_Total, datavar)
twoPred <-lm(df2.Detail ~ SelfPlu_Total + SMS_XB_Total, datavar)
threePred<-lm(df2.Detail ~ SelfPlu_Total + SMS_XB_Total + PCSTotal, datavar)

summary(onePred)
summary(twoPred)
summary(threePred)

anova(onePred, twoPred, threePred)

print("##############################################")
print("Personality Variability Measures", quote=FALSE)
print("Detail Divided by Fluency", quote=FALSE)
print("##############################################")

onePred <-lm(df2.Detail.Idea ~ SelfPlu_Total, datavar)
twoPred <-lm(df2.Detail.Idea ~ SelfPlu_Total + SMS_XB_Total, datavar)
threePred<-lm(df2.Detail.Idea ~ SelfPlu_Total + SMS_XB_Total + PCSTotal, datavar)

summary(onePred)
summary(twoPred)
summary(threePred)

anova(onePred, twoPred, threePred)

#########################Creativity Scale Measures################################

print("##############################################")
print("Creativity Scale Measures", quote=FALSE)
print("Fluency", quote=FALSE)
print("##############################################")

onePred <-lm(df1.Fluency ~ CPS_Total, datavar)
twoPred <-lm(df1.Fluency ~ CPS_Total + NFC_Total, datavar)
threePred<-lm(df1.Fluency ~ CPS_Total + NFC_Total + ToI_Total, datavar)
fourPred<- lm(df1.Fluency ~ CPS_Total + NFC_Total + ToI_Total + PCSTotal, datavar)

summary(onePred)
summary(twoPred)
summary(threePred)
summary(fourPred)

anova(onePred, twoPred, threePred, fourPred)

print("##############################################")
print("Creativity Scale Measures", quote=FALSE)
print("Flexibility", quote=FALSE)
print("##############################################")

onePred <-lm(df1.Flexibility ~ CPS_Total, datavar)
twoPred <-lm(df1.Flexibility ~ CPS_Total + NFC_Total, datavar)
threePred<-lm(df1.Flexibility ~ CPS_Total + NFC_Total + ToI_Total, datavar)
fourPred<- lm(df1.Flexibility ~ CPS_Total + NFC_Total + ToI_Total + PCSTotal, datavar)

summary(onePred)
summary(twoPred)
summary(threePred)
summary(fourPred)

anova(onePred, twoPred, threePred, fourPred)

print("##############################################")
print("Creativity Scale Measures", quote=FALSE)
print("Originality - Subjective", quote=FALSE)
print("##############################################")

onePred <-lm(Originality ~ CPS_Total, datavar)
twoPred <-lm(Originality ~ CPS_Total + NFC_Total, datavar)
threePred<-lm(Originality ~ CPS_Total + NFC_Total + ToI_Total, datavar)
fourPred<- lm(Originality ~ CPS_Total + NFC_Total + ToI_Total + PCSTotal, datavar)

summary(onePred)
summary(twoPred)
summary(threePred)
summary(fourPred)

anova(onePred, twoPred, threePred, fourPred)

print("##############################################")
print("Creativity Scale Measures", quote=FALSE)
print("Originality - Frequency", quote=FALSE)
print("##############################################")

onePred <-lm(OriginalityII ~ CPS_Total, datavar)
twoPred <-lm(OriginalityII ~ CPS_Total + NFC_Total, datavar)
threePred<-lm(OriginalityII ~ CPS_Total + NFC_Total + ToI_Total, datavar)
fourPred<- lm(OriginalityII ~ CPS_Total + NFC_Total + ToI_Total + PCSTotal, datavar)

summary(onePred)
summary(twoPred)
summary(threePred)
summary(fourPred)

anova(onePred, twoPred, threePred, fourPred)

print("##############################################")
print("Creativity Scale Measures", quote=FALSE)
print("Detail", quote=FALSE)
print("##############################################")

onePred <-lm(df2.Detail ~ CPS_Total, datavar)
twoPred <-lm(df2.Detail ~ CPS_Total + NFC_Total, datavar)
threePred<-lm(df2.Detail ~ CPS_Total + NFC_Total + ToI_Total, datavar)
fourPred<- lm(df2.Detail ~ CPS_Total + NFC_Total + ToI_Total + PCSTotal, datavar)

summary(onePred)
summary(twoPred)
summary(threePred)
summary(fourPred)

anova(onePred, twoPred, threePred, fourPred)

print("##############################################")
print("Creativity Scale Measures", quote=FALSE)
print("Detail divided by Fluency", quote=FALSE)
print("##############################################")

onePred <-lm(df2.Detail.Idea ~ CPS_Total, datavar)
twoPred <-lm(df2.Detail.Idea ~ CPS_Total + NFC_Total, datavar)
threePred<-lm(df2.Detail.Idea ~ CPS_Total + NFC_Total + ToI_Total, datavar)
fourPred<- lm(df2.Detail.Idea ~ CPS_Total + NFC_Total + ToI_Total + PCSTotal, datavar)

summary(onePred)
summary(twoPred)
summary(threePred)
summary(fourPred)

anova(onePred, twoPred, threePred, fourPred)

sink("Output/IncrementalValidity/PersonalityVariability.txt", append=FALSE, split=FALSE)

print("##############################################")
print("Creativity Scale Measures", quote=FALSE)
print("Flexibility", quote=FALSE)
print("##############################################")


twoPred <-lm(df1.Flexibility ~ BFI_O_Total + SelfPlu_Total, datavar)
threePred<-lm(df1.Flexibility ~ BFI_O_Total + SelfPlu_Total + PCSTotal, datavar)

print("##############################################")
print("Using Self-Pluralism and Openness", quote=FALSE)
print("Two Predictors", quote=FALSE)
print("##############################################")

summary(twoPred)

print("##############################################")
print("Adding the PCS", quote=FALSE)
print("Three Predictors", quote=FALSE)
print("##############################################")

summary(threePred)

print("##############################################")
print("Are the two models significantly different?", quote=FALSE)
print("If so, give the R squared change", quote=FALSE)
print("##############################################")

anova(twoPred, threePred)
sink()