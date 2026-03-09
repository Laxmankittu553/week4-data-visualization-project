import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data/sales_data.csv")

print("\n--- DATA PREVIEW ---")
print(data.head())

# Calculate statistics
total_sales = data["Total_Sales"].sum()
average_sales = data["Total_Sales"].mean()

print("\nTotal Sales:", total_sales)
print("Average Sales:", average_sales)

# Best selling product
best_product = data.groupby("Product")["Quantity"].sum()
print("\nBest Selling Products:")
print(best_product)

# ----- Visualization 1 -----
plt.figure(figsize=(8,5))
best_product.plot(kind="bar")
plt.title("Product Sales Comparison")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.tight_layout()

plt.savefig("visualizations/product_sales_chart.png")

# ----- Visualization 2 -----
sales_by_product = data.groupby("Product")["Total_Sales"].sum()

plt.figure(figsize=(8,5))
sales_by_product.plot(kind="pie", autopct='%1.1f%%')
plt.title("Sales Distribution by Product")
plt.ylabel("")

plt.savefig("visualizations/sales_distribution_pie.png")

print("\nCharts saved in visualizations folder.")