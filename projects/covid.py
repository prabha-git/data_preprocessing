import sys
sys.path.append("../")
import gbq.save_to_gbq as save_to_gbq
import web_scrapping.covid as web_scrapping
import data_cleaning.covid as data_cleaning

data = web_scrapping.get_data()
data = data_cleaning.clean_data(data)
save_to_gbq.append_to_table(destination_table='dataset.covid_stats',project_id='covid-303903',df=data)