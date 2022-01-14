import sys
sys.path.append(r'C:\Users\axelpm\Desktop\cico')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\data')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\parser')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\reader')

import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State

from src.data.data_constants import FOOD_NAME
from src.data.data import Regs, Foods, Data
from src.data.data_utils import contains
from ui_components import table, suggestions

regs = Regs.load()
foods = Foods.load()

app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div([
    table('regs-table', regs),
    table('foods-table', foods),
    suggestions('foods-suggested-inputs', foods),
    dcc.Input(id='food-name-read-input', type='text', list='foods-suggested-inputs', value=''),
    html.Button(id='foods-search-button', n_clicks=0, children='Search'),
    dcc.Store(id='regs-db-cache', data=Data.to_cacheable(regs.get())),
    dcc.Store(id='foods-db-cache', data=Data.to_cacheable(foods.get()))
])

@app.callback(Output('foods-table', 'data'),
              Input('foods-search-button', 'n_clicks'),
              State('foods-db-cache', 'data'),
              State('food-name-read-input', 'value'),)
def app_read_food(n_clicks, foods_cacheable, food_name):
    foods = Foods.from_cacheable_to_data(foods_cacheable)
    return Data.to_tabular(Data.query_from(foods, {FOOD_NAME: (contains, [food_name])}))

if __name__ == '__main__':
    app.run_server(debug=True)
    # app.run_server(debug=False, port=8080, host='0.0.0.0')
