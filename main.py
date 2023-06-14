from flask import request
from flask import Flask
from flask import render_template
import pyodbc
import os
from azure.storage.blob import BlobClient, BlobServiceClient
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
server = 'assignmentservershruthaja.database.windows.net'
database = 'assignment2'
username = 'shruthaja'
password = 'mattu4-12'
driver = '{ODBC Driver 17 for SQL Server}'

# Establish the connection
conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')

# Create a cursor object
cursor = conn.cursor()

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
print(cursor)
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    if request.method=='POST':
        query="select * from dbo.earthquake where dbo.earthquake.mag>5.0"
    return render_template("index.html")


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)