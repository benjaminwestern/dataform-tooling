# Convert Schema

## Overview
This tool's purpose is to transform a complex nested JSON schema into a flattened JSON schema. The output can be easily used as part of a BigQuery SQL table schema definition in a Dataform project.

## Usage

```bash
python process_json.py --input_file <input_file_path> --output_file <output_file_path>
```

**Arguments**
* `--input_file`: Path to the input JSON file.
* `--output_file`: Path to the output JSON file.

### Example Input (ga_sessions.json)

```json
[
  {
    "name": "sessions",
    "type": "RECORD",
    "fields": [
      {
        "name": "session_id",
        "type": "INT64"
      },
      {
        "name": "user_id",
        "type": "INT64"
      },
      {
        "name": "device",
        "type": "RECORD",
        "fields": [
          {
            "name": "operating_system",
            "type": "STRING"
          },
          {
            "name": "browser",
            "type": "STRING"
          }
        ]
      },
      {
        "name": "events",
        "type": "ARRAY",
        "fields": [
          {
            "name": "event_name",
            "type": "STRING"
          },
          {
            "name": "event_params",
            "type": "RECORD",
            "fields": [
              {
                "name": "key",
                "type": "STRING"
              },
              {
                "name": "value",
                "type": "STRING"
              }
            ]
          }
        ]
      }
    ]
  }
]
```

### Example Output (ga_sessions_dataform.json)

```json
{
    "sessions": {
        "type": "RECORD",
        "fields": {
            "session_id": "INT64",
            "user_id": "INT64",
            "device": {
                "type": "RECORD",
                "fields": {
                    "operating_system": "STRING",
                    "browser": "STRING"
                }
            },
            "events": {
                "type": "ARRAY",
                "fields": {
                    "event_name": "STRING",
                    "event_params": {
                        "type": "RECORD",
                        "fields": {
                            "key": "STRING",
                            "value": "STRING"
                        }
                    }
                }
            }
        }
    }
}
```