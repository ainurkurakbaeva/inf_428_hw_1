import pandas as pd
from elasticsearch import Elasticsearch, helpers
import json

# Set up the Elasticsearch client
es = Elasticsearch("http://localhost:9200")  # Replace with your ES host if different

# Load the CSV file using pandas
def load_csv_to_dataframe(csv_file):
    df = pd.read_csv(csv_file)
    return df

# Function to prepare data for bulk indexing into Elasticsearch
def generate_bulk_data(df, index_name):
    actions = []
    for _, row in df.iterrows():
        doc = row.to_dict()  # Convert row to dictionary
        action = {
            "_op_type": "index",  # Operation type, could also be "create", "update", or "delete"
            "_index": index_name,  # Elasticsearch index
            "_id": row['user_id'],  # ID field (you can customize it)
            "_source": doc  # The document data
        }
        actions.append(action)
    return actions

# Function to index the data into Elasticsearch
def index_data_to_elasticsearch(csv_file, index_name):
    # Load data from CSV
    df = load_csv_to_dataframe(csv_file)

    # Prepare the bulk actions
    bulk_actions = generate_bulk_data(df, index_name)

    # Bulk index the data
    try:
        helpers.bulk(es, bulk_actions)
        print(f"Successfully indexed data into '{index_name}'")
    except Exception as e:
        print(f"Error indexing data: {e}")

# Example usage
csv_file = "C:/Users/User/AinurKurakbaeva/DataAnalytics/inf_428_hw_1/task_2/test_case_data/high_score_departments.csv"
index_name = "threat_scores"  # Name of the Elasticsearch index where data will be stored

# Call function to index data into Elasticsearch
index_data_to_elasticsearch(csv_file, index_name)
