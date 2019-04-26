import dash
import dash_core_components as dcc
import dash_html_components as html
import base64

boat_photo=base64.b64encode(open('resources/Titanic.png', 'rb').read())

lorum='Lorem ipsum dolor sit amet, consectetaur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

tab_1_layout = html.Div([
    html.H3('Introduction'),
    html.Div([
    html.Div([
        html.Div(id='page-1-content', children=lorum*5),
        html.A('View code on github', href='https://github.com/austinlasseter/titanic_classifier'),
    ],className='ten columns'),
    html.Div([
    html.Img(src='data:image/png;base64,{}'.format(boat_photo.decode()), style={'height':'400px'}),
    ],className='two columns'),


    ],className='nine columns'),

])
