import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="ecommerce_analytics",
    user="postgres",
    password="postgres123"
)

queries = {
    "category_revenue": """
        SELECT p.category,
               COUNT(DISTINCT o.order_id) AS total_orders,
               ROUND(SUM(oi.sale_price)::numeric, 2) AS total_revenue,
               ROUND(SUM(oi.sale_price)::numeric / SUM(SUM(oi.sale_price)::numeric) OVER() * 100, 2) AS revenue_percentage
        FROM order_items oi
        JOIN orders o ON oi.order_id = o.order_id
        JOIN products p ON oi.product_id = p.product_id
        GROUP BY p.category
        ORDER BY total_revenue DESC
    """,
    "monthly_trend": """
        SELECT TO_CHAR(o.order_date, 'YYYY-MM') AS month,
               COUNT(DISTINCT o.order_id) AS total_orders,
               ROUND(SUM(oi.sale_price)::numeric, 2) AS monthly_revenue
        FROM orders o
        JOIN order_items oi ON o.order_id = oi.order_id
        GROUP BY TO_CHAR(o.order_date, 'YYYY-MM')
        ORDER BY month
    """,
    "region_performance": """
        SELECT c.region,
               COUNT(DISTINCT o.order_id) AS total_orders,
               COUNT(DISTINCT c.customer_id) AS unique_customers,
               ROUND(SUM(oi.sale_price)::numeric, 2) AS total_revenue,
               ROUND(SUM(oi.sale_price)::numeric / COUNT(DISTINCT c.customer_id), 2) AS revenue_per_customer
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        JOIN order_items oi ON o.order_id = oi.order_id
        GROUP BY c.region
        ORDER BY total_revenue DESC
    """,
    "top_products": """
        SELECT p.product_name, p.category,
               SUM(oi.quantity) AS total_units_sold,
               ROUND(SUM(oi.sale_price)::numeric, 2) AS total_revenue
        FROM order_items oi
        JOIN products p ON oi.product_id = p.product_id
        GROUP BY p.product_name, p.category
        ORDER BY total_revenue DESC
        LIMIT 5
    """
}

for filename, query in queries.items():
    df = pd.read_sql(query, conn)
    df.to_csv(f"{filename}.csv", index=False)
    print(f"✅ {filename}.csv saved")

conn.close()