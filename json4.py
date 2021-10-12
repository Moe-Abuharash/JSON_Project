from plotly import offline
from plotly.graph_objs import Scattergeo, Layout
import json

infile = open('US_fires_9_14.json', 'r')
#outfile = open('readable_eq_data.json', 'w')

eq_data = json.load(infile)

#son.dump(eq_data,outfile, indent=4)

#print(len(eq_data["features"]))

#list_of_eqs = eq_data["features"]
lats,lons,bright = [], [], []

for eq in eq_data:
    if eq['brightness'] > 450:
        lat = eq['latitude']
        lon = eq['longitude']
        brightness = eq['brightness']
        lats.append(lat)
        lons.append(lon)
        bright.append(brightness)


print(bright[:5])
print(lats[:5])
print(lons[:5])

data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':bright,
    'marker':{
        'size':[0.05*b for b in bright],
        'color':bright,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'brightness'}
    }
}]

my_layout = Layout(title = 'U.S. Fires 9/14/20 - 9/21/20')

fig = {'data': data, 'layout': my_layout}



offline.plot(fig, filename= 'globalfiresgreaterthan450.html')


