from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    cnt = sqlite3.connect('topics.db')
    result = cnt.execute('SELECT * FROM topic')
    rows = result.fetchall()
    contents = '<h1><a href="/"Web</a></h1>'
    contents += '<ol>'
    
    for id, title,body in topics: 
        contents += '<li><a href="/read/'+str(id)+'">'+title+'</a></li>'
    contents += '</ol>'
    contents +='<h2>Welcome</h2>Hello, WEB'
    return "Hello Flask"
app.run(debug = True)