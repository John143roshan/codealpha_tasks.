# ==========================================
# CodeAlpha Internship - Exploratory Data Analysis
# Project: Sales Performance Analysis of an Indian E-commerce Company
# Author: John Meddy Roshan
# ==========================================

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Improve graph appearance
plt.style.use("ggplot")

# Load Dataset
df = pd.read_csv("Data/Sample - Superstore.csv", encoding="latin1")

# ==========================================
# DATASET OVERVIEW
# ==========================================

print("=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

# ==========================================
# BASIC STATISTICS
# ==========================================

print("\n" + "=" * 60)
print("BASIC STATISTICS")
print("=" * 60)

print(df.describe())

print("\nTotal Sales:")
print(df["Sales"].sum())

print("\nTotal Profit:")
print(df["Profit"].sum())

print("\nAverage Sales:")
print(df["Sales"].mean())

print("\nAverage Profit:")
print(df["Profit"].mean())

# ==========================================
# VISUALIZATION 1 - SALES DISTRIBUTION
# ==========================================

plt.figure(figsize=(8,5))
sns.histplot(df["Sales"], bins=30)

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("Images/sales_distribution.png")

plt.show()

# ==========================================
# VISUALIZATION 2 - PROFIT DISTRIBUTION
# ==========================================

plt.figure(figsize=(8,5))
sns.histplot(df["Profit"], bins=30)

plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("Images/profit_distribution.png")

plt.show()

# ==========================================
# VISUALIZATION 3 - SALES BY CATEGORY
# ==========================================

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar", color="skyblue")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig("Images/category_sales.png")

plt.show()


# ==========================================
# VISUALIZATION 4 - SALES BY REGION
# ==========================================

region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar", color="lightgreen")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig("Images/region_sales.png")

plt.show()


# ==========================================
# VISUALIZATION 5 - SALES BY CUSTOMER SEGMENT
# ==========================================

segment_sales = df.groupby("Segment")["Sales"].sum()

plt.figure(figsize=(8,5))
segment_sales.plot(kind="bar", color="orange")

plt.title("Sales by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig("Images/segment_sales.png")

plt.show()

# ==========================================
# VISUALIZATION 6 - PROFIT BY CATEGORY
# ==========================================

category_profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8,5))
category_profit.plot(kind="bar", color="green")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")

plt.tight_layout()

plt.savefig("Images/category_profit.png")

plt.show()


# ==========================================
# VISUALIZATION 7 - MONTHLY SALES TREND
# ==========================================

df["Order Date"] = pd.to_datetime(df["Order Date"])

df["Month"] = df["Order Date"].dt.to_period("M").astype(str)

monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(12,5))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("Images/monthly_sales.png")

plt.show()

# ==========================================
# VISUALIZATION 8 - TOP 10 PRODUCTS BY SALES
# ==========================================

top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))
top_products.plot(kind="bar", color="purple")

plt.title("Top 10 Products by Sales")
plt.xlabel("Product Name")
plt.ylabel("Total Sales")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("Images/top10_products.png")

plt.show()


# ==========================================
# VISUALIZATION 9 - TOP 10 STATES BY SALES
# ==========================================

top_states = df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
top_states.plot(kind="bar", color="teal")

plt.title("Top 10 States by Sales")
plt.xlabel("State")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("Images/top10_states.png")

plt.show()

# ==========================================
# VISUALIZATION 10 - CORRELATION HEATMAP
# ==========================================

plt.figure(figsize=(8,6))

correlation = df[["Sales", "Profit", "Quantity", "Discount"]].corr()

sns.heatmap(correlation, annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("Images/correlation_heatmap.png")

plt.show()


# ==========================================
# VISUALIZATION 11 - DISCOUNT VS PROFIT
# ==========================================

plt.figure(figsize=(8,6))

plt.scatter(df["Discount"], df["Profit"], alpha=0.5)

plt.title("Discount vs Profit")

plt.xlabel("Discount")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("Images/discount_vs_profit.png")

plt.show()

# ==========================================
# BUSINESS INSIGHTS
# ==========================================

print("\n" + "=" * 60)
print("BUSINESS INSIGHTS")
print("=" * 60)

print(f"\nTotal Sales: ${df['Sales'].sum():,.2f}")
print(f"Total Profit: ${df['Profit'].sum():,.2f}")

top_category = df.groupby("Category")["Sales"].sum().idxmax()
print(f"\nTop Performing Category: {top_category}")

top_region = df.groupby("Region")["Sales"].sum().idxmax()
print(f"Highest Sales Region: {top_region}")

top_segment = df.groupby("Segment")["Sales"].sum().idxmax()
print(f"Highest Revenue Customer Segment: {top_segment}")

top_state = df.groupby("State")["Sales"].sum().idxmax()
print(f"Top State by Sales: {top_state}")

best_product = df.groupby("Product Name")["Sales"].sum().idxmax()
print(f"Best Selling Product: {best_product}")