import data_cleaning as dc
print(dc.data_order_payments.shape)
print(dc.data_order_payments.head())
print(dc.data_order_payments.info())
print(dc.data_order_payments.describe())
print(dc.data_order_payments.duplicated().sum())
payments_grouped= dc.data_order_payments.groupby('order_id').agg({
    'payment_installments':'max'
    , 'payment_value':'sum'}).reset_index()