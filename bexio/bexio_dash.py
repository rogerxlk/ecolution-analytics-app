import dash
from utils.preprocess_data import load_data_bexio
from utils.callbacks import register_bexio_callbacks
from bexio.utils.layout import layout_bexio

app = dash.Dash(__name__)

df = load_data_bexio()
app.layout = layout_bexio()
register_bexio_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)
