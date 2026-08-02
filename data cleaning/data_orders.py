import data_cleaning as dc
import pandas as pd
print(dc.data_orders.shape)
print(dc.data_orders.head())
print(dc.data_orders.info())
print(dc.data_orders.describe())
print(dc.data_orders.duplicated().sum())
print(dc.data_orders.isnull().sum())
data_columns=['order_purchase_timestamp','order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date']
for col in data_columns:
    dc.data_orders[col]=pd.to_datetime(dc.data_orders[col], format='%Y-%m-%d %H:%M:%S')
dc.data_orders.dropna(subset=['order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date'], inplace=True)
