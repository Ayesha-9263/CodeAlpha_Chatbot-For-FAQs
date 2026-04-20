# 🤖 AI FAQ Chatbot

Hello everyone
I am Ayesha Ansari,  
This is another project that I developed during my Artificial Intelligence Internship at CodeAlpha.

## 🚀 Project Overview

In this project, I created a simple FAQ Chatbot using Python.  
The chatbot is designed to answer user questions by matching them with the most similar predefined questions.

Instead of using complex NLP libraries, I implemented this project using a simple and effective approach with cosine similarity, which makes it lightweight and easy to understand.

---

## ✨ Features

- 💬 Interactive command-line chatbot
- 🔍 Matches user questions using similarity techniques
- ⚡ Fast and efficient response system
- 🧠 Beginner-friendly implementation
- 🔁 Continuous conversation support
- ✔ Handles unknown queries with proper response

---

## 🛠️ Technologies Used

- Python
- scikit-learn (TfidfVectorizer, cosine similarity)

---

## 📌 How It Works

1. A list of predefined questions and answers is created  
2. Questions are converted into numerical vectors using TF-IDF  
3. User input is also converted into a vector  
4. Cosine similarity is calculated between user input and stored questions  
5. The most similar question is identified  
6. The corresponding answer is displayed  

If no good match is found, the chatbot responds accordingly.

---

## ▶️ How to Run

1. Install required library:
