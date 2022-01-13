import sys
sys.path.append(r'C:\Users\axelpm\Desktop\cico')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\pipeline')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\processor')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\parser')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\database')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\reader')

import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State

from src.processor.processor_lib import set_correct_foods_db_types, read_from_json, data_into_json, data_into_records, wrap_null_values
from src.database.database_lib import query_from, contained_in
from src.pipeline.pipelines import load_regs_db, load_foods_db
from ui_components import table, suggestions
from src.parser.parser_fields import FOOD_NAME

regs = load_regs_db()
foods = load_foods_db()

app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div([
    table('regs-table', regs),
    table('foods-table', foods),
    suggestions('foods-suggested-inputs', foods),
    dcc.Input(id='food-name-read-input', type='text', list='foods-suggested-inputs', value=''),
    html.Button(id='foods-search-button', n_clicks=0, children='Search'),
    dcc.Store(id='regs-db-cache', data=data_into_json(regs)),
    dcc.Store(id='foods-db-cache', data=data_into_json(foods))
])

@app.callback(Output('foods-table', 'data'),
              Input('foods-search-button', 'n_clicks'),
              State('foods-db-cache', 'data'),
              State('food-name-read-input', 'value'),)
def app_read_food(n_clicks, foods_db, food_name):
    foods_db = read_from_json(foods_db, set_correct_foods_db_types)
    return data_into_records(query_from(foods_db, {FOOD_NAME: (contained_in, [food_name])}))

if __name__ == '__main__':
    app.run_server(debug=True)
    # app.run_server(debug=False, port=8080, host='0.0.0.0')
