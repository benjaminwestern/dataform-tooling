# BigQuery Schema Management
This script provides functionality for fetching and updating schemas of BigQuery tables.

## Requirements

* Google Cloud SDK (installed and configured)
* `google-cloud-bigquery` Python library:
    ```bash
    pip install google-cloud-bigquery
    ```

## Usage

```bash
python main.py --project_id <project_id> --dataset_id <dataset_id> --table_id <table_id> --json_file <json_file_path> --action <action>
```

**Arguments**
* `--project_id`: Your BigQuery project ID.
* `--dataset_id`: The ID of the dataset containing the table.
* `--table_id`: The ID of the table.
* `--json_file`: Path to the JSON file containing the schema (for update actions).
* `--action`: The action to perform, either `get` (fetch schema) or `update` (update schema).

## Examples

### Get Table Schema

```bash
python main.py --project_id your-project-id --dataset_id your-dataset-id --table_id your-table-id --json_file schema.json --action get
```

This command will fetch the schema of the table `your-table-id` in the dataset `your-dataset-id` of the project `your-project-id` and save it to the file `schema.json`.

### Update Table Schema

```bash
python main.py --project_id your-project-id --dataset_id your-dataset-id --table_id your-table-id --json_file schema.json --action update
```

This command will update the schema of the table `your-table-id` in the dataset `your-dataset-id` of the project `your-project-id` using the schema defined in the `schema.json` file.

## Notes

* Ensure your project has the necessary permissions to access and modify the target BigQuery table.
* The `schema.json` file should be in the format expected by the `google-cloud-bigquery` library.
* You can find more information about BigQuery schemas and the `google-cloud-bigquery` library in the [official documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables).

