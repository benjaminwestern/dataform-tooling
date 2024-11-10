# Run a Dataform workflow config

## Usage

This script runs a Dataform workflow config.
To use this script, you need to install the Google Cloud Dataform library:

```bash
pip install -r requirements.txt
```

Then, run the script with the following command:

```bash
python run_workflow.py <project> <location> <repository> <workflow_config_name>
```

**Arguments**
* `<project>`: The project ID.
* `<location>`: The location of the Dataform repository.
* `<repository>`: The Dataform repository name.
* `<workflow_config_name>`: The name of the workflow config.