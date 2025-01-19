import pandas as pd

def json_to_parquet(json_file_path, parquet_file_path):
    # Read the JSON file into a DataFrame
    df = pd.read_json(json_file_path)
    
    # Save the DataFrame as a Parquet file
    df.to_parquet(parquet_file_path, engine='pyarrow', index=False)
    print(f"Parquet file created at: {parquet_file_path}")

# Specify the file paths
json_file_path = 'emoji.json'        # Path to your JSON file
parquet_file_path = 'emoji.parquet'  # Path to save the Parquet file

# Convert JSON to Parquet
json_to_parquet(json_file_path, parquet_file_path)