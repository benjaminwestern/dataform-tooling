import json
import argparse

def process_json(json_data):
    def process_fields(fields):
        result = {}
        for field in fields:
            if 'fields' in field:
                result[field['name']] = {
                    'type': field['type'],
                    'fields': process_fields(field['fields'])
                }
            else:
                result[field['name']] = field['type']
        return result

    return process_fields(json_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a JSON file.')
    parser.add_argument('--input_file', required=True, help='Path to the input JSON file.')
    parser.add_argument('--output_file', required=True, help='Path to the output JSON file.')
    args = parser.parse_args()

    with open(args.input_file, 'r') as f:
        json_input = json.load(f)

    output = process_json(json_input)

    with open(args.output_file, 'w') as f:
        json.dump(output, f, indent=4)