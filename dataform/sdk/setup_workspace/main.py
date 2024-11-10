from google.cloud import dataform_v1beta1

dataform_client = dataform_v1beta1.DataformClient()

def create_workspace(dataform_client, project_id, region, repository, workspace_name):
    """Creates a new workspace in a Dataform repository.

    Args:
        dataform_client: The Dataform client.
        project_id: The project ID.
        region: The location of the Dataform repository.
        repository: The Dataform repository name.
        workspace_name: The name of the workspace to create.
    """

    repository_parent_string = f"projects/{project_id}/locations/{region}/repositories/{repository}"

    # Initialize request argument(s)
    request = dataform_v1beta1.CreateWorkspaceRequest(
        parent=repository_parent_string,
        workspace_id=workspace_name,
    )

    # Make the request
    response = dataform_client.create_workspace(request=request)

    # Handle the response
    print(f"Workspace created: {response.name}")

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Create a new workspace in a Dataform repository.")
    parser.add_argument("project", help="The project ID.")
    parser.add_argument("location", help="The location of the Dataform repository.")
    parser.add_argument("repository", help="The Dataform repository name.")
    parser.add_argument("workspace_name", help="The name of the workspace to create.")

    args = parser.parse_args()

    create_workspace(
        dataform_client,
        args.project,
        args.location,
        args.repository,
        args.workspace_name,
    )