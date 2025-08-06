import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from clustering.preprocess import load_data
from clustering.model import train_kmeans, plot_clusters

import logging

# Set up logging
logging.basicConfig(
    filename='logs/model.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

st.title("Customer Segmentation using K-Means")

# File uploader for CSV
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Load and display data
    df, features = load_data(uploaded_file)
    st.subheader("Data Preview")
    st.dataframe(df)

    # Select number of clusters
    k = st.slider("Select number of clusters (K), Count starts from 0 - 9", min_value=2, max_value=10, value=5)

    # Train model
    model, clustered_df = train_kmeans(df, features, k)

    # Show clustered data
    st.subheader("Clustered Data")
    st.dataframe(clustered_df)

    # Plot clusters
    st.subheader("Cluster Visualization")
    fig = plot_clusters(clustered_df, model)
    st.pyplot(fig)
