import sys
sys.path.append(r'C:\Users\axelpm\Desktop\cico')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\data')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\parser')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\reader')

import pandas as pd
pd.options.mode.chained_assignment = None

import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State

from src.data.data_constants import FOOD_NAME
from src.data.data import Regs, Foods, RegsFoods, Data
from src.data.data_utils import contains, merge
from ui_components import table, suggestions
from figs import fig_all_weeks, fig_all_days

regs = Regs.load()
foods = Foods.load()
regs_food_merge = RegsFoods(regs, foods)

app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div([
    suggestions('foods-suggested-inputs', foods),
    dcc.Input(id='food-name-read-input', type='text', list='foods-suggested-inputs', value=''),
    html.Button(id='foods-search-button', n_clicks=0, children='Search'),
    table('foods-table', Foods.to_visualizable(foods)),
    table('regs-table', RegsFoods.to_visualizable(regs_food_merge)),
    dcc.Graph(id='days-figs', figure=fig_all_days(regs_food_merge)),
    dcc.Graph(id='weeks-fig', figure=fig_all_weeks(regs_food_merge)),
    dcc.Store(id='regs-db-cache', data=Data.to_cacheable(regs)),
    dcc.Store(id='foods-db-cache', data=Data.to_cacheable(foods))
])

@app.callback(Output('foods-table', 'data'),
              Input('foods-search-button', 'n_clicks'),
              State('foods-db-cache', 'data'),
              State('food-name-read-input', 'value'),)
def app_read_food(n_clicks, foods_cacheable, food_name):
    return Data.to_tabular(Foods.to_visualizable(Data.query_from(Foods.from_cacheable_to_data(foods_cacheable), {FOOD_NAME: (contains, [food_name])})))

if __name__ == '__main__':
    app.run_server(debug=True)
    # app.run_server(debug=False, port=8080, host='0.0.0.0')
