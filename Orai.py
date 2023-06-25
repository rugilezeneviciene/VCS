import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://www.meteo.lt/en/miestas?placeCode=Vilnius"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

week_days = soup.find_all('span', class_='date')
temperatures = soup.find_all('span', class_='big up-from-zero')

#reikia apsirasyti visas temperaturas

night_temp = [temperature.get_text() for temperature in temperatures[::2]]    #temperature yra is psil. [::2 turi skaiciuoti temp elementus

#day_temp = [temperature.get_text() for temperature in temperatures[::2]]
week_day = [day.get_text() for day in week_days]

temp_values = night_temp

data = {'weekday': week_day,
        'temperature': temp_values}

df = pd.DataFrame(data)
df_sorted = df.sort_values(by='weekday')
plt.bar(df_sorted['weekday'], df_sorted['temperature'])
plt.xlabel('Savaites diena')
plt.ylabel('Temperatura')
plt.title('Oru prognoze Vilniuje')
plt.ylim(0,15)
plt.show()