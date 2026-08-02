import pandas as pd
import numpy as np
data_customers=pd.read_csv(r"olist_customers_dataset.csv")
data_geolocation=pd.read_csv(r"olist_geolocation_dataset.csv")
data_order_items=pd.read_csv(r"olist_order_items_dataset.csv")
data_order_payments=pd.read_csv(r"olist_order_payments_dataset.csv")
data_order_reviews=pd.read_csv(r"olist_order_reviews_dataset.csv")
data_orders=pd.read_csv(r"olist_orders_dataset.csv")
data_products=pd.read_csv(r"olist_products_dataset.csv")
data_sellers=pd.read_csv(r"olist_sellers_dataset.csv")
data_category_name_translation=pd.read_csv(r"product_category_name_translation.csv")

# print("----------------- data customers ------------------")
# print(data_customers.shape)
# print(data_customers.head())
# print(data_customers.info())
# print(data_customers.describe())
# print(data_customers.duplicated().sum())

# print("----------------- data geolocation ------------------")
# print(data_geolocation.shape)
# print(data_geolocation.head())  
# print(data_geolocation.info())
# print(data_geolocation.describe())
# print(data_geolocation.duplicated().sum())
# data_geolocation.drop_duplicates(inplace=True)
# print(data_geolocation.duplicated().sum())

# print("----------------- data order items ------------------")
# print(data_order_items.shape)
# print(data_order_items.head())
# print(data_order_items.info())
# print(data_order_items.describe())
# print(data_order_items.duplicated().sum())

# print("----------------- data order payments ------------------")
# print(data_order_payments.shape)
# print(data_order_payments.head())
# print(data_order_payments.info())
# print(data_order_payments.describe())
# print(data_order_payments.duplicated().sum())
# payments_grouped= data_order_payments.groupby('order_id').agg({
#     'payment_installments':'max'
#     , 'payment_value':'sum'}).reset_index()

# print("----------------- data order reviews ------------------")
# print(data_order_reviews.shape)
# print(data_order_reviews.head())
# print(data_order_reviews.info())
# print(data_order_reviews.describe())
# print(data_order_reviews.duplicated().sum())
# print(data_order_reviews.isnull().sum())


# print("----------------- data orders ------------------")
# print(data_orders.shape)
# print(data_orders.head())
# print(data_orders.info())
# print(data_orders.describe())
# print(data_orders.duplicated().sum())
# print(data_orders.isnull().sum())
# data_columns=['order_purchase_timestamp','order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date']
# for col in data_columns:
#     data_orders[col]=pd.to_datetime(data_orders[col], format='%Y-%m-%d %H:%M:%S')
# data_orders.dropna(subset=['order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date'], inplace=True)

# print("----------------- data products ------------------")
# print(data_products.shape)
# print(data_products.head())
# print(data_products.info())
# print(data_products.describe())
# print(data_products.duplicated().sum())
# print(data_products.isnull().sum())
# data_products["product_category_name"].fillna("others", inplace=True)
# mode_missing= ['product_name_lenght', 'product_description_lenght', 'product_photos_qty']
# for col in mode_missing:
#     data_products[col].fillna(data_products[col].mode()[0], inplace=True)
# remove_missing= ['product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm']
# for col in remove_missing:
#     data_products.drop(data_products[data_products[col].isnull()].index, inplace=True)

# print(data_products.isnull().sum())
# columns_numeric=['product_name_lenght', 'product_description_lenght', 'product_photos_qty','product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm']
# for col in columns_numeric:
#     Q1=data_products[col].quantile(0.25)
#     Q3=data_products[col].quantile(0.75)
#     IQR=Q3-Q1
#     lower_bound=Q1-1.5*IQR
#     upper_bound=Q3+1.5*IQR
#     outliers=data_products[(data_products[col]<lower_bound) | (data_products[col]>upper_bound)]
#     print(f"Number of outliers in {col}: {len(outliers)}")

# print("----------------- data sellers ------------------")
# print(data_sellers.shape)
# print(data_sellers.head())
# print(data_sellers.info())
# print(data_sellers.describe())
# print(data_sellers.duplicated().sum())   

# print("----------------- data category name translation ------------------")
# print(data_category_name_translation.shape)
# print(data_category_name_translation.head())
# print(data_category_name_translation.info())
# print(data_category_name_translation.describe())
# print(data_category_name_translation.duplicated().sum())

