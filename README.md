Multi-Language Sentiment Analysis using NLP 🌍🔍                                                                                                                                                                
Overview
This project implements a Multi-Language Sentiment Analysis system using Natural Language Processing (NLP) and Machine Learning. It processes text data in five different languages, translates it to English, cleans the text, and classifies it into one of six different emotions. The model is trained using Logistic Regression with TF-IDF vectorization.

Project Features
✔️ Supports 5 different languages 🏳️
✔️ Classifies text into 6 different emotions 🎭
✔️ Uses Google Translate API for automatic translation 🗣️➡️🇬🇧
✔️ Implements TF-IDF for text vectorization 🔢
✔️ Trained using Logistic Regression 🤖
✔️ Provides classification accuracy and evaluation metrics 📊

Dataset
The dataset consists of 50 sentences across 5 languages.
Each sentence is labeled with one of 6 emotions:
😊 Happy
😡 Angry
😢 Sad
😨 Fearful
🤯 Surprised
🤢 Disgusted
Workflow
1️⃣ Load Dataset – Read multilingual text and emotion labels.
2️⃣ Language Detection – Identify the language of each sentence.
3️⃣ Text Translation – Convert all text to English for uniform processing.
4️⃣ Preprocessing – Lowercasing, punctuation removal, stopword removal, etc.
5️⃣ Text Vectorization – Convert text into numerical features using TF-IDF.
6️⃣ Model Training – Train Logistic Regression on the dataset.
7️⃣ Evaluation – Calculate accuracy, precision, recall, and F1-score.
8️⃣ Save Model – Export trained model and vectorizer for future use.
