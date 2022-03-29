import plotly.express as px
import pandas as pd
import math
from math import sin, cos, sqrt, atan2

df = pd.read_csv('Finals/data_and_cleaning/Cleaning_windrose_1.csv', sep=',')


# Koordinaten Himmelsrichtungen zuordnen

Degree = [None]*len(df) # neue Liste mit Länge des Df

df ['Kompass'] = "" # neue Spalte

# Berechnen der Kompass Richtungen
for i in range(len(df)):

    R = 6373.0

    pointA = [ df['ORIGIN_AIRPORT_LAT'] [i], df['ORIGIN_AIRPORT_LON'] [i] ]
    pointB = [df['DESTINATION_AIRPORT_LAT'] [i], df['DESTINATION_AIRPORT_LON'] [i]]

    lat1 = math.radians(pointA[0]) # Gradzahl zwischen den Punkten, ausgehend vom Startpunkt bestimmen

    lat2 = math.radians(pointB[0])

    diffLong = math.radians(pointB[1] - pointA[1])

    x = math.sin(diffLong) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
            * math.cos(lat2) * math.cos(diffLong))

    initial_bearing = math.atan2(x, y)

    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360

    Degree [i] = compass_bearing # Ergebnis einfügen

df ['Degree'] = Degree # zum df hinzufügen

# Gradzahl wie einen Kompass vorstellen bei dem Null Grad -> Norden / 360 Grad -> Süden

df.loc[df.Degree >= 0 ,'Kompass']='N' # Gradzahlen, Räumen auf dem Kompass zuordnet / Himmelsrichtung zuordnen 
df.loc[df.Degree >= 11.25 ,'Kompass']='NNE' 
df.loc[df.Degree >= 33.75 ,'Kompass']='NE' 
df.loc[df.Degree >= 56.25 ,'Kompass']='ENE' 
df.loc[df.Degree >= 78.75 ,'Kompass']='E' 
df.loc[df.Degree >= 101.25 ,'Kompass']='ESE' 
df.loc[df.Degree >= 123.75 ,'Kompass']='SE'
df.loc[df.Degree >= 146.25 ,'Kompass']='SSE' 
df.loc[df.Degree >= 168.75 ,'Kompass']='S' 
df.loc[df.Degree >= 191.25 ,'Kompass']='SSW' 
df.loc[df.Degree >= 213.75 ,'Kompass']='SW' 
df.loc[df.Degree >= 236.25 ,'Kompass']='WSW'
df.loc[df.Degree >= 258.75 ,'Kompass']='W' 
df.loc[df.Degree >= 281.25 ,'Kompass']='WNW'
df.loc[df.Degree >= 303.75 ,'Kompass']='NW'
df.loc[df.Degree >= 326.25 ,'Kompass']='NNW' 
df.loc[df.Degree >= 348.75 ,'Kompass']='N' 

print (df.head(15))
df.to_csv(r'Finals/data_and_cleaning/Cleaning_windrose_2_new.csv')

print ( 'Done' )
