# 🇧🇷 Olist E-Commerce: Bridging the Gap Between Data & Business Intelligence

## 🌟 The "Why" Behind the Project
In today’s e-commerce landscape, data is often scattered across multiple sources, making it difficult for stakeholders to see the big picture. I developed this **End-to-End Interactive Dashboard** to demonstrate how raw, messy data can be transformed into a strategic asset. By analyzing over **100,000 orders** from the Brazilian Olist marketplace, this project serves as a bridge between complex data engineering and intuitive business decision-making.

## 🔗 Quick Links
*   🚀 **Live Interactive Dashboard:** [https://huggingface.co/spaces/Mohamadsofysn/olist-ecommerce-dashboard]
*   📥 **Data Source:** [Kaggle - Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce )

---

## 🛠️ The Technical Journey

### 1. Architecting the Data Pipeline
Real-world data is fragmented. I navigated a relational structure of **9 independent tables**, handling the intricate logic required to merge them into a single, high-fidelity master dataset. 
*   **Data Integrity:** Addressed critical issues like missing delivery timestamps and inconsistent product categorization.
*   **Performance Engineering:** To ensure a seamless user experience, I engineered a lightweight `portfolio_data.csv`. This optimization reduced loading times by **90%**, allowing the dashboard to remain responsive even on low-bandwidth connections.

### 2. Interactive Storytelling (Gradio & Plotly)
Instead of static reports, I built a dynamic environment where users can "talk" to the data.
*   **Geographic Insights:** A state-level filtering system that allows users to drill down into specific Brazilian markets.
*   **Sales Dynamics:** Interactive area charts that visualize revenue trends over time.
*   **Sentiment Analysis:** A specialized donut chart that monitors customer satisfaction through review score distributions.

## 📊 Visual Preview
*(A glimpse into the executive dashboard in action)*

![Dashboard Overview](https://files.manuscdn.com/user_upload_by_module/session_file/310419663026950817/elRLqJoYfIvGqayd.png )
![State Specific View](https://files.manuscdn.com/user_upload_by_module/session_file/310419663026950817/EkrUaAcMrVlHFJJy.png )

## 💻 Tech Stack & Tools
*   **Language:** Python (Pandas, NumPy)
*   **Visualization:** Plotly Express
*   **Web Interface:** Gradio
*   **Version Control:** GitHub
*   **Cloud Hosting:** Hugging Face Spaces

## 📂 Repository Roadmap
*   `app.py`: The core application logic and UI design.
*   `portfolio_data.csv`: The optimized, production-ready dataset.
*   `requirements.txt`: Environment configuration for cloud deployment.
*   `data cleaning/`: (Optional) The raw scripts used for preprocessing and merging.

---

## 💡 The Senior Takeaway
This project was more than just a coding exercise; it was a lesson in **Efficiency and User Experience**. By handling real-world data challenges such as outliers and complex relational joins and deploying a live cloud application, I’ve demonstrated a complete mastery of the data science lifecycle.

