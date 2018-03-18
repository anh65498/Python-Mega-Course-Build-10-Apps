
#create a base map
import folium           #works with python3
map = folium.Map(location=[45.5236, -122.6750], zoom_start=6, tiles="OpenStreetMap")
#help(folium.Map)

#save the map
map.save("Map1.html")
