# Iris Dataset Dashboard

This is an interactive dashboard built using Dash, Plotly, and Python, designed to visualize the famous Iris dataset. The dashboard displays multiple plots and allows users to filter the data by species and download reports. It is developed to provide insights into the distribution of various Iris flower attributes such as petal length, sepal length, and more.

## Features

- **Multiple Visualizations**: Includes histograms, boxplots, scatter plots, heatmaps, and 3D scatter plots to visualize the Iris dataset.
- **Data Filtering**: Allows users to filter the data by species.
- **Download Reports**: Users can download reports of each plot as an Excel file.
- **Responsive Layout**: Designed with Dash Bootstrap components to ensure the app is responsive and easy to use.

## App Overview

The app consists of the following main components:

1. **Filters Section**: A checklist to filter the Iris data by species (Setosa, Versicolor, Virginica).
2. **Plots Section**: Displays various visualizations (Histogram, Boxplot, Scatter Plot, Heatmap, 3D Scatter, Violin Plot) based on the selected species.
3. **Download Section**: Users can download the full dataset or reports for each individual plot.

## Prerequisites

Before running this app, ensure you have the following installed:

- Python 3.x
- Dash
- Plotly
- Pandas
- Scikit-learn
- Dash Bootstrap Components

You can install the necessary packages using pip:

```bash
pip install dash plotly pandas scikit-learn dash-bootstrap-components
