# Query Workflow Invocation Actions

## Usage

This script queries workflow invocation actions for a given Dataform workflow config.

To use this script, you need to install the Google Cloud Dataform library:

```bash
pip install google-cloud-dataform
```

Then, run the script with the following command:

```bash
python main.py <project> <location> <repository> <workflow_config_name>
```

**Arguments**
* `<project>`: The project ID.
* `<location>`: The location of the Dataform repository.
* `<repository>`: The Dataform repository name.
* `<workflow_config_name>`: The name of the workflow config.