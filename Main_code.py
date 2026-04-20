from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
print("=== CodeAlpha AI Chatbot ===")
# Questions & Answers
faq_data = [
    "what is AI?",
    "what is machine learning?",
    "what is python?",
    "what is data science?",
    "what is chatbot?"
    "how does AI work?"
    "what are the applications of AI?"
]

responses_list = [
    "AI means Artificial Intelligence.",
    "Machine Learning is a part of AI.",
    "Python is a programming language.",
    "Data Science is about analyzing data.",
    "A chatbot is a program that talks with users."
    "AI works by learning from data and making decisions."
    "AI is used in healthcare, fianance, and many other fields."
]

# Convert text into vectors
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(faq_data)

def run_chatbot():
    print("🤖 AI Chatbot is running (type 'exit' to stop)\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Bot: Goodbye!")
            break

        user_vec = vectorizer.transform([user_input])
        similarity = cosine_similarity(user_vec, X)

        index = similarity.argmax()

        if similarity.max() < 0.3:
            print("Bot: Sorry, I am not sure about that, try asking something else.")
        else:
            print("Bot:", responses_list[index])

run_chatbot()
