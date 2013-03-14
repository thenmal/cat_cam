from flask import Flask
from flask import render_template
from flask import session

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!7mN]LWX/,?RT'
count = 0
queue = []

@app.route('/')
def hello_world():
    global count
    if 'number' not in session:
        session['number'] = count
        queue.append(count)
        count += 1
    if session['number'] not in queue:
        session['number'] = count
        count += 1
        queue.append(session['number'])
    pos = queue.index(session['number']) + 1
    length = len(queue)
    return render_template('home.html', pos=pos, length=length)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
