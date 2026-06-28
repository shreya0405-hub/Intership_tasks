import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("customer_churn.csv")

# Display Dataset
print("First 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove Duplicate Records
df.drop_duplicates(inplace=True)

# Convert TotalCharges Column
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors='coerce')

# Fill Missing Values
df.fillna(df.median(numeric_only=True), inplace=True)

# Churn Distribution
plt.figure(figsize=(6,4))
sns.countplot(x='Churn', data=df)
plt.title("Customer Churn Distribution")
plt.savefig("images/churn_distribution.png")
plt.show()

# Contract Type vs Churn
plt.figure(figsize=(8,5))
sns.countplot(x='Contract', hue='Churn', data=df)
plt.title("Contract Type vs Churn")
plt.xticks(rotation=15)
plt.savefig("images/contract_analysis.png")
plt.show()

# Tenure Distribution
plt.figure(figsize=(10,5))
sns.histplot(data=df, x='tenure', hue='Churn', kde=True)
plt.title("Tenure Distribution")
plt.savefig("images/tenure_analysis.png")
plt.show()

# Monthly Charges Analysis
plt.figure(figsize=(8,5))
sns.boxplot(x='Churn', y='MonthlyCharges', data=df)
plt.title("Monthly Charges vs Churn")
plt.savefig("images/monthly_charges.png")
plt.show()

# Correlation Heatmap
numeric_df = df.select_dtypes(include=np.number)

plt.figure(figsize=(10,6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.savefig("images/correlation_heatmap.png")
plt.show()

# Churn Rate
churn_rate = df['Churn'].value_counts(normalize=True) * 100

print("\nChurn Rate:")
print(churn_rate)

# Insights
print("\nKey Insights:")
print("1. Customers with month-to-month contracts churn more.")
print("2. Customers with high monthly charges are likely to churn.")
print("3. Short tenure customers have higher churn rates.")
print("4. Long-term contracts improve retention.")

print("\nCustomer Churn Analysis Completed Successfully!")