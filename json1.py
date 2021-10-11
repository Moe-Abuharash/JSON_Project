from plotly import offline
from plotly.graph_objs import Scattergeo, Layout
import json

infile = open('US_fires_9_1.json', 'r')
outfile = open('readable_eq_data.json', 'w')

eq_data = json.load(infile)

json.dump(eq_data,outfile, indent=4)

print(eq_data["metadata"]['count'])
print(len(eq_data["features"]))

list_of_eqs = eq_data["features"]
mags = []
lats = []
lons = []

for eq in list_of_eqs:
    mag = eq['properties']['mag']
    lat = eq['geometry']['coordinates'][0]
    lon = eq['geometry']['coordinates'][1]
    mags.append(mag)
    lats.append(lat)
    lons.append(lon)

print(mags[:5])
print(lats[:5])
print(lons[:5])


data = [Scattergeo(lon=lons, lat=lats)]

my_layout = Layout(title = 'Global Earthquake 9/1 - 9/13')

fig = {'data':data, 'layout':my_layout}

offline.plot(fig, filename= 'globalearthquake 9/1 - 9/13 day.html')





