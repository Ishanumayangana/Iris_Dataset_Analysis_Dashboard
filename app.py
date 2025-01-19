from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from layout import app_layout
from callbacks import register_callbacks

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions = True

# Set the layout of the app
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', children=app_layout)
])

# Register the callbacks
register_callbacks(app)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
