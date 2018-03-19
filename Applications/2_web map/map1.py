#create a base map
import folium           #works with python3
map = folium.Map(location=[37.335142, -121.881276], zoom_start=5, tiles="OpenStreetMap")
#help(folium.Map) to see parameters

#ADD LOCATION MARKERS (those Google Map's red marker)
#1. add 1 location marker
folium.Marker([37.335142, -121.881276], popup="SJSU").add_to(map)
#python create JavaScript code using the Leaflet library

#2. add multiple location markers. 2 ways: Feature group or loop
#Feature Group: keep your code more organized and help when you add a control layer
feature_group = folium.FeatureGroup(name="Location Markers")
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

#import information from a text file and add location markers for each address
import pandas
df = pandas.read_csv("Volcanoes_USA.txt")
#print(volcanoes_data)
latitude_list = list(df["LAT"])         #list of latitudes
longitude_list = list(df["LON"])        #list of longitudes
elevation_list = list(df["ELEV"])       #list of elevation
html = """<h4><center> %s </center></h4> %s <br>
"""
name_list = list(df["NAME"])            #list of volcanoes' name
#len(latitude_list)     #return the number of item in list
#color_code: function return a string of color for a location marker based on its elevation
def  color_code(elevation):
    if ele < 1000:
        col = "green"
    elif 1000 <= ele <= 3000:
        col = "orange"
    else:
        col ="red"
    return col

#create location markers with longitude, latitude, name, elevation of each volcano
for lt, ln, nm, ele in zip(latitude_list, longitude_list, name_list, elevation_list):
    iframe = folium.IFrame(html=html %(str(nm), "Elevation: " + str(ele)), width=200,height=100)
    col = color_code(ele)

#dir(folium)
#help(folium.CircleMarker)
    feature_group.add_child(folium.CircleMarker([lt,ln],
                            popup=folium.Popup(iframe),
                            color="grey", fill_color= str(col), fill="true", fill_opacity=0.7))
'''
popup argument reads the value as html by default.
If there are characters such as ' map will not be displayed.
this is why can't pass name like lt and ln
'''
#CREATE A POLYGON MAP (for area, countries). default color is green
fg = folium.FeatureGroup(name="Polygon's Features")
fg.add_child(folium.GeoJson(open('world.json', 'r', encoding='utf-8-sig').read(), name='geojson',
            style_function= lambda x: {
                #assign the polygon map yellow color for country with population < 10 mil
                "fillColor": "green" if x['properties']['POP2005'] < 10000000
                #assign the map polygons cyan if population is between 10mil  and 20mil
                else "orange" if 10000000 <= x['properties']['POP2005'] < 20000000
                else "red"

            }))

#CREATE A COUNTRY-BY-POPULATION MAP with Choropleth map


map.add_child(feature_group)    #custom layer
map.add_child(fg)               #polygon layer
#save the map
map.save("Map1.html")
