# 🛒 Customer Behavior Analysis

## 📌 Project Overview

This project analyzes customer behavior using an e-commerce dataset. The objective is to perform descriptive statistics, probability analysis, correlation analysis, confidence interval estimation, and distribution analysis to gain insights into customer purchasing patterns.

The project is implemented entirely in **Python** using **Pandas**, **NumPy**, and **SciPy**.

---

## 🎯 Objectives

The analysis answers the following business questions:

1. Calculate the range of customer age.
2. Determine the mean, median, and mode of customer spending.
3. Compute the variance and standard deviation of time spent on the website.
4. Calculate the Interquartile Range (IQR) of customer spending.
5. Determine the relationship between the number of purchases and time spent on the website.
6. Calculate the z-score for a customer spending \$450.
7. Analyze the skewness of customer spending.
8. Compute the probability that a customer makes more than five purchases or spends more than \$300.
9. Calculate the 95% confidence interval for average customer spending.
10. Determine the probability that customers with at least five purchases have a cross-sell conversion rate greater than 80%.

---

## 📂 Dataset

Dataset used:

```
ecommerce_data.csv
```

The dataset contains customer information including:

| Column | Description |
|---------|-------------|
| Customer ID | Unique customer identifier |
| Age | Customer age |
| Amount Spent | Total amount spent |
| Time Spent on Site | Time spent browsing the website |
| Number of Purchases | Monthly purchases |
| Cross-sell Conversion Rate | Percentage of successful cross-sell conversions |

---

## 🛠 Technologies Used

- Python 3.x
- Pandas
- NumPy
- SciPy
- Jupyter Notebook

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/customer-behavior-analysis.git
```

Move inside the project

```bash
cd customer-behavior-analysis
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Run the Python script

```bash
python src/customer_behavior_analysis.py
```

or open the notebook

```bash
jupyter notebook
```

and execute

```
Customer_Behavior_Analysis.ipynb
```

---

## 📊 Statistical Analysis Performed

### Descriptive Statistics

- Mean
- Median
- Mode
- Variance
- Standard Deviation
- Range
- Interquartile Range (IQR)

---

### Correlation Analysis

Pearson Correlation was used to determine the relationship between

- Number of Purchases
- Time Spent on Site

---

### Probability Analysis

The following probabilities were computed:

- Purchase > 5 OR Amount Spent > \$300
- Cross-sell Conversion Rate > 80% given Purchases ≥ 5

---

### Confidence Interval

A 95% confidence interval was calculated for average customer spending using

- Sample Mean
- Sample Standard Deviation
- Z Critical Value (1.96)

---

### Distribution Analysis

The distribution of customer spending was analyzed using

- Skewness

Interpretation:

- Positive Skew → Right Skewed
- Negative Skew → Left Skewed

---

## 📈 Sample Output

```
Age Range: 47

Mean Spending: 238.23

Median Spending: 200.00

Mode Spending: 240.00

Variance(Time Spent): 277.78

Standard Deviation(Time Spent): 16.67

IQR: 200

Correlation: 0.9376

Z-score (450): 1.358

Skewness: 0.958

Probability (>5 Purchases OR Spending >300): 0.396

95% Confidence Interval:
(228.56, 247.90)

Probability(Purchases>=5 and Conversion>80):
0.351
```

---

## 📁 Project Structure

```
Customer-Behavior-Analysis
│
├── data
│   └── ecommerce_data.csv
│
├── notebooks
│   └── Customer_Behavior_Analysis.ipynb
│
├── src
│   └── customer_behavior_analysis.py
│
├── outputs
│   ├── summary_results.csv
│   └── analysis_report.txt
│
├── images
│
├── README.md
├── requirements.txt
└── LICENSE
```

---

## 📚 Python Libraries

```python
import pandas as pd
import numpy as np
from scipy.stats import skew
```

---

## 🚀 Future Improvements

- Interactive Dashboard using Streamlit
- Data Visualization using Matplotlib and Seaborn
- Customer Segmentation
- Predictive Analytics using Machine Learning
- Automated Report Generation

---

## 👨‍💻 Author

**Vijay Kumar Subramanian**

Customer Behavior Analysis Project

Built using Python, Pandas, NumPy and SciPy.

---
