# Script: mainpage.py
# Author: Andrew Smith
# Date: September 2024
# Description: Main landing page

from flask import Flask, render_template, request, redirect, url_for
import hashlib

userData = []

# Add User Data for Demonstration purpose
userData.append([1,"mel.gibson@mycompany.com", "b1de3dec47fd10a41669145570df961d", "Gibson", "Mel", "Mr", "077892456789", 1, "03/23/2025", 1, 1, 1, 1, "null"])
userData.append([2,"sly.stallone@mycompany.com", "b9eb312c6b776285dab43253df7c2c40", "Stallone", "Sly", "Mr", "079945646664", 1, "03/23/2025", 1, 1, 1, 1, "null"])
userData.append([3,"nicole.kidman@mycompany.com", "9c1d10fff0a08054dc4c808cd5ae8223", "Kidman", "Nicole", "Miss", "0749665223", 0, "03/23/2025", 1, 1, 0, 0, "null"])
userData.append([4,"angelina.jolie@mycompany.com", "23915be13492eec1f39eacf8456574fc", "Jolie", "Angelina", "Miss", "0771233333", 0, "03/23/2025", 1, 1, 0, 0, "null"])
userData.append([5,"john.travolta@mycompany.com", "0aaca691d1c853b17178c0ddda077796", "Travolta", "John", "Mr", "07749888999", 0, "03/23/2025", 1, 1, 0, 1, "null"])
userData.append([6,"sandra.bullock@mycompany.com", "ff8062c7a0ceee303cf593309fca1b6b", "Bullock", "Sandra", "Miss", "079945512", 0, "03/23/2025", 1, 1, 0, 1, "null"])
userData.append([7,"harrison.ford@mycompany.com", "b0dfcdfb749fb18159e2d61ead5f5e14", "Ford", "Harrison", "Mr", "07723478888", 1, "03/23/2025", 1, 1, 1, 1, "null"])
userData.append([8,"ben.stiller@mycompany.com", "9bb374323c1860b999a403150d5de424", "Stiller", "Ben", "Mr", "079487789777", 0, "03/23/2025", 1, 1, 0, 1, "null"])
userData.append([9,"chris.pratt@mycompany.com", "4f76aedd9220999a5731885ddcf51733", "Pratt", "Chris", "Mr", "0773574199", 0, "03/23/2025", 1, 1, 0, 1, "null"])
userData.append([10,"adam.sandler@mycompany.com", "b53116f942177afdf4bfa41fb87ebc6c", "Sandler", "Adam", "Mr", "07900886677", 0, "03/23/2025", 1, 1, 0, 1, "null"])

app = Flask(__name__)

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ""
    if request.method == 'POST':
        
        # getting input with name = fname in HTML form
        userName = request.form.get("useremail")
        # getting input with name = lname in HTML form 
        userPassword = request.form.get("password")    
        
        # Check for invalid login 
        if authoriseUserLogin(userName,userPassword) == False:
            msg = 'Invalid Login Details'
            render_template('login.html', msg=msg)
        else:
            msg = ""
            return render_template('dashboard.html', msg=msg)

    return render_template('login.html', msg=msg)

# A function used to authorise user login     
def authoriseUserLogin(userIn, passwordIn):
    # Make user data accessible
    global userData
    authorisedLogin=False 
    indexCounter = 0
    recordFound = -1 # Identifies if record found
    
    # Get the MD5 hash equivelant....
    
    encryptedResult = hashlib.md5(passwordIn.encode())    
    encUserPassword = encryptedResult.hexdigest()
    
    # Get the user password if it exists in the data 
    while indexCounter < len(userData):
        if userData[indexCounter][1] == userIn:
            recordFound = indexCounter
        indexCounter = indexCounter + 1
        
    if recordFound > -1:
        # Get the password stored in the data 
        storedEncryptedPassword = userData[recordFound][2]
        
        if encUserPassword == storedEncryptedPassword:
            authorisedLogin = True

    return authorisedLogin

# Forgot password     
@app.route("/forgotpassword", methods =["GET", "POST"])
def forgotPassword():
    return render_template('forgotpass.html')
    
# Dashboard app     
@app.route("/dashboard", methods =["GET", "POST"])
def dashboard():
    return render_template('dashboard.html')
    
if __name__ == '__main__':
    app.run()