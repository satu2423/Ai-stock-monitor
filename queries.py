KPI_QUERY = """
SELECT
    COUNT(DISTINCT warehouse_name) AS warehouses,
    COUNT(DISTINCT product_name) AS products,
    SUM(CASE WHEN status='CRITICAL' THEN 1 ELSE 0 END) AS critical_items,
    SUM(CASE WHEN status='WARNING' THEN 1 ELSE 0 END) AS warning_items
FROM core.stock_alerts
"""

HEATMAP_QUERY = """
SELECT
    warehouse_name,
    product_name,
    days_left
FROM core.stock_alerts
QUALIFY ROW_NUMBER() OVER (
    PARTITION BY warehouse_name, product_name
    ORDER BY date DESC
) = 1
"""

ALERTS_QUERY = """
SELECT
    warehouse_name,
    product_name,
    ROUND(days_left,1) AS days_left,
    lead_time_days,
    status
FROM core.stock_alerts
WHERE status <> 'OK'
ORDER BY days_left
"""

REORDER_QUERY = """
SELECT * FROM core.reorder_plan
"""
