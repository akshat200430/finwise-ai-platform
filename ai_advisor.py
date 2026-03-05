# from config import get_client
# import time

# def build_financial_chat_prompt(user_input, profile_data, chat_history):
#     context = f"""
# You are FinWise AI — a professional virtual financial advisor.

# User Financial Profile:
# Income: ₹{profile_data['income']}
# Expenses: ₹{profile_data['expenses']}
# Savings: ₹{profile_data['savings']}
# Debt: ₹{profile_data['debt']}
# Risk Tolerance: {profile_data['risk']}
# Goal: {profile_data['goal']}

# Guidelines:
# - Provide clear, structured, professional advice.
# - Be concise but actionable.
# - Suggest budgeting, investment, and debt reduction strategies.
# - Personalize recommendations based on financial data.
# - Use bullet points for clarity.
# """

#     conversation_history = ""
#     for role, msg in chat_history:
#         conversation_history += f"{role}: {msg}\n"

#     full_prompt = (
#         context
#         + "\nConversation History:\n"
#         + conversation_history
#         + f"\nUser: {user_input}\nAI:"
#     )

#     return full_prompt


# def generate_ai_response(prompt):
#     client = get_client()

#     try:
#         response = client.models.generate_content(
#             model="gemini-2.0-flash",
#             contents=prompt
#         )
#         return response.text

#     except Exception as e:
#         error_message = str(e)

#         # Handle quota errors gracefully
#         if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:
#             return (
#                 "⚠ AI quota exceeded for today.\n\n"
#                 "Please wait a few minutes or try again tomorrow.\n"
#                 "You can also enable billing in Google Cloud to increase limits."
#             )

#         return f"⚠ Unexpected error occurred:\n{error_message}"



from config import get_client


def build_financial_chat_prompt(user_input, profile_data, chat_history):
    context = f"""
You are FinWise AI — a professional virtual financial advisor.

User Financial Profile:
Income: ₹{profile_data['income']}
Expenses: ₹{profile_data['expenses']}
Savings: ₹{profile_data['savings']}
Debt: ₹{profile_data['debt']}
Risk Tolerance: {profile_data['risk']}
Goal: {profile_data['goal']}

Guidelines:
- Provide clear, structured, professional advice.
- Be concise but actionable.
- Suggest budgeting, investment, and debt reduction strategies.
- Personalize recommendations based on financial data.
- Use bullet points for clarity.
"""

    conversation_history = ""
    for role, msg in chat_history:
        conversation_history += f"{role}: {msg}\n"

    full_prompt = (
        context
        + "\nConversation History:\n"
        + conversation_history
        + f"\nUser: {user_input}\nAI:"
    )

    return full_prompt


def generate_ai_response(prompt):
    client = get_client()

    try:
        response = client.chat.completions.create(
           model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"⚠ AI Error: {str(e)}"