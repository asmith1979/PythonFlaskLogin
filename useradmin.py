# Script: UserAdmin.py
# Author: Andrew Smith
# Date: September 2024
# Description: User Administration back-end functionality

import random
import hashlib
from datetime import datetime 

##################################
###  Back-end User Data Store  ###
##################################

userData = []

# Add User Data for Demonstration purpose
userData.append([1,"mel.gibson@mycompany.com", "b1de3dec47fd10a41669145570df961d", "Gibson", "Mel", "Mr", "077892456789", True, "03/23/2025", "SUPERADMIN"])
userData.append([2,"sly.stallone@mycompany.com", "b9eb312c6b776285dab43253df7c2c40", "Stallone", "Sly", "Mr", "079945646664", True, "03/23/2025", "SUPERADMIN"])
userData.append([3,"nicole.kidman@mycompany.com", "9c1d10fff0a08054dc4c808cd5ae8223", "Kidman", "Nicole", "Miss", "0749665223", False, "03/23/2025", "ADMIN"])
userData.append([4,"angelina.jolie@mycompany.com", "23915be13492eec1f39eacf8456574fc", "Jolie", "Angelina", "Miss", "0771233333", False, "03/23/2025", "ADMIN"])
userData.append([5,"john.travolta@mycompany.com", "0aaca691d1c853b17178c0ddda077796", "Travolta", "John", "Mr", "07749888999", False, "03/23/2025", "ADMIN"])
userData.append([6,"sandra.bullock@mycompany.com", "ff8062c7a0ceee303cf593309fca1b6b", "Bullock", "Sandra", "Miss", "079945512", False, "03/23/2025", "ADMIN"])
userData.append([7,"harrison.ford@mycompany.com", "b0dfcdfb749fb18159e2d61ead5f5e14", "Ford", "Harrison", "Mr", "07723478888", True, "03/23/2025", "STANDARD"])
userData.append([8,"ben.stiller@mycompany.com", "9bb374323c1860b999a403150d5de424", "Stiller", "Ben", "Mr", "079487789777", False, "03/23/2025", "STANDARD"])
userData.append([9,"chris.pratt@mycompany.com", "4f76aedd9220999a5731885ddcf51733", "Pratt", "Chris", "Mr", "0773574199", False, "03/23/2025", "STANDARD"])
userData.append([10,"adam.sandler@mycompany.com", "b53116f942177afdf4bfa41fb87ebc6c", "Sandler", "Adam", "Mr", "07900886677", False, "03/23/2025", "STANDARD"])

##############################################
###  Private Back-end admin functionality  ###
##############################################

# Function: generatePassword
# Description: Generates a secure password
def generatePassword():
    genPassword = "12345678"
    
    alphaUpper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphaLower="abcdefghijklmnopqrstuvwxyz"
    numbers="0123456789"
    specialChars="@!~#"
    
    # Get first random character
    elementNo = random.randrange(0,len(alphaUpper))
    firstCharacter = alphaUpper[elementNo]
    
    # Get second random character 
    elementNo = random.randrange(0,len(alphaLower))
    secondCharacter = alphaLower[elementNo]
    
    # Get third random character 
    elementNo = random.randrange(0,len(numbers))
    thirdCharacter = numbers[elementNo]
    
    # Get fourth random character 
    elementNo = random.randrange(0,len(specialChars))
    fourthCharacter = specialChars[elementNo]
    
    # Get fifth random character 
    elementNo = random.randrange(0,len(alphaUpper))
    fifthCharacter = alphaUpper[elementNo]
    
    # Get sixth random character 
    elementNo = random.randrange(0,len(alphaLower))
    sixthCharacter = alphaLower[elementNo]
    
    # Get seventh random character 
    elementNo = random.randrange(0,len(numbers))
    seventhCharacter = numbers[elementNo]
    
    # Get eigth random character 
    elementNo = random.randrange(0,len(specialChars))
    eigthCharacter = specialChars[elementNo]
    
    genPassword=(firstCharacter+secondCharacter+thirdCharacter+fourthCharacter+fifthCharacter+sixthCharacter+seventhCharacter+eigthCharacter)
    
    return genPassword
    
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
        # Get the password stored in the user data 
        storedEncryptedPassword = userData[recordFound][2]
        
        if encUserPassword == storedEncryptedPassword:
            authorisedLogin = True

    return authorisedLogin
    
def getUserEmailAddress(emailAddressIn):
    global userData
    # A blank email address represents a null value - no email address found 
    emailAddressReturn = ""
    
    recordNo = 0
    dataStoreLength = len(userData)
    
    while recordNo < (dataStoreLength):
        if userData[recordNo][1] == emailAddressIn:
            emailAddressReturn = userData[recordNo][1]
            break    
            
        recordNo = recordNo + 1
    
    return emailAddressReturn 
    
    

def forgotPassword(emailAddressIn):
    # Detect if email address is in the data store to send
    emailAddr = getUserEmailAddress(emailAddressIn)
    newUserPassword = ""
    
    # Generate password if email address exists in userData 
    if emailAddr != "":
        newUserPassword = generatePassword()
        
        # Encrypt password to MD5 Hash 
        encryptedResult = hashlib.md5(newUserPassword.encode())
        encryptedPassword = encryptedResult.hexdigest()
        
        # Update encrypted password in the data store 
        recordNo = 0
        dataStoreLength = len(userData)
    
        while recordNo < (dataStoreLength):
            if userData[recordNo][1] == emailAddr:
                userData[recordNo][2] = encryptedPassword
                break    
            
            recordNo = recordNo + 1        
    
        print("New Password for " + emailAddr + " is " + newUserPassword)
    
    return emailAddr

################################################
###  Administration Dashboard Functionality  ###
################################################

# Function Name: addUserToDataStore
# Function Description: A function used to add a user to the user data store collection
# Function Parameters (input): email address, surname, firstname, title, phone number, active state, user account type 
def addUserToDataStore(emailAddressIn, surnameIn, firstnameIn, titleIn, phoneNoIn, activeIn, userAccountTypeIn):

    ##################################
    ###  Create Automated Details  ###
    ##################################
    
    # Get / Create new User ID
    newUserID = userData[(len(userData)-1)][0]
    # print("New User ID: " + str(newUserID))    

    # Get new user password 
    newUserPassword = generatePassword()    
    
    # Encrypt new user password to be stored in the data store in encrypted format 
    encryptedResult = hashlib.md5(newUserPassword.encode())
    encryptedPassword = encryptedResult.hexdigest()
    
    # print("New Password: " + str(encryptedPassword))
    
    # Get Formatted creation date 
    nowDateTime = datetime.now()
    formattedNowDateTime = nowDateTime.strftime("%Y-%m-%d %H:%M:%S")
    
    # print("Date Time: " + formattedNowDateTime)
    
    # Add New User details to the user data store 
    userData.append([newUserID, emailAddressIn, encryptedPassword, surnameIn, firstnameIn, titleIn, phoneNoIn, activeIn, formattedNowDateTime, userAccountTypeIn])
    
    

