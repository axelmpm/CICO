import sys
sys.path.append(r'C:\Users\axelpm\Desktop\cico')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\pipeline')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\processor')

import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

from src.processor.processor_lib import into_readable
from src.pipeline.pipelines import load_data
from src.paths import PROCESSED_DATA, HISTORIC_DATA
from ui_components import table

data = load_data(PROCESSED_DATA, HISTORIC_DATA)
readable_data = into_readable(data)
# readable_data = data

app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div([
    table(1, readable_data),
    table(2, readable_data),
    dcc.Store(id='data-stored', data=data.to_json(orient='split')),
])

if __name__ == '__main__':
    app.run_server(debug=True)
    # app.run_server(debug=False, port=8080, host='0.0.0.0')
