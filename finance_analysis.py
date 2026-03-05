# def calculate_financial_metrics(income, expenses, savings, debt):
#     monthly_savings = income - expenses
#     savings_ratio = (monthly_savings / income) if income else 0
#     debt_ratio = (debt / income) if income else 0
#     emergency_fund_target = expenses * 6
#     investment_capacity = monthly_savings * 0.5

#     return {
#         "monthly_savings": monthly_savings,
#         "savings_ratio": savings_ratio,
#         "debt_ratio": debt_ratio,
#         "emergency_fund": emergency_fund_target,
#         "investment_capacity": investment_capacity
#     }

def calculate_financial_metrics(income, expenses, savings, debt):

    # Monthly savings
    monthly_savings = max(income - expenses, 0)

    # Savings ratio
    savings_ratio = (monthly_savings / income) if income > 0 else 0

    # Debt ratio
    debt_ratio = (debt / income) if income > 0 else 0

    # Emergency fund recommendation (6 months of expenses)
    emergency_fund_target = expenses * 6 if expenses > 0 else 0

    # Investment capacity (50% of savings)
    investment_capacity = monthly_savings * 0.5

    return {
        "monthly_savings": monthly_savings,
        "savings_ratio": savings_ratio,
        "debt_ratio": debt_ratio,
        "emergency_fund": emergency_fund_target,
        "investment_capacity": investment_capacity
    }