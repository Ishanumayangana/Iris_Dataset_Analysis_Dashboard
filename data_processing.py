import pandas as pd
from sklearn import datasets

# Load Iris dataset
iris = datasets.load_iris()

# Create a DataFrame from the dataset
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target_names[iris.target]

def filter_data(selected_species):
    return iris_df[iris_df['species'].isin(selected_species)]
