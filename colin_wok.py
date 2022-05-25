# Author: CMOB 5/2/2022

# all of the modules
import folium
import pandas as pd
from geopy.geocoders import Nominatim

lon = []
lat = []
title = []
loc = []

dataset = "/Users/p22cobrien/Desktop/Project/final-project-ian-colin-1/Food Bank For NYC Open Sites copy.csv"
csv = pd.read_csv(dataset)
df = pd.DataFrame(csv)
addresses = df.loc[:, "address"]
names = df.loc[:, "name"]
for name in names:
    title.append(name)

for address in addresses:
    locator = Nominatim(user_agent="my-geocoder")
    location = locator.geocode("{0}".format(address), timeout=100)
    lon.append(location.longitude)
    lat.append(location.latitude)
    loc.append(address)


# setting up the map
m = folium.Map(location=[40.7128, -74.0060])

# data frame to put into markers on map
data = pd.DataFrame({
    'lon': lon,
    'lat': lat,
    'title': title,
    'loc': loc
}, dtype=str)

# takes the data frame and puts into markers the on the map.
for i in range(0, len(data)):
    html = f"""
          <h1> {data.iloc [i]['title']} </h1>
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
