import data_cleaning as dc
print(dc.data_order_items.shape)
print(dc.data_order_items.head())
print(dc.data_order_items.info())
print(dc.data_order_items.describe())
print(dc.data_order_items.duplicated().sum())