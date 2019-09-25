import os
from flask import Flask,render_template, request, redirect,flash, jsonify, url_for
import json
from flask_mail import Mail, Message
import pymysql


app = Flask(__name__)

connection = pymysql.connect(host='mydatabase.cccssd5sqciz.ca-central-1.rds.amazonaws.com',
                            user="****",
                            password="****",
                            db="****",
                            )
                            


app.secret_key = "its_secure"


app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')
mail = Mail(app)

# contact page - booking form


@app.route('/contact',methods=["GET", "POST"])
def contact():
    if request.method=="POST":
        print(request.form)
        username = request.form['first-name'] + " " + request.form['last-name']
        add_user(username, request.form['phone'], request.form['email'])
        last_added_user_id = get_last_user_id()
        print(last_added_user_id, "last_added_user_id", request.form['time'])
        add_booking(request.form['date'], request.form['service'],request.form['time'],last_added_user_id)
        send_mail(username, request.form['email'])
        send_mail_employee(username, request.form['date'], request.form['service'],request.form['time'],
        request.form['phone'])
        flash(" {}! Your booking is confirmed. Check your email for your booking. See you on {}".format(request.form['first-name'],request.form['date']))
        return redirect(url_for('contact'))
     
    return render_template("contact.html", title = "Contact")

# email-confirmation of booking To user

def send_mail(username, email):
    user_mail_list = []
    user_mail_list.append(email)
    print(user_mail_list,"user_mail_list")
    msg = Message(subject="Hello, {}".format(username),recipients=user_mail_list)
    msg.html="""<p><b style="color:gold>You're booked!</b></p><p>Your appointment is on: <b><i>{}</i></b>.</p> <p>Your Time is:<b><i>{}</i></b>.</p>""".format(request.form['date'],
    request.form['time'])
    mail.send(msg)
    
# email-to employee of user booking
        
def send_mail_employee(username,date, service,time,phone):
    msg = Message(subject="New Booking",recipients=["baywashstudio@gmail.com"])
    msg.body="New booking has just arrived.\n\n{} has booked an appointment on {} at {}.".format(username,
    request.form['date'], request.form['time'])
    mail.send(msg)
        
@app.route('/')
def index():
     return render_template("index.html", title = "Home")
     
     
@app.route('/portfolio')
def portfolio():
     return render_template("portfolio.html", title = "Gallery")
     
@app.route('/service')
def service():
     return render_template("service.html", title = "Services")
    
    
# queries to get: user / last user id and booking information

def add_user(username, phone, email):
    try:
        with connection.cursor() as cursor:
            sql = """INSERT INTO CUSTOMERS (CUSTOMER_NAME, CUSTOMER_TELEPHONE, 
            CUSTOMER_EMAIL) VALUES ('{}', '{}', '{}');""".format(username, phone, email)
            cursor.execute(sql)
            connection.commit()
        cursor.close()
    finally:
        print("ok")
      
     
def get_last_user_id():
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
          sql = """ SELECT MAX(CUSTOMER_ID) FROM CUSTOMERS;"""
          cursor.execute(sql)
          result = cursor.fetchall()
    cursor.close()
    return result[0]['MAX(CUSTOMER_ID)']

    
def add_booking(date, service_id, time,customer_id):
  try:
        print(time, "time is time", date, service_id, time,customer_id)
        with connection.cursor() as cursor:
            sql = """INSERT INTO BOOKINGS (DATE, SERVICE_ID, TIME,
            CUSTOMER_ID) VALUES ('{}', {}, '{}', {});""".format(date,service_id,
            time,customer_id)
            cursor.execute(sql)
            connection.commit()
        cursor.close()
  finally:
           
            print()





if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=False)
    
