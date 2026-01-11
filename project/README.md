# 📊 PFDA Project: E-Commerce & Consumer Behaviour

This folder contains my Programming for Data Analytics (PFDA) project, focused on analysing consumer behaviour in an e-commerce context using Python, SQL, and basic machine learning techniques.

The project follows data analysis — from raw data to cleaned insights and strategic recommendations.

## **Project Overview**

Customer analytics refers to the systematic analysis of customer data to understand consumer needs, preferences, and behaviours. According to [IBM](https://www.ibm.com/think/topics/customer-analytics), customer analytics enables organisations to leverage data to inform decision-making across functions such as marketing, product development, and customer experience design. By analysing customer interactions and behavioural patterns, businesses can improve engagement, increase sales, and foster long-term customer loyalty.

In an increasingly competitive digital marketplace, customer analytics plays a critical role in enabling organisations to make smarter, faster, and more informed decisions. Data derived from purchase history, demographic profiles, and customer feedback allows businesses to identify what drives value, personalise marketing efforts, and prioritise retention strategies. These insights support the development of more relevant products, more effective advertising campaigns, and improved customer experiences, ultimately contributing to sustained profitability and competitive advantage.

### **Rationale for Dataset Selection**

This dataset was selected because it aligns closely with both the academic objectives of this project and my personal academic background. With a BSc in Marketing and an MSc in Digital Marketing, specialising in strategy, I am particularly interested in translating data into actionable insights that support decision-making and competitive advantage.

Beyond technical analysis, I am motivated by understanding *why* consumers make the decisions they do. This dataset provides an opportunity to explore behavioural drivers of purchasing, assess engagement across channels, and apply predictive techniques to anticipate future outcomes. It therefore supports both descriptive and analytical objectives, as well as the development of strategic recommendations grounded in data.

### **Research Objectives**

The primary objectives of this project are to:

 - Profile customers based on demographic characteristics

 - Examine purchasing habits and behavioural drivers

 - Identify channel, device, and payment preferences

 - Analyse geographic and seasonal purchasing patterns

 - Evaluate customer satisfaction and loyalty indicators

 - Apply predictive models to quantify drivers of purchase value


 ### **Data Source:**

The dataset used in this project is the *Customer Shopping Trends Dataset*, obtained from [Kaggle](https://www.kaggle.com/datasets/iamsouravbanerjee/customer-shopping-trends-dataset). It contains customer-level data including demographic attributes, purchasing behaviour, engagement metrics, and satisfaction indicators.

## **🔍 What’s Covered in the Analysis?**

 * 📥 Data acquisition and inspection

 * 🧹 Data cleaning and preprocessing

 * 📊 Exploratory Data Analysis (EDA)

 * 🌍 Geographic analysis using offline city-to-country mapping

 * 🗄️ SQL database creation and querying (SQLite)

 * 🤖 Machine learning:

     * Linear Regression (baseline, interpretable)

     * Random Forest Regression (non-linear comparison)

 * 📈 Strategic insights for marketing and customer segmentation

 * ⚠️ Research limitations and assumptions
 

## **Modelling notes**

 * Models are explanatory, not production-grade predictors

 * Low R² values are expected due to:

     * High variability in transaction-level spending

     * Missing external factors (pricing, promotions, economics)

  * Models are used to:

    * Identify directional relationships

    * Support segmentation and targeting decisions

 ## 📌 **Key EDA Insights**

 * The customer base is predominantly young to middle-aged (average age ≈ 34).

 * Younger customers (18–25) exhibit higher spending variability and responsiveness.

 * Purchase intent is a strong indicator of transaction value.

 * Mobile and social-media-influenced users dominate purchasing behaviour.

 * Digital payments are associated with higher transaction values.

 * Seasonal patterns show revenue peaks in spring and summer.

## ⚠️ **Limitations (Summary)**

 * Partial geographic coverage due to offline city-to-country mapping

 * Data represents a single snapshot in time

 * Customers appear to be repeat purchasers only

 * Limited behavioural and external variables

 * Results should be interpreted within scope

*Full limitations and references are documented in **Section 8** of the notebook.*

## 🛠️Tools & Technologies

* **Python:** pandas, numpy, matplotlib, seaborn, plotly

* **SQL:** SQLite (sqlite3)

* **Machine Learning:** scikit-learn

* **Geolocation:** geonamescache (offline mapping)

* **Environment:** Jupyter Notebook


## 📁 **Installation:**

1. **Clone the repository:**

   ```
   git clone https://github.com/marianemcgrath/pfda.git

2. **Navigate to the project folder:**

   ```
   cd pfda/project

3. **Install required libraries:**

    ```
    pip install -r requirements.txt

4. **Launch the notebook:**

    ```
    jupyter notebook project/project.ipynb

📌 *All visualisations are automatically saved to the plots/ directory*

#### 👩‍💻 **About the Analyst:**

**Mariane McGrath**

[Email](marianemcgrath@gmail.com)

[LinkedIn](https://www.linkedin.com/in/marianemcgrath/)

## 📄 **License**

This project was completed as part of the *Programming for Data Analysis* module at *ATU Galway-Mayo*.

**Lecturer:** Andrew Beatty

**Date:** January 2026

☕ **Final Note**

This README was brought to you by a Frankeinstein of AI suggestions (ChatGPT, DeepSeek & Grok), a looming deadline, 567 cups of coffee, 4 all-nighters and the haunting fear that someone might read all this.