import pandas as pandas
import numpy as np
import json


df_LatLng = pandas.read_json(r'C:\Users\Simon\Google Drive\DHBW\Semester 5\Studienarbeit\Python_R\StravaTestDataEgan\Json_Data_DeGendt\DeGendt_Stage8_LatLng.json')


# Generate Empty lists for latitutde and longitude
latitude = []
longitude = []
# Empty Text will contain geodata
geoDataLatLngSwitched = ""

# iterare through dataframe and extract latitude and longitude into seperate lists
for i in range(0, len(df_LatLng)):
    latitude.append(df_LatLng.loc[ i , 'latlng' ][0])
    longitude.append(df_LatLng.loc[ i , 'latlng' ][1])

# Insert lat and long as individual columns
df_LatLng.insert(1, "Lat", latitude, True)
df_LatLng.insert(2, "Lng", longitude, True)

# Delete old column
del df_LatLng['latlng']


print(df_LatLng)


# iterate through rows of dataframe and write switched columns into geoDataLatLngSwitched
for index, row in df_LatLng.iterrows():
	geoDataLatLngSwitched += "[" + str(row['Lng']) + "," + str(row['Lat']) + "], \n"


# open file
file1 = open(r"C:\Users\Simon\Google Drive\DHBW\Semester 5\Studienarbeit\Python_R\StravaTestDataEgan\Json_Data_DeGendt\DeGendt_Stage8_LatLng_Switched.txt","w")
# write each line to file
file1.writelines(geoDataLatLngSwitched)
