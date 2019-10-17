import dash
import dash_core_components as dcc
import dash_html_components as html
import base64

boat_photo=base64.b64encode(open('resources/Diabetes_map.jpeg', 'rb').read())


tab_1_layout = html.Div([
    html.H3('Introduction'),
    html.Div([
    html.Div([
        dcc.Markdown("This dashboard is a summary of the final project for the DCT35 course"),
        dcc.Markdown("* Project aim: assess the importance of aggregated level of physical activity when predicting diabetes in local areas"),
        dcc.Markdown("* Method: predict the proportion of adults with diabetes with- and without accounting for physical activity"),
        dcc.Markdown("* Results: TBC"),
        html.A('View code on github', href='https://github.com/szilviaaltorjai/tabs_modelclassifier'),
    ],className='eight columns'),
    html.Div([
    html.Img(src='data:image/png;base64,{}'.format(boat_photo.decode()), style={'height':'400px'}),
    ],className='two columns'),


    ],className='two columns'),

])
