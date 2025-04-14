Import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Load the dataset and perform initial inspection/cleaning
df = pd.read_csv('survey.csv') # Load the dataset
df.head() # Display the first few rows of the dataset
df.info() # Display information about the dataset, including data types and non-null counts
df.dropna(inplace=True) # Drop rows with missing values 
df.drop_duplicates(inplace=True) # Drop duplicate rows
df.columns = [col.lower().strip().replace(' ', '_') for col in df.columns] # Normalize column names
df.rename(columns={'age': 'age_years', 'income': 'annual_income'}, inplace=True) # Rename columns for clarity
df['satisfaction'] = df['satisfaction'].replace({'Very Unsatisfied': 1, 'Unsatisfied': 2, 'Neutral': 3, 'Satisfied': 4, 'Very Satisfied': 5}) # Map satisfaction levels to numerical values
df['income'] = df['income'].replace({'\$': '', ',': ''}, regex=True).astype(float) # Clean income column
df['income'] = df['income'].fillna(df['income'].mean()) # Fill missing income values with mean
df['age'] = df['age'].astype(int) # Convert age to integer type
df.to_csv('survey_cleaned.csv', index=False) # Save cleaned data to a new CSV file

# Exploratory Data Analysis
plt.figure(figsize=(10, 6))
sns.histplot(df['age'], bins=30, kde=True) # Histogram of age distribution      
plt.title('Age Distribution')
plt.xlabel('Age')   


