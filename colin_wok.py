# Author: CMOB 5/2/2022

# all of the modules
# import os
import folium
# from folium import IFrame, Popup, plugins
import pandas as pd
# import geopandas
# import rioxarray as rxr
# import earthpy as et
# import earthpy.spatial as es
# import json

# setting up the map
m = folium.Map(location=[40.7128, -74.0060])

lon = [-73.8589411, -73.8494246, -73.851252]
lat = [40.889903, 40.8910298, 40.8868126]
name = ['MOUNT PISGAH BAPTIST CHURCH', 'THE GRACE OF GOD MINISTRIES – CHURCH INC', 'Bronx Bethany Community Corporation Food Provider']
loc = ['709 EAST 228 STREET, BRONX, NY, 10466', '963 EAST 233 STREET, BRONX, NY, 10466', '971 EAST 227 STREET, BRONX, NY, 10466']

# data frame to put into markers on map
data = pd.DataFrame({
    'lon': lon,
    'lat': lat,
    'name': name,
    'loc': loc
}, dtype=str)

# takes the data frame and puts into markers the on the map.
for i in range(0, len(data)):
    html = f"""
          <h1> {data.iloc [i]['name']} </h1>
          <p> Address: {data.iloc[i]['loc']} </p>
            """
    iframe = folium.IFrame(html=html, width=200, height=200)
    popup = folium.Popup(iframe, max_width=2650)
    folium.Marker(
                 location=[data.iloc[i]['lat'], data.iloc[i]['lon']],
                 popup=popup,
                 ).add_to(m)

# saves the map, allowing it to be opened in a web browser
m.save('map.html')

m
