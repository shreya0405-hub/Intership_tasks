import pandas as pd
import matplotlib.pyplot as plt
import os

# -----------------------------------
# 1. Create Output Folder
# -----------------------------------

output_folder = "output"

# Create folder if it does not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# -----------------------------------
# 2. Load the Dataset
# -----------------------------------

df = pd.read_csv("titanic.csv")

print("=================================")
print("TITANIC DATASET")
print("=================================")

# -----------------------------------
# 3. Display Basic Information
# -----------------------------------

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
print(df.info())

# -----------------------------------
# 4. Check Missing Values
# -----------------------------------

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# -----------------------------------
# 5. Handle Missing Values
# -----------------------------------

# Fill missing Age values with mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Fill missing Embarked values with mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Drop Cabin column because it has too many missing values
df.drop(columns=['Cabin'], inplace=True)

# -----------------------------------
# 6. Remove Duplicate Records
# -----------------------------------

print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())

df.drop_duplicates(inplace=True)

# -----------------------------------
# 7. Standardize Inconsistent Formats
# -----------------------------------

# Remove extra spaces from Name column
df['Name'] = df['Name'].str.strip()

# Convert Sex column to lowercase
df['Sex'] = df['Sex'].str.lower()

# -----------------------------------
# 8. Validate Data Types
# -----------------------------------

print("\nData Types:")
print(df.dtypes)

# -----------------------------------
# 9. Structural Validation
# -----------------------------------

# Check if Passenger IDs are unique
print("\nAre Passenger IDs Unique?")
print(df['PassengerId'].is_unique)

# Remove invalid ages
df = df[df['Age'] > 0]

# -----------------------------------
# 10. Detect and Remove Outliers
# -----------------------------------

Q1 = df['Fare'].quantile(0.25)
Q3 = df['Fare'].quantile(0.75)

IQR = Q3 - Q1

df = df[
    (df['Fare'] >= Q1 - 1.5 * IQR) &
    (df['Fare'] <= Q3 + 1.5 * IQR)
]

# -----------------------------------
# 11. Final Missing Value Check
# -----------------------------------

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# -----------------------------------
# 12. Save Cleaned Dataset
# -----------------------------------

cleaned_file = os.path.join(output_folder, "cleaned_titanic.csv")

df.to_csv(cleaned_file, index=False)

print("\nCleaned dataset saved successfully!")

# -----------------------------------
# 13. Data Visualization
# -----------------------------------

# Graph 1: Gender Distribution
plt.figure(figsize=(6, 4))

df['Sex'].value_counts().plot(kind='bar')

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")

gender_graph = os.path.join(output_folder, "gender_distribution.png")

plt.savefig(gender_graph)

plt.close()

# -----------------------------------

# Graph 2: Age Distribution
plt.figure(figsize=(6, 4))

plt.hist(df['Age'], bins=20)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

age_graph = os.path.join(output_folder, "age_distribution.png")

plt.savefig(age_graph)

plt.close()

# -----------------------------------

# Graph 3: Survival Count
plt.figure(figsize=(6, 4))

df['Survived'].value_counts().plot(kind='bar')

plt.title("Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Count")

survival_graph = os.path.join(output_folder, "survival_count.png")

plt.savefig(survival_graph)

plt.close()

# -----------------------------------
# 14. Final Output
# -----------------------------------

print("\n=================================")
print("DATA CLEANING COMPLETED SUCCESSFULLY")
print("=================================")

print("\nFiles saved in 'output' folder:")
print("1. cleaned_titanic.csv")
print("2. gender_distribution.png")
print("3. age_distribution.png")
print("4. survival_count.png")

print("\nCleaned Dataset Shape:")
print(df.shape)

print("\nFirst 5 Rows of Cleaned Dataset:")
print(df.head())
