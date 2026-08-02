import data_cleaning as dc
print(dc.data_sellers.shape)
print(dc.data_sellers.head())
print(dc.data_sellers.info())
print(dc.data_sellers.describe())
print(dc.data_sellers.duplicated().sum())   