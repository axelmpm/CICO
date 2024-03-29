from dash import dash_table
from dash import html

from src.data.data import Data

def table(id, data):
    return dash_table.DataTable(
        id=id,
        columns=[{"name": c, "id": c,
                  "deletable": True, "selectable": True,
                  "hideable": True} for c in data.columns],
        data=Data.to_tabular(data),
        editable=True,
        filter_action="native",
        sort_action="native",
        sort_mode="single",
        column_selectable="multi",
        row_selectable="multi",
        row_deletable=True,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current=0,
        page_size=6,
        style_header={
            'backgroundColor': 'rgb(210, 210, 210)',
            'color': 'black',
            'fontWeight': 'bold',
            'textAlign': 'center',
        },
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(220, 220, 220)',
            }
        ],
        style_cell={
            'minWidth': 95, 'maxWidth': 95, 'width': 95
        },
        style_data={
            'textAlign': 'center',
            'whiteSpace': 'normal',
            'height': 'auto',
            'backgroundColor': 'white',
            'color': 'black',
        }
    )

def suggestions(id, data):
    return html.Datalist(id=id, children=[html.Option(value=word) for word in data.get_all_food_names()])
