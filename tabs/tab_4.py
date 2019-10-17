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
names=df['FIPS2'].values
index=df['FIPS2'].index.values
nameslist = list(zip(index, names))

tab_4_layout = html.Div([
    html.H3('Results for Testing Dataset'),
    html.Div([
        html.Div([
            html.Div('Select a county code to view their predicted diabetes prevalence:'),
            dcc.Dropdown(
                id='page-4-dropdown',
                options=[{'label': k, 'value': i} for i,k in nameslist],
                value=nameslist[0][0]
            ),

        ],className='six columns'),
        html.Div([
        ],className='six columns'),
    ],className='twelve columns'),

])
