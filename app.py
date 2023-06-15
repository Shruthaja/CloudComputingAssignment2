import pyodbc
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
server = 'assignmentservershruthaja.database.windows.net'
database = 'assignment2'
username = 'shruthaja'
password = 'mattu4-12'
driver = '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')

cursor = conn.cursor()


@app.route('/', methods=['GET', 'POST'])
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    result = []
    if request.method == 'POST':
        query = "select * from dbo.earthquake where dbo.earthquake.mag>5.0"
        cursor.execute(query)
        result = cursor.fetchall()
    return render_template("index.html", result=result)


@app.route('/page2.html', methods=['GET', 'POST'])
def page2():
    result = []
    if request.method == "POST":
        mag = request.form['mag']
        ranje = request.form['range']
        ranje = int(ranje)
        ranje = -1 * ranje
        latest_date = '2023-06-11T19:11:07.423Z'
        query = "select * from dbo.earthquake WHERE dbo.earthquake.time >= DATEADD(DAY , ? , '2023-06-11T19:11:07.423Z') AND time <= '2023-06-11T19:11:07.423Z' and dbo.earthquake.mag=?;"
        cursor.execute(query, ranje, mag)
        result = cursor.fetchall()
    return render_template("page2.html", result=result)


@app.route('/page3.html', methods=['GET', 'POST'])
def page3():
    result = []
    if request.method == "POST":
        lat = request.form['lat']
        long = request.form['long']
        distance = request.form['distance']
        query = "SELECT * FROM [dbo].[earthquake] WHERE ( 6371 * ACOS(COS(RADIANS(latitude)) * COS(RADIANS(?)) * COS(RADIANS(longitude) - RADIANS(?)) + SIN(RADIANS(latitude)) * SIN(RADIANS(?)) )) <=? ;"
        cursor.execute(query, lat, long, lat, distance)
        result = cursor.fetchall()
    return render_template("page3.html", result=result)


@app.route('/page4.html', methods=['GET', 'POST'])
def page4():
    # result = []
    # smagnum = ''
    # emagnum = ''
    # if request.method == "POST":
    #     smagnum = request.form['smagnum']
    #     emagnum = request.form['emagnum']
    #     query = "Select latitude,longitude,mag from dbo.earthquake where mag between ? and ? and  ( 6371 * ACOS(COS(RADIANS(latitude)) * COS(RADIANS(?)) * COS(RADIANS(longitude) - RADIANS(?)) + SIN(RADIANS(latitude)) * SIN(RADIANS(?)) )) <=? "
    #     lat = "61.051700592041"
    #     long = "-151.144195556641"
    #     distance = "200"
    #     cursor.execute(query, smagnum, emagnum, lat, long, lat, distance)
    #     result = cursor.fetchall()
    #     result1 = [{}]
    #     for i in result:
    #         i = list(i)
    #         result1.append({"x": i[0], "y": i[1], "z": i[2]})
    #     result1.pop()
    #     return render_template("page4.html", result=result1, smagnum=smagnum, emagnum=emagnum)
    return render_template("page4.html")

@app.route('/page5.html', methods=['GET', 'POST'])
# ‘/’ URL is bound with hello_world() function.
def page5():
    result = []
    result1 = []
    if request.method == 'POST':
        query = "SELECT CASE WHEN DATEPART(HOUR, [time]) >= 18 OR DATEPART(HOUR, [time]) < 6 THEN 'Night-time (6 PM - 6 AM)' ELSE 'Day-time (6 AM - 6 PM)' END AS time_range, COUNT(*) AS earthquake_count FROM [dbo].[earthquake] WHERE mag > 4 GROUP BY CASE WHEN DATEPART(HOUR, [time]) >= 18 OR DATEPART(HOUR, [time]) < 6 THEN 'Night-time (6 PM - 6 AM)' ELSE 'Day-time (6 AM - 6 PM)' END;"
        cursor.execute(query)
        result = cursor.fetchall()
        query = "SELECT CASE WHEN DATEPART(HOUR, [time]) >= 18 OR DATEPART(HOUR, [time]) < 6 THEN 'Night-time (6 PM - 6 AM)' ELSE 'Day-time (6 AM - 6 PM)' END AS time_range, [time], [latitude], [longitude], [depth], [mag], [magType], [nst], [gap], [dmin], [rms], [net], [id], [updated], [place], [type], [horizontalError], [depthError], [magError], [magNst], [status], [locationSource], [magSource] FROM [dbo].[earthquake] WHERE mag > 4 GROUP BY CASE WHEN DATEPART(HOUR, [time]) >= 18 OR DATEPART(HOUR, [time]) < 6 THEN 'Night-time (6 PM - 6 AM)' ELSE 'Day-time (6 AM - 6 PM)' END, [time], [latitude], [longitude], [depth], [mag], [magType], [nst], [gap], [dmin], [rms], [net], [id], [updated], [place], [type], [horizontalError], [depthError], [magError], [magNst], [status], [locationSource], [magSource];"
        cursor.execute(query)
        result1 = cursor.fetchall()
    return render_template("page5.html", result=result, result1=result1)


if __name__ == '__main__':
    app.run(debug=True)
