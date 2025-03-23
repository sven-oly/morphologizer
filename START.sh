export PROJECT_ID=morphologizer-395504
export QUEUE_ID=morphologizer-395504-queue
export LOCATION_ID=us-central1
export QUOTA_PROJECT_ID=$PROJECT_ID
gcloud config set project $PROJECT_ID
gcloud auth application-default set-quota-project $PROJECT_ID


python3 main.py runserver

