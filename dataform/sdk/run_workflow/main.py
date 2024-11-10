from google.cloud import dataform_v1beta1

dataform_client = dataform_v1beta1.DataformClient()

def run_workflow(dataform_client, project, location, respository, workflow_config_name):
    """Runs a workflow config.

    Args:
        dataform_client: The Dataform client.
        project: The project ID.
        location: The location of the Dataform repository.
        respository: The Dataform repository name.
        workflow_config_name: The name of the workflow config.

    Returns:
        The name of the created workflow invocation.
    """

    repo_uri = f'projects/{project}/locations/{location}/repositories/{respository}'
    workflow_config = f'projects/{project}/locations/{location}/repositories/{respository}/workflowConfigs/{workflow_config_name}'

    request = dataform_v1beta1.CreateWorkflowInvocationRequest(
        parent=repo_uri,
        workflow_invocation=dataform_v1beta1.types.WorkflowInvocation(
            workflow_config=workflow_config
        )
    )

    response = dataform_client.create_workflow_invocation(request=request)
    name = response.name
    return name

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Run a Dataform workflow config.")
    parser.add_argument("project", help="The project ID.")
    parser.add_argument("location", help="The location of the Dataform repository.")
    parser.add_argument("repository", help="The Dataform repository name.")
    parser.add_argument("workflow_config_name", help="The name of the workflow config.")

    args = parser.parse_args()

    workflow_invocation_name = run_workflow(
        dataform_client,
        args.project,
        args.location,
        args.repository,
        args.workflow_config_name,
    )

    print(f"Workflow invocation created: {workflow_invocation_name}")