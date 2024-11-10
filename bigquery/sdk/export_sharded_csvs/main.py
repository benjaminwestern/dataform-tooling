from google.cloud import bigquery
import csv
import argparse

def export_query_to_csv_sharded(project_id, query_file, destination_prefix, batch_size=15000):
    """Queries BigQuery and exports the results to sharded CSV files.

    Args:
        project_id: Your Google Cloud project ID.
        dataset_id: The BigQuery dataset ID.
        table_id: The BigQuery table ID.
        query_file: Path to the file containing the BigQuery SQL query.
        destination_prefix: The local path prefix for the sharded CSV files 
                           (e.g., "sales_export_").  Files will be named 
                           like "sales_export_00001.csv", "sales_export_00002.csv", etc.
        batch_size: The number of records per shard.
    """
    client = bigquery.Client(project=project_id)

    with open(query_file, 'r') as f:
        query = f.read()

    try:
        query_job = client.query(query)
        results = query_job.result()

        schema = results.schema
        file_index = 1
        row_count = 0
        csvfile = None  # Initialize outside loop

        for row in results:
            if row_count % batch_size == 0:
                if csvfile:  # Close previous file
                    csvfile.close()

                file_path = f"{destination_prefix}{file_index:05d}.csv" # Pad file index
                csvfile = open(file_path, 'w', newline='', encoding='utf-8')
                writer = csv.writer(csvfile)
                writer.writerow([field.name for field in schema]) # Write header
                file_index += 1

            writer.writerow(row)
            row_count += 1


        if csvfile: # Close the last open file
            csvfile.close()


        print(f"Query results exported to sharded files starting with {destination_prefix}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Export BigQuery data to sharded CSV files.')
    parser.add_argument('project_id', help='Your Google Cloud project ID.')
    parser.add_argument('dataset_id', help='The BigQuery dataset ID.')
    parser.add_argument('table_id', help='The BigQuery table ID.')
    parser.add_argument('query_file', help='Path to the file containing the BigQuery SQL query.')
    parser.add_argument('destination_prefix', help='The local path prefix for the sharded CSV files.')
    parser.add_argument('--batch_size', type=int, default=15000, help='The number of records per shard.')
    args = parser.parse_args()

    export_query_to_csv_sharded(
        args.project_id,
        args.dataset_id,
        args.table_id,
        args.query_file,
        args.destination_prefix,
        args.batch_size
    )