#1 Apskaičiuoti vidurkį, sumą, minimumą, maksimumą ir kitus statistinius rodiklius
# stulpeliuose arba grupėse naudojant mean(), sum(), min(), max() ir kitas funkcijas.
#2 Grupuoti duomenis pagal tam tikrą stulpelį ir atlikti agregavimo operacijas,
# pvz., apskaičiuoti bendrą sumą ar vidurkį kiekvienai grupės naudojant groupby() funkciją.
#3 mmeiksmus, pvz., pašalinti dublikatus,
# užpildyti trūkstamas reikšmes arba pašalinti netinkamas reikšmes.
#4 Sukurti naujus stulpelius, atlikdami skaičiavimus ar manipuliacijas su
# esamais stulpeliais, pvz., pridėti, sudėti arba suskaidyti reikšmes.
#5 Redaguoti duomenų tipus, pvz., konvertuoti skaičių tipo stulpelius į
# datų tipo stulpelius arba atvirkščiai.
#6 Atlikti duomenų filtravimą, rūšiavimą ir sujungimą pagal sąlygas arba stulpelius.
#7 Vizualizuoti duomenis naudojant įvairias diagramas ir grafikus

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('employees.csv')
#print(df.head(5))
Mean = df['SALARY'].mean()
#print(Mean)

min_salary = df['SALARY'].min()
#print(min_salary)

max_salary = df['SALARY'].max()
#print(max_salary)

#skaiciuojame atlyginimu suma, pagal departamento ID=
sum_group = df.groupby('DEPARTMENT_ID')['SALARY'].sum()
#print(sum_group, end='\n\n')

#skaiciuojame atlyginimu vidurki pagal departamenta
avg_group = df.groupby('DEPARTMENT_ID')['SALARY'].mean()
#print(avg_group, end='\n\n')

#print(df.head(5))
#pasaliname dublikatus ir sukuriame nauja employess2 failiuka
# #df.drop_duplicates(subset=None, inplace = True)
# with open('employees.csv', 'r') as in_file, open('employees2.csv', 'w') as out_file:
#     seen = set()
#     for line in in_file:
#         if line in seen: continue
#         seen.add(line)
#         out_file.write(line)
#sukurti nauja stulpeli po salary rise + 15 proc.

df['increased_salary'] = df.SALARY * 1.15

#print(df.head(5))

df["DEPARTMENT_ID"] = pd.to_datetime(df["DEPARTMENT_ID"])
# print(df['DEPARTMENT_ID'].dtypes)

filtravimas = df.groupby('DEPARTMENT_ID').agg({'SALARY': ['mean']})
#print(filtravimas)
filtravimas.plot(kind='bar', figsize=(12,5))
plt.title('Atlyginimu vidurkis pagal departamentus')
plt.xlabel('Departamento_id')
plt.ylabel('Algu vidurkis')
plt.show()

stats = df.agg({'SALARY':['sum', 'mean', 'min', 'max', 'size']})
print(stats)