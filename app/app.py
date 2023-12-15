from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import pandas as pd
import csv
from sqlalchemy import create_engine, inspect, text
from pandas import read_sql
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from authlib.integrations.flask_client import OAuth
from authlib.common.security import generate_token
from flask_session import Session
import sentry_sdk

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

load_dotenv()

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/importance')
def importance():
    return render_template('importance.html')

# Load data from CSV file
df = pd.read_csv('/home/jessica_chan_3/flask_e2e_project/data/clean_medicalmalpractice.csv')

@app.route('/data')
def display_csv():
    data = []
    with open('/home/jessica_chan_3/flask_e2e_project/data/clean_medicalmalpractice.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data.append(row)

    # Retrieve a sample of 50 rows from the data
    sample_data = data[:50]

    return render_template('data.html', data=sample_data)

@app.route('/api', methods=['GET'])
def api_get():
    name = request.args.get('name', 'nothing')
    response = {"message": f'Hi {name}! Welcome to my Medical Malpractice Web App!'}
    return jsonify(response)

@app.route('/api', methods=['POST'])
def api_post():
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'Invalid JSON'}), 400
    
    name = data.get('name', 'nothing')
    return jsonify({'message': f'Hello {name}! Welcome to my Medical Malpractice Web App!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)