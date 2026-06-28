import pandas as pd
import matplotlib.pyplot as plt
import folium

# Load dataset
df = pd.read_csv("data/sales_data.csv")

print("===== DATASET =====")
print(df)

# High demand and low store presence
df["Demand_Score"] = df["Sales"] / df["Stores"]

print("\n===== HIGH DEMAND REGIONS =====")
high_demand = df.sort_values(by="Demand_Score", ascending=False)
print(high_demand[["Region", "Demand_Score"]])

# Plot sales chart
plt.figure(figsize=(10, 6))
plt.bar(df["Region"], df["Sales"])
plt.xticks(rotation=45)
plt.xlabel("Region")
plt.ylabel("Sales")
plt.title("Sales by Region")

# Save chart
plt.tight_layout()
plt.savefig("output/sales_chart.png")
plt.show()

# Create map centered on India
india_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Add markers
for _, row in df.iterrows():
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=f"{row['Region']} - Sales: {row['Sales']}",
        tooltip=row["Region"]
    ).add_to(india_map)

# Save map
india_map.save("output/demand_map.html")

print("\nMap saved as output/demand_map.html")
print("Chart saved as output/sales_chart.png")