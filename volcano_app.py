import folium
import pandas

data = pandas.read_csv("resources/webmap/volcanoes.txt")
lat = list(data["LAT"])
lan = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html_info = """<h4>Volcano Information:</h4>
Height: %s m
"""

html_link = """
Volcano Name:
<a href="https://www.google.com/search?q=%%22%s volcano%%22" target="_blank">%s</a><br>
Height: %s m
"""

def color_producer(elevation):
    if elevation < 1500:
        return "green"
    elif 1500 <= elevation < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[48.7767982,-121.8109970], zoom_start=7)
fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el, name in zip(lat, lan, elev, name):
    iframe = folium.IFrame(html=html_link % (name, name, el), width=200, height=100)
    #fg.add_child(folium.Marker(location = [lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=color_producer(el))))
    fgv.add_child(folium.CircleMarker(location = [lt, ln], radius=7, popup=folium.Popup(iframe), fill_color=color_producer(el), color='grey', fill_opacity=0.6))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(
    data=open("resources/webmap/world_1.json", "r", encoding="utf-8-sig").read(), 
    style_function=lambda x : {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange'
    if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")