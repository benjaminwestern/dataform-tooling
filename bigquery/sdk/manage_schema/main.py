from google.cloud import bigquery
import argparse
import json

client = bigquery.Client()

def get_table_schema(project_name, dataset_name, table_name, json_file_path):
    """Fetches the schema of a BigQuery table and saves it to a JSON file."""

    table_id = f'{project_name}.{dataset_name}.{table_name}'

    table = client.get_table(table_id)

    print(
        "Got table '{}.{}.{}'.".format(
            table.project, table.dataset_id, table.table_id)
    )
    print("Table schema: {}".format(table.schema))
    print("Table description: {}".format(table.description))
    print("Table has {} rows".format(table.num_rows))

    client.schema_to_json(table.schema, json_file_path)

def update_schema_from_json(project_name, dataset_name, table_name, json_file_path):
    """Updates the schema of a BigQuery table from a JSON file."""

    table_id = f'{project_name}.{dataset_name}.{table_name}'

    table = client.get_table(table_id)

    with open(json_file_path, 'r') as f:
        new_schema_json = json.load(f)

    new_schema = client.schema_from_json(new_schema_json)

    table.schema = new_schema
    table = client.update_table(table, ["schema"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='BigQuery Schema Management')
    parser.add_argument('--project_id', required=True, help='BigQuery Project ID.')
    parser.add_argument('--dataset_id', required=True, help='BigQuery Dataset ID.')
    parser.add_argument('--table_id', required=True, help='BigQuery Table ID.')
    parser.add_argument('--json_file', required=True, help='Path to the JSON schema file.')
    parser.add_argument('--action', choices=['get', 'update'], required=True, help='Action to perform: get or update')

    args = parser.parse_args()

    if args.action == 'get':
        get_table_schema(args.project_id, args.dataset_id, args.table_id, args.json_file)
    elif args.action == 'update':
        update_schema_from_json(args.project_id, args.dataset_id, args.table_id, args.json_file)