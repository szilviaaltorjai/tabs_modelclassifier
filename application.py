import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import pickle
from tabs import tab_1, tab_2, tab_4
#from utils import fig

## Instantiante Dash
app = dash.Dash()
application = app.server
app.config['suppress_callback_exceptions'] = True
app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})
app.title='Diabetes!'


## Layout
app.layout = html.Div([
    html.H1('Predicting diabetes in US counties'),
    dcc.Tabs(id="tabs-template", value='tab-1-template', children=[
        dcc.Tab(label='Introduction', value='tab-1-template'),
        dcc.Tab(label='Model Evaluation', value='tab-2-template'),
        dcc.Tab(label='User Inputs', value='tab-4-template'),
    ]),
    html.Div(id='tabs-content-template'),
#    dcc.Graph(figure=fig, id=fig)
])


############ Callbacks

@app.callback(Output('tabs-content-template', 'children'),
              [Input('tabs-template', 'value')])
def render_content(tab):
    if tab == 'tab-1-template':
        return tab_1.tab_1_layout
    elif tab == 'tab-2-template':
        return tab_2.tab_2_layout
    elif tab == 'tab-4-template':
        return tab_4.tab_4_layout

# Tab 2 callbacks

# @app.callback(Output('page-2-graphic', 'figure'),
#               [Input('page-2-radios', 'value')])
# def radio_results(value):
#     return display_eval_metrics(value)

# Tab 4 Callback # 1



####### Run the app #######
if __name__ == '__main__':
    application.run(debug=True)
