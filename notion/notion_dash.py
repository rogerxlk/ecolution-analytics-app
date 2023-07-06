import dash
from utils.preprocess_data import load_data_notion
from utils.callbacks import register_notion_callbacks
from notion.utils.layout import layout_notion

app = dash.Dash(__name__)

df, _, _, _ = load_data_notion()
app.layout = layout_notion(df)
register_notion_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True, port=8051)
