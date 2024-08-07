# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.



from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('./data/daily_sales_data_final.csv')


fig = px.line(df, x="date", y="sales", color="location")

colors = {
    'background': '#263536',
    'backgroundColor': '#111111',
    'text': '#7FDBFF'
}

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(children='Sales of Pink Morsel',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    dcc.RadioItems(['north', 'south', 'east', 'west', 'all'], value='all', id='select'),


    dcc.Graph(
        id='Pink Morsel',
        figure=fig
    )
])

@callback(
    Output('Pink Morsel', 'figure'),
    Input('select', 'value'))
def update_graph(option):
    if(option != 'all'):
        filtered_df = df[df.location == option]
        figNew = px.line(filtered_df, x="date", y="sales")
    else:
        figNew = px.line(df, x="date", y="sales", color="location")

    return figNew

if __name__ == '__main__':
    app.run(debug=True)
