# Author: CMOB 5/2/2022

# all of the modules
import os
import folium
from folium import IFrame, Popup, plugins
import pandas as pd
import geopandas
import rioxarray as rxr
import earthpy as et
import earthpy.spatial as es
import json

# setting up the map
m = folium.Map(location=[40.7128, -74.0060])

# data frame to put into markers on map
data = pd.DataFrame({
    'lon': [-58, 2, 145, 30.32],
    'lat': [-34, 49, -38, 59.93],
    'name': ['1', '2', '3', '4'],
    'loc': ['address 1', 'address2', 'address3', 'address4'],
    'site': ['https://youtu.be/fEvM-OUbaKs', 'https://youtu.be/fEvM-OUbaKs', 'https://youtu.be/fEvM-OUbaKs', 'https://youtu.be/fEvM-OUbaKs']
}, dtype=str)

# takes the data frame and puts into markers the on the map.
for i in range(0, len(data)):
    html = f"""
          <h1> {data.iloc [i]['name']} </h1>
          <p> Address: {data.iloc[i]['loc']} </p>
          <p> Website: <a href={data.iloc[i]['site']}> link </a> </p>
            """
    iframe = folium.IFrame(html=html, width=200, height=200)
    popup = folium.Popup(iframe, max_width=2650)
    folium.Marker(
                 location=[data.iloc[i]['lat'], data.iloc[i]['lon']],
                 popup=popup,
                 ).add_to(m)

m.save('map.html')
