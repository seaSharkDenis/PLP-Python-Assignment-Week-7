import pandas as pd
import matplotlib.pyplot as plt

# Load dataset using pandas
population_data = pd.read_csv('random_population_data.csv')

# Display first 20 rows of data set
print("First 20 rows of the population dataset: ")
print(population_data.head(20))
print()

# Explore the structure of the dataset
print("Structure of the population dataset: ")
print(population_data.info())
print()

# Data cleanup by dropping missing values
cleaned_dataset = population_data.dropna()
print(cleaned_dataset.info())


### Task 2: Basic Data Analysis
# Basic statistics
summary = cleaned_dataset.describe()
print(summary)

# # Groupings on a categorical column
# mean by age
mean_by_age = cleaned_dataset.groupby('sex')['age'].mean()
print(mean_by_age)

# Salary distribution by sex.
print(cleaned_dataset.groupby('sex')['salary'].describe())


### Task 3: Data Visualization
# Average salary by occupation
avg_salary = cleaned_dataset.groupby('occupation')['salary'].mean().sort_values()

# Bar chart
avg_salary.plot(kind='bar', color='skyblue')
plt.title("Average Salary by Occupation")
plt.xlabel("Occupation")
plt.ylabel("Salary")
plt.xticks(rotation=45)
plt.show()


# Nationality distribution
nationality_counts = cleaned_dataset['nationality'].value_counts()

# Pie chart
nationality_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title("Nationality Distribution")
plt.tight_layout()
plt.show()

# Salary Distribution using a histogram
cleaned_dataset.plot(kind='hist', bins=20, color='lightgreen', edgecolor='black')
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()