from dash import dcc, html


def layout_notion(df):
    return html.Div(
        style={"padding": "50px"},
        children=[
            html.H1("Notion Db Energieberatung", style={"textAlign": "center"}),
            html.Div(
                style={"display": "flex", "justifyContent": "center", "gap": "20px"},
                children=[
                    dcc.Dropdown(
                        id="year-filter",
                        options=[
                            {"label": str(int(year)), "value": int(year)}
                            for year in df["Year"].unique()
                        ],
                        value=df["Year"].max(),
                        clearable=False,
                        style={"width": "100%"},
                    ),
                    dcc.Dropdown(
                        id="done-filter",
                        options=[
                            {"label": "Done", "value": "Done"},
                            {"label": "Undone", "value": "Undone"},
                            {"label": "All", "value": "All"},
                        ],
                        value="Done",
                        clearable=False,
                        style={"width": "100%"},
                    ),
                ],
            ),
            html.Div(
                style={"padding": "50px"},
                children=[
                    html.Div(id="priority-table-div"),
                    dcc.Graph(id="stacked_bar_chart_per_canton"),
                    dcc.Graph(id="pie_chart_per_service"),
                    dcc.Graph(id="bar_chart_per_service"),
                    dcc.Graph(id="pie-chart-track"),
                ],
            ),
            html.Div(id="priority-table-data", style={"display": "none"}),
        ],
    )
