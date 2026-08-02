# 🛍️ Brazilian E-Commerce Analytics Dashboard

[![Live Demo](https://huggingface.co/spaces/Mohamadsofysn/olist-ecommerce-dashboard)](https://huggingface.co/Mohamadsofysn)

## 👋 Hello! Welcome to my project.
I built this end-to-end data analysis and visualization project using the **Brazilian E-Commerce Public Dataset by Olist**. I worked on the foundational stages with a former colleague, and I recently took the project across the finish line by optimizing the data and deploying this interactive web dashboard. 

My main goal was to take raw, messy relational data and turn it into a fast, interactive tool that shows real business insights like sales trends and customer satisfaction.

## 🧠 My Process & How I Built It

### 1. Data Cleaning
I started with 9 raw datasets from Kaggle. I cleaned them by handling missing values strategically (e.g., assigning 'unknown' to missing categorical data and 'No Comment' to blank reviews) and dropping incomplete orders to make sure the data was solid.

### 2. Feature Engineering
To make the data actually useful for analysis, I:
* Converted all date strings into proper `Datetime` objects.
* Calculated a new `delivery_time` feature (in days).
* Capped outliers in product weights and dimensions so they wouldn't skew the visualizations.

### 3. Data Merging & The Memory Challenge
I merged all 9 tables into one massive master dataset (`final_master_dataset.csv`). However, when I tried to plug this huge file into my dashboard, I ran into a strict `MemoryError`. 

**The Solution:** Instead of giving up, I optimized the pipeline. I extracted a lightweight version called `portfolio_data.csv` that contains *only* the specific columns needed for the charts. This reduced the memory footprint by over 90% and made the dashboard load instantly.

### 4. Dashboard Development
I built the front-end using **Gradio** and **Plotly Express**. The dashboard allows users to select different Brazilian states from a dropdown menu and instantly see the sales trends and review scores for that specific region.

## 🛠️ Tech Stack
* **Data Processing:** Python, Pandas, NumPy
* **Data Visualization:** Plotly Express
* **Web App & Deployment:** Gradio, Hugging Face Spaces

## 📁 What's in this Repository?
I didn't upload the 9 original heavy datasets to keep the repo clean. Here is what you'll find:
* `data_cleaning.py`, `merging_tables.py`, `reduce_data.py`, etc.: The scripts showing my exact logic for cleaning and wrangling the data.
* `portfolio_data.csv`: The optimized, lightweight dataset powering the dashboard.
* `app.py`: The main script that runs the Gradio interface.
* `requirements.txt`: The dependencies needed to run the app.

## 💻 How to Run It Locally
If you want to run this on your own machine:

1. Clone this repository:
   ```bash
   git clone <YOUR_GITHUB_REPO_LINK_HERE>
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
3. Run the dashboard:
   ```bash
   python app.py   