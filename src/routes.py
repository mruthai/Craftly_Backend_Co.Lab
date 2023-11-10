# src/routes.py
from flask import render_template, request, redirect, url_for
from src import app
from src.models.chat import Chat

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/letter', methods=['POST'])
def generate_cover_letter():
    resume = request.form['resume']
    job_description = request.form['job_description']
    previous_cover_letter = request.form['previous_cover_letter']

    cover_letter = Chat.generate_cover_letter(resume, job_description, previous_cover_letter)
    
    return render_template('index.html', cover_letter=cover_letter)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    chat_response = Chat().get_ai_answer(user_input)
    return render_template('index.html', chat_response=chat_response)
