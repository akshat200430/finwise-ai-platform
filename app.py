# import streamlit as st
# from finance_analysis import calculate_financial_metrics
# from visualization import savings_pie_chart, financial_bar_chart
# from ai_advisor import generate_ai_response, build_financial_chat_prompt
# from utils import format_currency

# st.set_page_config(layout="wide")

# # ---------------------------------
# # AI Usage Control System
# # ---------------------------------

# if "api_calls" not in st.session_state:
#     st.session_state.api_calls = 0

# if "ai_cache" not in st.session_state:
#     st.session_state.ai_cache = {}

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# def safe_ai_call(prompt):
#     # Return cached response if exists
#     if prompt in st.session_state.ai_cache:
#         return st.session_state.ai_cache[prompt]

#     # Limit API calls per session
#     if st.session_state.api_calls >= 10:
#         return "⚠ AI session limit reached. Please try again later."

#     response = generate_ai_response(prompt)

#     # Cache response
#     st.session_state.ai_cache[prompt] = response
#     st.session_state.api_calls += 1

#     return response

# # Load CSS
# with open("styles.css") as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# # SIDEBAR
# st.sidebar.title("Profile Configuration")

# profile = st.sidebar.selectbox("Profile Type", ["Student", "Professional", "Business"])
# income = st.sidebar.number_input("Monthly Salary (₹)", 0)
# expenses = st.sidebar.number_input("Monthly Expenses (₹)", 0)
# savings = st.sidebar.number_input("Existing Savings (₹)", 0)
# debt = st.sidebar.number_input("Total Debts (₹)", 0)
# goal = st.sidebar.text_input("Financial Goal")
# risk = st.sidebar.selectbox("Risk Tolerance", ["Low", "Medium", "High"])

# # Show AI usage
# st.sidebar.markdown("### 🔋 AI Usage")
# remaining = 10 - st.session_state.api_calls
# st.sidebar.progress(st.session_state.api_calls / 10)
# st.sidebar.write(f"Remaining Calls: {remaining}")

# section = st.sidebar.radio("Navigate", 
#                            ["Financial Overview", 
#                             "Goal Planning", 
#                             "AI Chat Assistant"])

# metrics = calculate_financial_metrics(income, expenses, savings, debt)

# # ---------------------------------
# # SECTION 1 — FINANCIAL OVERVIEW
# # ---------------------------------
# if section == "Financial Overview":

#     st.markdown('<div class="section-header">Your Financial Summary</div>', unsafe_allow_html=True)

#     col1, col2, col3, col4 = st.columns(4)

#     col1.metric("Monthly Savings", format_currency(metrics["monthly_savings"]))
#     col2.metric("Savings Ratio", f"{metrics['savings_ratio']*100:.1f}%")
#     col3.metric("Debt Ratio", f"{metrics['debt_ratio']*100:.1f}%")
#     col4.metric("Investment Capacity", format_currency(metrics["investment_capacity"]))

#     st.markdown('<div class="section-header">Financial Overview Visualizations</div>', unsafe_allow_html=True)

#     col1, col2 = st.columns(2)

#     with col1:
#         st.pyplot(savings_pie_chart(income, expenses, metrics["monthly_savings"]))

#     with col2:
#         st.pyplot(financial_bar_chart(metrics))

#     st.markdown('<div class="section-header">AI Financial Recommendations</div>', unsafe_allow_html=True)

#     if st.button("Generate AI Advice"):
#         prompt = f"""
#         Income: {income}
#         Expenses: {expenses}
#         Savings: {savings}
#         Debt: {debt}
#         Risk: {risk}
#         Goal: {goal}
#         Provide structured financial advice.
#         """

#         advice = safe_ai_call(prompt)
#         st.success("AI Advice Generated")
#         st.write(advice)

# # ---------------------------------
# # SECTION 2 — GOAL PLANNING
# # ---------------------------------
# elif section == "Goal Planning":

#     st.markdown('<div class="section-header">Advanced Goal-Oriented Planning</div>', unsafe_allow_html=True)

#     target_amount = st.number_input("Target Amount (₹)", 0)
#     years = st.number_input("Years to Achieve Goal", 1)

#     if target_amount > 0:
#         monthly_needed = target_amount / (years * 12)

#         st.metric("Monthly Investment Needed", format_currency(monthly_needed))

#         if st.button("Generate Goal Plan"):
#             prompt = f"""
#             Goal: {goal}
#             Target Amount: {target_amount}
#             Years: {years}
#             Income: {income}
#             Risk: {risk}
#             Create a step-by-step financial action plan.
#             """
#             plan = safe_ai_call(prompt)
#             st.write(plan)

# # ---------------------------------
# # SECTION 3 — AI CHAT ASSISTANT
# # ---------------------------------
# elif section == "AI Chat Assistant":

#     st.markdown('<div class="section-header">Financial Assistant Chat</div>', unsafe_allow_html=True)

#     profile_data = {
#         "income": income,
#         "expenses": expenses,
#         "savings": savings,
#         "debt": debt,
#         "risk": risk,
#         "goal": goal
#     }

#     user_input = st.text_input("Ask your financial question")

#     if st.button("Send Message") and user_input:

#         st.session_state.chat_history.append(("User", user_input))

#         prompt = build_financial_chat_prompt(
#             user_input,
#             profile_data,
#             st.session_state.chat_history
#         )

#         with st.spinner("FinWise AI is analyzing your financial situation..."):
#             response = safe_ai_call(prompt)

#         st.session_state.chat_history.append(("AI", response))

#     # Display chat history
#     for role, message in st.session_state.chat_history:
#         if role == "User":
#             st.chat_message("user").write(message)
#         else:
#             st.chat_message("assistant").write(message)


import streamlit as st
from finance_analysis import calculate_financial_metrics
from visualization import savings_pie_chart, financial_bar_chart
from ai_advisor import generate_ai_response, build_financial_chat_prompt
from utils import format_currency

st.set_page_config(layout="wide")

# ---------------------------------
# AI Usage Control System
# ---------------------------------

if "api_calls" not in st.session_state:
    st.session_state.api_calls = 0

if "ai_cache" not in st.session_state:
    st.session_state.ai_cache = {}

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


def safe_ai_call(prompt):

    # Return cached response if exists
    if prompt in st.session_state.ai_cache:
        return st.session_state.ai_cache[prompt]

    # Limit API calls
    if st.session_state.api_calls >= 10:
        return "⚠ AI session limit reached. Please refresh the page."

    response = generate_ai_response(prompt)

    st.session_state.ai_cache[prompt] = response
    st.session_state.api_calls += 1

    return response


# ---------------------------------
# Load CSS
# ---------------------------------

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# ---------------------------------
# SIDEBAR
# ---------------------------------

st.sidebar.title("Profile Configuration")

profile = st.sidebar.selectbox(
    "Profile Type", ["Student", "Professional", "Business"]
)

income = st.sidebar.number_input("Monthly Salary (₹)", min_value=0)
expenses = st.sidebar.number_input("Monthly Expenses (₹)", min_value=0)
savings = st.sidebar.number_input("Existing Savings (₹)", min_value=0)
debt = st.sidebar.number_input("Total Debts (₹)", min_value=0)

goal = st.sidebar.text_input("Financial Goal")

risk = st.sidebar.selectbox(
    "Risk Tolerance", ["Low", "Medium", "High"]
)

# ---------------------------------
# AI Usage Indicator
# ---------------------------------

st.sidebar.markdown("### 🔋 AI Usage")

remaining = max(10 - st.session_state.api_calls, 0)

st.sidebar.progress(st.session_state.api_calls / 10)

st.sidebar.write(f"Remaining Calls: {remaining}")


# ---------------------------------
# Navigation
# ---------------------------------

section = st.sidebar.radio(
    "Navigate",
    [
        "Financial Overview",
        "Goal Planning",
        "AI Chat Assistant"
    ]
)

metrics = calculate_financial_metrics(income, expenses, savings, debt)


# ---------------------------------
# SECTION 1 — FINANCIAL OVERVIEW
# ---------------------------------

if section == "Financial Overview":

    st.markdown(
        '<div class="section-header">Your Financial Summary</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Monthly Savings",
        format_currency(metrics["monthly_savings"])
    )

    col2.metric(
        "Savings Ratio",
        f"{metrics['savings_ratio']*100:.1f}%"
    )

    col3.metric(
        "Debt Ratio",
        f"{metrics['debt_ratio']*100:.1f}%"
    )

    col4.metric(
        "Investment Capacity",
        format_currency(metrics["investment_capacity"])
    )

    st.markdown(
        '<div class="section-header">Financial Overview Visualizations</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.pyplot(
            savings_pie_chart(
                income,
                expenses,
                metrics["monthly_savings"]
            )
        )

    with col2:
        st.pyplot(
            financial_bar_chart(metrics)
        )

    st.markdown(
        '<div class="section-header">AI Financial Recommendations</div>',
        unsafe_allow_html=True
    )

    if st.button("Generate AI Advice"):

        prompt = f"""
Income: {income}
Expenses: {expenses}
Savings: {savings}
Debt: {debt}
Risk: {risk}
Goal: {goal}

Provide structured financial advice.
"""

        advice = safe_ai_call(prompt)

        st.success("AI Advice Generated")

        st.write(advice)


# ---------------------------------
# SECTION 2 — GOAL PLANNING
# ---------------------------------

elif section == "Goal Planning":

    st.markdown(
        '<div class="section-header">Advanced Goal-Oriented Planning</div>',
        unsafe_allow_html=True
    )

    target_amount = st.number_input("Target Amount (₹)", min_value=0)

    years = st.number_input("Years to Achieve Goal", min_value=1)

    if target_amount > 0:

        monthly_needed = target_amount / (years * 12)

        st.metric(
            "Monthly Investment Needed",
            format_currency(monthly_needed)
        )

        if st.button("Generate Goal Plan"):

            prompt = f"""
Goal: {goal}
Target Amount: {target_amount}
Years: {years}
Income: {income}
Risk: {risk}

Create a step-by-step financial action plan.
"""

            plan = safe_ai_call(prompt)

            st.write(plan)


# ---------------------------------
# SECTION 3 — AI CHAT ASSISTANT
# ---------------------------------

elif section == "AI Chat Assistant":

    st.markdown(
        '<div class="section-header">Financial Assistant Chat</div>',
        unsafe_allow_html=True
    )

    profile_data = {
        "income": income,
        "expenses": expenses,
        "savings": savings,
        "debt": debt,
        "risk": risk,
        "goal": goal
    }

    user_input = st.text_input("Ask your financial question")

    if st.button("Send Message") and user_input:

        st.session_state.chat_history.append(("User", user_input))

        prompt = build_financial_chat_prompt(
            user_input,
            profile_data,
            st.session_state.chat_history
        )

        with st.spinner(
            "FinWise AI is analyzing your financial situation..."
        ):
            response = safe_ai_call(prompt)

        st.session_state.chat_history.append(("AI", response))

    for role, message in st.session_state.chat_history:

        if role == "User":
            st.chat_message("user").write(message)

        else:
            st.chat_message("assistant").write(message)
