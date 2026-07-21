"""
===============================================================
Customer Behavior Analysis
===============================================================

Author : Bhavya
Dataset: ecommerce_data.csv

Description:
This script performs statistical analysis on customer behavior
using an e-commerce dataset.

Libraries:
- Pandas
- NumPy
- SciPy

===============================================================
"""

import pandas as pd
import numpy as np


# ===============================================================
# Load Dataset
# ===============================================================

DATA_PATH = "../data/ecommerce_data.csv"

df = pd.read_csv(DATA_PATH)

print("=" * 60)
print("Customer Behavior Analysis")
print("=" * 60)


# ===============================================================
# Dataset Overview
# ===============================================================

print("\nDataset Shape:", df.shape)

print("\nColumns:")

print(df.columns.tolist())

print("\nMissing Values")

print(df.isnull().sum())


# ===============================================================
# Column Names
# ===============================================================

AGE = "Age"
AMOUNT = "Amount Spent"
TIME = "Time Spent on Site"
PURCHASE = "Number of Purchases"
CONVERSION = "Cross-sell Conversion Rate"


# ===============================================================
# Q1
# Range of Customer Age
# ===============================================================

age_range = df[AGE].max() - df[AGE].min()

print("\nQ1. Range of Customer Age")

print(f"Answer : {age_range}")


# ===============================================================
# Q2
# Mean Median Mode
# ===============================================================

mean_amount = df[AMOUNT].mean()

median_amount = df[AMOUNT].median()

mode_amount = df[AMOUNT].mode()[0]

print("\nQ2. Mean, Median and Mode")

print(f"Mean   : {mean_amount:.2f}")

print(f"Median : {median_amount:.2f}")

print(f"Mode   : {mode_amount:.2f}")


# ===============================================================
# Q3
# Variance and Standard Deviation
# ===============================================================

variance = df[TIME].var()

std_dev = df[TIME].std()

print("\nQ3. Variance and Standard Deviation")

print(f"Variance           : {variance:.2f}")

print(f"Standard Deviation : {std_dev:.2f}")


# ===============================================================
# Q4
# Interquartile Range
# ===============================================================

Q1 = df[AMOUNT].quantile(.25)

Q3 = df[AMOUNT].quantile(.75)

IQR = Q3 - Q1

print("\nQ4. Interquartile Range")

print(f"Q1  : {Q1}")

print(f"Q3  : {Q3}")

print(f"IQR : {IQR}")


# ===============================================================
# Q5
# Correlation
# ===============================================================

correlation = df[PURCHASE].corr(df[TIME])

print("\nQ5. Correlation")

print(f"Correlation Coefficient : {correlation:.4f}")

if correlation > 0.7:
    print("Interpretation : Strong Positive Correlation")

elif correlation > 0.3:
    print("Interpretation : Moderate Positive Correlation")

elif correlation < -0.7:
    print("Interpretation : Strong Negative Correlation")

else:
    print("Interpretation : Weak Correlation")


# ===============================================================
# Q6
# Z-score
# ===============================================================

customer_spending = 450

mean = df[AMOUNT].mean()

std = df[AMOUNT].std()

z_score = (customer_spending - mean) / std

print("\nQ6. Z-score")

print(f"Customer Spending : ${customer_spending}")

print(f"Z-score           : {z_score:.3f}")

if z_score > 1:
    print("Interpretation : High-value Customer")

else:
    print("Interpretation : Average Customer")


# ===============================================================
# Q7
# Skewness
# ===============================================================

skewness = df[AMOUNT].skew()

print("\nQ7. Skewness")

print(f"Skewness : {skewness:.3f}")

if skewness > 0:
    print("Distribution : Right Skewed")

elif skewness < 0:
    print("Distribution : Left Skewed")

else:
    print("Distribution : Symmetric")


# ===============================================================
# Q8
# Probability
# Purchases >5 OR Spending >300
# ===============================================================

event_purchase = df[PURCHASE] > 5

event_spending = df[AMOUNT] > 300

probability = (event_purchase | event_spending).mean()

print("\nQ8. Probability")

print(f"P(Purchases >5 OR Spending >300) = {probability:.3f}")


# ===============================================================
# Q9
# Confidence Interval
# ===============================================================

sample_mean = df[AMOUNT].mean()

sample_std = df[AMOUNT].std()

sample_size = len(df)

z = 1.96

margin_error = z * (sample_std / np.sqrt(sample_size))

lower = sample_mean - margin_error

upper = sample_mean + margin_error

print("\nQ9. 95% Confidence Interval")

print(f"Lower Bound : {lower:.2f}")

print(f"Upper Bound : {upper:.2f}")


# ===============================================================
# Q10
# Conditional Probability
# ===============================================================

customers = df[df[PURCHASE] >= 5]

conditional_probability = (
    customers[CONVERSION] > 80
).mean()

print("\nQ10. Conditional Probability")

print(
    "P(Cross-sell Conversion >80% | Purchases >=5)"
)

print(f"Answer : {conditional_probability:.3f}")


# ===============================================================
# Summary
# ===============================================================

print("\n")
print("=" * 60)
print("Summary")
print("=" * 60)

print(f"Age Range                        : {age_range}")

print(f"Mean Amount Spent                : {mean_amount:.2f}")

print(f"Median Amount Spent              : {median_amount:.2f}")

print(f"Mode Amount Spent                : {mode_amount:.2f}")

print(f"Variance (Time Spent)            : {variance:.2f}")

print(f"Standard Deviation               : {std_dev:.2f}")

print(f"Interquartile Range              : {IQR:.2f}")

print(f"Correlation                      : {correlation:.4f}")

print(f"Z-score ($450)                   : {z_score:.3f}")

print(f"Skewness                         : {skewness:.3f}")

print(f"P(Purchases>5 OR Spend>300)      : {probability:.3f}")

print(f"95% Confidence Interval          : ({lower:.2f}, {upper:.2f})")

print(f"P(Conversion>80 | Purchases>=5)  : {conditional_probability:.3f}")

print("=" * 60)
print("Analysis Completed Successfully!")
print("=" * 60)
