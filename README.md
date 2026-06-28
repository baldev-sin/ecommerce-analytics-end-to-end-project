# 🛒 E-Commerce Sales Analytics Project

An end-to-end data analytics project using **PostgreSQL**, **Python**, and **Tableau Public** to analyze e-commerce sales data and derive actionable business insights.

---

## 📌 Project Overview

This project simulates a real-world e-commerce analytics pipeline — from raw data generation to an interactive dashboard. It covers data storage, SQL querying, Python-based EDA, and Tableau visualization.

**Business Questions Answered:**
- Which product categories generate the most revenue?
- What does the monthly sales trend look like?
- Which regions perform best?
- What are the top 5 products by revenue?

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| PostgreSQL | Database storage and SQL querying |
| Python (Pandas, Matplotlib, Seaborn, Faker) | Data generation, cleaning, and EDA |
| Tableau Public | Interactive dashboard |

---

## 📁 Project Structure

```
ecommerce_project/
│
├── load_data.py          # Generates and loads fake data into PostgreSQL
├── export_csv.py         # Exports SQL query results to CSV files
├── eda.py                # EDA and chart generation
│
├── category_revenue.csv  # Revenue by product category
├── monthly_trend.csv     # Monthly sales trend
├── region_performance.csv# Revenue by region
├── top_products.csv      # Top 5 products by revenue
│
└── eda_dashboard.png     # Python-generated EDA charts
```

---

## 🗄️ Database Schema

```
customers       → customer_id, name, city, region, signup_date
products        → product_id, name, category, sub_category, unit_price
orders          → order_id, customer_id, order_date, ship_date, shipping_mode
order_items     → item_id, order_id, product_id, quantity, discount, sale_price
```

**Dataset Size:**
- 500 customers
- 20 products across 6 categories
- 2,000 orders
- ~4,000 order items

---

## 🔍 SQL Analysis

**4 key business queries written:**

1. **Category Revenue** — with window functions to calculate revenue percentage
2. **Monthly Trend** — using `TO_CHAR` for date formatting and aggregation
3. **Region Performance** — revenue per customer analysis across 4 regions
4. **Top 5 Products** — ranked by total revenue

---

## 📊 Key Insights

- **Electronics dominates** with 76.4% of total revenue
- **West region** has the highest total revenue
- **South region** has the highest revenue per customer despite fewer customers
- **October and March** consistently show revenue spikes

---

## 📈 Tableau Dashboard

🔗 [View Live Dashboard](https://public.tableau.com/app/profile/baldev.singh6124/viz/E-commerceAnalysis_17826547197490/Dashboard1)

Dashboard includes:
- Monthly Revenue Trend (Line Chart)
- Revenue by Category (Pie Chart)
- Region Performance (Bar Chart)
- Top 5 Products (Horizontal Bar Chart)

---

## 🚀 How to Run

### 1. Setup PostgreSQL Database
```sql
CREATE DATABASE ecommerce_analytics;
```

### 2. Install Python Dependencies
```bash
pip install psycopg2-binary faker pandas matplotlib seaborn
```

### 3. Load Data
```bash
python load_data.py
```

### 4. Export CSVs
```bash
python export_csv.py
```

### 5. Run EDA
```bash
python eda.py
```

---

## 👤 Author

**Baldev Singh**  
[Tableau Public Profile](https://public.tableau.com/app/profile/baldev.singh6124)
