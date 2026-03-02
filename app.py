# import streamlit as st
# import os
# from dotenv import load_dotenv
# from google import genai

# load_dotenv()

# client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# st.title("AI Financial Advisor 💰")

# question = st.text_input("Ask your financial question:")

# if question:
#     try:
#         response = client.models.generate_content(
#             model="gemini-flash-lite-latest",
#             contents=question
#         )
#         st.write(response.text)
#     except Exception as e:
#         st.error(f"Error: {e}")



import streamlit as st
import os
from dotenv import load_dotenv
from google import genai
import matplotlib.pyplot as plt

# ----------------------
# Page Configuration
# ----------------------
st.set_page_config(
    page_title="AI Financial Advisor",
    page_icon="💰",
    layout="wide"
)

# ----------------------
# Custom CSS Styling
# ----------------------
st.markdown("""
<style>
.main-title {
    font-size: 40px;
    font-weight: bold;
    color: #00C897;
}
.sub-text {
    font-size: 18px;
    color: gray;
}
.card {
    padding: 20px;
    border-radius: 10px;
    background-color: #1E1E1E;
}
</style>
""", unsafe_allow_html=True)

# ----------------------
# Load API
# ----------------------
load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# ----------------------
# Sidebar - User Profile
# ----------------------
st.sidebar.title("👤 User Profile")

age = st.sidebar.slider("Age", 18, 60, 21)
monthly_income = st.sidebar.number_input("Monthly Income (₹)", min_value=1000, step=1000)
risk_level = st.sidebar.selectbox("Risk Appetite", ["Low", "Medium", "High"])
investment_goal = st.sidebar.text_input("Investment Goal (e.g., Car, House, Retirement)")

# ----------------------
# Main Title
# ----------------------
st.markdown('<p class="main-title">AI Financial Advisor 💰</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Smart. Data-driven. Personalized Investment Planning.</p>', unsafe_allow_html=True)

st.divider()

# ----------------------
# User Question Section
# ----------------------
question = st.text_area("💬 Ask Your Financial Question")

if st.button("Generate Advice 🚀"):

    if question == "":
        st.warning("Please enter your financial question.")
    else:
        with st.spinner("Analyzing your financial data..."):

            prompt = f"""
            You are a professional financial advisor.

            User Profile:
            Age: {age}
            Monthly Income: ₹{monthly_income}
            Risk Level: {risk_level}
            Goal: {investment_goal}

            Question:
            {question}

            Provide structured financial advice with:
            - Investment allocation %
            - SIP suggestions
            - Safe options
            - Growth options
            - Emergency fund advice
            """

            try:
                response = client.models.generate_content(
                    model="gemini-flash-lite-latest",
                    contents=prompt
                )

                st.success("✅ AI Recommendation Generated")

                col1, col2 = st.columns([2, 1])

                # Left Column - AI Advice
                with col1:
                    st.subheader("📊 Financial Recommendation")
                    st.write(response.text)

                # Right Column - Sample Allocation Chart
                with col2:
                    st.subheader("📈 Suggested Allocation")

                    # Example Allocation (You can later parse real AI output)
                    allocation = [40, 30, 20, 10]
                    labels = ["SIP", "Stocks", "FD", "Emergency Fund"]

                    fig, ax = plt.subplots()
                    ax.pie(allocation, labels=labels, autopct='%1.1f%%')
                    st.pyplot(fig)

            except Exception as e:
                st.error(f"Error: {e}")