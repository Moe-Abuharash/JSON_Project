from plotly import offline
from plotly.graph_objs import Scattergeo, Layout
import json

infile = open('eq_data_1_day_m1.json', 'r')
outfile = open('readable_eq_data.json', 'w')

eq_data = json.load(infile)

json.dump(eq_data, outfile, indent=4)

#print(eq_data["metadata"]['count'])
print(len(eq_data["features"]))

list_of_eqs = eq_data["features"]

mags,lats,lons, hover_texts = [], [], [], []

for eq in list_of_eqs:
    mag = eq['properties']['mag']
    lat = eq['geometry']['coordinates'][1]
    lon = eq['geometry']['coordinates'][0]
    title = eq['properties']['title']
    mags.append(mag)
    lats.append(lat)
    lons.append(lon)
    hover_texts.append(title)
    
print(mags[:5])
print(lats[:5])
print(lons[:5])


#data = [Scattergeo(lon=lons, lat=lats)]
data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':hover_texts,
    'marker':{
        'size':[5*m for m in mags],
        'color':mags,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorband':{'title':'Magnitude'}
    }
}]
my_layout = Layout(title = 'Global Earthquake 1 Day')

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename= 'globalearthquake1day.html')





