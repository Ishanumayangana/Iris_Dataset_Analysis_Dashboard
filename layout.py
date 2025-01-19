from dash import dcc, html
import dash_bootstrap_components as dbc

app_layout = html.Div(style={
    'backgroundColor': '#f0f4f8',
    'fontFamily': 'Arial, sans-serif',
    'padding': '20px',
    'color': '#333'}, children=[

    # Title
    html.H1("Iris Dataset Analysis", style={
        'text-align': 'center',
        'color': '#333',
        'fontSize': '36px',
        'marginBottom': '40px',
        'fontFamily': 'Roboto, sans-serif'
    }),

    # Main container with two divs: Left (filters) and Right (dashboard button)
    html.Div(style={'display': 'flex', 'justifyContent': 'space-between'}, children=[

        # Filters Section (Vertically aligned, Left)
        html.Div(style={
            'display': 'flex',
            'flexDirection': 'column',
            'alignItems': 'flex-start',
            'padding': '10px'}, children=[

            # Checklist for Species Filter (Multiple selections)
            dcc.Checklist(
                id='species-checklist',
                options=[{'label': species, 'value': species} for species in ['setosa', 'versicolor', 'virginica']],
                value=['setosa'],  # Default value
                inline=True,  # Display in-line checkboxes (bullet points)
                style={'width': '100%'}
            ),

            # Download button for the full dataset
            html.Div(style={'padding': '10px'}, children=[
                html.Button("Download Full Dashboard", id="download-button", n_clicks=0, style={
                    'backgroundColor': '#1f77b4', 'color': 'white', 'border': 'none', 'padding': '10px 20px',
                    'fontSize': '16px', 'cursor': 'pointer'
                }),
                dcc.Download(id="download-dashboard")
            ]),
        ]),

        # Empty space in the middle
        html.Div(style={'flex': 1}),

        # Empty space to push the button to the top right corner
        html.Div(style={'display': 'flex', 'justifyContent': 'flex-end', 'padding': '10px'}, children=[]),
    ]),

    # Grid layout for the plots
    html.Div(id='plots-container', style={
        'display': 'grid',
        'gridTemplateColumns': 'repeat(2, 1fr)',
        'gap': '20px'})
])
