library ('forecast')
library ('sp')
library ('rworldmap')
library ('plyr')
library ('ggmap')
library('mapproj')
library('dplyr')
library('tidyr')
library('stringi')

#newmap <- getMap(resolution = "low")
#plot(newmap, xlim = c(-76.75, -76.5), ylim = c(39.18, 39.4), asp = 1)

map <- get_map(location = 'Baltimore, Maryland', maptype="toner", source="stamen", zoom=12)
ggmap(map)

setwd("C:/Users/I856176/Documents/Code/DataPrep/Geospatial") # Check your Working Directory!

# Formatting
df=read.table("BPD_Part_1_Victim_Based_Crime_Data.csv",sep=",",header=TRUE, fill=TRUE)
df$CrimeDate <-as.Date(df$CrimeDate, format='%m/%d/%Y')
df$Month <-months.Date(df$CrimeDate)

#Separating Latitude and Longitude
df<-cbind(df, data.frame(lat = stri_extract_first(df$Location.1, regex = "\\d{1,}.\\d{1,}"),
           lon = stri_extract_last(df$Location.1, regex = "-\\d{1,}.\\d{1,}"))) # Remember, longitude here is negative!
df$lon<-as.numeric(as.character(df$lon))
df$lat<-as.numeric(as.character(df$lat))

unique(df$Weapon)

# Change your dates of interest
dtlower<- as.Date('2015-06-30', format='%Y-%m-%d')
dtupper<- as.Date('2015-08-01', format='%Y-%m-%d')

hands<-df[which(df$CrimeDate > dtlower & df$CrimeDate < dtupper & df$Weapon == 'HANDS'), ]
guns<-df[which(df$CrimeDate > dtlower & df$CrimeDate < dtupper & df$Weapon == 'FIREARM'), ]
knives<-df[which(df$CrimeDate > dtlower & df$CrimeDate < dtupper & df$Weapon == 'KNIFE'), ]
other<-df[which(df$CrimeDate > dtlower & df$CrimeDate < dtupper & df$Weapon == 'OTHER'), ]

allweapons <- ggmap(map) + 
  geom_point(data=hands, aes(x = lon, y = lat), color="darkgreen") +
  geom_point(data=knives, aes(x = lon, y = lat), color="orange") +
  geom_point(data=guns, aes(x = lon, y = lat), color="red") +
  geom_point(data=other, aes(x = lon, y = lat), color="purple") +
  labs(x="Longitude", y="Latitude") +
  ggtitle("Weapon-Oriented Crimes, Baltimore, MD: July 2015")

allweapons
