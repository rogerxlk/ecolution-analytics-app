import plotly
from dash import dcc
from dash.dependencies import Input, Output
from notion.utils.plots import *
from notion.utils.preprocess_data import load_data_notion
import json


def register_notion_callbacks(app):
    @app.callback(
        Output("priority-table-data", "children"),
        [Input("year-filter", "value"), Input("done-filter", "value")],
    )
    def update_priority_table_data(year_filter, done_filter):
        df, df_track, df_Done, df_Undone = load_data_notion()
        if done_filter == "Done":
            df_filtered = df_Done
        elif done_filter == "Undone":
            df_filtered = df_Undone
        else:
            df_filtered = df

        df_filtered = df_filtered[df_filtered["Year"] == year_filter]
        priority_table = plot_priority_table(df_filtered)

        # dcc.Store only accepts JSON-like data, so we need to convert the figure into JSON
        return json.dumps(priority_table, cls=plotly.utils.PlotlyJSONEncoder)

    @app.callback(
        Output("priority-table-div", "children"),
        [Input("done-filter", "value"), Input("priority-table-data", "children")],
    )
    def display_priority_table(done_filter, priority_table_data):
        if done_filter == "Undone":
            # Convert the figure back from JSON to a Python dict
            priority_table = json.loads(priority_table_data)
            return dcc.Graph(id="priority-table", figure=priority_table)
        else:
            return []  # return an empty list (i.e., no children)

    @app.callback(
        Output("pie_chart_per_service", "figure"),
        Output("bar_chart_per_service", "figure"),
        Output("stacked_bar_chart_per_canton", "figure"),
        Output("pie-chart-track", "figure"),
        [Input("year-filter", "value"), Input("done-filter", "value")],
    )
    def update_other_charts(year_filter, done_filter):
        df, df_track, df_Done, df_Undone = load_data_notion()
        if done_filter == "Done":
            df_filtered = df_Done
        elif done_filter == "Undone":
            df_filtered = df_Undone
        else:
            df_filtered = df

        df_filtered = df_filtered[df_filtered["Year"] == year_filter]
        pie_chart_per_service = plot_pie_chart_per_service(df_filtered)
        bar_chart_per_service = plot_bar_chart_per_service(df_filtered)
        stacked_bar_chart_per_canton = plot_stacked_bar_chart_per_canton(df_filtered)
        pie_chart_track = plot_pie_chart_track(df_track)
        return (
            pie_chart_per_service,
            bar_chart_per_service,
            stacked_bar_chart_per_canton,
            pie_chart_track,
        )
