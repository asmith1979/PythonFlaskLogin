# Script: mainpage.py
# Author: Andrew Smith
# Date: September 2024
# Description: Main landing page (route handling)

from flask import Flask, render_template, request, redirect, url_for, session
import useradmin as user_admin

app = Flask(__name__)
app.secret_key = "super-secret-key"  # required for sessions

@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop('useremail', None)
    return redirect(url_for('login'))

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ""
    if request.method == 'POST':
        
        # getting input with name = fname in HTML form
        userName = request.form.get("useremail")
        # getting input with name = lname in HTML form 
        userPassword = request.form.get("password")    
        
        session['useremail'] = request.form['useremail']
        print(dict(session))
        
        # Check for invalid login        
        if user_admin.authoriseUserLogin(userName,userPassword) == False or user_admin.getStatusFromEmail(userName) == False:
            msg = 'Invalid Login Details'
            session.pop('useremail', None)            
            return render_template('login.html', msg=msg)
        else:            
            msg = ""
            return render_template('dashboard.html', msg=msg)

    return render_template('login.html', msg=msg)

# Forgot password     
@app.route("/forgotpassword", methods =["GET", "POST"])
def forgotPassword():
    msg = ""
    if request.method == 'POST':
        
        # Get the email address that has been entered to send the new password to 
        userEmailAddress = request.form.get("useremail")
        
        if user_admin.forgotPassword(userEmailAddress) == "":
            msg = "No Email Address Found"
            return render_template('forgotpass.html', msg=msg)
        else:
            msg = ("A new user password has been emailed to " +userEmailAddress)
            return render_template('forgotpass.html', msg=msg)
    
    return render_template('forgotpass.html', msg=msg)
    
# Dashboard app     
@app.route("/dashboard", methods =["GET", "POST"])
def dashboard():
    if 'useremail' in session:
        msg = ("You are logged in as " + session['useremail'])
        return render_template('dashboard.html', msg=msg)
    else:
        msg = 'You need to login'
        # return render_template('login.html', msg=msg)
        return redirect(url_for('login'))

# User Profile Page     
@app.route("/userprofile", methods=["GET", "POST"])
def userProfile():
    if 'useremail' in session:
        accountstatus = ""
        msg = ("You are logged in as " + session['useremail'])
        title = (user_admin.getTitleFromEmail(session['useremail']))
        surname = (user_admin.getSurnameFromEmail(session['useremail']))   
        firstname = (user_admin.getFirstnameFromEmail(session['useremail']))
        seclevel = (user_admin.getPermissionLevelFromEmail(session['useremail']))
        photo = ("/static/profileimg/")
        image = user_admin.getPhotoFromEmail(session['useremail'])
        if image != "":
            photo = (photo+image)
        else:
            photo = (photo+"noprofileimg.png")
        if user_admin.getStatusFromEmail(session['useremail']) == True:
            accountstatus = "ACTIVE"
        else:
            accountstatus = "INACTIVE"
        datecreated = user_admin.getDateCreatedFromEmail(session['useremail'])
            
        return render_template('userprofile.html', msg=msg, title=title, surname=surname, firstname=firstname, seclevel=seclevel, accountstatus=accountstatus, datecreated=datecreated, photo=photo)
    else:
        msg = 'You need to login'
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()