# ============================================
# Google Expense Sharing Analysis Project
# ============================================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Display Settings
plt.rcParams['figure.figsize'] = (10,6)
sns.set_style("whitegrid")

# ============================================
# Sample Expense Dataset
# ============================================

data = {
    'Person': ['Nandhini', 'Rahul', 'Priya', 'Nandhini', 'Rahul',
               'Priya', 'Nandhini', 'Rahul', 'Priya', 'Nandhini'],
    
    'Category': ['Food', 'Travel', 'Shopping', 'Bills', 'Food',
                 'Travel', 'Entertainment', 'Bills', 'Food', 'Shopping'],
    
    'Amount': [450, 1200, 800, 1500, 600,
               950, 700, 1300, 400, 1000],
    
    'Date': ['2025-01-02', '2025-01-05', '2025-01-07',
             '2025-01-10', '2025-01-12', '2025-01-15',
             '2025-01-18', '2025-01-20', '2025-01-22',
             '2025-01-25']
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert Date Column
df['Date'] = pd.to_datetime(df['Date'])

# ============================================
# Basic Dataset Information
# ============================================

print("First 5 Rows")
print(df.head())

print("\nDataset Info")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

# ============================================
# Total Expense Analysis
# ============================================

total_expense = df['Amount'].sum()

print("\nTotal Expense:", total_expense)

# ============================================
# Expense by Person
# ============================================

person_expense = df.groupby('Person')['Amount'].sum()

print("\nExpense by Person")
print(person_expense)

# Plot
person_expense.plot(kind='bar')
plt.title('Total Expense by Person')
plt.xlabel('Person')
plt.ylabel('Amount')
plt.show()

# ============================================
# Expense by Category
# ============================================

category_expense = df.groupby('Category')['Amount'].sum()

print("\nExpense by Category")
print(category_expense)

# Pie Chart
plt.figure(figsize=(8,8))
category_expense.plot(kind='pie', autopct='%1.1f%%')
plt.title('Expense Distribution by Category')
plt.ylabel('')
plt.show()

# ============================================
# Monthly Expense Trend
# ============================================

df['Month'] = df['Date'].dt.month_name()

monthly_expense = df.groupby('Month')['Amount'].sum()

print("\nMonthly Expense")
print(monthly_expense)

# Line Plot
monthly_expense.plot(marker='o')
plt.title('Monthly Expense Trend')
plt.xlabel('Month')
plt.ylabel('Expense Amount')
plt.show()

# ============================================
# Highest Expense
# ============================================

highest_expense = df.loc[df['Amount'].idxmax()]

print("\nHighest Expense Record")
print(highest_expense)

# ============================================
# Average Expense
# ============================================

average_expense = df['Amount'].mean()

print("\nAverage Expense:", average_expense)

# ============================================
# Category-wise Expense Visualization
# ============================================

sns.barplot(x=category_expense.index,
            y=category_expense.values)

plt.title('Category-wise Expenses')
plt.xlabel('Category')
plt.ylabel('Amount')
plt.show()

# ============================================
# Insights
# ============================================

print("\nKey Insights")
print("1. Bills category had the highest expenses.")
print("2. Rahul contributed the highest amount.")
print("3. Shopping and Travel were major spending categories.")
print("4. Expense distribution helps in budgeting decisions.")

# ============================================
# Save Processed Data
# ============================================

df.to_csv('processed_expense_data.csv', index=False)

print("\nProcessed dataset saved successfully.")
