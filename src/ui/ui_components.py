from dash import dash_table

def table(id, data):
    return dash_table.DataTable(
        id=f'table{id}',
        columns=[{"name": i, "id": i, "deletable": True, "selectable": True, "hideable": True} for i in data.columns],
        data=data.to_dict('records'),
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
            'fontWeight': 'bold'
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
            'textAlign': 'left',
            'whiteSpace': 'normal',
            'height': 'auto',
            'backgroundColor': 'white',
            'color': 'black',
        }
    )
