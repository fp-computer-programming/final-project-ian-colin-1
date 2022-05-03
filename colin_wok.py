# Author: CMOB 5/2/2022

import folium
import pandas as pd
import geopandas

m = folium.Map(location=[74.0060, 40.7128])

m.save('map.html')
