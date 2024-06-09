import requests
import pandas as pd
from datetime import date

url = 'http://v0.ovapi.nl/line/'

def retrieve_API_info(url: str) -> [any, int] :
    response = requests.get(url)
    status_code = response.status_code
    return response.json(), status_code

def convert_json_records_into_dataframe(records: any) -> pd.DataFrame : 
    df = pd.DataFrame.from_dict(records, orient='index')  
    return df 

def add_date_column_in_dataframe(df: pd.DataFrame, date: date) -> pd.DataFrame :
    df["Date"] = date
    return df


def save_dataframe_to_csv_file(df:pd.DataFrame, date:date) -> None:
    df.to_csv(f"file_{today_date}.csv") 


if __name__ == '__main__':
    netherlands_transports_url = 'http://v0.ovapi.nl/line/'
    netherlands_transports_records, status_code = retrieve_API_info(netherlands_transports_url)
    if status_code == 200:
        try:
            netherlands_transports_df = convert_json_records_into_dataframe(netherlands_transports_records)
            today_date = date.today()
            netherlands_transports_df_with_date = add_date_column_in_dataframe(netherlands_transports_df, date=today_date)
            save_dataframe_to_csv_file(netherlands_transports_df_with_date, today_date)
            print("successful download for", date.today())
        except:
            print("unsuccessful loading of records into the csv file")
    else:
        print('unsuccessful retrieval of data')




