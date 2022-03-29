import plotly.graph_objects as go
import pandas as pd
import json

df = pd.read_csv('../data_and_cleaning/flights_all_cleaned.csv', sep=',')
#print ( df.dtypes ) # überprüfen

df = df[[
    'ORIGIN_AIRPORT', 'ORIGIN_AIRPORT_LAT','ORIGIN_AIRPORT_LON',
    'DESTINATION_AIRPORT', 'DESTINATION_AIRPORT_LAT', 'DESTINATION_AIRPORT_LON']] # Daten reduzieren 


df = df.groupby(df.columns.tolist(),as_index=False).size() # Dublikate zusammenfassen und zählen 

df_airports =  pd.read_csv('../data_and_cleaning/airports.csv', sep=',') # DF nur mit Airports
#print ( df_airports.head(15)) # Testprint

fig = go.Figure()

for i in range(len(df)): # Strecken darstellen
    fig.add_trace(
        go.Scattergeo(
            locationmode = 'USA-states',
            lon = [df['ORIGIN_AIRPORT_LON'][i], df['DESTINATION_AIRPORT_LON'][i]], # Koordinaten für Flugstrecke übergeben 
            lat = [df['ORIGIN_AIRPORT_LAT'][i], df['DESTINATION_AIRPORT_LAT'][i]],
            mode = 'lines',
            line = dict(width = 0.5 ,color = 'rgb(47,79,79)'), # Für die Verbindungen werden grüne Linien gezogen
            opacity = float(df['size'][i]) / float(df['size'].max()), # Die Denkkraft der Linien wird je nach Häufigkeit der Verbindung angepasst / Wichtig für die Übersichtlichkeit
            
        )
    )


fig.add_trace(go.Scattergeo( # Airports durch Markerpunkte verzeichnen 
    locationmode = 'USA-states', 
    lon = df_airports['LONGITUDE'], # Koordinaten des Punkes übergeben 
    lat = df_airports['LATITUDE'],
    text = df_airports['AIRPORT'], 
    hoverinfo = 'text',
    mode = 'markers',
    marker = dict(
        size = 4,
        color = 'rgb(139, 0, 0)', # Markerpunkte werden dunkelrot dargestellt
        )))


fig.update_layout( # Layout bearbeiten
    title_text = '<b>Flightconnections on 01.01.2015 in the USA</b><br><i>(Hover for airport names)', # Zweizeilige Überschrift
    title_font_size=25,
    showlegend = False,
    geo = dict(
        scope = 'north america', # Fokus der Darstellung wird auf den Kontinent Nordamerika eingestellt
        projection_type = 'azimuthal equal area',
        showland = True,
        landcolor = 'rgb(224,238,238)', # Mapfarben anpassen
        countrycolor = 'rgb(205,170,125)', # Festland-Hintergrund leicht grün einfärben 
    )
)

fig.show()

