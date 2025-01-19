from dash.dependencies import Input, Output
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from data_processing import iris_df, filter_data
from layout import app_layout

def register_callbacks(app):
    @app.callback(
        Output('plots-container', 'children'),
        [Input('species-checklist', 'value')]
    )
    def update_plots(selected_species):
        filtered_df = filter_data(selected_species)

        children = []

        # Histogram
        fig1 = px.histogram(filtered_df, x='petal length (cm)', title='Histogram of Petal Length', color='species')
        children.append(html.Div(style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}, children=[
            dcc.Graph(id='histogram', figure=fig1, style={'width': '95%', 'height': '350px'}),
            html.Button("Download Report", id="download-histogram-report", n_clicks=0),
            dcc.Download(id="download-histogram")
        ]))

        # Boxplot
        fig2 = px.box(filtered_df, x='species', y='sepal length (cm)', title='Boxplot of Sepal Length by Species', color='species')
        children.append(html.Div(style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}, children=[
            dcc.Graph(id='boxplot', figure=fig2, style={'width': '95%', 'height': '350px'}),
            html.Button("Download Report", id="download-boxplot-report", n_clicks=0),
            dcc.Download(id="download-boxplot")
        ]))

        # Scatter Plot
        fig3 = px.scatter(filtered_df, x='petal length (cm)', y='petal width (cm)', color='species', title='Petal Length vs Petal Width')
        children.append(html.Div(style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}, children=[
            dcc.Graph(id='scatter-plot', figure=fig3, style={'width': '95%', 'height': '350px'}),
            html.Button("Download Report", id="download-scatter-report", n_clicks=0),
            dcc.Download(id="download-scatter")
        ]))

        # Heatmap for each species (Setosa, Versicolor, Virginica)
        fig4 = px.imshow(
            filtered_df[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']].groupby(filtered_df['species']).mean().transpose(),
            title="Heatmap of Features by Species",
            labels={'x': 'Species', 'y': 'Feature'},
            color_continuous_scale='YlGnBu'
        )
        children.append(html.Div(style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}, children=[
            dcc.Graph(id='heatmap', figure=fig4, style={'width': '95%', 'height': '350px'}),
            html.Button("Download Report", id="download-heatmap-report", n_clicks=0),
            dcc.Download(id="download-heatmap")
        ]))

        # 3D Scatter Plot
        fig5 = px.scatter_3d(filtered_df, x='petal length (cm)', y='petal width (cm)', z='sepal length (cm)', color='species', title='3D Scatter Plot of Iris Dataset')
        children.append(html.Div(style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}, children=[
            dcc.Graph(id='3d-scatter-plot', figure=fig5, style={'width': '95%', 'height': '350px'}),
            html.Button("Download Report", id="download-3d-scatter-report", n_clicks=0),
            dcc.Download(id="download-3d-scatter")
        ]))

        # Violin Plot (New unique plot)
        fig6 = px.violin(filtered_df, y="sepal length (cm)", x="species", box=True, points="all", title="Violin Plot of Sepal Length by Species")
        children.append(html.Div(style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}, children=[
            dcc.Graph(id='violin-plot', figure=fig6, style={'width': '95%', 'height': '350px'}),
            html.Button("Download Report", id="download-violin-report", n_clicks=0),
            dcc.Download(id="download-violin")
        ]))

        return children

    # Callback to download histogram data as an Excel file
    @app.callback(
        Output('download-histogram', 'data'),
        [Input('download-histogram-report', 'n_clicks')],
        prevent_initial_call=True
    )
    def download_histogram_report(n_clicks):
        return dcc.send_data_frame(iris_df.to_excel, "histogram_data.xlsx")

    # Callback to download boxplot data as an Excel file
    @app.callback(
        Output('download-boxplot', 'data'),
        [Input('download-boxplot-report', 'n_clicks')],
        prevent_initial_call=True
    )
    def download_boxplot_report(n_clicks):
        return dcc.send_data_frame(iris_df.to_excel, "boxplot_data.xlsx")

    # Callback to download scatter plot data as an Excel file
    @app.callback(
        Output('download-scatter', 'data'),
        [Input('download-scatter-report', 'n_clicks')],
        prevent_initial_call=True
    )
    def download_scatter_report(n_clicks):
        return dcc.send_data_frame(iris_df.to_excel, "scatter_data.xlsx")

    # Callback to download 3D scatter plot data as an Excel file
    @app.callback(
        Output('download-3d-scatter', 'data'),
        [Input('download-3d-scatter-report', 'n_clicks')],
        prevent_initial_call=True
    )
    def download_3d_scatter_report(n_clicks):
        return dcc.send_data_frame(iris_df.to_excel, "3d_scatter_data.xlsx")

    # Callback to download heatmap data as an Excel file
    @app.callback(
        Output('download-heatmap', 'data'),
        [Input('download-heatmap-report', 'n_clicks')],
        prevent_initial_call=True
    )
    def download_heatmap_report(n_clicks):
        heatmap_data = iris_df[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']].groupby(iris_df['species']).mean()
        return dcc.send_data_frame(heatmap_data.to_excel, "heatmap_data.xlsx")

    # Callback to download violin plot data as an Excel file
    @app.callback(
        Output('download-violin', 'data'),
        [Input('download-violin-report', 'n_clicks')],
        prevent_initial_call=True
    )
    def download_violin_report(n_clicks):
        violin_data = iris_df[['species', 'sepal length (cm)']]
        return dcc.send_data_frame(violin_data.to_excel, "violin_data.xlsx")

    # Callback to download the full dataset as an Excel file
    @app.callback(
        Output('download-dashboard', 'data'),
        [Input('download-button', 'n_clicks')],
        prevent_initial_call=True
    )
    def download_dashboard(n_clicks):
        return dcc.send_data_frame(iris_df.to_excel, "iris_dashboard.xlsx")
