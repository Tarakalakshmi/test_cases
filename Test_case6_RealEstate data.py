#The dataset is Real_estate
import pandas as pd
import numpy as np
df=pd.read_csv("C:\\Users\\User\\Downloads\\12.real state.csv")
print(df.info())

print('1')
#Find City wise list all the Villa which is not less than ten thousand.
villa_data = df[(df['type'] == 'villa') & (df['price'] > 10000) & df['city']]
vd=villa_data[['city', 'price', 'type']]
print(vd)

print('2')
#In GALT city which residential type has more than 800sq__ft. Display their respective details street,sq__ft,sale_date,city.
galt_residential = df[(df['city'] == 'GALT') & (df['type'] == 'Residential') & (df['sq__ft'] > 800)]
result = galt_residential[['street', 'sq__ft', 'sale_date', 'city']]
print(result)

print('3')
#Which is the cheapest Villa in CA. name the city,street and price for the Villa.
cheapest_villa = df[(df['type'] == 'villa') & (df['state'] == 'CA')]
cheap_villa=df.sort_values('price',ascending=True)
city = cheap_villa['city']
street = cheap_villa['street']
price = cheap_villa['price']
print(f"the cheapest villa in CA is located in {city}, on {street}, and it cost ${price}")

print('4')
#List top 5 residency details which lie in the budget of 60000-120000, an area more than 1450, min bedroom 3 and, min bathroom 2.
residency_details = df[(df['type'] == 'Residential') & (df['price'] > 60000) &(df['price'] < 1200000) & (df['sq__ft'] > 1450) & (df['beds'] == 3) & (df['baths'] == 2)]
rd=residency_details[['type', 'price', 'sq__ft', 'beds', 'baths']]
print("top 5 residency deails:")
print(rd)





















