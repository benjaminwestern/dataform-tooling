# Provide the project ID
PROJECT_ID=$1
REGION=$2
REPOSITORY_ID=$3
WORKSPACE_NAME=$4
# Define the payload
# Workspace name CANNOT be the same as the remote default branch name
PAYLOAD="{\"name\":\"$WORKSPACE_NAME\"}"

curl -X POST \
	-H "Authorization: Bearer $(gcloud auth print-access-token)" \
	-H "Content-Type: application/json; charset=utf-8" \
    -d "$PAYLOAD" \
	"https://dataform.googleapis.com/v1beta1/projects/$PROJECT_ID/locations/$REGION/repositories/$REPOSITORY_ID/workspaces?workspaceId=$WORKSPACE_NAME"