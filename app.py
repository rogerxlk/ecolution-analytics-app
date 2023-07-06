import os
import secrets
from flask import Flask, redirect, request, url_for, send_from_directory
from dash import Dash, Output, Input, html, dcc, State
from urllib.parse import quote
from config import config
import dash_bootstrap_components as dbc
from components.navigation_bar import create_navigation_bar
from notion.utils.preprocess_data import load_data_notion
from notion.utils.callbacks import register_notion_callbacks
from bexio.utils.callbacks import register_bexio_callbacks
from bexio.utils.layout import layout_bexio
from notion.utils.layout import layout_notion

app = Flask(__name__, static_url_path="/static", static_folder="static")
app.config.from_object(config)
app.secret_key = secrets.token_hex(16)


@app.route("/")
def index():
    user_principal_name = request.headers.get("X-MS-CLIENT-PRINCIPAL-NAME", "")

    print("Debug status: ", app.config["DEBUG"])

    if app.config["DEBUG"]:
        user_principal_name = "info@ecolution.swiss"

    if not user_principal_name.endswith("@ecolution.swiss") and not app.config["DEBUG"]:
        return "Access denied: not a company email"
    return redirect("/dashboard/notion")


@app.route("/logout")
def logout():
    if app.config["DEBUG"]:
        return redirect(url_for("index"))
    else:
        post_logout_redirect_uri = quote(request.url_root)
        return redirect(
            f"https://login.microsoftonline.com/common/oauth2/logout?post_logout_redirect_uri={post_logout_redirect_uri}"
        )


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


@app.errorhandler(500)
def internal_error(error):
    return "500 error caught. " + str(error), 500


def add_dash(server):
    external_stylesheets = [
        dbc.themes.BOOTSTRAP,
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css",
    ]

    dash_app = Dash(
        server=server,
        external_stylesheets=external_stylesheets,
        routes_pathname_prefix="/dashboard/",
    )
    dash_app.title = "Ecolution Analytics"

    # register callbacks
    register_notion_callbacks(dash_app)
    register_bexio_callbacks(dash_app)

    @dash_app.callback(
        Output("navbar-collapse", "is_open"),
        [Input("navbar-toggler", "n_clicks")],
        [State("navbar-collapse", "is_open")],
    )
    def toggle_navbar_collapse(n, is_open):
        if n:
            return not is_open
        return is_open

    @dash_app.callback(
        Output("redirect", "pathname"), [Input("logout-button", "n_clicks")]
    )
    def logout_dash(n):
        if n:
            return "/logout"

    @dash_app.callback(Output("page-content", "children"), [Input("url", "pathname")])
    def display_page(pathname):
        if pathname == "/dashboard/notion":
            df_notion, _, _, _ = load_data_notion()
            return layout_notion(df_notion)
        elif pathname == "/dashboard/bexio":
            # df_bexio = load_data_bexio()
            return layout_bexio()
        else:
            return "404 - Page not found"

    dash_app.layout = html.Div(
        [
            create_navigation_bar(),
            html.Div(style={"height": "20px"}),
            dcc.Location(id="url", refresh=False),
            dcc.Location(id="redirect"),
            html.Div(id="page-content"),
        ]
    )

    return dash_app


if __name__ == "__main__":
    dash_app = add_dash(app)
    dash_app.title = "Ecolution Analytics"
    app.run()
