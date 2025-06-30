# 🌐 Speech to Text Translator

A web application that allows users to choose between **Speech-to-Text** and **Text-to-Text** translation modes. Built with Flask, HTML/CSS (TailwindCSS), and integrated with MongoDB for storing user login details.

---

## 🚀 Features

- 🎤 **Speech-to-Text Translation**
- 📝 **Text-to-Text Translation**
- ☁️ MongoDB Atlas integration for storing user login/signup data
- 🌈 Clean and modern UI using TailwindCSS
- 🔐 Secure authentication system

---

## 📁 Project Structure

speech/
│
├── templates/
│ ├── index.html # Home page with mode selection
│ ├── speech.html # Speech-to-text page
│ ├── text.html # Text-to-text page
│
├── app.py # Main Flask application
├── requirements.txt # Python dependencies

yaml
Copy
Edit

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/speech-to-text-translator.git
cd speech-to-text-translator
2. Create & activate virtual environment
bash
Copy
Edit
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Add your MongoDB URL
In app.py, replace the MongoDB URI with your actual connection string.
Make sure to encode special characters in your password using urllib.parse.quote_plus.

python
Copy
Edit
from pymongo import MongoClient
client = MongoClient("your_mongodb_connection_url")
5. Run the app
bash
Copy
Edit
python app.py
Then open your browser at http://127.0.0.1:5000

✅ Future Enhancements
User registration & login page

Language selection for translations

History of translations per user

Real-time speech recognition improvements

🛠️ Tech Stack
Backend: Python, Flask

Frontend: HTML, TailwindCSS, JavaScript

Database: MongoDB Atlas

Deployment: (Optional: Render, Heroku, etc.)

📜 License
This project is open-source and available under the MIT License.

vbnet
Copy
Edit

Let me know if you'd like to include authentication or language detection features in the README.
