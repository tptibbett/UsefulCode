# Personality Consistency Scale (PCS) Dissertation Pipeline
### Documentation Updated: Apr 2nd, 2017
### Author: Tom Tibbett
### Purpose: Noting which files are relevant to analysis and organizing an ETL pipeline

### Documentation -- What is this?

This pipeline was created by me in conjunction with completing my dissertation in the Psychological and Brain Sciences department at Texas A&M University. The documentation of this pipeline details relevant files and contingencies for analysis.  The pipeline consists of five basic files, some in Python and others in R.  These scripts create files which are dependent upon one another; be careful to start with Desc.IPYNB and progress down this readme in a linear fashion.  Eventually, I may have an update that includes bash scripts.  This should remove the problem of having to run each script one after the other.  Currently, I am looking to see if it is alright to post anonymized data-- the IRB will get back to me.  For now, no data files are posted.

### Housekeeping Map -- Where are things kept?

* Pipeline > QualtricsOutput: Place the cleaned output here in CSV
* Pipeline > Scripts: The five scripts to run are here
* Pipeline > Scripts > Output: Outputted files are stored here

## Descriptive Statistics -- Desc.IPYNB

### Requires:

* Python 2.7 and Jupyter Notebook
* PCSResults_Sept27.csv: Cleaned Qualtrics Output
* Flexibility_onlyvalid.csv: Flexibility column scores
* Detail_onlyvalid.csv: Detail column scores
* Originality_onlyvalid.csv: Originality column scores
* Columns.csv: Renamed columns for PCSResults

### Description: 

Desc.IPYNB does simple descriptives.  It outputs mean scores and other statistics, as well as creates a streamlined, merged file. This stage does reverse coding as well as removing suspicious participants. Finally, it completes corrections on misspellings that prevent simple aggregation.

### Output

* PCS_cleaned_data.csv: Streamlined data set for later 
* Table_Alpha.csv: Cronbach's alpha for each scale
* Table_Politics.csv: Aggregates Political Affiliation
* Table_Gender.csv: Aggregates Gender
* Table_Religion.csv: Aggregates Religious Preference
* Table_Class.csv: Aggregates Academic Class
* Table_Age.csv: Descriptive Stats for Age
* Table_Qualtrics.csv: Qualtrics Descriptive Statistics
* Table_Departments.csv: Aggregates Department at the University

## Interrater Reliability -- ICC.R

### Requires:

* R/RStudio, Package IRR
* PCS_cleaned_data.csv: Output from Desc.R
* Fluency_LaurenCoding.csv: Original Fluency Scores
* Fluency_NaaCoding.csv: Original Fluency Scores
* Flexibility_LaurenCoding.csv: Original Flexibility Scores
* Flexibility_NaaCoding.csv: Original Flexibility Scores
* Detail_LaurenCoding.csv: Original Detail Scores
* Detail_NaaCoding.csv: Original Detail Scores

### Description: 

Analyses coders to output interrater reliability (alpha/ICC).  Coders may then choose to conference and find consensus.

### Output:

* Fluency.txt: Fluency Results between 3 coders
* Flexibility.txt: Flexibility Results between 3 coders
* Detail.txt: Detail Results between 3 coders

## Originality Type II Processing -- OrigII.R

### Requires:

* R/RStudio
* OriginalityCoding_TypeII.csv: Originality Sorting

### Description: 

One coder categorized each idea.  As a more objective measure of originality, this script will measure the total number of ideas and then yield a percentage: the number of ideas in a category divided by the total ideas among all participants. All ideas under 60 (3.5%) will receive one point. All ideas under 32 (1%) will receive two points.  The script will finally assign a score to each participant by matching the scores back to the participant number.

### Output:

* OrigIIScores.csv: Creates a simple score for each participant

## Correlation Matrix -- Corr.R

### Requires:

* R/RStudio
* PCS_cleaned_data.csv: Output by Desc.R
* OrigIIScores.csv: Output by OrigII.R

### Description: 

This script will create a simple correlation matrix between all variables created so far.  It will also create tables which detail the inferential statistics necessary for reporting analyses, with particular focus on the predicted analyses: creativity performance and the Personality Consistency Scale.

### Output: 

* CorrMatrix.csv: Correlation Matrix 
* CorrPvalues.csv: Correlation Analysis Tables
* PCSfinal.csv: Merged PCS_cleaned_data with OrigIIScores

## Incremental Validity -- IncVal.R

### Requires:

* R/RStudio
* PCSplusOrigII.csv: Output by Corr.R

### Description: 

This script will analyze whether the PCS can explain variance over and above preexisting scales.  For each of the five measures of creativity (including Type II Originality), the PCS will be weighted against scales in Personality Variability and Creativity respectively.  R-squared change will be calculated for each step of the analysis, the first block being all existing measures, and the last with the Personality Consistency Scale added to the model.

### Output:

* Table_FluVar.csv: PCS adding to Fluency vs. other variability scales
* Table_FluCre.csv: PCS adding to Fluency vs. other creativity scales
* Table_FlexVar.csv: PCS adding to Flexibility vs. other variability scales
* Table_FlexCre.csv: PCS adding to Flexibility vs. other creativity scales
* Table_OrigVar.csv: PCS adding to Originality vs. other variability scales
* Table_OrigCre.csv: PCS adding to Originality vs. other creativity scales
* Table_OrigIIVar.csv: PCS adding to Originality II vs. other variability scales
* Table_OrigIICre.csv: PCS adding to Originality II vs. other creativity scales
* Table_DetVar.csv: PCS adding to Detail vs. other variability scales
* Table_DetCre.csv: PCS adding to Detail vs. other creativity scales