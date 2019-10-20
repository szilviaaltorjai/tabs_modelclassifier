import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly
import plotly.graph_objs as go
import pickle
#from plotly.subplots import make_subplots

### Comparison of Possible Models

Viridis=[
"#440154", "#440558", "#450a5c", "#450e60", "#451465", "#461969",
"#461d6d", "#462372", "#472775", "#472c7a", "#46307c", "#45337d",
"#433880", "#423c81", "#404184", "#3f4686", "#3d4a88", "#3c4f8a",
"#3b518b", "#39558b", "#37598c", "#365c8c", "#34608c", "#33638d",
"#31678d", "#2f6b8d", "#2d6e8e", "#2c718e", "#2b748e", "#29788e",
"#287c8e", "#277f8e", "#25848d", "#24878d", "#238b8d", "#218f8d",
"#21918d", "#22958b", "#23988a", "#239b89", "#249f87", "#25a186",
"#25a584", "#26a883", "#27ab82", "#29ae80", "#2eb17d", "#35b479",
"#3cb875", "#42bb72", "#49be6e", "#4ec16b", "#55c467", "#5cc863",
"#61c960", "#6bcc5a", "#72ce55", "#7cd04f", "#85d349", "#8dd544",
"#97d73e", "#9ed93a", "#a8db34", "#b0dd31", "#b8de30", "#c3df2e",
"#cbe02d", "#d6e22b", "#e1e329", "#eae428", "#f5e626", "#fde725"]

compare_models=pd.read_pickle('resources/compare_models.pkl')

#fig = make_subplots(specs=[[{"secondary_y": True}]])

mydata1 = go.Bar(
    x=compare_models.loc['RMSE'].index,
    y=compare_models.loc['RMSE'],
    name=compare_models.index[0],
#    secondary_y=False,
    marker=dict(color=Viridis[50])
)
mydata2 = go.Bar(
    x=compare_models.loc['R2'].index,
    y=compare_models.loc['R2'],
    name=compare_models.index[1],
#    secondary_y=True,
    marker=dict(color=Viridis[30])
)

mylayout = go.Layout(
    title='Comparison of Linear Models with and without physical activity',
    xaxis = dict(title = 'Predictive models'), # x-axis label
    yaxis = dict(title = 'RMSE matrixes'), # y-axis label
#    fig.update_yaxes(title_text="R2 matrixes", secondary_y=True),
#    fig.update_yaxes(title_text="R2 matrixes", secondary_y=True),

)
fig = go.Figure(data=[mydata1, mydata2], layout=mylayout)

tab_2_layout = html.Div([
    html.H3('Model Evaluation Statistics'),
    html.Div([
        html.Div([
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                id='page-2-radios',
                value='Comparison of Models'
            ),
        ],className='two columns'),
        html.Div([
            dcc.Graph(figure=fig, id='page-2-graphic')
        ],className='ten columns'),
    ], className='twelve columns')




])
