# Script: rspadmin.py
# Author: Andrew Smith
# Date: September 2024
# Description: RSP Admin application

import oracledb

# Open connection to the database
dbConnection = oracledb.connect(user="REQUEST3", password="request3",dsn="localhost/xepdb1")





# Close the database connection
dbConnection.close()