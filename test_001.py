from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd
import dash
from selenium import webdriver


driver = webdriver.Chrome()
def test_header_001(dash_duo):
    app = dash.Dash(__name__)
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
            },
            id='head'
        ),
        dcc.RadioItems(['north', 'south', 'east', 'west', 'all'], value='all', id='select'),


        dcc.Graph(
            id='Pink Morsel',
            figure=fig
        )
    ])
    dash_duo.start_server(app)

    dash_duo.wait_for_text_to_equal("#head", "Sales of Pink Morsel", timeout=4)

    assert dash_duo.find_element("#head").text == "Sales of Pink Morsel"

    assert dash_duo.get_logs() == [], "browser console should contain no error"

def test_header_002(dash_duo):
    app = dash.Dash(__name__)
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
            },
            id='head'
        ),
        dcc.RadioItems(['north', 'south', 'east', 'west', 'all'], value='all', id='select'),


        dcc.Graph(
            id='Pink Morsel',
            figure=fig
        )
    ])
    dash_duo.start_server(app)

    assert dash_duo.find_element("#select")

    assert dash_duo.get_logs() == [], "browser console should contain no error"

def test_header_003(dash_duo):
    app = dash.Dash(__name__)
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
            },
            id='head'
        ),
        dcc.RadioItems(['north', 'south', 'east', 'west', 'all'], value='all', id='select'),


        dcc.Graph(
            id='Pink Morsel',
            figure=fig
        )
    ])
    dash_duo.start_server(app)

    assert dash_duo.find_element("#Pink Morsel")

    assert dash_duo.get_logs() == [], "browser console should contain no error"