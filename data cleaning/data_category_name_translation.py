import data_cleaning as dc
print(dc.data_category_name_translation.shape)
print(dc.data_category_name_translation.head())
print(dc.data_category_name_translation.info())
print(dc.data_category_name_translation.describe())
print(dc.data_category_name_translation.duplicated().sum())

