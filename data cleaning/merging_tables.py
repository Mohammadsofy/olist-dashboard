
import data_cleaning as dc
import pandas as pd

master_df1 = pd.merge(dc.data_orders, dc.data_order_items, on='order_id', how='left')
master_df1.to_csv("data cleaning/merging/master_df1.csv", index=False)
master_df2 = pd.merge(master_df1, dc.data_order_payments, on='order_id', how='left')
master_df2.to_csv("data cleaning/merging/master_df2.csv", index=False)
master_df3 = pd.merge(master_df2, dc.data_products, on='product_id', how='left')
master_df3.to_csv("data cleaning/merging/master_df3.csv", index=False)
master_df4= pd.merge(master_df3, dc.data_customers, on='customer_id', how='left')
master_df4.to_csv("data cleaning/merging/master_df4.csv", index=False)
master_df5= pd.merge(master_df4, dc.data_sellers, on='seller_id', how='left')
master_df5.to_csv("data cleaning/merging/master_df5.csv", index=False)
master_df6= pd.merge(master_df5, dc.data_category_name_translation, on='product_category_name', how='left')
master_df6.to_csv("data cleaning/merging/master_df6.csv", index=False)
master_df7 = pd.merge(master_df6, dc.data_order_reviews, on='order_id', how='left')
master_df7.to_csv("data cleaning/merging/master_df7.csv", index=False)
master_df_final = pd.merge(master_df7, dc.data_geolocation, left_on='customer_zip_code_prefix', right_on='geolocation_zip_code_prefix', how='left')
master_df_final.to_csv("data cleaning/merging/final_master_dataset.csv", index=False)



