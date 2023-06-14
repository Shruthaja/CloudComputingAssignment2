from flask import request
from flask import Flask
from flask import render_template
from flask_cdn import CDN
cdn = CDN()
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
@app.route('/',methods=['GET','POST'])
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    result=[]
    if request.method=='POST':
        query="select * from dbo.earthquake where dbo.earthquake.mag>5.0"
        cursor.execute(query)
        result=cursor.fetchall()
    return render_template("index.html",result=result)
@app.route('/page2.html',methods=['GET','POST'])
def page2():
    result=[]
    if request.method=="POST":
        mag=request.form['mag']
        ranje=request.form['range']
        ranje=int(ranje)
        ranje=-1*ranje
        latest_date='2023-06-11T19:11:07.423Z'
        query="select * from dbo.earthquake WHERE dbo.earthquake.time >= DATEADD(DAY , ? , '2023-06-11T19:11:07.423Z') AND time <= '2023-06-11T19:11:07.423Z' and dbo.earthquake.mag=?;"
        cursor.execute(query,ranje,mag)
        result=cursor.fetchall()
    return render_template("page2.html",result=result)
if __name__ == '__main__':
    cdn.init_app(app)
    app.run(debug=True)