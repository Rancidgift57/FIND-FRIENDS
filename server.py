from flask import Flask,render_template,url_for,request,jsonify
from flask_mail import Mail, Message
import smtplib
import psycopg2
from smtplib import SMTPAuthenticationError
from friends import find_friends
from requestsend import frireq
import subprocess

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Example: smtp.gmail.com for Gmail
app.config['MAIL_PORT'] = 587 
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USERNAME'] ='nnair7598@gmail.com' 
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = ('FIND FRIENDS', '')  # Specify sender's name and email

mail = Mail(app)

DB_NAME = 'findfriends'
DB_USER = 'postgres'
DB_PASSWORD = 'root'
DB_HOST = 'localhost'  # or your database host
DB_PORT = '5432'       # or your database port


@app.route('/homepage', methods=['POST'])
def execute_find_friends():
    email = request.form['email']
    #passw = request.form['password']
    find_friends(email)
        #print(email)  
    return render_template('homepage.html', email=email)
    
        
    


def connect_to_database():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn

def insert_data(conn, name, email,year, branch, prn, residing_pincode, first_hobby, second_hobby,
                third_hobby, favorite_food, social_media_usage, community_involvement,
                travel_destinations, preferred_gadget, physical_well_being, mental_well_being,
                creative_activities, future_goals, password):
    cursor = conn.cursor()
    sql = "INSERT INTO friendfind(name, email,year, branch, prn, residing_pincode, first_hobby, second_hobby,third_hobby, favorite_food, social_media_usage, community_involvement,travel_destinations, preferred_gadget, physical_well_being, mental_well_being,creative_activities, future_goals, password) VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (name, email,year, branch, prn, residing_pincode, first_hobby, second_hobby,
                third_hobby, favorite_food, social_media_usage, community_involvement,
                travel_destinations, preferred_gadget, physical_well_being, mental_well_being,
                creative_activities, future_goals, password))
    conn.commit()
    cursor.close()

@app.route('/submit', methods=['POST'])
def submit_form():
    conn = connect_to_database()

    name = request.form['name']
    email = request.form['email']
    year = request.form['year']
    branch = request.form['branch']
    prn = request.form['prn']
    residing_pincode = request.form['residing-pincode']
    first_hobby = request.form['1st-hobby']
    second_hobby = request.form['2nd-hobby']
    third_hobby = request.form['3rd-hobby']
    favorite_food = request.form['favorite-food']
    social_media_usage = request.form['social-media-usage']
    community_involvement = request.form['community-involvement']
    travel_destinations = request.form['travel-destinations']
    preferred_gadget = request.form['preferred-gadget']
    physical_well_being = request.form['physical-well-being']
    mental_well_being = request.form['mental-well-being']
    creative_activities = request.form['creative-activities']
    future_goals = request.form['future-goals']
    password = request.form['password']
    insert_data(conn, name, email,year, branch, prn, residing_pincode, first_hobby, second_hobby,
                third_hobby, favorite_food, social_media_usage, community_involvement,
                travel_destinations, preferred_gadget, physical_well_being, mental_well_being,
                creative_activities, future_goals, password)
    conn.close()
    return "data submitted successfully"


@app.route('/')
def index():
	return render_template('login.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

def sender(filename):
    try:
        with open(filename, 'r') as file:
            emails = file.read().splitlines()
    
        subject = '🎉🎉🎉Friend Request on Find Friends🎉🎉🎉'
        message_body = 'You have friend request waiting on FIND FREINDS.Open now to connect \n\nBest Regards\n\nTeam Find Friends'

        for email in emails:
            msg = Message(subject=subject, recipients=[email], body=message_body)
            mail.send(msg)

        return 'Emails sent successfully'
    except SMTPAuthenticationError as e:
        return f'Authentication error: {str(e)}'
    except Exception as ex:
        return f'Error sending emails: {str(ex)}'

@app.route('/send-emails')
def send_emails():
    return sender('match_1.txt')

@app.route('/send-emailsw')
def send_emails_w():
    return sender('match_2.txt')

@app.route('/send-emailsr')
def send_emails_r():
    return sender('match_3.txt')




@app.route('/form' , methods=['POST'])
def passreq():
    oldpass = request.form['oldpass']
    newpass = request.form['rewritepass']
    frireq(oldpass,newpass)
    return "password changed successfully"




	
