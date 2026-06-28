import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---- Load CSVs ----
category_df = pd.read_csv("category_revenue.csv")
monthly_df = pd.read_csv("monthly_trend.csv")
region_df = pd.read_csv("region_performance.csv")
products_df = pd.read_csv("top_products.csv")

# ---- Plot Style ----
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle("E-Commerce Sales Analysis", fontsize=18, fontweight='bold')

# ---- Chart 1: Category Revenue (Pie) ----
axes[0, 0].pie(
    category_df['total_revenue'],
    labels=category_df['category'],
    autopct='%1.1f%%',
    startangle=90
)
axes[0, 0].set_title("Revenue by Category")

# ---- Chart 2: Monthly Trend (Line) ----
axes[0, 1].plot(
    monthly_df['month'],
    monthly_df['monthly_revenue'],
    marker='o', color='steelblue', linewidth=2
)
axes[0, 1].set_title("Monthly Revenue Trend")
axes[0, 1].set_xlabel("Month")
axes[0, 1].set_ylabel("Revenue")
axes[0, 1].tick_params(axis='x', rotation=45)

# ---- Chart 3: Region Performance (Bar) ----
sns.barplot(
    data=region_df,
    x='region',
    y='total_revenue',
    palette='Blues_d',
    ax=axes[1, 0]
)
axes[1, 0].set_title("Revenue by Region")
axes[1, 0].set_xlabel("Region")
axes[1, 0].set_ylabel("Revenue")

# ---- Chart 4: Top Products (Horizontal Bar) ----
sns.barplot(
    data=products_df,
    x='total_revenue',
    y='product_name',
    palette='Oranges_d',
    ax=axes[1, 1]
)
axes[1, 1].set_title("Top 5 Products by Revenue")
axes[1, 1].set_xlabel("Revenue")
axes[1, 1].set_ylabel("")

plt.tight_layout()
plt.savefig("eda_dashboard.png", dpi=150, bbox_inches='tight')
plt.show()
print("✅ EDA complete! Chart saved as eda_dashboard.png")