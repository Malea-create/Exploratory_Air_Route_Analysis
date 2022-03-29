# Zusammensatzung von verspäteten, pünktlichen und ausgefallenen Flügen 

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

df = pd.read_csv('../data_and_cleaning/flights.csv', sep=',')

df_new = df[['AIRLINE','CANCELLATION_REASON','DEPARTURE_DELAY', 'ARRIVAL_DELAY', 'CANCELLED','AIR_SYSTEM_DELAY','SECURITY_DELAY','AIRLINE_DELAY','LATE_AIRCRAFT_DELAY', 'WEATHER_DELAY']] # Für geringere Laufzeit Spalten reduzieren
df_new = df_new.replace( np.nan, 0 ) # Nan werte mit 0 ersetzen

df_new['ALL'] = "All Flights"

# Airlines ausschreiben 

df_new['AIRLINE'] = df_new['AIRLINE'].map({ # Bessere Aussagekraft bei ausgeschriebenen Namen der Airlines

'UA':'United Air Lines Inc.',
'AA':'American Airlines Inc.',
'US':'US Airways Inc.',
'F9':'Frontier Airlines Inc.',
'B6':'JetBlue Airways',
'OO':'Skywest Airlines Inc.',
'AS':'Alaska Airlines Inc.',
'NK':'Spirit Air Lines',
'WN':'Southwest Airlines Co.',
'DL':'Delta Air Lines Inc.',
'EV':'Atlantic Southeast Airlines',
'HA':'Hawaiian Airlines Inc.',
'MQ':'American Eagle Airlines Inc.',
'VX':'Virgin America'}, 

na_action=None) # Werte ändern 


# Delays & Cannelations auf eine Zeile reduzieren 

# Ein Flug ist jeweils immer einem Zustand zugeordnet, entweder ist er verspätet, pünktlich oder ausgefallen, 
# innerhalb der Kategorien wird dann noch in einzelne Gründe unterschieden. 
# Das Zusammenfassen der Spalten funktioniert mit mehreren Loc-Funktionen, 
# die je nach Kategorie des Fluges einen Wert in eine neue Spalte speichert, die später von der Treemap dargestellt wird.

df_new ['DELAYED'] = 'Flights on schedule' # neue Spalte

#Delays & Reasons
df_new.loc[df_new.DEPARTURE_DELAY > 0,'DELAYED']='Delayed w/o reason' # mit loc Funktion Werte ändern (Bedigung in einer Spalte veränder andere)
df_new.loc[df_new.ARRIVAL_DELAY > 0,'DELAYED']='Delayed w/o reason' # mit verschiedenen Bedingungen füllen 
df_new.loc[df_new.AIR_SYSTEM_DELAY > 0,'DELAYED']='Air-System Delay'
df_new.loc[df_new.SECURITY_DELAY > 0,'DELAYED']='Security Delay'
df_new.loc[df_new.AIRLINE_DELAY > 0,'DELAYED']='Airline Delay'
df_new.loc[df_new.LATE_AIRCRAFT_DELAY > 0,'DELAYED']='Late Aircraft Delay'
df_new.loc[df_new.WEATHER_DELAY > 0,'DELAYED']='Weather Delay'

#Cannellations & Reasons
df_new.loc[df_new.CANCELLED > 0,'DELAYED']='Cancelled w/o reason'
df_new.loc[df_new.CANCELLATION_REASON == 'A','DELAYED']='Cancellation due Airline'
df_new.loc[df_new.CANCELLATION_REASON == 'B','DELAYED']='Cancellation due Weather'
df_new.loc[df_new.CANCELLATION_REASON == 'C','DELAYED']='Cancellation due Air System'
df_new.loc[df_new.CANCELLATION_REASON == 'D','DELAYED']='Cancellation due Security'



#Duration of the Delay

df_new ['Lateness'] = '' # neue Leere Spalte
df_new['Lateness'] = df_new.sum(axis=1) # In jeder Zeile wird eine Summierungsfunktion ausgeführt,da die einzige übrige Zahl im Dataframe die Anzahl der Verspätungsminuten ist, alle restlichen String-Werte werden übergangen

df_new.loc[df_new.CANCELLED > 0,'Lateness']= 0 # Verwirrende Information bereinigen 


#print ( df_new.head(150)) # überprüfen


# Darstellung in Treemap um Zusammensetzung darzustellen
fig = px.treemap(
    
 df_new, path=['ALL','AIRLINE','DELAYED'], # Daten laden

 color_continuous_scale = 'rdbu_r', 
 
 title = "Composition of the Flights in each Airline", # Style

 color='Lateness', # Farbe der Treemap wird auf diese neue Lateness-Spalte gesetzt, das Viereck wird je nach durchschnittlicher Verspätung eingefärbt

 color_continuous_midpoint=np.average( df_new['Lateness'] ), # Mit dem Attribut color_continuous_midpoint der Treemap kann die gewählte Farbskala auf die Werte in der Lateness-Spalte gemünzt werden, der Mittelwert der Verspätung entspricht nun dem Mittelwert der der Farbskala

 )

#Zusätzliche Informationen

custom_data = df_new ['Lateness'].round(2) # Runden für spätere Anzeige 


fig.data[0].textinfo = 'label+percent parent' # für besseren Vergleich untereinander

fig.data[0].hovertemplate = '%{label}<br>'+'Amount of Flights in this Airline: %{value}<br>'+'Average lateness (in min): %{customdata[0]}<br>' #  default Hovertemplate überschreiben mit spezifizierten Infos / in jedem Viereck der prozentuale Fluganteil, den die Kategorie pro Airline hat, angezeigt wird

fig.add_annotation(text=" - dark red color represents long delay times      <br>   - negative latness represents premature flights<br> - click on the different squares for a closeup      ", x=0.02, y=0.02, showarrow=False, bgcolor= "white", bordercolor= "black" , height = 50) # Grafik erklären




fig.show()

