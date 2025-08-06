from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import logging
import numpy as np

# Set up logging
logging.basicConfig(
    filename='logs/model.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def train_kmeans(df, features, k):
    try:
        if df.empty:
            logging.error("Input dataframe is empty.")
            raise ValueError("Input dataframe is empty.")
        
        if not all(feature in df.columns for feature in features):
            missing = [f for f in features if f not in df.columns]
            logging.error(f"Missing features: {missing}")
            raise ValueError(f"Missing features in data: {missing}")
        
        df = df.copy()
        model = KMeans(n_clusters=k, random_state=42)
        df['Cluster'] = model.fit_predict(df[features])
        
        logging.info(f"KMeans model trained with k={k} and features={features}")
        return model, df

    except Exception as e:
        logging.exception("Error in train_kmeans")
        raise e

def plot_clusters(df, model):
    try:
        if 'Cluster' not in df.columns:
            logging.error("Dataframe does not contain 'Cluster' column.")
            raise ValueError("Dataframe does not contain 'Cluster' column.")

        fig, ax = plt.subplots()
        scatter = ax.scatter(df['Annual_Income'], df['Spending_Score'], c=df['Cluster'], cmap='viridis')
        ax.scatter(*model.cluster_centers_.T, s=200, c='red', label='Centroids')
        ax.set_xlabel("Annual Income")
        ax.set_ylabel("Spending Score")
        ax.set_title("Customer Segments")
        ax.legend()

        logging.info("Cluster plot created successfully.")
        return fig

    except Exception as e:
        logging.exception("Error in plot_clusters")
        raise e