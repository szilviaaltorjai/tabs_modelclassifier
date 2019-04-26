import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import pandas as pd
from tabs import tab_1, tab_2, tab_3
from utils import display_eval_metrics, Viridis


df=pd.read_csv('resources/final_probs.csv')


## Instantiante Dash
app = dash.Dash()
application = app.server
app.config['suppress_callback_exceptions'] = True
app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

## Layout
app.layout = html.Div([
    html.H1('Surviving the Titanic'),
    dcc.Tabs(id="tabs-example", value='tab-1-example', children=[
        dcc.Tab(label='Introduction', value='tab-1-example'),
        dcc.Tab(label='Model Evaluation', value='tab-2-example'),
        dcc.Tab(label='Testing Results', value='tab-3-example'),
    ]),
    html.Div(id='tabs-content-example')
])


############ Callbacks

@app.callback(Output('tabs-content-example', 'children'),
              [Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'tab-1-example':
        return tab_1.tab_1_layout
    elif tab == 'tab-2-example':
        return tab_2.tab_2_layout
    elif tab == 'tab-3-example':
        return tab_3.tab_3_layout

# Tab 2 callbacks

@app.callback(Output('page-2-graphic', 'figure'),
              [Input('page-2-radios', 'value')])
def radio_results(value):
    return display_eval_metrics(value)

# Tab 3 callback # 1
@app.callback(dash.dependencies.Output('page-3-content', 'children'),
              [dash.dependencies.Input('page-3-dropdown', 'value')])
def page_3_dropdown(value):
    name=df.loc[value, 'Name']
    return f'You have selected "{name}"'

# Tab 3 callback # 2
@app.callback(dash.dependencies.Output('survival-prob', 'children'),
              [dash.dependencies.Input('page-3-dropdown', 'value')])
def page_3_survival(value):
    survival=df.loc[value, 'survival_prob']
    actual=df.loc[value, 'Survived']
    survival=round(survival*100)
    return f'Predicted probability of survival is {survival}%, Actual survival is {actual}'

# Tab 3 callback # 2
@app.callback(dash.dependencies.Output('survival-characteristics', 'children'),
              [dash.dependencies.Input('page-3-dropdown', 'value')])
def page_3_characteristics(value):
    mydata=df.drop(['Survived', 'survival_prob', 'Name'], axis=1)
    return html.Table(
        [html.Tr([html.Th(col) for col in mydata.columns])] +
        [html.Tr([
            html.Td(mydata.iloc[value][col]) for col in mydata.columns
        ])]
    )

####### Run the app #######
if __name__ == '__main__':
    application.run(debug=True, port=8080)
