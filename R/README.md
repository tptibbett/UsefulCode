# R Code
## Scale Development
This folder concerns my dissertation in scale development.  I created and validated a scale in perceived personality consistency using both quantitative and qualitative analyses.  I decided to code the analyses almost completely in R.  The pipeline involves descriptive statistics, inferential statistics, reliability (both interrater and internal consistency), and validity (convergent, discriminant, predictive, and incremental).  Results indicated evidence for a valid 5-item measure.

## APA_t.R
This code is a simple function I created to quickly convert t-tests to APA style.  It was particularly useful when utilized for gender studies.  It yields the APA documentation, the interpretation, and the mean scores.  Other information can be acquired from summaries of the analysis itself.

## Baltimore_Police_Crime_Geospatial.R
This code utilizes ggmap, stacking on ggplot2, to create a scatterplot overlay on a subset of geography.  I utilized years of monthly crime reports on a publically accessible database for Baltimore, MD, to find out just how much hand-to-hand combat goes on in Baltimore.  This code utilizes ggplot, ggmap, and various base R functions.  This code was driven by practice and curiosity.

## Chicago_FoodInspection.R
This script utilizes ggmap, stringr, plyr, MASS, and randomForest packages using a real world data set of Health Code Violations.  One of the obstacles was that violations were not easily converted to factors; furthermore, multiple violations were recorded in the same dataframe cell, needing extraction. The code first plots where the violations took place at user-input data ranges and considers potential factors with GLM and randomForest.  This code was driven by my desire to practice with text analysis.  This script is under construction.

## SEM_USElection.R
This code utilizes the lavaan library to do structural equation modeling.  The impetus was a US Presidential Election study and the emotional reactions and life satisfaction changes in a longitudinal study.  In the code, I create four SEM models and compare them. This code was driven by my academic projects in the Emotion Science Lab.

## Simple_Mediation_Indecision.R
This code utilizes the lavaan library to do simple mediation modeling.  The project involved work in the indecision literature, particularly focused on the psychological construct of regret.  The script also utilizes basic R functions like correlation matrices.  The script was driven by my academic collaboration with DePaul University.