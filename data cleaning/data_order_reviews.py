import data_cleaning as dc
import pandas as pd
print(dc.data_order_reviews.shape)
print(dc.data_order_reviews.head())
print(dc.data_order_reviews.info())
print(dc.data_order_reviews.describe())
print(dc.data_order_reviews.duplicated().sum())
print(dc.data_order_reviews.isnull().sum())
dc.data_order_reviews['review_creation_date'] =pd.to_datetime(dc.data_order_reviews['review_creation_date'])
dc.data_order_reviews['review_answer_timestamp'] =pd.to_datetime(dc.data_order_reviews['review_answer_timestamp'])

dc.data_order_reviews['review_comment_message'].fillna('No comment')
dc.data_order_reviews['review_comment_title'].fillna('No title')

