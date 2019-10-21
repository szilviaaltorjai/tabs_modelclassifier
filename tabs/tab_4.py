import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import numpy as np
import pickle

filepath='resources/predict_proba.csv'
df=pd.read_csv(filepath)
names=df['Name'].values
index=df['Name'].index.values
nameslist = list(zip(index, names))

tab_4_layout = html.Div([
    html.H3('Predicted probability of the county being above the national average of diabetes prevalence (random forest)'),
    html.Div([
        html.Div('Select:', className='one column'),
        # Title
            html.Div([
                html.Div('Select a county name'),
                dcc.Dropdown(
                id='page-4-dropdown',
                options=[{'label': k, 'value': i} for i,k in nameslist],
                value=nameslist[0][0]
            ),
        ],className='five columns'),
        html.Div(id='Probability', className='six columns'),
        html.Div(id='diabetes', children=''),
    ],className='twelve columns'),

])
