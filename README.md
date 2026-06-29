
# 🤖 FAQ Chatbot using NLP

An AI-powered FAQ Chatbot developed as part of the CodeAlpha Python Programming Internship. This project uses Python, Flask, Machine Learning, HTML, CSS, and JavaScript to answer frequently asked questions from a trained dataset through a modern and responsive chat interface.


## 📌 Features

- 🤖 Intelligent FAQ Chatbot
- 🧠 NLP Text Preprocessing
- 🔍 TF-IDF Vectorization
- 📊 Cosine Similarity Matching
- 🌐 Flask Web Application
- 💬 Interactive Chat Interface
- 📱 Responsive Design
- ⚡ Fast Response Time

## 🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- Pandas
- NLTK
- Scikit-learn

## 📂 Project Structure

```text
FAQ_Chatbot/
│
├── app.py
├── chatbot.py
├── preprocess.py
├── requirements.txt
├── README.md
│
├── data/
│   └── faq.csv
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── screenshots/
│   ├── home.png
│   └── chat.png
│
└── nltk_data/

````

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/FAQ_Chatbot.git
````

### 2. Open Project

```bash
cd FAQ_Chatbot
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Download NLTK Data

```python
import nltk
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
```

### 7. Run the Project

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

## 🧠 NLP Workflow

```
User Question
      │
      ▼
Text Preprocessing
      │
      ▼
Tokenization
      │
      ▼
Stopword Removal
      │
      ▼
Lemmatization
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Cosine Similarity
      │
      ▼
Best Matching FAQ
      │
      ▼
Answer Display
```

## 📷 Screenshots

<img width="896" height="468" alt="image" src="https://github.com/user-attachments/assets/e4402cb8-7754-4f81-9907-9e49faf08eda" />


<img width="960" height="481" alt="image" src="https://github.com/user-attachments/assets/1b5c5890-b8f8-4467-8d0a-03db315be5c0" />

<img width="958" height="448" alt="image" src="https://github.com/user-attachments/assets/efdd600c-0b98-4069-b080-13b884a728bd" />



## 🚀 Future Improvements

* Voice Input
* Voice Output
* Multiple Languages
* Database Support
* AI Intent Classification
* User Authentication
* Dark Mode
* Chat History
* OpenAI API Integration

## 📈 Skills Demonstrated

* Python Programming
* Natural Language Processing (NLP)
* Machine Learning
* TF-IDF Vectorization
* Cosine Similarity
* Flask Web Development
* Frontend Development
* REST API
* Data Processing

---

## 👩‍💻 Author

**Pratiksha Tomar**

B.Tech CSE (AI & ML)

Python Developer | Machine Learning Enthusiast | Web Developer

## CodeAlpha Internship Project 🚀
