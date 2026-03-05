# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd
# import numpy as np

# # -------------------------------
# # Safe Savings Pie Chart
# # -------------------------------
# def savings_pie_chart(income, expenses, savings):

#     # Ensure non-negative values
#     expenses = max(expenses, 0)
#     savings = max(savings, 0)

#     total = expenses + savings

#     # Handle empty or zero data safely
#     if total == 0:
#         fig, ax = plt.subplots()
#         ax.text(0.5, 0.5,
#                 "No financial data available",
#                 horizontalalignment='center',
#                 verticalalignment='center',
#                 fontsize=12)
#         ax.axis('off')
#         return fig

#     data = [expenses, savings]
#     labels = ["Expenses", "Remaining Savings"]

#     fig, ax = plt.subplots()
#     ax.pie(
#         data,
#         labels=labels,
#         autopct='%1.1f%%',
#         startangle=90
#     )
#     ax.set_title("Savings & Expense Distribution")

#     return fig


# # -------------------------------
# # Safe Financial Bar Chart
# # -------------------------------
# def financial_bar_chart(metrics):

#     # Extract safely
#     monthly_savings = max(metrics.get("monthly_savings", 0), 0)
#     emergency_fund = max(metrics.get("emergency_fund", 0), 0)
#     investment_capacity = max(metrics.get("investment_capacity", 0), 0)

#     values = [monthly_savings, emergency_fund, investment_capacity]

#     # If all zero → safe empty chart
#     if sum(values) == 0:
#         fig, ax = plt.subplots()
#         ax.text(0.5, 0.5,
#                 "No financial metrics available",
#                 horizontalalignment='center',
#                 verticalalignment='center',
#                 fontsize=12)
#         ax.axis('off')
#         return fig

#     data = pd.DataFrame({
#         "Category": ["Savings", "Emergency Fund", "Investment Capacity"],
#         "Amount": values
#     })

#     fig, ax = plt.subplots()

#     sns.barplot(
#         data=data,
#         x="Category",
#         y="Amount",
#         ax=ax
#     )

#     ax.set_title("Financial Component Analysis")
#     ax.set_ylabel("Amount (₹)")
#     ax.set_xlabel("")

#     return fig

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


def savings_pie_chart(income, expenses, savings):

    # Convert invalid values to 0
    income = 0 if income is None or np.isnan(income) else income
    expenses = 0 if expenses is None or np.isnan(expenses) else expenses
    savings = 0 if savings is None or np.isnan(savings) else savings

    expenses = max(expenses, 0)
    savings = max(savings, 0)

    # If everything is zero, avoid pie crash
    if expenses == 0 and savings == 0:
        expenses = 1
        savings = 1

    data = [expenses, savings]
    labels = ["Expenses", "Savings"]

    fig, ax = plt.subplots()

    ax.pie(
        data,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90
    )

    ax.axis("equal")

    return fig


def financial_bar_chart(metrics):

    values = [
        max(metrics.get("monthly_savings", 0), 0),
        max(metrics.get("emergency_fund", 0), 0),
        max(metrics.get("investment_capacity", 0), 0)
    ]

    categories = [
        "Savings",
        "Emergency Fund",
        "Investment Capacity"
    ]

    df = pd.DataFrame({
        "Category": categories,
        "Amount": values
    })

    fig, ax = plt.subplots()

    sns.barplot(
        data=df,
        x="Category",
        y="Amount",
        ax=ax
    )

    ax.set_title("Financial Capacity Overview")

    return fig