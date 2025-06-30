from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId
import speech_recognition as sr
import google.generativeai as genai
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # for session management
CORS(app)

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://nazeershaik9081:nazeer6676@cluster0.nvygdxx.mongodb.net/")
db = client['translatorDB']  # create/use database
users_collection = db['users']  # create/use collection

# Gemini config
GOOGLE_API_KEY = 'YOUR_GEMINI_API_KEY'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/speech')
def speech_page():
    return render_template('speech.html')

@app.route('/text')
def text_page():
    return render_template('text.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data['email']
    password = data['password']

    # Check if user exists
    if users_collection.find_one({"email": email}):
        return jsonify({"error": "User already exists"}), 400

    users_collection.insert_one({"email": email, "password": password})
    return jsonify({"message": "Registered successfully"}), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data['email']
    password = data['password']

    user = users_collection.find_one({"email": email, "password": password})
    if user:
        session['user_id'] = str(user['_id'])
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio_data = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio_data, language='en-IN')
        return jsonify({ "text": text })
    except sr.UnknownValueError:
        return jsonify({ "error": "Could not understand audio." }), 400
    except sr.RequestError as e:
        return jsonify({ "error": f"Speech Recognition service error: {str(e)}" }), 500

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text', '')
    target_language = data.get('target_language', 'hi')

    prompt = f"Translate the following text to {target_language}:\n'{text}'"
    try:
        response = model.generate_content(prompt)
        translation = response.text.strip()
        return jsonify({'translation': translation})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
