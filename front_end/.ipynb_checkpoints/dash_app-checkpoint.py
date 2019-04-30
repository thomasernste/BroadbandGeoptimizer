# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from flask import Flask
import sqlalchemy
import psycopg2
import sys
import os
import dash
import dash_table
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
from IPython.display import IFrame
import pandas as pd
from dash.dependencies import Input, Output, State
from IPython.display import IFrame



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


def connect():
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    user = os.environ['POSTGRES_USER']
    password = os.environ['POSTGRES_PASSWORD']
    host = os.environ['POSTGRES_HOST']
    db = os.environ['POSTGRES_DB']
    port = 5432
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con, meta

con, meta = connect()

mapbox_access_token = 'pk.eyJ1IjoidGplcm5zdGUiLCJhIjoiY2p1eGQwMGllMGxzajN6bWZmMmRhNGpmZyJ9.mTnmBDnPOb5sBYzSEF10rA'

# Create the data for Tab 1, the general scatterplot
df_tab1 = pd.read_sql("SELECT mc_downspeed, median_acquisition_cost as original_unpaid_balance, primary_city, zip_code FROM broadband_housing_complete WHERE fiber_yn = 1", con)
broadband_speed_1 = df_tab1['mc_downspeed'].tolist()
property_values_1 = df_tab1['original_unpaid_balance'].tolist()
city_1 = df_tab1['primary_city'].tolist()
zip_code_1 = df_tab1['zip_code'].tolist()


# Create the data for Tab 2, the table for those cities with fiber optic networks with property costs in the bottom 20% of the state
df_tab2 = pd.read_sql("SELECT primary_city, zip_code, median_acquisition_cost as original_unpaid_balance, dba_name FROM broadband_housing_complete WHERE fiber_yn = 1 and median_acquisition_cost < 135000 ORDER BY median_acquisition_cost", con)

city_2 = df_tab2['primary_city'].tolist()
zip_code_2 = df_tab2['primary_city'].tolist()
median_acquisition_cost_2 = df_tab2['original_unpaid_balance'].tolist()
dba_name = df_tab2['dba_name'].tolist()


# Create the data for Tab 3, the map of Washington showing the cities with fiber optic networks and property costs in the bottom 20% of the state
df_tab3 = pd.read_sql("SELECT mc_downspeed, median_acquisition_cost as original_unpaid_balance, primary_city, longitude, latitude FROM broadband_housing_complete", con)

# df_tab3 = pd.read_sql("SELECT mc_downspeed, median_acquisition_cost as original_unpaid_balance, primary_city, longitude, latitude FROM broadband_housing_complete WHERE fiber_yn = 1 and median_acquisition_cost < 148000 and mc_downspeed = 1000", con)

latitude_3 = df_tab3['latitude']
longitude_3 = df_tab3['longitude']
city_3 = df_tab3['primary_city']


app.layout = html.Div([
    html.H1('Broadband Scout'),
    dcc.Tabs(id="tabs-example", value='tab-1', children=[
        dcc.Tab(label='Scatter Plot', value='tab-1'),
        dcc.Tab(label='Table', value='tab-2'),
        dcc.Tab(label='Map', value='tab-3'),
        
    ]),
    html.Div(id='tabs-content-example')
])

@app.callback(Output('tabs-content-example', 'children'),
              [Input('tabs-example', 'value')])

def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
       html.H2(children='Property Values vs. Broadband Speeds in the State of Washington'),

       html.Div(children='''
           - Median "property values" grouped by zip code
       '''),
            
       html.Div(children='''
            - Only includes places that have access to fiber optic infrastructure
       '''),
            

        dcc.Graph(
           id='scatter_chart',
           figure = {
        'data' : [
        go.Scatter(
            x = broadband_speed_1,
            y = property_values_1,
            text=city_1,
            mode = 'markers',
            hoverinfo='text'
                )
            ],
               'layout' : go.Layout(
                   title = "Scatterplot of All Cities in Washington including the Broadband Speeds for all types of infrastruture and Property Values",
                   xaxis = {'title' : "Broadband Speeds"},
                   yaxis = {'title' : "Property values (Median House Price)"},
                   hovermode = 'closest'

                   )
               }
            )
        ]),

    
    if tab == 'tab-2':
        return html.Div([
       html.H2(children='Table of Cities in Washington with the following characteristics'),

       html.Div(children='''
           - Fast Fiber optic broadband infrastructure
           '''
               ),
       html.Div(children='''
           - Contain zip codes where median property values are among Lowest 20% zip codes in the State of Washington
           '''
               ),
        dash_table.DataTable(
           style_data={'whiteSpace': 'normal'},
           css=[{'selector': '.dash-cell div.dash-cell-value', 'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'}],
            id='table',
            data=df_tab2.to_dict('rows'),
            columns=[{"name": i, "id": i} for i in df_tab2.columns],
            content_style='grow',
#             style_as_list_view=True,
            selected_rows=[],
#             n_fixed_columns=True,
            is_focused=True,
            pagination_mode=True,
            pagination_settings = {'page_size': 30,
                                  'current_page': 0},
#             row_deletable = True,
            sorting = 'fe'
        )],)


    if tab == 'tab-3':
        return html.Div([
       html.H1(children='Map of Washington - Cities where:'),

       html.Div(children='''
           - Very fast and reliable fiber optic broadband infrastructure is available
           '''
               ),
       html.Div(children='''
           - Median Property Values are among lowest 20% in State of Washington
           '''
               ),

        dcc.Graph(
           id='scatter_chart',
           figure = {
        'data' : [
        go.Scattermapbox(
        lat=latitude_3,
        lon=longitude_3,
        mode='markers',
        text=city_3,
        hoverinfo='text',
        marker=go.scattermapbox.Marker(
            size=12
        ),
                )
            ],
               'layout' : go.Layout(  
            autosize=False,
            hovermode='closest',
            mapbox=go.layout.Mapbox(
                accesstoken=mapbox_access_token,
                bearing=0,
                pitch=0,
                zoom=6.3,
                center=go.layout.mapbox.Center(
                    lat=47,
                    lon=-120
                   ),
        ),
                width=1200,
                height=900
               ),
           }
        )
        ])
           
    
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port='5000')

