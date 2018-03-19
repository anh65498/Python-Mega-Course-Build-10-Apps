#create a base map
import folium           #works with python3
map = folium.Map(location=[43.075968, -107.290284], zoom_start=5, tiles="OpenStreetMap")
#help(folium.Map) to see parameters

#ADD LOCATION MARKERS (those Google Map's red marker)
#1. add 1 location marker
folium.Marker([37.335142, -121.881276], popup="SJSU",
            icon=folium.Icon(icon='home')).add_to(map)
#python create JavaScript code using the Leaflet library

#2. add multiple location markers. 2 ways: Feature group or loop
#Feature Group: keep your code more organized and help when you add a control layer
basic_fg = folium.FeatureGroup(name="Basic Locations")
basic_fg.add_child(folium.Marker([37.871906, -122.258563],
              popup='University of California, Berkeley',
              icon=folium.Icon(icon='education')))
basic_fg.add_child(folium.Marker([32.882407, -117.234817],
                popup='University of California, San Diego',
                icon=folium.Icon(icon='education')))
asic_fg.add_child(folium.Marker([34.068921, -118.445181],
                popup='University of California, Los Angeles',
                icon=folium.Icon(icon='education')))
#FOR loop
for coordinates in [[36.129075, -115.165290], [36.102576, -115.170253], [36.124745, -115.172081]]:
    basic_fg.add_child(folium.Marker(coordinates,popup='Las Vegas hotel',
                  icon=folium.Icon(color='white', icon="star-empty")))

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
vol_fg = folium.FeatureGroup(name="Volcanoes' Locations")
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
    iframe = folium.IFrame(html=html %(str(nm), "Elevation: " + str(ele)), width=100,height=50)
    col = color_code(ele)

#dir(folium)
#help(folium.CircleMarker)
    vol_fg.add_child(folium.CircleMarker([lt,ln],
                            popup=folium.Popup(iframe),
                            color="grey", fill_color= str(col), fill="true", fill_opacity=0.7))
'''
popup argument reads the value as html by default.
If there are characters such as ' map will not be displayed.
this is why can't pass name like lt and ln
'''
##CREATE A COUNTRY-BY-POPULATION MAP with Choropleth map
pop_fg = folium.FeatureGroup(name="Population Colorcode")
pop_fg.add_child(folium.GeoJson(open('world.json', 'r', encoding='utf-8-sig').read(), name='geojson',
            style_function= lambda x: {
                #assign the polygon map yellow color for country with population < 10 mil
                "fillColor": "green" if x['properties']['POP2005'] < 10000000
                #assign the map polygons cyan if population is between 10mil  and 20mil
                else "orange" if 10000000 <= x['properties']['POP2005'] < 20000000
                else "red"
            }))


map.add_child(basic_fg)         #basic location layer
map.add_child(pop_fg)           #polygon layer
map.add_child(vol_fg)           #volcanoes location layer
#if add_child(vol_fg) goes before add_child(pop_fg), volcanoes' popup will not show

#turn on/off between base, location marker and choropleth map
map.add_child(folium.LayerControl())
#save the map
map.save("Map1.html")
