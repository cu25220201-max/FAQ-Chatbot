import os
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from preprocess import preprocess_text



load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-2.5-flash")
else:
    model = None


class FAQChatbot:

    def __init__(self, faq_file="data/faq.csv"):

        base_dir = os.path.dirname(os.path.abspath(__file__))
        faq_path = os.path.join(base_dir, faq_file)

        print("Reading FAQ File:", faq_path)

        if not os.path.exists(faq_path):
            raise FileNotFoundError(f"FAQ file not found:\n{faq_path}")

        self.df = pd.read_csv(faq_path, encoding="utf-8")

        if "Question" not in self.df.columns or "Answer" not in self.df.columns:
            raise Exception("faq.csv must contain Question and Answer columns.")

        self.df.fillna("", inplace=True)

        self.df["Processed_Question"] = self.df["Question"].apply(preprocess_text)

        self.vectorizer = TfidfVectorizer()

        self.question_vectors = self.vectorizer.fit_transform(
            self.df["Processed_Question"]
        )

        print(f"Loaded {len(self.df)} FAQs successfully.")

    
    def ask_gemini(self, question):

        if model is None:
            return "Gemini API key not found."

        try:
            response = model.generate_content(question)
            return response.text
        except Exception as e:
            return f"Gemini Error: {e}"

   
    def get_answer(self, user_question):

        processed_question = preprocess_text(user_question)

        user_vector = self.vectorizer.transform([processed_question])

        similarity_scores = cosine_similarity(
            user_vector,
            self.question_vectors
        )

        best_match_index = similarity_scores.argmax()

        best_score = similarity_scores[0][best_match_index]

        
        if best_score >= 0.30:

            answer = self.df.iloc[best_match_index]["Answer"]

            return answer, best_score

        # Gemini AI Answer
        ai_answer = self.ask_gemini(user_question)

        return ai_answer, 1.00




if __name__ == "__main__":

    chatbot = FAQChatbot()

    while True:

        question = input("\nYou : ")

        if question.lower() == "exit":
            print("Bot : Goodbye!")
            break

        answer, score = chatbot.get_answer(question)

        print("\nBot :", answer)
        print("Confidence :", round(score, 2))