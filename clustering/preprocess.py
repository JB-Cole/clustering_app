import pandas as pd
import logging
import os
import io

# Set up logging
logging.basicConfig(
    filename='logs/preprocess.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def load_data(file):
    try:
        if file is None:
            logging.error("No file provided")
            raise ValueError("No file provided")

        # Read the uploaded CSV file
        df = pd.read_csv(io.BytesIO(file.read()))
        logging.info(f"Loaded data from uploaded file with shape {df.shape}")

        # Validate expected columns
        required_cols = ['Annual_Income', 'Spending_Score']
        for col in required_cols:
            if col not in df.columns:
                logging.error(f"Missing required column: {col}")
                raise ValueError(f"Missing required column: {col}")

        features = ['Annual_Income', 'Spending_Score']
        return df, features

    except Exception as e:
        logging.exception("Error loading and validating data")
        raise e