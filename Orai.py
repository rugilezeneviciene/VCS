import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "http://www.meteo.lt/en/miestas?placeCode=Vilnius"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

week_days = soup.find_all('span', class_='date')
temperatures = soup.find_all('span', class_='big up-from-zero')[::2]   #uzdedame limita, kad ieskotu 7


night_temp = [temperature.get_text() for temperature in temperatures]
week_day = [day.get_text() for day in week_days]

temp_list =[]
for temperature in temperatures:
    temp_text = temperature.get_text().replace('°C', '')
    temp_values = int(temp_text[:-1])
    temp_list.append(temp_values)

min_length = min(len(week_day), len(temp_list))

reorder_weekdays = week_day[:min_length]
reorder_temperature = temp_list[:min_length]

#apsirasome skale
week_day_order = ["Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

data = {
        'weekday': reorder_weekdays,
        'temperature': reorder_temperature
}

df = pd.DataFrame(data)
print(df)
df_sorted = df.sort_values(by=['weekday'],key=lambda x: pd.Categorical(x, categories=week_day_order, ordered=True))
plt.figure(figsize=(12,5))
plt.bar(df_sorted['weekday'], df_sorted['temperature'])
plt.xlabel('Savaites diena')
plt.ylabel('Temperatura')
plt.title('Oru prognoze Vilniuje')
#plt.xticks(rotation=60)
plt.show()

