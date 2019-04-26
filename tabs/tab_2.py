import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

choices=['Comparison of Models',
'Final Model Metrics',
'ROC-AUC',
'Confusion Matrix',
'Regression Coefficients']

tab_2_layout = html.Div([
    html.H3('Model Evaluation Statistics'),
    html.Div([
        html.Div([
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                id='page-2-radios',
                options=[{'label': i, 'value': i} for i in choices],
                value='Comparison of Models'
            ),
        ],className='two columns'),
        html.Div([
            dcc.Graph(id='page-2-graphic')
        ],className='ten columns'),
    ], className='twelve columns')




])
