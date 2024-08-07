# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.



from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('./data/daily_sales_data_final.csv')

print(df)

fig = px.line(df, x="date", y="sales", color="location")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
