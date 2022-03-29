# Cleaning für windrose
# Zusammensetzen von Flugdaten und Airportdaten (Koordinaten einfügen)

import pandas as pd

df = pd.read_csv('Finals/data_and_cleaning/flights.csv', sep=',') # flights.csv von kaggel
dest = pd.read_csv('Finals/data_and_cleaning/airports.csv', sep=',') # Airport daten um Koordinaten hinzuzufügen


# Airports Koordinaten zuordnen

df ['ORIGIN_AIRPORT_LAT'] = "" # neue Spalten einfügen
df ['ORIGIN_AIRPORT_LON'] = "" 
df ['DESTINATION_AIRPORT_LAT'] = "" 
df ['DESTINATION_AIRPORT_LON'] = "" 
df ['State_Depature'] = "" # neue Spalten einfügen
df ['State_Destination'] = "" # neue Spalten einfügen


for i in range(len(dest)): # Spalten für Airport befüllen

    x = dest ['IATA_CODE'] [i] # Flughafen spezifische IATA-Code benutzten, um die Koordinaten der Flughäfen aus einem anderen Datenset zuordnen zu können

    # Koordinaten für Start- und Zielflughafen / Bundesstaat wird in neuen Spalten eingefügt

    df.loc[df.ORIGIN_AIRPORT == x ,'ORIGIN_AIRPORT_LAT'] = dest ['LATITUDE'] [i] # Origin Airport
    df.loc[df.ORIGIN_AIRPORT == x ,'ORIGIN_AIRPORT_LON'] = dest ['LONGITUDE'] [i]

    df.loc[df.DESTINATION_AIRPORT == x ,'DESTINATION_AIRPORT_LAT'] = dest ['LATITUDE'] [i] # Depature Airport
    df.loc[df.DESTINATION_AIRPORT == x ,'DESTINATION_AIRPORT_LON'] = dest ['LONGITUDE'] [i]

    df.loc[df.ORIGIN_AIRPORT == x ,'State_Depature'] = dest ['STATE'] [i] # Origin Airport
    df.loc[df.DESTINATION_AIRPORT == x ,'State_Destination'] = dest ['STATE'] [i]

print ( df.head(15))

df.to_csv(r'Finals/data_and_cleaning/Cleaning_windrose_1.csv')

print ( 'Done' )

