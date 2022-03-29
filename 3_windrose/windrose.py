import plotly.graph_objects as go
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots


# Cleaning in 2 Teilen ausgelagert, wegen langer Laufzeit
# Durchschnittliche Verspätung je Richtung untersuchen 

df_org = pd.read_csv('../data_and_cleaning/Cleaning_windrose_2_new.csv', sep=',')

df_org ['ALL'] = "1"

# SubPlots definieren

#P lotly Express – Bibliothek verfügt nicht über  Subplot-Funktion -> plotly.graph_objects 
fig = make_subplots( 
    rows=3, cols=3,
    specs=[[{"type": "barpolar"}, {"type": "barpolar"}, {"type": "bar"}],
           [{"type": "barpolar"}, {"type": "barpolar"}, {"type": "barpolar"}],
           [{"type": "barpolar"}, {"type": "barpolar"}, {"type": "barpolar"}]
           ],

    subplot_titles=("","Division of states in sections", "Generell amount of flights in each part of the US")
)


# Datenaufbereitung Staten oben links

df = df_org[ (df_org.State_Depature == "AK") | (df_org.State_Depature == "ID") | (df_org.State_Depature == "MT") | (df_org.State_Depature == "OR") | (df_org.State_Depature == "WA") | (df_org.State_Destination == "AK") | (df_org.State_Destination == "ID") | (df_org.State_Destination == "MT") | (df_org.State_Destination == "OR") | (df_org.State_Destination == "WA")]



df = df[['ALL', 'Kompass']] # Laufzeit für die folgenden Schritte verringern 
l1 = len (df) # größe des df allgemein

# die Daten gruppieren, alle Flüge, die bisher eine eigene Zeile hatten, werden nach Flugrichtung zusammengefasst
# groupby in Kombination mit size(), hierdurch werden alle Duplikate entfernt, die Anzahl der ehemaligen Duplikate wird aber in einer neuen Spalte gespeichert
df = df[df.duplicated(['ALL', 'Kompass'])].groupby(['Kompass']).size().reset_index(name='Duplicates') 

sorter = [ 'E', 'ENE', 'NE', 'NNE', 'N', 'NNW', 'NW','WNW', 'W', 'WSW', 'SW', 'SSW', 'S', 'SSE', 'SE', 'ESE'] # Df für die Anzeige als Kompass in die richtige Reihenfolge bringen
sorterIndex = dict(zip(sorter, range(len(sorter)))) # Dict mit Liste erstellen 
df['newindex'] = df['Kompass'].map(sorterIndex) # Reihenfolge als Index übergeben
df = df.set_index('newindex')
df = df.sort_index()


# Subplot 1 Barpolar
fig.add_trace(
    
    go.Barpolar(
    r = df ["Duplicates"] , theta = df ["Kompass"], ),
              row=2, col=1)


# Datenaufbereitung Staten oben mitte 

df = df_org[ (df_org.State_Depature == "IA") | (df_org.State_Depature == "MN") | (df_org.State_Depature == "NE") | (df_org.State_Depature == "ND") | (df_org.State_Depature == "SD") | (df_org.State_Depature == "WY") | 
(df_org.State_Destination == "IA") | (df_org.State_Destination == "MN") | (df_org.State_Destination == "NE") | (df_org.State_Destination == "ND") | (df_org.State_Destination == "SD") | (df_org.State_Destination == "WY")]

df = df[['ALL', 'Kompass']] #Daten eingrenzen
l2 = len (df) # größe des df allgemein
df = df[df.duplicated(['ALL', 'Kompass'])].groupby(['Kompass']).size().reset_index(name='Duplicates')

sorter = ['E', 'ENE', 'NE', 'NNE', 'N', 'NNW', 'NW','WNW', 'W', 'WSW', 'SW', 'SSW', 'S', 'SSE', 'SE', 'ESE'] # Df für die Anzeige als Kompass in die richtige Reihenfolge bringen
sorterIndex = dict(zip(sorter, range(len(sorter)))) # Dict mit Liste erstellen 
df['newindex'] = df['Kompass'].map(sorterIndex) # Reihenfolge als Index übergeben
df = df.set_index('newindex')
df = df.sort_index()


# Subplot 2 Barpolar

fig.add_trace(

    go.Barpolar(
    r = df ["Duplicates"] , theta = df ["Kompass"] ),
              row=2, col=2)

# Datenaufbereitung Staten oben rechts

df = df_org[ (df_org.State_Depature == "CT") | (df_org.State_Depature == "DE") | (df_org.State_Depature == "DC") | (df_org.State_Depature == "ME") | (df_org.State_Depature == "MD") | (df_org.State_Depature == "MI") | 
(df_org.State_Depature == "MA") | (df_org.State_Depature == "NH") | (df_org.State_Depature == "NJ") | (df_org.State_Depature == "NY") | (df_org.State_Depature == "OH") | (df_org.State_Depature == "PA") | (df_org.State_Depature == "RI") | 
(df_org.State_Depature == "VT") | (df_org.State_Depature == "VA") | (df_org.State_Depature == "WV") | (df_org.State_Depature == "WI") | (df_org.State_Depature == "IN") | (df_org.State_Depature == "IL") |
(df_org.State_Destination == "CT") | (df_org.State_Destination == "DE") | (df_org.State_Destination == "DC") | (df_org.State_Destination == "ME") | (df_org.State_Destination == "MD") | (df_org.State_Destination == "MI") 
| (df_org.State_Destination == "MA") | (df_org.State_Destination == "NH") | (df_org.State_Destination == "NJ") | (df_org.State_Destination == "NY") | (df_org.State_Destination == "OH") | (df_org.State_Destination == "PA") | (df_org.State_Destination == "RI") |
 (df_org.State_Destination == "VT") | (df_org.State_Destination == "VA") | (df_org.State_Destination == "WV") | (df_org.State_Destination == "WI") | (df_org.State_Destination == "IN") | (df_org.State_Destination == "IL")  ]

df = df[['ALL', 'Kompass']] #Daten eingrenzen
l3 = len (df) # größe des df allgemein
df = df[df.duplicated(['ALL', 'Kompass'])].groupby(['Kompass']).size().reset_index(name='Duplicates')

sorter = ['E', 'ENE', 'NE', 'NNE', 'N', 'NNW', 'NW','WNW', 'W', 'WSW', 'SW', 'SSW', 'S', 'SSE', 'SE', 'ESE'] # Df für die Anzeige als Kompass in die richtige Reihenfolge bringen
sorterIndex = dict(zip(sorter, range(len(sorter)))) # Dict mit Liste erstellen 
df['newindex'] = df['Kompass'].map(sorterIndex) # Reihenfolge als Index übergeben
df = df.set_index('newindex')
df = df.sort_index()

# Subplot 3 Barpolar

fig.add_trace(

    go.Barpolar(
    r = df ["Duplicates"] , theta = df ["Kompass"] ),
              row=2, col=3)

# Datenaufbereitung Staten unten links

df = df_org[ (df_org.State_Depature == "AZ") | (df_org.State_Depature == "CA") | (df_org.State_Depature == "HI") | (df_org.State_Depature == "NV") | (df_org.State_Depature == "UT") |
(df_org.State_Destination == "AZ") | (df_org.State_Destination == "CA") | (df_org.State_Destination == "HI") | (df_org.State_Destination == "NV") | (df_org.State_Destination == "UT")  ]

df = df[['ALL', 'Kompass']] #Daten eingrenzen
l4 = len (df) # größe des df allgemein
df = df[df.duplicated(['ALL', 'Kompass'])].groupby(['Kompass']).size().reset_index(name='Duplicates')

sorter = ['E', 'ENE', 'NE', 'NNE', 'N', 'NNW', 'NW','WNW', 'W', 'WSW', 'SW', 'SSW', 'S', 'SSE', 'SE', 'ESE'] # Df für die Anzeige als Kompass in die richtige Reihenfolge bringen
sorterIndex = dict(zip(sorter, range(len(sorter)))) # Dict mit Liste erstellen 
df['newindex'] = df['Kompass'].map(sorterIndex) # Reihenfolge als Index übergeben
df = df.set_index('newindex')
df = df.sort_index()


# Subplot 4 Barpolar

fig.add_trace(
    
    go.Barpolar(
    r = df ["Duplicates"] , theta = df ["Kompass"] ),
              row=3, col=1)


# Datenaufbereitung Staten unten mitte 

df = df_org[ (df_org.State_Depature == "CO") | (df_org.State_Depature == "KS") | (df_org.State_Depature == "NM") | (df_org.State_Depature == "OK") | (df_org.State_Depature == "TX") |
(df_org.State_Destination == "CO") | (df_org.State_Destination == "KS") | (df_org.State_Destination == "NM") | (df_org.State_Destination == "OK") | (df_org.State_Destination == "TX")]

df = df[['ALL', 'Kompass']] #Daten eingrenzen
l5 = len (df) # größe des df allgemein
df = df[df.duplicated(['ALL', 'Kompass'])].groupby(['Kompass']).size().reset_index(name='Duplicates')

sorter = ['E', 'ENE', 'NE', 'NNE', 'N', 'NNW', 'NW','WNW', 'W', 'WSW', 'SW', 'SSW', 'S', 'SSE', 'SE', 'ESE'] # Df für die Anzeige als Kompass in die richtige Reihenfolge bringen
sorterIndex = dict(zip(sorter, range(len(sorter)))) # Dict mit Liste erstellen 
df['newindex'] = df['Kompass'].map(sorterIndex) # Reihenfolge als Index übergeben
df = df.set_index('newindex')
df = df.sort_index()


# Subplot 5 Barpolar

fig.add_trace(

    go.Barpolar(
    r = df ["Duplicates"] , theta = df ["Kompass"] ),
              row=3, col=2)

# Datenaufbereitung Staten unten rechts

df = df_org[ (df_org.State_Depature == "AL") | (df_org.State_Depature == "AR") | (df_org.State_Depature == "FL") | (df_org.State_Depature == "GA") | (df_org.State_Depature == "KX") | (df_org.State_Depature == "LA") 
| (df_org.State_Depature == "MS") | (df_org.State_Depature == "MO") | (df_org.State_Depature == "NC")| (df_org.State_Depature == "SC") | (df_org.State_Depature == "TN") |
 (df_org.State_Destination == "AL") | (df_org.State_Destination == "AR") | (df_org.State_Destination == "FL") | (df_org.State_Destination == "GA") | (df_org.State_Destination == "KX") | (df_org.State_Destination == "LA") | 
 (df_org.State_Destination == "MS") | (df_org.State_Destination == "MO") | (df_org.State_Destination == "NC")| (df_org.State_Destination == "SC") | (df_org.State_Destination == "TN")]

df = df[['ALL', 'Kompass']] #Daten eingrenzen
l6 = len (df) # größe des df allgemein
df = df[df.duplicated(['ALL', 'Kompass'])].groupby(['Kompass']).size().reset_index(name='Duplicates')

sorter = ['E', 'ENE', 'NE', 'NNE', 'N', 'NNW', 'NW','WNW', 'W', 'WSW', 'SW', 'SSW', 'S', 'SSE', 'SE', 'ESE'] # Df für die Anzeige als Kompass in die richtige Reihenfolge bringen
sorterIndex = dict(zip(sorter, range(len(sorter)))) # Dict mit Liste erstellen 
df['newindex'] = df['Kompass'].map(sorterIndex) # Reihenfolge als Index übergeben
df = df.set_index('newindex')
df = df.sort_index()


# Subplot 6 Barpolar

fig.add_trace(
    
    go.Barpolar(
    r = df ["Duplicates"] , theta = df ["Kompass"] ),
              row=3, col=3)


# Subplot 7 Bar (optional)

fig.add_trace(go.Bar(x=[ "States North-East", "States North", "States North-West", "States South-East", "States South", "States South-West" ], y=[ l1, l2, l3, l4, l5, l6 ], marker_color=[ 'rgb(99, 110, 250)', 'rgb(240, 85, 58)', 'rgb(0, 204, 150)', 'rgb(171, 99, 250)', 'rgb(255, 161, 91)','rgb(26, 211, 243)']), # einfaches Barchart für übersicht
              row=1, col=3)



# Add images zur erklärung der Bezirke

import base64

image_filename = '../data_and_cleaning/usstates_black.png'
imagem_tunel = base64.b64encode(open(image_filename, 'rb').read()) 


fig.add_layout_image(
    dict(
        source='data:image/png;base64,{}'.format(imagem_tunel.decode()), # Bild hinzufügen 
        xref="paper", yref="paper",
        x=0.5, y=1.1, # Größe und Position festlegen
        sizex=0.4, sizey=0.4,
        xanchor="center", yanchor="top"
    )
)

fig.update_layout( showlegend=False)

fig.update_layout(
    title_text=("<b>Flight directions</b><br>" +
           "<i>in different Parts of the US</i>"),
    title_font_size=30,
    template="plotly_dark" # Dunkle darstellung für guten Kontrast
)


fig.show()
