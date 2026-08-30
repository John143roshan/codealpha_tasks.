import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the dataset
file_path = "Data/Sample - Superstore.csv"
df = pd.read_csv(file_path, encoding="latin1")

# Create folder for visualizations
output_folder = "visualizations"
os.makedirs(output_folder, exist_ok=True)

# Visualization style
sns.set_theme(style="whitegrid")

# 1. Sales by Category
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(f"{output_folder}/sales_by_category.png")
plt.close()

# 2. Sales by Region
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(f"{output_folder}/sales_by_region.png")
plt.close()

# 3. Monthly Sales Trend
df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
)

plt.figure(figsize=(10, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{output_folder}/monthly_sales_trend.png")
plt.close()

# 4. Sales by Customer Segment
segment_sales = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
segment_sales.plot(kind="bar")
plt.title("Total Sales by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(f"{output_folder}/sales_by_segment.png")
plt.close()

# 5. Discount vs Profit
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Discount", y="Profit", alpha=0.5)
plt.title("Relationship Between Discount and Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig(f"{output_folder}/discount_vs_profit.png")
plt.close()

print("Task 3 visualizations created successfully!")
print(f"Files saved in: {output_folder}")
