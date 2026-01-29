"""


This file demonstrates:
1. Secure user data collection
2. Sentiment analysis with bias awareness
3. Fair product recommendation system
4. Ethical logging practices
5. Responsible ML model usage

Ethical Principles Followed:
- Privacy protection
- Bias awareness
- Transparency
- Fairness
- Responsible usage of AI outputs
"""

# -------------------------------------------------
# TASK 1: USER DATA COLLECTION WITH PRIVACY
# -------------------------------------------------
"""PROMPT : "Generate a Python script that collects user name, age, and email.
Add comments on how to anonymize or protect this data."""
import hashlib

print("\n--- Task 1: User Data Collection with Privacy ---")

name = input("Enter your name: ")
age = input("Enter your age: ")
email = input("Enter your email: ")

# Hashing email to anonymize identity
hashed_email = hashlib.sha256(email.encode()).hexdigest()

# NOTE:
# - Do NOT store raw personal data
# - Hash or encrypt sensitive information
# - Collect minimum required data only

user_data = {
    "name": name,
    "age": age,
    "email_hash": hashed_email
}

print("Stored Secure User Data:", user_data)


# -------------------------------------------------
# TASK 2: SENTIMENT ANALYSIS WITH BIAS AWARENESS
# -------------------------------------------------
"""
Generate a Python function for sentiment analysis and include
comments to handle or reduce data bias.
"""
print("\n--- Task 2: Sentiment Analysis with Bias Awareness ---")

def analyze_sentiment(text):
    positive_words = ["good", "happy", "great", "excellent"]
    negative_words = ["bad", "sad", "terrible", "poor"]

    text = text.lower()
    score = 0

    for word in positive_words:
        if word in text:
            score += 1

    for word in negative_words:
        if word in text:
            score -= 1

    # Ethical Notes:
    # - Dataset should be balanced and diverse
    # - Remove offensive or culturally biased terms
    # - Avoid making decisions using limited keywords

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

sample_text = input("Enter a sentence for sentiment analysis: ")
print("Sentiment:", analyze_sentiment(sample_text))


# -------------------------------------------------
# TASK 3: PRODUCT RECOMMENDATION WITH FAIRNESS
# -------------------------------------------------
"""
Write a Python program that recommends products based on user
history and follows ethical guidelines like transparency and fairness.
"""
print("\n--- Task 3: Ethical Product Recommendation ---")

def recommend_products(user_categories, products):
    recommendations = []

    for product in products:
        if product["category"] in user_categories:
            recommendations.append(product)

    # Ethical Guidelines:
    # - Avoid favoritism toward sponsored products
    # - Give equal visibility to all sellers
    # - Clearly explain recommendation logic to users

    return recommendations

user_history = ["electronics", "books"]

product_list = [
    {"name": "Laptop", "category": "electronics"},
    {"name": "Story Book", "category": "books"},
    {"name": "Shoes", "category": "fashion"},
]

recommended = recommend_products(user_history, product_list)

print("Recommendations based on your interests:")
for item in recommended:
    print("-", item["name"])

print("Reason: Products were recommended based on your browsing categories.")


# -------------------------------------------------
# TASK 4: ETHICAL LOGGING (NO SENSITIVE DATA)
# -------------------------------------------------
"""
Generate logging functionality for a Python web application and
ensure logs do not record sensitive information.
"""
print("\n--- Task 4: Ethical Logging ---")

import logging

logging.basicConfig(filename="app.log", level=logging.INFO)

def login_user(username, password):
    # Never log passwords, emails, or tokens

    logging.info(f"Login attempt by user: {username}")

    if password == "admin123":
        logging.info("Login successful")
        print("Login Successful")
        return True
    else:
        logging.warning("Login failed")
        print("Login Failed")
        return False

login_user("test_user", "1234")

# Ethical Logging Rules:
# - Do not log personal identifiers
# - Logs must help debugging, not invade privacy


# -------------------------------------------------
# TASK 5: ML MODEL WITH RESPONSIBLE USAGE NOTES
# -------------------------------------------------
"""
Generate a machine learning model and add documentation on
responsible usage, explainability, and limitations.
"""
print("\n--- Task 5: Responsible Machine Learning Model ---")

from sklearn.linear_model import LinearRegression
import numpy as np

# Sample training data (very small dataset)
X = np.array([[1], [2], [3], [4]])
y = np.array([100, 200, 300, 400])

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[5]])
print("Predicted Output:", prediction)

"""
Responsible AI Usage Notes:
- This model is trained on limited sample data
- Predictions may not generalize to real-world cases
- Do NOT use for medical, legal, or financial decisions
- Always evaluate accuracy and bias before deployment
- Provide explainable results to end users
"""

print("\n--- End of Lab 5 Ethical AI Demonstration ---")
