from google.oauth2 import service_account


def get_credentials(project_id):
    service_account_key_path=""
    if project_id == 'covid-303903':
        service_account_key_path = "../../keys/covid-gbq-data-owner.json"
    credentials = service_account.Credentials.from_service_account_file(
    service_account_key_path,scopes=["https://www.googleapis.com/auth/cloud-platform"])
    return credentials
    