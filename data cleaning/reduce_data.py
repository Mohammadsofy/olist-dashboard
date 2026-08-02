import pandas as pd
import time

start_time = time.time()

# 1. تحديد الأعمدة المطلوبة فقط لتقليل استهلاك الذاكرة والوقت
cols_to_read = ['order_purchase_timestamp', 'order_delivered_customer_date', 
                'payment_value', 'review_score', 'product_category_name_english', 'customer_state']

# 2. قراءة الملف مع تحديد الأعمدة المطلوبة فقط
df = pd.read_csv('data cleaning/merging/final_master_dataset.csv', usecols=cols_to_read)

# 3. تحويل التواريخ مع تحديد التنسيق (Format) لجعلها سريعة جداً
date_format = '%Y-%m-%d %H:%M:%S'
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'], format=date_format, errors='coerce')
df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'], format=date_format, errors='coerce')

# 4. حذف أي صفوف بها تواريخ خاطئة أو مفقودة
df = df.dropna(subset=['order_delivered_customer_date', 'order_purchase_timestamp'])

# 5. حساب مدة التوصيل
df['delivery_time'] = (df['order_delivered_customer_date'] - df['order_purchase_timestamp']).dt.days

# 6. حفظ الملف الخفيف
df.to_csv('data cleaning/merging/portfolio_data.csv', index=False)

