import gradio as gr
import pandas as pd
import plotly.express as px

# تحميل البيانات الخفيفة
df = pd.read_csv('data cleaning/merging/portfolio_data.csv')

def update_dashboard(state):
    # تصفية البيانات بسرعة
    filtered_df = df[df['customer_state'] == state]
    
    # 1. رسم المبيعات
    fig1 = px.line(filtered_df.groupby('order_purchase_timestamp')['payment_value'].sum().reset_index(), 
                  x='order_purchase_timestamp', y='payment_value', title=f"Sales in {state}")
    
    # 2. رسم التقييمات
    fig2 = px.pie(filtered_df, names='review_score', title="Customer Satisfaction", hole=0.3)
    
    return fig1, fig2

# بناء الواجهة (Interface)
with gr.Blocks(title="Olist Fast Dashboard") as demo:
    gr.Markdown("#Olist E-Commerce Fast Analytics")
    
    with gr.Row():
        state_input = gr.Dropdown(choices=list(df['customer_state'].unique()), 
                                 value="SP", label="Select State")
    
    with gr.Row():
        plot1 = gr.Plot(label="Sales Trend")
        plot2 = gr.Plot(label="Reviews")
    
    # ربط الفلتر بالرسومات
    state_input.change(fn=update_dashboard, inputs=state_input, outputs=[plot1, plot2])
    
    # تشغيل تلقائي عند الفتح
    demo.load(fn=update_dashboard, inputs=state_input, outputs=[plot1, plot2])

demo.launch()
