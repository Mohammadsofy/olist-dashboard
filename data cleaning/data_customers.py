import data_cleaning as dc
print(dc.data_customers.shape)
print(dc.data_customers.head())
print(dc.data_customers.info())
print(dc.data_customers.describe())
print(dc.data_customers.duplicated().sum())
