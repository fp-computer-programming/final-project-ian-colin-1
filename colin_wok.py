# Author: CMOB 5/2/2022

import os
import folium
from folium import plugins
import pandas as pd
import geopandas
import rioxarray as rxr
import earthpy as et
import earthpy.spatial as es
import json

m = folium.Map(location=[40.7128, -74.0060])


data = pd.DataFrame({
    'lon': [-58, 2, 145, 30.32],
    'lat': [-34, 49, -38, 59.93],
    'name': ['1', '2', '3', '4']
}, dtype=str)

for i in range(0, len(data)):
    folium.Marker(
                 location=[data.iloc[i]['lat'], data.iloc[i]['lon']],
                 popup=data.iloc[i]['name'],
                 ).add_to(m)


m.save('map.html')
