#The dataset name is Pokemon
#Drawing insights from pokemon dataset

#how to read csv file?
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

df=pd.read_csv("C:\\Users\\User\\Downloads\\Pokemon_dataset.csv")

#finding first and last rows
print(df.head(5))
print(df.tail(5))

#how many columns are there?
print(df.info())

#Check the shape of the DataFrame (rows, columns)?
shape = df.shape
print("Shape of the DataFrame:", shape)

#check statistical information about the dataframe?
print(df.describe())

#How many Pokémon are legendary?
legendary_count = len(df[df['Legendary']])
print("Number of Legendary Pokémon:", legendary_count)


#Legendary Pokémon by type?
legendary_type=df[(df['Legendary']== True) & df['Type 1']]['Type 1'].value_counts().reset_index(name='count')
print(legendary_type)


#Legendary Pokémon by fighter stats?
legendary_pokemon=df[df['Legendary']]
legend_by_spAtk=legendary_pokemon.sort_values(by='Sp. Atk')
print(legend_by_spAtk[['Name','Legendary','Type 1','Sp. Atk']])
#You can replace 'Sp. Atk' with any other fighter stat
#(e.g., 'Defense', 'HP','Attack' etc.)to find Legendary Pokémon by that specific stat.
legendary_pokemon = df[df['Legendary']]
legendary_by_attack = legendary_pokemon.sort_values(by='Attack', ascending=False)
print(legendary_by_attack[['Name', 'Type 1', 'Attack']])


#Cleaning the dataset
# Step 1: Handling Missing Values
# Check which columns have missing values and how many.
missing_values=df.isnull().sum()
print("missing values:",missing_values)

#It appears that "Type 2" has missing values. Let's fill those with a reasonable value.
df['Type 2'].fillna('none',inplace=True)
print(df['Type 2'])

#check the datatypes
data_types=df.dtypes
print("Data types:",data_types)

# Check for and remove duplicate rows.
df.drop_duplicates(inplace=True)
print("Cleaned dataset:")
print(df.head(5))

#How are Pokemon numbers distributed across generations?
generation_counts = df.groupby('Generation').count()['#']
plt.bar(generation_counts.index, generation_counts.values)
# Add labels and title
plt.xlabel('Generation')
plt.ylabel('Number of Pokémon')
plt.title('Distribution of Pokémon Across Generations')
plt.show()


#What are the most common types of Pokemon?
types_pokemon=df['Type 1'].value_counts().head(5)
print("Top 5 most common types of pokemons:",types_pokemon)
types_pokemon=df['Type 2'].value_counts().head(5)
print("Top 5 most common types of pokemons:",types_pokemon)

#What are the strongest and weakest Pokemon species?
strongest_pokemon=df[df['Total']==df['Total'].max()]
weakest_pokemon=df[df['Total']==df['Total'].min()]

strongest_species=strongest_pokemon['Name'].values[0]
weakest_species=weakest_pokemon['Name'].values[0]

strongest_total = strongest_pokemon['Total'].values[0]
weakest_total = weakest_pokemon['Total'].values[0]

# Print the results
print("The strongest Pokémon species is:", strongest_species)
print("Total strength:", strongest_total)

print("The weakest Pokémon species is:", weakest_species)
print("Total strength:", weakest_total)

#What are the strongest and weakest types of Pokemon?
type_strength = df.groupby('Type 1')['Total'].mean()
strongest_type = type_strength.index[0]
strongest_average_total = type_strength.iloc[0]

weakest_type = type_strength.index[-1]
weakest_average_total = type_strength.iloc[-1]

#Print the results
print("The strongest type of Pokémon is:", strongest_type)
print("Average total strength:", strongest_average_total)

print("The weakest type of Pokémon is:", weakest_type)
print("Average total strength:", weakest_average_total)

#Do any types of Pokemon excel at certain statistics over others?
type_stats = df.groupby('Type 1')[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].mean()
best_stat_for_type = type_stats.idxmax(axis=1)
best_stat_value = type_stats.max(axis=1)

print("Types that excel in specific statistics:")
for pokemon_type, stat in zip(best_stat_for_type.index, best_stat_for_type):
    value = best_stat_value.loc[pokemon_type]
    print(f"Type {pokemon_type} excels in {stat} with an average value of {value:.2f}")

#Are any of the statistics correlated?
selected_columns = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Total']
correlation_matrix = df[selected_columns].corr()
print("Correlation Matrix:",correlation_matrix)

#Considerations regarding the results?
""" Considerations:
# Look for strong positive and negative correlations.
# Positive correlations indicate that when one stat goes up, the other tends to go up.
# Negative correlations indicate that when one stat goes up, the other tends to go down.
# A coefficient close to 0 suggests no strong linear relationship.

# Consider domain knowledge and context to interpret the results.
# Keep in mind that correlation does not imply causation.
# Be cautious about multicollinearity if using these variables in modeling.
# Check for and address outliers if necessary."""

#Create a training/test split?
X = df[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']]
y = df['Total']

# Split the data into a training set and a test set (e.g., 80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Print the shapes of the training and test sets to verify
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

#split data int Train and model sets?
print("Print the shapes of the training and validation sets to verify:")
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42)
print("X_train shape:", X_train.shape)
print("X_valid shape:", X_valid.shape)
print("y_train shape:", y_train.shape)
print("y_valid shape:", y_valid.shape)













