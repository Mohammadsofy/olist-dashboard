import data_cleaning as dc

print(dc.data_products.shape)
print(dc.data_products.head())
print(dc.data_products.info())
print(dc.data_products.describe())
print(dc.data_products.duplicated().sum())
print(dc.data_products.isnull().sum())
dc.data_products["product_category_name"].fillna("others", inplace=True)
mode_missing= ['product_name_lenght', 'product_description_lenght', 'product_photos_qty']
for col in mode_missing:
    dc.data_products[col].fillna(dc.data_products[col].mode()[0], inplace=True)
remove_missing= ['product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm']
for col in remove_missing:
    dc.data_products.drop(dc.data_products[dc.data_products[col].isnull()].index, inplace=True)

print(dc.data_products.isnull().sum())

