# Baltimore Police Crime Geospatial
# Date of Creation: 07/27/2016
# Created by Tom Tibbett
# This program creates a geospatial render of crime data and plots them on a map in a visually pleasing way.
# The crime data csv was created with another script adapted from this GitHub.  See MultiFileConcat.py

# Clear the Environment
rm(list=ls())

# If you do not have ggmap, install it first!
# install.packages("ggmap")
library ('ggmap')

# Choose the limits of your map, either by place or by lat/long
#plot(newmap, xlim = c(-76.75, -76.5), ylim = c(39.18, 39.4), asp = 1)
map <- get_map(location = 'Baltimore, Maryland', maptype="watercolor", source="stamen", zoom=12)
ggmap(map)

# Check your Working Directory!
getwd()
setwd("/data/")

# Formatting
df=read.table("BPD_Part_1_Victim_Based_Crime_Data.csv",sep=",",header=TRUE, fill=TRUE)
df$CrimeDate <-as.Date(df$CrimeDate, format='%m/%d/%Y')
df$Month <-months.Date(df$CrimeDate)

#Separating Latitude and Longitude
df<-cbind(df, data.frame(lat = stri_extract_first(df$Location.1, regex = "\\d{1,}.\\d{1,}"),
           lon = stri_extract_last(df$Location.1, regex = "-\\d{1,}.\\d{1,}"))) # Remember, longitude here is negative!
df$lon<-as.numeric(as.character(df$lon))
df$lat<-as.numeric(as.character(df$lat))

# What types of weapons were there?
unique(df$Weapon)

# Change your dates of interest - I chose May 2015
# Keep in mind that subsetting too many points will prevent ggmap from completing the task.
dtlower<- as.Date('2015/04/30', format='%Y/%m/%d') # Make sure the date ACTUALLY exists.
dtupper<- as.Date('2015/06/01', format='%Y/%m/%d')

# These are confrontations involving specific weapons
hands<-df[which(df$CrimeDate > dtlower & df$CrimeDate < dtupper & df$Weapon == 'HANDS'), ]
guns<-df[which(df$CrimeDate > dtlower & df$CrimeDate < dtupper & df$Weapon == 'FIREARM'), ]
knives<-df[which(df$CrimeDate > dtlower & df$CrimeDate < dtupper & df$Weapon == 'KNIFE'), ]
other<-df[which(df$CrimeDate > dtlower & df$CrimeDate < dtupper & df$Weapon == 'OTHER'), ]

# Choose your weapon(s) - I chose hand-to-hand combat
allweapons <- ggmap(map) + 
  geom_point(data=hands, aes(x = lon, y = lat), color="blue", alpha=.4) +
  #geom_point(data=knives, aes(x = lon, y = lat), color="orange") + 
  #geom_point(data=guns, aes(x = lon, y = lat), color="red") +
  #geom_point(data=other, aes(x = lon, y = lat), color="purple") +
  labs(x="Longitude", y="Latitude") +
  ggtitle("Hand-to-Hand Combat - Baltimore, MD: May 2015")

# View the Map in RStudio
allweapons