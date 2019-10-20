import dash
import dash_core_components as dcc
import dash_html_components as html
import base64

boat_photo=base64.b64encode(open('resources/Diabetes_map.jpeg', 'rb').read())


tab_1_layout = html.Div([
    html.H3('Introduction'),
    html.Div([
    html.Div([
        dcc.Markdown("This dashboard is a summary of the final project for the DCDAT35 course"),
        dcc.Markdown("* Project aim: to predict diabetes in local areas"),
        dcc.Markdown("* Method: Predict the prevalence of diabetes among adults with two linear models which include and do not include physical activity (linear model). Predict the probability that the area is above the national average of diabetes prevalence (random forest)"),
        dcc.Markdown("* Results: Accounting for physical activity improves the model predicting power. The probability of a county being above the national average ranges between 46%-60%."),
        html.A('View code on github', href='https://github.com/szilviaaltorjai/tabs_modelclassifier'),
    ],className='nine columns'),
    html.Div([
    html.Img(src='data:image/png;base64,{}'.format(boat_photo.decode()), style={'height':'400px'}),
    ],className='three columns'),


    ],className='seven columns'),

])
