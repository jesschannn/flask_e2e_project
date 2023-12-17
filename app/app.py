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
from oauth.db_functions import update_or_create_user
import logging

GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')

app = Flask(__name__)
app.secret_key = os.urandom(12)
oauth = OAuth(app)

load_dotenv()  # Load environment variables from .env file

# Database connection settings from environment variables
DB_HOSTNAME = os.getenv("DB_HOSTNAME")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORT}/{DB_DATABASE}"
    "?charset=utf8mb4"
)

# Database connection settings
db_engine = create_engine(conn_string, pool_pre_ping=True)

@app.route('/')
def index():
    try: 
        logging.debug("success! index page has been accessed")    
        return render_template('base.html')
    except Exception as e:
        logging.error(f"You have encountered an error! {e}")
        return "Please try again or reach out to Jessica Chan"

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

@app.route('/google/')
def google():
    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )

    # Redirect to google_auth function
    ###note, if running locally on a non-google shell, do not need to override redirect_uri
    ### and can just use url_for as below
    redirect_uri = url_for('google_auth', _external=True)
    print('REDIRECT URL: ', redirect_uri)
    session['nonce'] = generate_token()
    ##, note: if running in google shell, need to override redirect_uri 
    ## to the external web address of the shell, e.g.,
    redirect_uri = 'https://5000-cs-749231008733-default.cs-us-east1-vpcf.cloudshell.dev/google/auth/'
    return oauth.google.authorize_redirect(redirect_uri, nonce=session['nonce'])

@app.route('/google/auth/')
def google_auth():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token, nonce=session['nonce'])
    session['user'] = user
    update_or_create_user(user)
    print(" Google User ", user)
    return redirect('/dashboard')

@app.route('/dashboard/')
def dashboard():
    user = session.get('user')
    if user:
        return render_template('dashboard.html', user=user)
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)