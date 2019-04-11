import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output

filepath='00_resources/final_probs.csv'
df=pd.read_csv(filepath)
names=df['Name'].values
index=df['Name'].index.values
nameslist = list(zip(index, names))

tab_3_layout = html.Div([
    html.H1('Page 3'),
    html.Div('Select a passenger to view their predicted survival:'),
    dcc.Dropdown(
        id='page-3-dropdown',
        options=[{'label': k, 'value': i} for i,k in nameslist],
        value=nameslist[0][0]
    ),
    html.Div(id='page-3-content'),
    html.Div(id='survival-prob')
])
