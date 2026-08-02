import data_cleaning as dc
print(dc.data_geolocation.shape)
print(dc.data_geolocation.head())  
print(dc.data_geolocation.info())
print(dc.data_geolocation.describe())
print(dc.data_geolocation.duplicated().sum())
dc.data_geolocation.drop_duplicates(inplace=True)
print(dc.data_geolocation.duplicated().sum())

geolocation_clean=dc.data_geolocation.groupby('geolocation_zip_code_prefix').agg({
    'geolocation_lat':'mean'
    , 'geolocation_lng':'mean'}).reset_index()