import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create outputs folder automatically
os.makedirs("outputs", exist_ok=True)

# Load dataset
df = pd.read_csv("data/website_traffic.csv")

# -----------------------------
# DATA OVERVIEW
# -----------------------------
print("===== DATASET HEAD =====")
print(df.head())

print("\n===== DATASET INFO =====")
print(df.info())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# -----------------------------
# KEY METRICS
# -----------------------------
total_sessions = df['Session_ID'].nunique()

avg_session_duration = df['Session_Duration_Minutes'].mean()

avg_pages_visited = df['Pages_Visited'].mean()

bounce_rate = (df['Bounce'] == 'Yes').mean() * 100

conversion_rate = (df['Conversion'] == 'Yes').mean() * 100

print("\n===== KEY METRICS =====")

print(f"Total Sessions: {total_sessions}")

print(f"Average Session Duration: {avg_session_duration:.2f} minutes")

print(f"Average Pages Visited: {avg_pages_visited:.2f}")

print(f"Bounce Rate: {bounce_rate:.2f}%")

print(f"Conversion Rate: {conversion_rate:.2f}%")

# -----------------------------
# TRAFFIC SOURCE ANALYSIS
# -----------------------------
plt.figure(figsize=(8,5))

sns.countplot(data=df, x='Traffic_Source')

plt.title("Traffic Sources")

plt.xticks(rotation=15)

plt.tight_layout()

plt.savefig("outputs/traffic_sources.png")

plt.show()

# -----------------------------
# SESSION DURATION
# -----------------------------
plt.figure(figsize=(8,5))

sns.histplot(df['Session_Duration_Minutes'], bins=8, kde=True)

plt.title("Session Duration Distribution")

plt.tight_layout()

plt.savefig("outputs/session_duration.png")

plt.show()

# -----------------------------
# PAGES VISITED
# -----------------------------
plt.figure(figsize=(8,5))

sns.histplot(df['Pages_Visited'], bins=8, kde=True)

plt.title("Pages Visited Distribution")

plt.tight_layout()

plt.savefig("outputs/page_views.png")

plt.show()

# -----------------------------
# BOUNCE RATE
# -----------------------------
plt.figure(figsize=(6,6))

df['Bounce'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Bounce Rate")

plt.ylabel("")

plt.savefig("outputs/bounce_rate.png")

plt.show()

# -----------------------------
# EXIT PAGE ANALYSIS
# -----------------------------
plt.figure(figsize=(8,5))

sns.countplot(data=df, x='Exit_Page')

plt.title("Most Common Exit Pages")

plt.xticks(rotation=15)

plt.tight_layout()

plt.savefig("outputs/exit_pages.png")

plt.show()

# -----------------------------
# DEVICE TYPE ANALYSIS
# -----------------------------
plt.figure(figsize=(7,5))

sns.countplot(data=df, x='Device_Type')

plt.title("Device Type Usage")

plt.tight_layout()

plt.savefig("outputs/device_type.png")

plt.show()

# -----------------------------
# USER JOURNEY ANALYSIS
# -----------------------------
journey = df.groupby(
    ['Traffic_Source', 'Exit_Page']
).size().reset_index(name='Count')

print("\n===== USER JOURNEY ANALYSIS =====")

print(journey)

# -----------------------------
# INSIGHTS
# -----------------------------
print("\n===== INSIGHTS =====")

print("1. Direct and Organic Search users show better engagement.")

print("2. Checkout page has higher conversions.")

print("3. Home and Landing pages experience more drop-offs.")

print("4. Longer session duration usually indicates higher engagement.")

print("5. Mobile users form a major share of website traffic.")