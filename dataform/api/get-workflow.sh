# Provide the project ID
PROJECT_ID=$1
REGION=$2
REPOSITORY_ID=$3
WORKFLOW_CONFIG_NAME=$4

curl -X GET \
	-H "Authorization: Bearer $(gcloud auth print-access-token)" \
	-H "Content-Type: application/json; charset=utf-8" \
	"https://dataform.googleapis.com/v1beta1/projects/$PROJECT_ID/locations/$REGION/repositories/$REPOSITORY_ID/workflowConfigs/$WORKFLOW_CONFIG_NAME"