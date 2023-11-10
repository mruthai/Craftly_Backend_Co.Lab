# src/routes.py
from flask import render_template, request, redirect, url_for
from src import app
from src.models.chat import Chat

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_cover_letter():
    resume = request.form['resume']
    job_description = request.form['job_description']
    previous_cover_letter = request.form['previous_cover_letter']

    cover_letter = Chat.generate_cover_letter(resume, job_description, previous_cover_letter)
    
    return render_template('cover_letter.html', cover_letter=cover_letter)
