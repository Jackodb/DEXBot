import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

def test():
    print('hoi')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)

#df = pd.read_csv('test.csv',encoding='utf-8',usecols=['Price','Mountain_neutral_view','Current'])

price = [0.009906885, 0.012007145, 0.014552658999999999, 0.017637823, 0.021377042000000002, 0.025908973999999998, 0.031401677, 0.038058833, 0.046127305, 0.055906294, 0.067758428, 0.082123215, 0.099533336, 0.120634404, 0.146208897, 0.177205184, 0.214772682, 0.260304491, 0.315489043, 0.38237272, 0.463435737, 0.561684113, 0.680761145, 0.8250825079999999, 1.0, 1.212, 1.468944, 1.780360128, 2.157796475, 2.615249328, 3.169682185, 3.8416548089999996, 4.6560856280000005, 5.643175781, 6.839529047, 8.289509205, 10.04688516, 12.17682481, 14.75831167, 17.88707374, 21.67913338, 26.27510965, 31.845432899999995, 38.59666467, 46.77915758, 56.69633899, 68.71596286, 83.28374698, 100.93990129999999]
mountain = [21.31220488, 23.4627921, 25.83039231, 28.43690403, 31.30643549, 34.46552768, 37.94339981, 41.77221955, 45.98740057, 50.62793009, 55.73672949, 61.36105127, 67.55291614, 74.36959414, 81.87413436, 90.1359481, 99.23145085, 109.24476909999998, 120.26851840000002, 132.4046601, 145.7654443, 160.4744481, 176.6677185, 194.4950311, 214.12127489999997, 194.4950311, 176.6677185, 160.4744481, 145.7654443, 132.4046601, 120.26851840000002, 109.24476909999998, 99.23145085, 90.1359481, 81.87413436, 74.36959414, 67.55291614, 61.36105127, 55.73672949, 50.62793009, 45.98740057, 41.77221955, 37.94339981, 34.46552768, 31.30643549, 28.43690403, 25.83039231, 23.4627921, 21.31220488]
current = [1.0656102440000002, 1.173139605, 1.291519616, 1.4218452019999999, 1.565321775, 1.723276384, 1.897169991, 2.088610978, 2.299370029, 2.531396505, 2.786836475, 3.068052564, 3.377645807, 3.7184797069999997, 4.093706718, 4.506797405, 4.961572543, 5.462238455, 6.01342592, 6.620233005, 7.288272215, 8.023722405, 8.833385925, 9.724751555, 10.70606375, 9.724751555, 8.833385925, 8.023722405, 7.288272215, 6.620233005, 6.01342592, 5.462238455, 4.961572543, 4.506797405, 4.093706718, 3.7184797069999997, 3.377645807, 3.068052564, 2.786836475, 2.531396505, 2.299370029, 2.088610978, 1.897169991, 1.723276384, 1.565321775, 1.4218452019999999, 1.291519616, 1.173139605, 1.0656102440000002]

bar_background_colors_initial = []
bar_background_colors_current = []

for i in price:
    i = round(i,3)
    if i < 1:
        bar_background_colors_initial.append('rgba(58, 98, 87, 0.5)')
        bar_background_colors_current.append('rgba(51, 204, 51, 0.9)')
    else:
        if i == 1:
            bar_background_colors_initial.append('rgba(217,217,217,0.5)')
            bar_background_colors_current.append('rgba(242,242,242,0.9)')
        else:
            bar_background_colors_initial.append('rgba(230, 0, 0, 0.5)')
            bar_background_colors_current.append('rgba(255, 0, 0, 0.9)')

app.layout = html.Div(className='wrapper',style={'height':'80vh'},children=[
    html.H1(children='Staggered Orders Overview'),
    html.H2(children='A mountain based visualisation of (base asset/quote asset)'),

    dcc.Graph(
        figure=go.Figure(
            data=[
                go.Bar(
                    x=[i for i in range(len(list(price)))],
                    y=list(current),
                    name='Buy',
                    marker=go.bar.Marker(
                        color=bar_background_colors_current
                    )
                ),
                go.Bar(
                    x=[i for i in range(len(list(price)))],
                    y=list(mountain),
                    name='Sell',
                    marker=go.bar.Marker(
                        color=bar_background_colors_initial
                    )
                )
            ],
            layout=go.Layout(
                autosize=True,
                xaxis=dict(
                    title='BTS/USD',
                    zerolinecolor='rgba(153,153,153,0.2)'
                ),
                yaxis=dict(
                    title='Order size',
                    gridcolor='rgba(153,153,153,0.2)'
                ),
                barmode='stack',
                plot_bgcolor='rgb(21,43,42)',
                paper_bgcolor='rgb(21,43,42)',
                font={
                    'color':'white'
                }
            )
        ),
        style={'height':'100%','width':'60vw','display':'inline-block'}
    )
])

app.run_server(debug=True)
