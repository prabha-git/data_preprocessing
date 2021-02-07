import sys
sys.path.append("../gbq")
import gbq_credentials
import pandas_gbq

def append_to_table(project_id,destination_table,df):
    credentials = gbq_credentials.get_credentials(project_id)
    pandas_gbq.context.credentials = credentials
    df.to_gbq(destination_table=destination_table,project_id=project_id,if_exists='append')