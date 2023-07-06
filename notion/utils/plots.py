import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plot_bar_chart_per_service(df_filtered):
    grouped_budget = df_filtered.groupby(["Service"])["NetBudget"].sum().reset_index()
    grouped_margin = df_filtered.groupby(["Service"])["NetMargin"].mean().reset_index()
    grouped_margin["NetMargin"] = grouped_margin["NetMargin"] * 100

    fig_bar = make_subplots(specs=[[{"secondary_y": True}]])

    for service in grouped_budget["Service"]:
        fig_bar.add_trace(
            go.Bar(
                x=[service],
                y=grouped_budget[grouped_budget["Service"] == service]["NetBudget"],
                name=service,
            )
        )

    fig_bar.add_trace(
        go.Scatter(
            x=grouped_margin["Service"],
            y=grouped_margin["NetMargin"],
            name="Avg NetMargin",
            line=dict(color="black"),
        ),
        secondary_y=True,
    )

    fig_bar.update_yaxes(
        title_text="Netto Budget", secondary_y=False, tickprefix="CHF ", tickformat=","
    )
    fig_bar.update_yaxes(title_text="Netto Marge (%)", secondary_y=True)

    fig_bar.update_layout(
        title="Netto Budget und durchschnittliche Netto Marge pro Service"
    )

    return fig_bar


def plot_pie_chart_per_service(df_filtered):
    service_counts = df_filtered["Service"].value_counts().reset_index()
    service_counts.columns = ["Service", "Count"]
    pie_chart = go.Figure(
        data=[go.Pie(labels=service_counts["Service"], values=service_counts["Count"])]
    )
    pie_chart.update_traces(textinfo="value")
    pie_chart.update_layout(title="Anzahl Aufträge pro Service")
    return pie_chart


def plot_stacked_bar_chart_per_canton(df_filtered):
    cantons = df_filtered["Canton"].unique()
    services = df_filtered["Service"].unique()

    data = []
    for service in services:
        service_data = df_filtered[df_filtered["Service"] == service][
            "Canton"
        ].value_counts()
        service_data = service_data.reindex(cantons).fillna(0)
        data.append(go.Bar(name=service, x=cantons, y=service_data))

    fig = go.Figure(data=data)
    fig.update_layout(barmode="stack", title="Anzahl Aufträge pro Kanton und Service")

    return fig


def plot_pie_chart_track(df_track):
    average_hours = df_track.groupby("Name")["Hours"].mean().round(2).reset_index()
    average_hours.columns = ["Name", "Average_Hours"]

    pie_chart = go.Figure(
        data=[
            go.Pie(labels=average_hours["Name"], values=average_hours["Average_Hours"])
        ]
    )
    pie_chart.update_traces(textinfo="value")
    pie_chart.update_layout(title="Durchschnittlicher Stundenaufwand pro Bereich")
    return pie_chart


def plot_priority_table(df):
    df_filtered = df[
        (~df["Priority"].isna())
        & (df["Done"] == False)
        & (df["💸 RE(n) versendet"] == False)
        & (df["📨 Fakturieren"] == False)
    ]

    table = go.Figure(
        data=[
            go.Table(
                header=dict(
                    values=["Name", "Priority", "Progress"],
                    fill_color="paleturquoise",
                    align="left",
                ),
                cells=dict(
                    values=[
                        df_filtered["Name"],
                        df_filtered["Priority"],
                        (df_filtered["Progress"] * 100).map("{:.0f}%".format),
                    ],
                    fill_color="lavender",
                    align="left",
                ),
            )
        ]
    )
    table.update_layout(title="Überfällige Projekte")
    return table


# def plot_bar_chart_services_per_month(df_filtered): #todo: plot is not really accurate
#     grouped_budget = df_filtered.groupby(['Month', 'Service'])['NetBudget'].sum().reset_index()
#     grouped_margin = df_filtered.groupby(['Month'])['NetMargin'].mean().reset_index()
#     grouped_margin['NetMargin'] = grouped_margin['NetMargin'] * 100
#     months = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober',
#               'November', 'Dezember']
#     bar_chart = make_subplots(specs=[[{"secondary_y": True}]])
#
#     for service in grouped_budget['Service'].unique():
#         bar_chart.add_trace(go.Bar(x=grouped_budget[grouped_budget['Service'] == service]['Month'],
#                                    y=grouped_budget[grouped_budget['Service'] == service]['NetBudget'],
#                                    name=service))
#
#     bar_chart.add_trace(go.Scatter(x=grouped_margin['Month'],
#                                    y=grouped_margin['NetMargin'],
#                                    name='Durchschnittliche Netto Marge (%)',
#                                    line=dict(color='black')),
#                         secondary_y=True)
#
#     bar_chart.update_yaxes(title_text="Netto Budget", secondary_y=False, tickprefix="CHF ", tickformat=',')
#     bar_chart.update_yaxes(title_text="Netto Marge (%)", secondary_y=True)
#     bar_chart.update_xaxes(ticktext=months, tickvals=list(range(1, 13)))
#
#     bar_chart.update_layout(
#         title="Netto Budget und durchschnittliche Netto Marge pro Monat und Service",
#         xaxis_title="Monat",
#         barmode='stack'
#     )
#     return bar_chart
