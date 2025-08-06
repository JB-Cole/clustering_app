# Customer Segmentation using K-Means

This project is a Streamlit web application that performs customer segmentation using the K-Means clustering algorithm. It allows users to upload a CSV file containing customer data and visualizes the clusters based on selected features.

## Features
- Upload a CSV file with customer data.
- Preview the uploaded data.
- Select the number of clusters (K) for K-Means clustering.
- Display the clustered data.
- Visualize the clusters using a scatter plot.

## Requirements
The project requires the following Python packages:
- `pandas>=1.5.3`
- `scikit-learn>=1.2.2`
- `streamlit>=1.34.0`
- `matplotlib>=3.7.1`

Install the dependencies using the provided `requirements.txt` file:
```bash
pip install -r requirements.txt
```

## Project Structure
- `app/`: Contains the main application files.
- `clusenv/`: Virtual environment directory (if created).
- `clustering/`: Directory for preprocessing and model logic.
  - `preprocess.py`: Handles data loading and validation.
  - `model.py`: Contains the K-Means training and plotting functions.
- `data/`: Directory for sample data files (e.g., `mall_customers.csv`).
- `logs/`: Directory for log files generated during preprocessing.
- `requirements.txt`: Lists project dependencies.

## Setup
1. **Clone the Repository**:
   Create a local copy of the project (if applicable).
   
2. **Create a Virtual Environment**:
   ```bash
   python -m venv clusenv
   ```

3. **Activate the Environment**:
   - On Windows: `clusenv\Scripts\activate`
   - On macOS/Linux: `source clusenv/bin/activate`

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**:
   Navigate to the `app` directory and run:
   ```bash
   streamlit run clustering_app.py
   ```

## Usage
1. Open the app in your browser (default URL: `http://localhost:8501`).
2. Upload a CSV file containing at least the columns `Annual_Income` and `Spending_Score`.
3. Adjust the number of clusters using the slider.
4. View the data preview, clustered results, and cluster visualization.

## Logging
Logs are saved to `logs/preprocess.log` with timestamps, including any errors encountered during data loading.

## Contributing
Feel free to fork the repository and submit pull requests for improvements or bug fixes.

## License
[Add license information here if applicable, e.g., MIT License]