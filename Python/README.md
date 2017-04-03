# Python Code
## EliminatingObsLoop.py
The drive for creating this code was my own interest.  This script eliminates observations amongst several files simultaneously. It makes use of the numpy, pandas, os, and glob libraries.  An academic colleague asked me to remove certain control pictures (IAPS) from a social science experiment. I wrote her this script to delete observations from multiple different data files, then recreate them (without the excluded observations) in a separate folder.  Later, these files were combined with MultiFileConcat.py.  

## First_NonNull_Column.ipynb
The initial drive for this script's creation was a customer engagement in industry-- it has been anonymized.  In longitudinal data, the script detected when people dropped out of the service (or otherwise 'churned').  The script calls from an SAP HANA database utilizing a flavor of SQL.  It eventually led to usable data for machine learning.  I later utilized a support vector machine to indicate to the client which features were important in why customers left their service.

## HANATextAnalyticsPrep.py
The motivation for this script was a request from a VP in Industry. In summary, public access data is transformed to conduct Text Analysis in SAP HANA.  It utilizes pandas and numpy to address a specific problem. Specifically, there was a limitation in SAP HANA in that it only preferred text under 5000 characters.  This script detected which entries were over 5000 ahead of time, allowing us to identify and potentially truncate them.  

## MultiFileConcat.py
The origin of this script was a request by a client in industry.  However, I have also used it in my academic studies. It utilizes numpy, pandas, os, and glob.  The purpose is to union all files of a certain type in one working directory.  I utilized this to help a peer pre-process hundreds of individual data files.  I later altered this to unify month csvs of police activity in Baltimore, Maryland.  See Baltimore_Police_Crime_Geospatial.R for this application.

## TimeSeriesPrep.py
This script specifically involved a customer engagement in industry-- it has been anonymized.  It makes use of the numpy, pandas, datetime, and dateutil libraries.  Specifically, the client was curious to use Time Series analysis in order to predict unit sales.  However, they also introduced a series of promotional calendars to complicate matters.  The promotional calendar code has been commented out, as they select specific date-ranges with very little rhyme or reason.

## TwoStageReinforcement.py
This script formed from a collaboration on an academic project-- the coauthor asked me to program it.  TwoStageReinforcement.py preprocesses data for a complex decision-making task by Gillan, Otto, Phelps, & Daw, 2015.  Using conditional logic, numpy, and pandas, I differentiate between trial types, add to reward as participants respond correctly, and identify whether their responses changed from one option to the other.  Later, the output of this script was put into proprietary software with strict requirements.