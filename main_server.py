from flask import request, Flask, jsonify, session, make_response
from flask_mysqldb import MySQL

app = Flask(__name__)  

#config mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'udaan'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#initialize mysql
mysql = MySQL(app)

@app.route('/')
def home():
    found = False
    #create cursor
    cur = mysql.connection.cursor()

    #execute query
    result = cur.execute("SELECT * FROM admin")
    while result > 0:
        row = cur.fetchone()
        if request.authorization and request.authorization.username == row['name'] and request.authorization.password == row['password']:
            found = True
            break
        result = result-1

    #close the connection
    cur.close()

    if found:
        return ('API working')
    return make_response('Could Not Verify!',401,{'WWW-Authenticate' : 'Basic realm="Login Required"'})

@app.route('/add-asset',methods=['POST'])
def asset():
    found = False
    #create cursor
    cur = mysql.connection.cursor()

    #execute query
    result = cur.execute("SELECT * FROM admin")
    while result > 0:
        row = cur.fetchone()
        if request.authorization and request.authorization.username == row['name'] and request.authorization.password == row['password']:
            found = True
            break
        result = result-1

    #close the connection
    cur.close()

    if not found:
        return make_response('Could Not Verify!',401,{'WWW-Authenticate' : 'Basic realm="Login Required"'})

    data = request.get_json()
    assetId = data['assetId']
    description = data['description']

    #create cursor
    cur = mysql.connection.cursor()

    #execute query
    cur.execute("INSERT INTO assets(assetID,description) values(%s,%s)",(assetId, description))

    #commit to DB
    mysql.connection.commit()

    #close the connection
    cur.close()

    #flash('Asset Added to the database','success')
    return ('Asset Added to the database')

@app.route('/add-task',methods=['POST'])
def addTask():
    found = False
    #create cursor
    cur = mysql.connection.cursor()

    #execute query
    result = cur.execute("SELECT * FROM admin")
    while result > 0:
        row = cur.fetchone()
        if request.authorization and request.authorization.username == row['name'] and request.authorization.password == row['password']:
            found = True
            break
        result = result-1

    #close the connection
    cur.close()

    if not found:
        return make_response('Could Not Verify!',401,{'WWW-Authenticate' : 'Basic realm="Login Required"'})

    data = request.get_json()
    taskId = data['taskId']
    assetId = data['assetId']
    freq = data['freq']

    #create cursor
    cur = mysql.connection.cursor()

    #execute query
    cur.execute("INSERT INTO tasks(taskId,assetId,freq) values(%s,%s,%s)",(taskId,assetId, freq))

    #commit to DB
    mysql.connection.commit()

    #close the connection
    cur.close()

    return ('added task to the database')

@app.route('/add-worker',methods=['POST'])
def addWorker():
    found = False
    #create cursor
    cur = mysql.connection.cursor()

    #execute query
    result = cur.execute("SELECT * FROM admin")
    while result > 0:
        row = cur.fetchone()
        if request.authorization and request.authorization.username == row['name'] and request.authorization.password == row['password']:
            found = True
            break
        result = result-1

    #close the connection
    cur.close()

    if not found:
        return make_response('Could Not Verify!',401,{'WWW-Authenticate' : 'Basic realm="Login Required"'})

    data = request.get_json()
    workerId = data['workerId']
    name = data['name']
    skillset = data['skillset']

    #create cursor
    cur = mysql.connection.cursor()

    #execute query
    cur.execute("INSERT INTO workers(workerId,name,skillset) values(%s,%s,%s)",(workerId,name,skillset))

    #commit to DB
    mysql.connection.commit()

    #close the connection
    cur.close()
    return ('worker added successfully')

@app.route('/allocate-task',methods=['POST'])
def allocateTask():
    found = False
    #create cursor
    cur = mysql.connection.cursor()

    #execute query
    result = cur.execute("SELECT * FROM admin")
    while result > 0:
        row = cur.fetchone()
        if request.authorization and request.authorization.username == row['name'] and request.authorization.password == row['password']:
            found = True
            break
        result = result-1

    #close the connection
    cur.close()

    if not found:
        return make_response('Could Not Verify!',401,{'WWW-Authenticate' : 'Basic realm="Login Required"'})

    data = request.get_json()
    assetId = data['assetId']
    taskId = data['taskId']
    workerId = data['workerId']
    timeOfAllocation = data['timeOfAllocation']
    taskToBePerformedBy = data['taskToBePerformedBy']

    #create cursor
    cur = mysql.connection.cursor()

    #execute query
    cur.execute("INSERT INTO allocatetask(assetId,taskId,workerId,toa,ttbpb) values(%s,%s,%s,%s,%s)",(assetId,taskId,workerId,timeOfAllocation,taskToBePerformedBy))

    #commit to DB
    mysql.connection.commit()

    #close the connection
    cur.close()
    return ('allocated task to the user')

@app.route('/assets/all',methods=['GET'])
def showAssets():
    found = False
    #create cursor
    cur = mysql.connection.cursor()

    #execute query
    result = cur.execute("SELECT * FROM admin")
    while result > 0:
        row = cur.fetchone()
        if request.authorization and request.authorization.username == row['name'] and request.authorization.password == row['password']:
            found = True
            break
        result = result-1

    #close the connection
    cur.close()

    if not found:
        return make_response('Could Not Verify!',401,{'WWW-Authenticate' : 'Basic realm="Login Required"'})

    data = []
    #create cursor
    cur = mysql.connection.cursor()

    #execute query
    result = cur.execute("SELECT * FROM assets")
    while result > 0:
        row = cur.fetchone()
        data.append(row)
        result = result-1

    #close the connection
    cur.close()
    return jsonify(data)

@app.route('/get-tasks-for-worker/<workerId>',methods=['GET'])
def getTasksForWorker(workerId):
    found = False
    #create cursor
    cur = mysql.connection.cursor()

    #execute query
    result = cur.execute("SELECT * FROM admin")
    while result > 0:
        row = cur.fetchone()
        if request.authorization and request.authorization.username == row['name'] and request.authorization.password == row['password']:
            found = True
            break
        result = result-1

    #close the connection
    cur.close()

    if not found:
        return make_response('Could Not Verify!',401,{'WWW-Authenticate' : 'Basic realm="Login Required"'})

    data = []
    #create cursor
    cur = mysql.connection.cursor()

    #execute query
    result = cur.execute("SELECT * FROM allocatetask WHERE workerId like %s",[workerId])
    print(result)
    while result > 0:
        row = cur.fetchone()
        data.append(row)
        result = result-1

    #close the connection
    cur.close()
    return jsonify(data)

if __name__ == "__main__":
    app.secret_key = 'secret1'
    app.run()