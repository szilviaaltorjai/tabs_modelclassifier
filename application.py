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

# Tab 4 callback # 2

@app.callback(Output('Probability', 'children'),
              [Input('page-4-dropdown', 'value')])
def page_4_diabetes(value):
    filepath='resources/predict_proba.csv'
    df=pd.read_csv(filepath)
    names=df['Name'].values
    index=df['Name'].index.values
    nameslist = list(zip(index, names))

    df=df[df['Name']==value]
    diabetes=df.loc[value, 'Probability']
    return f'Predicted probability of diabetes is {diabetes}%'



####### Run the app #######
if __name__ == '__main__':
    application.run(debug=True)
