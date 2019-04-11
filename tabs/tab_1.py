import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


tab_1_layout = html.Div([
    html.H1('Page 1'),
    html.Div(id='page-1-content', children='content for page 1 goes here')
])
