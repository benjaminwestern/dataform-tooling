from google.cloud import dataform_v1beta1

dataform_client = dataform_v1beta1.DataformClient()

def query_workflow_job(dataform_client, project, location, respository, workflow_config_name):
    """Queries workflow invocation actions for a given workflow config.

    Args:
        dataform_client: The Dataform client.
        project: The project ID.
        location: The location of the Dataform repository.
        respository: The Dataform repository name.
        workflow_config_name: The name of the workflow config.
    """

    workflow_config = f'projects/{project}/locations/{location}/repositories/{respository}/workflowConfigs/{workflow_config_name}'

    request = dataform_v1beta1.QueryWorkflowInvocationActionsRequest(
        name=workflow_config
    )

    # Make the request
    page_result = dataform_client.query_workflow_invocation_actions(request=request)

    # Handle the response
    for response in page_result:
        print(response)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Query workflow invocation actions for a Dataform workflow config.")
    parser.add_argument("project", help="The project ID.")
    parser.add_argument("location", help="The location of the Dataform repository.")
    parser.add_argument("repository", help="The Dataform repository name.")
    parser.add_argument("workflow_config_name", help="The name of the workflow config.")

    args = parser.parse_args()

    query_workflow_job(
        dataform_client,
        args.project,
        args.location,
        args.repository,
        args.workflow_config_name,
    )