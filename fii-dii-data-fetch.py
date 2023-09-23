from datetime import date, timedelta
import requests,io
import pandas as pd

start_date = date(2022, 2,4 )
end_date = date(2022, 2, 4)
delta = timedelta(days=1)
df=pd.DataFrame()
while start_date <= end_date:
    try:
       csv_url='https://archives.nseindia.com/content/nsccl/fao_participant_oi_'+start_date.strftime("%d%m%Y")+'.csv'
       filename='fao_participant_oi_'+start_date.strftime("%d%m%Y")+'.csv'
       req = requests.get(csv_url,timeout=1)
       url_content = req.content
       c=pd.read_csv(io.StringIO(url_content.decode('utf-8')),skiprows=1)
       c['Date']=start_date.strftime("%d-%m-%Y")
       df=pd.concat([df,c],ignore_index=True,axis=0)
       print('Done for '+start_date.strftime("%d-%m-%Y"))
    except:
       print('no data for '+start_date.strftime("%d-%m-%Y"))
       
    start_date += delta 
df.to_csv('filename.csv')