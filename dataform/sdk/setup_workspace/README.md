# Setup a Dataform workspace

## Usage

This script creates a new workspace in a Dataform repository, using the Google Cloud Dataform library. Your project must have a Dataform repository set up in order to use this script.

To use this script, you need to install the Google Cloud Dataform library:

```bash
pip install -r requirements.txt
```

Then, run the script with the following command:

```bash
python main.py <project> <location> <repository> <workspace_name>
```

**Arguments**
* `<project>`: The project ID.
* `<location>`: The location of the Dataform repository.
* `<repository>`: The Dataform repository name.
* `<workspace_name>`: The name of the workspace to create.