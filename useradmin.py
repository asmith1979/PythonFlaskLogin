# Script: UserAdmin.py
# Author: Andrew Smith
# Date: September 2024
# Description: User Administration back-end functionality

import random

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