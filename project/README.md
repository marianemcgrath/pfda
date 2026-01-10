# 🛍️ Consumer Behaviour Analysis in an E-Commerce Context

## **1. Project Overview**

Customer analytics refers to the systematic analysis of customer data to understand consumer needs, preferences, and behaviours. According to [IBM](https://www.ibm.com/think/topics/customer-analytics), customer analytics enables organisations to leverage data to inform decision-making across functions such as marketing, product development, and customer experience design. By analysing customer interactions and behavioural patterns, businesses can improve engagement, increase sales, and foster long-term customer loyalty.

In an increasingly competitive digital marketplace, customer analytics plays a critical role in enabling organisations to make smarter, faster, and more informed decisions. Data derived from purchase history, demographic profiles, and customer feedback allows businesses to identify what drives value, personalise marketing efforts, and prioritise retention strategies. These insights support the development of more relevant products, more effective advertising campaigns, and improved customer experiences, ultimately contributing to sustained profitability and competitive advantage.

### **2. Rationale for Dataset Selection**

This dataset was selected because it aligns closely with both the academic objectives of this project and my personal academic background. With a BSc in Marketing and an MSc in Digital Marketing, specialising in strategy, I am particularly interested in translating data into actionable insights that support decision-making and competitive advantage.

Beyond technical analysis, I am motivated by understanding *why* consumers make the decisions they do. This dataset provides an opportunity to explore behavioural drivers of purchasing, assess engagement across channels, and apply predictive techniques to anticipate future outcomes. It therefore supports both descriptive and analytical objectives, as well as the development of strategic recommendations grounded in data.

### **3. Research Objectives**

The primary objectives of this project are to:

 - Profile customers based on demographic characteristics

 - Examine purchasing habits and behavioural drivers

 - Identify channel, device, and payment preferences

 - Analyse geographic and seasonal purchasing patterns

 - Evaluate customer satisfaction and loyalty indicators

 - Apply predictive models to quantify drivers of purchase value

 - These objectives align with common applications of customer analytics in digital marketing and e-commerce strategy.

 ### **4. Data Source:**

The dataset used in this project is the *Customer Shopping Trends Dataset*, obtained from [Kaggle](https://www.kaggle.com/datasets/iamsouravbanerjee/customer-shopping-trends-dataset). It contains customer-level data including demographic attributes, purchasing behaviour, engagement metrics, and satisfaction indicators.

**Main Features:**

 - Customer demographics (age, gender, location)

 - Purchase behaviour and intent

 - Engagement with advertising and social media

 - Payment methods and device usage

 - Loyalty programme participation and satisfaction


 ### **5. Key EDA Insights**

 - The customer base is predominantly young to middle-aged, with an average age of approximately 34 years and the majority of customers falling within the 18–45 age range. This indicates that the platform primarily attracts working-age consumers.

 - Spending behaviour varies by age group, with younger customers (18–25) exhibiting the highest average purchase values and greater variability in spending. This suggests stronger responsiveness to product offerings and promotional stimuli among younger segments.

 - Gender differences in purchase amount are present but relatively modest. Compared to age and behavioural variables, gender appears to be a secondary factor in explaining spending behaviour.

 - Purchase intent is a strong behavioural indicator of transaction value. Need-based and impulsive purchases show the widest distribution and highest outliers, indicating that both necessity-driven and spontaneous decisions can lead to high-value transactions.

 - Discount usage is common across all demographic groups; however, no strong relationship was observed between discount usage and customer satisfaction or spending levels. This suggests that discounts alone may not significantly influence long-term value or perceived satisfaction.

 - Channel and device analysis highlights a strong digital and mobile preference. Smartphone and tablet users display higher levels of social media influence, particularly among younger age groups, reinforcing the importance of mobile-first and social-media-driven marketing strategies.

 - Payment behaviour is dominated by digital payment methods, with PayPal and credit cards accounting for the highest transaction volumes and revenue. Cash payments are associated with lower average purchase amounts, suggesting higher-value transactions are more likely to occur through digital channels.

 - Revenue is geographically concentrated within a small number of countries. Among these top markets, average brand loyalty varies significantly, indicating that some regions demonstrate stronger long-term customer engagement while others rely more heavily on transactional purchasing behaviour.

 - Temporal analysis reveals clear seasonal purchasing patterns, with both transaction volume and revenue peaking during spring and summer months and declining toward the end of the year. Higher revenue periods are primarily driven by increased transaction volume rather than higher average order values.

 - Overall, the exploratory analysis indicates that purchase value is influenced by a combination of demographic, behavioural, channel-related, and geographic factors, providing a strong foundation for predictive modelling to quantify the relative importance of these drivers.

## 📁 **6. Repository Structure**

'''

pfda/
├── data/                # Raw and cleaned datasets
├── project.ipynb        # Main analysis notebook
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
└── .gitignore


## **7. Tools & Technologies**

The analysis was conducted using Python within a Jupyter Notebook environment. The following libraries were used:

 - pandas — data manipulation and cleaning

 - NumPy — numerical operations

 - matplotlib & seaborn — data visualisation

 - plotly — interactive visualisations

 - scikit-learn — machine learning models

 - SQLite (sqlite3) — database integration and SQL analysis

### **8. Installation:**

1. **Clone this magical repository:**

   ```
   git clone https://github.com/marianemcgrath/pfda.git

   cd pfda/project

2. **Install required packages:**

    ```
    pip install -r requirements.txt

3. **Launch the notebook:**

    ```
    jupyter notebook project.ipynb








#### 👩‍💻 About the Analyst

**Mariane McGrath**
Data Detective & Consumer Whisperer

🔍 Uncovering patterns

📊 Transforming data into decisions

🎯 Making numbers tell stories

### ⭐ Show Some Love!

If this project gave you a better understanding of Consumer Behaviour:

- Give it a star on GitHub!

- Share with fellow data enthusiasts!

### 🤝 Collaboration

Found a bug? Have an idea? Want to collaborate?

**Reach out**

[Email](marianemcgrath@gmail.com)

[LinkedIn](https://www.linkedin.com/in/marianemcgrath/)

## 9. License

This project was completed as part of the *Programming for Data Analysis* module at *ATU Galway-Mayo*.

**Lecturer:** Andrew Beatty

**Date:** January 2026
