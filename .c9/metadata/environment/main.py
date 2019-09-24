{"changed":true,"filter":false,"title":"main.py","tooltip":"/main.py","value":"import os\nfrom flask import Flask,render_template, request, redirect,flash, jsonify, url_for\nimport json\nfrom flask_mail import Mail, Message\nimport pymysql\n\n\n\n# email-confirmation of booking To user\n\ndef send_mail(username, email):\n    user_mail_list = []\n    user_mail_list.append(email)\n    print(user_mail_list,\"user_mail_list\")\n    msg = Message(subject=\"Hello, {}\".format(username),recipients=user_mail_list)\n    msg.html=\"\"\"<p><b style=\"color:gold\">You're booked!</b></p><p>Your appointment is on: <b><i>{}</i></b>.</p> <p>Your Time is:<b><i>{}</i></b>.</p>\"\"\".format(request.form['date'],\n    request.form['time'])\n    mail.send(msg)\n    \n# email-to employee of user booking\n        \ndef send_mail_employee(username,date, service,time,phone):\n    msg = Message(subject=\"New Booking\",recipients=[\"baywashstudio@gmail.com\"])\n    msg.body=\"New booking has just arrived.\\n\\n{} has booked an appointment on {} at {}.\".format(username,\n    request.form['date'], request.form['time'])\n    mail.send(msg)\n        \n@app.route('/')\ndef index():\n     return render_template(\"index.html\", title = \"Home\")\n     \n     \n@app.route('/portfolio')\ndef portfolio():\n     return render_template(\"portfolio.html\", title = \"Gallery\")\n     \n@app.route('/service')\ndef service():\n     return render_template(\"service.html\", title = \"Services\")\n    \n# queries to get: user / last user id and booking information\ndef add_user(username, phone, email):\n    try:\n        with connection.cursor() as cursor:\n            sql = \"\"\"INSERT INTO CUSTOMERS (CUSTOMER_NAME, CUSTOMER_TELEPHONE, \n            CUSTOMER_EMAIL) VALUES ('{}', '{}', '{}');\"\"\".format(username, phone, email)\n            cursor.execute(sql)\n            connection.commit()\n        cursor.close()\n    finally:\n        print(\"ok\")\n      \n     \ndef get_last_user_id():\n    with connection.cursor(pymysql.cursors.DictCursor) as cursor:\n          sql = \"\"\" SELECT MAX(CUSTOMER_ID) FROM CUSTOMERS;\"\"\"\n          cursor.execute(sql)\n          result = cursor.fetchall()\n    cursor.close()\n    return result[0]['MAX(CUSTOMER_ID)']\n\n    \ndef add_booking(date, service_id, time,customer_id):\n  try:\n        print(time, \"time is time\", date, service_id, time,customer_id)\n        with connection.cursor() as cursor:\n            sql = \"\"\"INSERT INTO BOOKINGS (DATE, SERVICE_ID, TIME,\n            CUSTOMER_ID) VALUES ('{}', {}, '{}', {});\"\"\".format(date,service_id,\n            time,customer_id)\n            cursor.execute(sql)\n            connection.commit()\n        cursor.close()\n  finally:\n           \n            print(\"close it\")\n","undoManager":{"mark":5,"position":5,"stack":[[{"start":{"row":0,"column":0},"end":{"row":67,"column":0},"action":"insert","lines":["# email-confirmation of booking To user","","def send_mail(username, email):","    user_mail_list = []","    user_mail_list.append(email)","    print(user_mail_list,\"user_mail_list\")","    msg = Message(subject=\"Hello, {}\".format(username),recipients=user_mail_list)","    msg.html=\"\"\"<p><b style=\"color:gold\">You're booked!</b></p><p>Your appointment is on: <b><i>{}</i></b>.</p> <p>Your Time is:<b><i>{}</i></b>.</p>\"\"\".format(request.form['date'],","    request.form['time'])","    mail.send(msg)","    ","# email-to employee of user booking","        ","def send_mail_employee(username,date, service,time,phone):","    msg = Message(subject=\"New Booking\",recipients=[\"baywashstudio@gmail.com\"])","    msg.body=\"New booking has just arrived.\\n\\n{} has booked an appointment on {} at {}.\".format(username,","    request.form['date'], request.form['time'])","    mail.send(msg)","        ","@app.route('/')","def index():","     return render_template(\"index.html\", title = \"Home\")","     ","     ","@app.route('/portfolio')","def portfolio():","     return render_template(\"portfolio.html\", title = \"Gallery\")","     ","@app.route('/service')","def service():","     return render_template(\"service.html\", title = \"Services\")","    ","# queries to get: user / last user id and booking information","def add_user(username, phone, email):","    try:","        with connection.cursor() as cursor:","            sql = \"\"\"INSERT INTO CUSTOMERS (CUSTOMER_NAME, CUSTOMER_TELEPHONE, ","            CUSTOMER_EMAIL) VALUES ('{}', '{}', '{}');\"\"\".format(username, phone, email)","            cursor.execute(sql)","            connection.commit()","        cursor.close()","    finally:","        print(\"ok\")","      ","     ","def get_last_user_id():","    with connection.cursor(pymysql.cursors.DictCursor) as cursor:","          sql = \"\"\" SELECT MAX(CUSTOMER_ID) FROM CUSTOMERS;\"\"\"","          cursor.execute(sql)","          result = cursor.fetchall()","    cursor.close()","    return result[0]['MAX(CUSTOMER_ID)']","","    ","def add_booking(date, service_id, time,customer_id):","  try:","        print(time, \"time is time\", date, service_id, time,customer_id)","        with connection.cursor() as cursor:","            sql = \"\"\"INSERT INTO BOOKINGS (DATE, SERVICE_ID, TIME,","            CUSTOMER_ID) VALUES ('{}', {}, '{}', {});\"\"\".format(date,service_id,","            time,customer_id)","            cursor.execute(sql)","            connection.commit()","        cursor.close()","  finally:","           ","            print(\"close it\")",""],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]},{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""]},{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":4,"column":14},"action":"insert","lines":["import os","from PIL import Image","from flask import Flask, render_template, request, flash, jsonify, url_for","from run import connection","import pymysql"],"id":3}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":21},"action":"remove","lines":["from PIL import Image"],"id":4}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"remove","lines":["",""],"id":5}],[{"start":{"row":0,"column":0},"end":{"row":4,"column":0},"action":"remove","lines":["import os","from flask import Flask, render_template, request, flash, jsonify, url_for","from run import connection","import pymysql",""],"id":6},{"start":{"row":0,"column":0},"end":{"row":4,"column":14},"action":"insert","lines":["import os","from flask import Flask,render_template, request, redirect,flash, jsonify, url_for","import json","from flask_mail import Mail, Message","import pymysql"]}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":11},"action":"remove","lines":["import json"],"id":7},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":10,"column":0},"end":{"row":18,"column":4},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1569288538763}