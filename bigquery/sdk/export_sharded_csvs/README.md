## Export BigQuery Table to Sharded CSV Files

This script exports data from a BigQuery table that is referenced in a provided .sql file to sharded CSV files.

## Requirements
* Google Cloud SDK (installed and configured)
* `pip install -r requirements.txt` (to install the required Python libraries)

## Usage

```bash
python main.py --project_id <project_id> --dataset_id <dataset_id> --table_id <table_id> --query_file <query_file_path> --destination_prefix <destination_prefix> --batch_size <batch_size>
```

**Arguments**
* `--project_id`: Your BigQuery project ID.
* `--dataset_id`: The ID of the dataset containing the table.
* `--table_id`: The ID of the table.
* `--query_file`: Path to the file containing the BigQuery SQL query.
* `--destination_prefix`: The local path prefix for the sharded CSV files (e.g., "sales_export_"). Files will be named like "sales_export_00001.csv", "sales_export_00002.csv", etc.
* `--batch_size`: The number of records per shard.

## Examples

### Export Data with a Custom Query

```bash
python main.py --project_id your-project-id --dataset_id your-dataset-id --table_id your-table-id --query_file my_query.sql --destination_prefix sales_data_ --batch_size 10000
```

This command will execute the query defined in the `my_query.sql` file, fetch the results, and export them to sharded CSV files starting with the prefix "sales_data_" with a batch size of 10,000 records per file.

## Notes

* Ensure your project has the necessary permissions to access the target BigQuery table.
* You can specify a custom BigQuery query in the `--query_file` argument.
* The `--batch_size` argument controls the number of records per shard. Adjust it based on your needs and limitations.
* CSV files cannot contain nested or repeated fields. If your table schema includes such fields, consider flattening the data before exporting it.

