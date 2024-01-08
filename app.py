import os
from flask import *
import mysql.connector
import pandas as pd
import random
from flask_mail import *

db = mysql.connector.connect(
    user='root', port=3309, database='lightweightpolicy')
cur = db.cursor()
app = Flask(__name__)
app.secret_key = '!@#$H%S$BV#AS><)SH&BSGV*(_Sjnkxcb9+_)84JSUHB&*%$^+='


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/patient', methods=['POST', 'GET'])
def Patientlog():
    if request.method == 'POST':
        aadhar = request.form['aadhar']
        password = request.form['password']
        cur.execute(
            "select * from patient_reg where aadhar=%s and password=%s", (aadhar, password))
        content = cur.fetchall()
        db.commit()
        if content == []:
            msg = "Credentials Does't exist"
            return render_template('patientlog.html', msg=msg)
        else:
            print(content)
            aadhar = content[0][5]
            session['id'] = content[0][0]
            session['aadhar'] = aadhar
            return render_template('patienthome.html', msg="Login success")
    return render_template('patientlog.html')


@app.route('/patientreg', methods=['POST', 'GET'])
def Patientreg():
    if request.method == 'POST':
        name = request.form['name']
        profile = request.files['profile']
        profilename = profile.filename
        address = request.form['address']
        aadhar = request.form['aadhar']
        bp = request.form['bp']
        sugar = request.form['sugar']
        hypertention = request.form['hypertention']
        password = request.form['password']
        # profile.save('/static/uploadfiles/' + profile.filename)

        mypath = os.path.join("static","profiles", profilename)
        profile.save(mypath)
        profilepath = "profiles/" + profilename
        sql = "select * from patient_reg where aadhar='%s' and password='%s'" % (
            aadhar, password)
        cur.execute(sql)
        data = cur.fetchall()
        db.commit()
        if data == []:
            sql = "insert into patient_reg(name,profile,address,aadhar,bp,sugar,hypertention,profilename,password) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (name, profilepath, address, aadhar, bp,
                   sugar, hypertention, profilename, password)
            cur.execute(sql, val)
            db.commit()
            return render_template('patientlog.html')
        else:
            warning = 'Details already Exist'
            return render_template('patientreg.html', msg=warning)
    return render_template('patientreg.html')


@app.route("/myappointments", methods=["POST", "GET"])
def myappointments():
    if request.method == "POST":
        billnumber = request.form['billnumber']
        serialnumber = request.form['serialnumber']
        patientname = request.form['patientname']
        aadhar = request.form['aadhar']
        bp = request.form['bp']
        sugar = request.form['sugar']
        hypertention = request.form['hypertention']
        sql = "insert into appointments(serialnumber,patientname,aadhar,bp,sugar,hypertention,billnumber)values(%s,%s,%s,%s,%s,%s,%s)"
        values = (serialnumber, patientname, aadhar,
                  bp, sugar, hypertention, billnumber)
        cur.execute(sql, values)
        db.commit()
        sql = "select id,patientname,serialnumber,billnumber from appointments"
        cur.execute(sql)
        data = cur.fetchall()
        return render_template("myappointments.html", data=data)

    sql = "select * from patient_reg"
    cur.execute(sql)
    data = cur.fetchall()
    return render_template("myreport.html", data=data)


@app.route("/allreports")
def allreports():
    sql = "select Id,FileName,aadhar,status from reports"
    cur.execute(sql)
    data = cur.fetchall()
    print(data)
    return render_template("allreports.html", data=data)


@app.route("/download1/<int:aadhar>")
def download1(aadhar=0):
    sql = "select filename from reports where aadhar='%s'" % (aadhar)
    cur.execute(sql)
    filename = cur.fetchall()[0]

    filename = filename[0]
    # Assuming files are stored in a directory named 'files' in the same directory as your Flask application
    file_path = f"uploads/{filename}"
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
            print(f"File content: {content}")  # or log this information
    except Exception as e:
        print(f"Error reading file: {e}")  # or log this information
    return send_file(file_path, as_attachment=True)


@app.route('/patientreq', methods=['POST', 'GET'])
def patientreq():
    if request.method == 'POST':
        Name = request.form['Name']
        doc = request.form['Doc']
        Age = request.form['Age']
        Symptoms = request.form['symptoms']
        AppointmentDate = request.form['AppointmentDate']
        Time = request.form['Time']
        sql = "insert into patientreq (Name,Type,Age,symptoms,AppointmentDate,Time) values ('%s','%s','%s','%s','%s','%s')" % (
            Name, doc, Age, Symptoms, AppointmentDate, Time)
        cur.execute(sql)
        db.commit()
        msg = "Your appointment request Sent to Management"
        return render_template('patienthome.html', msg=msg)
    return render_template('patienthome.html')


@app.route('/labtechnician', methods=['POST', 'GET'])
def labtechnician():
    if request.method == 'POST':
        useremail = request.form['useremail']
        password = request.form['passcode']
        if useremail == "technician@gmail.com" and password == 'technician':
            return render_template('managementhome.html')
    return render_template('management.html')


@app.route("/patientreports")
def patientreports():
    sql = "select id,billnumber,serialnumber,patientname,aadhar,status1 from appointments"
    cur.execute(sql)
    data = cur.fetchall()
    return render_template("patientreports.html", data=data)


@app.route("/download/<int:aadhar>/")
def download(aadhar=0):
    print(aadhar)
    sql = "select filename from reports where aadhar='%s'" % (aadhar)
    cur.execute(sql)
    filename = cur.fetchall()[0]

    filename = filename[0]
    # Assuming files are stored in a directory named 'files' in the same directory as your Flask application
    file_path = f"uploads/{filename}"
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
            print(f"File content: {content}")  # or log this information
    except Exception as e:
        print(f"Error reading file: {e}")  # or log this information

    return send_file(file_path, as_attachment=True)


@app.route("/vreport/<x>")
def vreport(x=0):
    sql = "select Id,AES_DECRYPT(FileData, 'sec_key') from reports where Id='%s'" % (
        x)
    data = pd.read_sql_query(sql, db)
    return render_template("vreport.html", cols=data.columns.values, rows=data.values.tolist())


@app.route('/UploadReports')
def UploadReports():
    sql = "select id,patientname,serialnumber,billnumber,status1 from appointments"
    data = pd.read_sql_query(sql, db)
    db.commit()
    return render_template('viewappointments.html', cols=data.columns.values, rows=data.values.tolist())


@app.route('/accept_request/<x>/<y>/<z>')
def acceptreq(x=0, y='', z=''):
    print(x, y)
    session["rowid"] = x
    session['username'] = y
    print(session["rowid"])
    print(z)
    sql = "select Name,Department,Email from docreg where Department='%s' " % (
        z)
    data = pd.read_sql_query(sql, db)
    db.commit()
    print(data)
    if data.empty:
        flash('Doctor is not available')
        return redirect(url_for('view_appointments'))
    else:
        sql = "update patientreq set status='accepted' where status='pending' and Id='%s' and Name='%s'" % (
            x, y)
        cur.execute(sql)
        db.commit()
    return render_template('acptreq.html', cols=data.columns.values, rows=data.values.tolist())


@app.route('/Connect/<x>/<y>/<z>')
def mergereq(x='', y='', z=''):
    print("======")
    print(x)
    print(y)
    print(z)
    sql = "select name,Type,Age from patientreq where status='accepted' and Name='%s'" % (
        session['username'])
    cur.execute(sql)
    da = cur.fetchall()
    db.commit()
    dat = [j for i in da for j in i]
    print(dat)

    sql = "insert into connectdata(Patientname,patientAge,Type)values('%s','%s','%s')" % (
        dat[0], dat[2], dat[1])
    cur.execute(sql)
    db.commit()

    return redirect(url_for('view_appointments'))


@app.route('/Doc_requests')
def Docrequests():
    sql = "select Name,Department,Age,Number,Email from docreg where status='pending'"
    data = pd.read_sql_query(sql, db)
    db.commit()
    return render_template('Doc.html', cols=data.columns.values, rows=data.values.tolist())


@app.route('/acpt_doc/<x>/<y>')
def acceptdoc(x='', y=''):
    sql = "update docreg set status='accepted' where status='pending' and Name='%s' and Email='%s'" % (
        x, y)
    cur.execute(sql)
    db.commit()
    sender_address = 'gorantladathatreya@gmail.com'
    sender_pass = 'exxkcsimkdhrvcsc'
    content = "Your Request Is Accepted by the Management Plas You Can Login Now"
    receiver_address = y
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = "A Lightweight Policy Update Scheme for Outsourced Personal Health Records Sharing project started"
    message.attach(MIMEText(content, 'plain'))
    ss = smtplib.SMTP('smtp.gmail.com', 587)
    ss.starttls()
    ss.login(sender_address, sender_pass)
    text = message.as_string()
    ss.sendmail(sender_address, receiver_address, text)
    ss.quit()
    return redirect(url_for('Docrequests'))


@app.route('/Docs')
def Docs():
    sql = "select Name,Department,Age,number,Email from docreg where status='accepted'"
    data = pd.read_sql_query(sql, db)
    db.commit()
    return render_template("docs.html", cols=data.columns.values, rows=data.values.tolist())


@app.route('/adminlog', methods=['POST', 'GET'])
def adminlog():
    if request.method == 'POST':
        adminemail = request.form['adminemail']
        adminpassword = request.form['adminpassword']
        if adminemail == "admin@gmail.com" and adminpassword == "admin":
            return render_template("docrequest.html")
        else:
            return render_template("doctorlog.html")
    return render_template('doctorlog.html')


@app.route("/dashboard")
def dashboard():
    sql = "select id,patientname,serialnumber,billnumber from appointments"
    cur.execute(sql)
    data = cur.fetchall()
    return render_template("dashboard.html", data=data)


@app.route("/patientreport", methods=["POST", "GET"])
def patientreport():
    if request.method == "POST":
        keyvalue = request.form['keyvalue']
        sql = "select Id,FIlename,AES_DECRYPT(FileData, 'sec_key') from reports where Patientid='%s'" % (
            keyvalue)
        # sql="select Filedata from reports where Patientid='%s'"%(keyvalue)
        data = pd.read_sql_query(sql, db)
        return render_template("patientreport.html", x=2, cols=data.columns.values, rows=data.values.tolist())
    return render_template("patientreport.html", x=1)


@app.route('/view_patient')
def viewpatient():
    sql = "select * from connectdata where Type='%s' and status='pending'" % (
        session['dept'])
    cur.execute(sql)
    data = cur.fetchall()
    db.commit()
    print(data)
    if data == []:
        msg = "You dont have any appointments "
        return render_template("viewpatient.html", msg=msg)
    Name = data[0][1]
    Age = data[0][2]
    Type = data[0][3]
    return render_template('viewpatient.html', name=Name, age=Age, type=Type)


@app.route("/patient_access/<a>/<b>")
def patientaccess(a='', b=0):
    sql = "select Email from patient_reg where Name='%s' and Age='%s'" % (a, b)
    cur.execute(sql)
    data = cur.fetchall()
    db.commit()
    print(data)
    if data != []:
        Email = data[0][0]
        session['email'] = Email
        sql = "update connectdata set status='accept' where status='pending' and PatientName='%s'" % (
            a)
        cur.execute(sql)
        db.commit()
        return render_template("uploadfile.html", email=Email)

    return render_template("uploadfile.html")


@app.route('/upload_file/<int:id>/')
def uploadfile(id=0):
    print(id)
    return render_template('uploadfile.html', id=id)


@app.route("/reportuploadfile", methods=["POST", "GET"])
def reportuploadfile():
    if request.method == 'POST':
        id = request.form['id']
        filedata = request.files['filedata']
        n = filedata.filename
        data = filedata.read()
        mydata = data.decode()
        filedata.save(os.path.join("uploads/",n))
        f = open("uploads/"+n, "a")
        f.write(mydata)
        f.close()
        # path = os.path.join("uploads/", n)
        # filedata.save(path)
        status = "accepted"
        id1 = random.randint(0000, 9999)
        PatientId = "PID" + str(id1)
        sql = "insert into reports(FileName,FileData,aadhar,Status,Patientid) values(%s,AES_ENCRYPT(%s,'sec_key'),%s,%s,%s)"
        val = (n, data, session['aadhar'], status, PatientId)
        cur.execute(sql, val)
        db.commit()
        msg = "file Uploaded successfully"
        print(msg)
        sql = "update appointments set status1='accepted' where id='%s'" % (id)
        cur.execute(sql)
        db.commit()
        return redirect(url_for("UploadReports"))


@app.route('/view_files')
def viewfiles():
    sql = "select Id,FileName,Filedata,PatientEmail from reports where PatientEmail='%s' and status='accepted'" % (
        session['email'])
    data = pd.read_sql_query(sql, db)
    db.commit()
    return render_template('files.html', cols=data.columns.values, rows=data.values.tolist())


@app.route('/performs/<d>')
def performs(d=0):
    print(d)
    sql = "update reports set status='updated' where Id='%s' and PatientEmail='%s'" % (
        d, session['email'])
    cur.execute(sql)
    db.commit()
    return redirect(url_for('viewfiles'))
    # return render_template('performs.html')


@app.route('/authority', methods=['POST', 'GET'])
def authority():
    if request.method == 'POST':
        name = request.form['Username']
        password = request.form['passcode']
        if name == 'Authority' and password == 'auth':
            return render_template('authhome.html')

    return render_template('authority.html')


@app.route('/vr')
def vr():
    sql = "select Id,FileName,PatientEmail from reports where status='updated'"
    data = pd.read_sql_query(sql, db)
    db.commit()
    return render_template('vr.html', cols=data.columns.values, rows=data.values.tolist())


@app.route('/proxy_server', methods=['POST', 'GET'])
def proxyserver():
    if request.method == 'POST':
        name = request.form['Username']
        password = request.form['passcode']
        if name == "proxy" and password == "server":
            return render_template('proxylog.html')
    return render_template('proxy.html')


@app.route('/Generate_Key/<c>/')
def generatekey(c=0):
    x = random.randrange(000000, 999999)
    print(x)
    print(c)
    sql = "update reports set Key1='%s',status='done' where Id = '%s' and status='updated' " % (
        x, c)
    cur.execute(sql)
    db.commit()

    return redirect(url_for('vr'))


@app.route('/all_requests')
def allrequests():
    sql = "select Id,FileName,PatientEmail,Key1 from reports where status='done' and PatientEmail='%s'" % (
        session['email'])
    data = pd.read_sql_query(sql, db)
    db.commit()
    return render_template('all.html', cols=data.columns.values, rows=data.values.tolist())


@app.route('/sentmail/<e>/<k>/<z>')
def sentmail(e='', k=0, z=0):
    sender_address = 'gorantladathatreya@gmail.com'
    sender_pass = 'exxkcsimkdhrvcsc'
    sql = "select PatientId from reports where Id='%s'" % (z)
    cur.execute(sql)
    xyz = cur.fetchall()
    db.commit()
    print(xyz)
    patientkey = xyz[0][0]
    content = str(k) + "\n Your Key" + str(patientkey)
    print(z)
    print(content)
    receiver_address = e
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = "A Lightweight Policy Update Scheme for Outsourced Personal Health Records Sharing project started"
    message.attach(MIMEText(content, 'plain'))
    ss = smtplib.SMTP('smtp.gmail.com', 587)
    ss.starttls()
    ss.login(sender_address, sender_pass)
    text = message.as_string()
    ss.sendmail(sender_address, receiver_address, text)
    ss.quit()
    sql = "update reports set Status='complete' where Id='%s' and PatientEmail='%s'" % (
        z, session['email'])
    cur.execute(sql)
    db.commit()
    return redirect(url_for("allrequests"))


@app.route('/myprofile', methods=['POST', 'GET'])
def myprofile():
    sql = "select * from patient_reg where aadhar='%s'" % (session['aadhar'])
    cur.execute(sql)
    data = cur.fetchall()
    db.commit()
    return render_template('report.html', data=data)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True, port=8000)
