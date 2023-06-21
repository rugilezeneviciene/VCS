import pandas as pd
import matplotlib.pyplot as plt
# #vienmate duomenu struktura kuri saugo vienos eilutes duomenis su indeksais
# data = pd.Series([10,20,30,40,50])      #vienmate
# print(data)

#dvimate duomenu struktura, kuri saugo duomenis lenteles pavidalu su stulpeliu ir eiluciu indeksais
# data = {'Name': ['Mantas', 'Deividas', 'Migle', 'Ausrine'],
#         'Age': [29, 27, 24, 45],
#         'City': ['Marijampole', 'Vilnius', 'Kaunas', 'Silute']
#         }
#
# df = pd.DataFrame(data)      #df reiskia dataframe, reiskia kad bus lentele. naudojamas atvaizduoti duomenims
# #print(df)
# #jei noretume atvaizduoti 2 pirmas eilutes data frame
# #print(df.head(2))
# #atvaizduojame konkretu stulpeli
# #print(df['Name'])
# selected_columns=df[['Name', 'Age']]
# #print(selected_columns)
#
# #prideti nauja stulpeli
# df['Salary'] = [1600, 1400, 1300, 1200]
# #print(df)
#
# #grupuokime duomenis pagal miesta ir gaukime vidutini atlyginima
# average_salary_by_city = df.groupby('City')['Salary'].mean() #mean yra vidurkis pandos kalboje
# #print(average_salary_by_city)
# average_age=df['Age'].mean()
# #print(f"Average age: {average_age}")
# #filtruojame. Jei noretume nerodyti kazkuriu stulpeliu, galima pasirinkti selected columns
#
# filtered_data = df[df['Age'] > 25][['Name', 'Age']]
# print(filtered_data)


#grupuoti pagal first name stulpeli ir suskaiciuoti dydi

df = pd.read_csv('employees.csv')
#print(df.head(5))

group_sizes = df.groupby('FIRST_NAME').size()
#print(group_sizes)

group_average = df.groupby('FIRST_NAME')['SALARY'].mean()

group_stats = df.groupby('FIRST_NAME')['SALARY'].describe()
#print(group_stats)
#
group_max = df.groupby('FIRST_NAME')['SALARY'].max()
#print(group_max)
# group_agg = df.groupby('FIRST_NAME').agg({'SALARY': ['sum', 'mean', max]})
# print(group_agg)
# #atvaizduojame linijine diagrama
# group_agg.plot(kind='line')
# #pridedamos antrastes
# plt.title('Suvestines statistika pagal vardus ir algas')
# plt.xlabel('Vardas')
# plt.ylabel('Atlyginimas')
#
# #atvaizduojama diagrama
# plt.show()

group_agg = df.groupby('FIRST_NAME').agg({'SALARY': ['sum', 'mean', max]})
print(group_agg)
#atvaizduojame linijine diagrama
group_agg.plot(kind='bar', figsize=(8,4))
#pridedamos antrastes
plt.title('Suvestines statistika pagal vardus ir algas')
plt.xlabel('Vardas')
plt.ylabel('Atlyginimas')

#atvaizduojama diagrama
plt.show()




