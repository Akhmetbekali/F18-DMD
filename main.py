import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import psycopg2
import os

db_host = 'gleb.page'
db_password = 'ThisPostgresIsAwesome'


class Data:
    # Connect to DB
    conn = psycopg2.connect(f"dbname=postgres user=postgres host={db_host} port=5432 password={db_password}")
    cur = conn.cursor()

    # Dictionary with proper column names for different queries
    @staticmethod
    def get_column_names(number):
        return {
            1: ['Car ID'],
            2: ['Hour from', 'Hour to', 'Sockets occupied'],
            3: ['Morning', 'Afternoon', 'Evening'],
            4: ['Payment dates'],
            5: ['Average distance', 'Average trip duration'],
            6: ['Morning', 'Afternoon', 'Evening'],
            7: ['Car ID', 'Orders in last 3 months'],
            8: ['Customer ID', 'Total chargings'],
            9: ['Part name', 'Workshop ID', 'Parts needed'],
            10: ['Car ID', 'Average cost']
        }[number]

    # Perform query to DB and convert it to pandas dataframe
    @staticmethod
    def perform_query(number):
        if number == 6:
            return Data.q6()

        sql_file = open(f"queries/q{number}.sql", "r")
        Data.cur.execute(sql_file.read())
        return pd.DataFrame(Data.cur.fetchall(), columns=Data.get_column_names(number))

    # Query six has pretty shitty data format to process it with pandas
    @staticmethod
    def q6():
        sql_file_morning = open("queries/q6_m.sql", "r")
        sql_file_afternoon = open("queries/q6_a.sql", "r")
        sql_file_evening = open("queries/q6_e.sql", "r")
        result = []
        Data.cur.execute(sql_file_morning.read())
        result.append(Data.cur.fetchall())
        Data.cur.execute(sql_file_afternoon.read())
        result.append(Data.cur.fetchall())
        Data.cur.execute(sql_file_evening.read())
        result.append(Data.cur.fetchall())
        df = pd.DataFrame(result).T
        df.columns = Data.get_column_names(6)
        return df


# Define Dash application
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Define Dash application layout
app.layout = html.Div([
    html.H1('F18 DMD'),
    html.Br(),
    html.Div(children='Gleb Petrakov'),
    html.Div(children='Ali Akhmetbek'),
    html.Br(),
    html.Div(children='Choose query from dropdown menu to acquire results'),
    html.Br(),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': f'Query {i}', 'value': i} for i in range(1, 11)],
        value=1
    ),
    html.Br(),
    dash_table.DataTable(id='table',
                         columns=[{"name": i, "id": i} for i in Data.get_column_names(1)],
                         data=Data.perform_query(1).to_dict('rows'), )
])


# Callback for datatable column update
@app.callback(Output('table', 'columns'), [Input('dropdown', 'value')])
def update_columns(user_selection):
    return [{"name": i, "id": i} for i in Data.get_column_names(user_selection)]


# Callback for datatable data update
@app.callback(Output('table', 'data'), [Input('dropdown', 'value')])
def update_datatable(user_selection):
    return Data.perform_query(user_selection).to_dict('rows')


host = '127.0.0.1'
docker_host = os.environ.get('HOST_ADDRESS')
if docker_host is not None:
    host = docker_host

port = '8050'
docker_port = os.environ.get('HOST_PORT')
if docker_port is not None:
    port = docker_port

if __name__ == '__main__':
    app.run_server(debug=False, host=host, port=port)
