import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from tabs import tab_1, tab_2, tab_3
import pandas as pd


filepath='00_resources/final_probs.csv'
df=pd.read_csv(filepath)


## Instantiante Dash
app = dash.Dash()
server = app.server
app.config['suppress_callback_exceptions'] = True
app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

## Layout
app.layout = html.Div([
    html.H1('Dash Tabs component demo'),
    dcc.Tabs(id="tabs-example", value='tab-1-example', children=[
        dcc.Tab(label='Tab One', value='tab-1-example'),
        dcc.Tab(label='Tab Two', value='tab-2-example'),
        dcc.Tab(label='Tab Three', value='tab-3-example'),
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

# Tab 2 callback
@app.callback(Output('page-2-content', 'children'),
              [Input('page-2-radios', 'value')])
def page_2_radios(value):
    return 'You have selected "{}"'.format(value)
#
# Tab 3 callback
@app.callback(dash.dependencies.Output('page-3-content', 'children'),
              [dash.dependencies.Input('page-3-dropdown', 'value')])
def page_3_dropdown(value):
    name=df.loc[value, 'Name']
    return f'You have selected "{name}"'


# Tab 3 callback
@app.callback(dash.dependencies.Output('survival-prob', 'children'),
              [dash.dependencies.Input('page-3-dropdown', 'value')])
def page_3_dropdown(value):
    survival=df.loc[value, 'survival_prob']
    survival=round(survival*100)
    return f'Predicted probability of survival is {survival}%'

####### Run the app #######
if __name__ == '__main__':
    app.run_server()
