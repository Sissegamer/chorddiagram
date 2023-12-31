import holoviews as hv
from holoviews import opts, dim
from bokeh.io import show
import pandas as pd

hv.extension('bokeh')

#read data from excel
excel_data_name = 'Matches.xlsx'
dt = pd.read_excel(excel_data_name)

#sorting of data by provider and receiver
datasorted = dt.groupby(['NACEIDProvider', 'NACEIDReceiver']).size().reset_index(name='Anzahl')
wertpaare = list(zip(datasorted['NACEIDProvider'], datasorted['NACEIDReceiver'], datasorted['Anzahl']))

source = [pair[0] for pair in wertpaare]
target = [pair[1] for pair in wertpaare]
weights = [pair[2] for pair in wertpaare]

data = {'NACE Code Provider': source,
        'NACE Code Receiver': target,
        'Anzahl': weights}

df = pd.DataFrame(data)

#Create the chord diagram
chord = hv.Chord(df)

#Configure the chart
chord.opts(
    opts.Chord(cmap='Category20', labels='index',
               node_color='index', edge_color=dim('Anzahl').str(),
               height=400, width=400)
)

#Convert the HoloViews object to a Bokeh Plot instance
bokeh_plot = hv.render(chord, backend='bokeh')

#Show the chart in a separate Bokeh web browser window
show(bokeh_plot)