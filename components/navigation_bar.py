import dash_bootstrap_components as dbc
from dash import html


def create_navigation_bar():
    return dbc.Navbar(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(
                            html.Img(src="/static/logo.png", height="30px"),
                            width=2,
                            className="my-auto",
                        ),
                    ],
                    className="align-items-center",
                    style={"marginLeft": "20px"},
                ),
            ),
            dbc.NavbarToggler(id="navbar-toggler", style={"marginRight": "20px"}),
            dbc.Collapse(
                dbc.Nav(
                    [
                        dbc.NavItem(dbc.NavLink("Notion", href="/dashboard/notion")),
                        dbc.NavItem(dbc.NavLink("Bexio", href="/dashboard/bexio")),
                        dbc.NavItem(
                            dbc.Button(
                                html.I(className="fas fa-sign-out-alt"),
                                href="/logout",
                                color="secondary",
                                className="ml-auto",
                            )
                        ),
                    ],
                    className="ml-auto",
                    navbar=True,
                    style={
                        "paddingRight": "20px",
                        "paddingLeft": "20px",
                        "flexWrap": "wrap",
                        "justifyContent": "flex-end",
                        "alignItems": "center",
                    },  # Add styles for layout
                ),
                id="navbar-collapse",
                navbar=True,
                is_open=False,
            ),
        ],
        color="dark",
        dark=True,
    )
