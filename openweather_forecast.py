import requests
import json
import datetime
from pandas.io.json import json_normalize
import pandas as pd

cities=['Madrid','Paris','Berlin','Oslo','Porto']
appended_data=[]

for x in cities:
    url='http://api.openweathermap.org/data/2.5/forecast?q='+x+'&appid=PLEASE INSERT YOUR PERSONAL API_KEY'
    response = requests.get(url)
    data = json.loads(response.text)
    df = pd.DataFrame.from_dict(json_normalize(data['list']), orient='columns')
    df2=pd.DataFrame.from_dict(json_normalize(data['city']),orient='columns')
    df['city_temp']=''
    df['city_temp']=df['main.temp']-273.15
    df=df.drop(['dt', 'weather','main.temp','main.feels_like','main.temp_min','main.temp_max','main.pressure','main.sea_level','main.grnd_level','main.humidity','main.temp_kf','clouds.all','wind.speed','wind.deg','sys.pod'], axis=1)
    df2=pd.DataFrame(df2)
    city=df2['name'][0]
    city=str(city)
    df=df.rename(columns={'city_temp':city})
    df=df.set_index('dt_txt')
    appended_data.append(df)
appended_data = pd.concat(appended_data,axis=1,sort=False)    
display(appended_data)
