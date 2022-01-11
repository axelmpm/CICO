import sys
sys.path.append(r'C:\Users\axelpm\Desktop\cico')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\pipeline')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\processor')

import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

from src.processor.processor_lib import into_readable, grouped_by_day
from src.pipeline.pipelines import load_data
from src.paths import PROCESSED_DATA, HISTORIC_DATA
from ui_components import table, suggestions

data = load_data(PROCESSED_DATA, HISTORIC_DATA)
readable = into_readable(data)

app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div([
    # table(1, readable),
    # table(2, grouped_by_day(readable)),
    # suggestions('list-suggested-inputs', readable),
    dcc.Input(
        id='input-1',
        type='text',
        # list='list-suggested-inputs',
        value='',
    ),
    dcc.Store(id='data-stored', data=data.to_json(orient='split')),
])

if __name__ == '__main__':
    app.run_server(debug=True)
    # app.run_server(debug=False, port=8080, host='0.0.0.0')
