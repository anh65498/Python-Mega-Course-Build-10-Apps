#create a base map
import folium           #works with python3
map = folium.Map(location=[37.335142, -121.881276], zoom_start=11, tiles="OpenStreetMap")
#help(folium.Map) to see parameters

#ADD LOCATION MARKERS (those Google Map's red marker)
#1. add 1 location marker
folium.Marker([37.335142, -121.881276], popup="Dima").add_to(map)
#python create JavaScript code using the Leaflet library

#2. add multiple location markers. 2 ways: Feature group or loop
#Feature Group: keep your code more organized and help when you add a control layer
feature_group = folium.FeatureGroup(name="My Map")
feature_group.add_child(folium.Marker([37.871906, -122.258563],
              popup='University of California, Berkeley',
              icon=folium.Icon(icon='bookmark')))
feature_group.add_child(folium.Marker([32.882407, -117.234817],
                popup='University of California, San Diego',
                icon=folium.Icon(icon='bookmark')))
#FOR loop
for coordinates in [[36.129075, -115.165290], [36.102576, -115.170253], [36.124745, -115.172081]]:
    feature_group.add_child(folium.Marker(coordinates,popup='Las Vegas hotel',
                  icon=folium.Icon(color='salmon')))
#import address from a text file and add location markers for each address
import pandas
df = pandas.read_csv("Volcanoes_USA.txt")
#print(volcanoes_data)
latitude_list = list(df["LAT"])
longitude_list = list(df["LON"])
#len(latitude_list)     #return the number of item in list
for lt, ln in zip(latitude_list, longitude_list):
    feature_group.add_child(folium.Marker([lt,ln],popup='Volcano'))


map.add_child(feature_group)

#save the map
map.save("Map1.html")
