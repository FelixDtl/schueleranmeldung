
from flask import Flask, render_template, session, redirect, request
from flask_session import Session
import redis

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "redis" # null, filesystem, redis, cookie ...
Session(app)


@app.route('/', methods=['GET', 'POST'])
def index():  # put application's code here
    if request.method == 'POST':
        eingabe = request.form.get('start[typ]')
        # Speichern Sie die Eingabedaten in der Sitzung
        session['eingabe'] = eingabe
        return redirect('/ausbildung')
    return render_template('index.html')



@app.route('/ausbildung')
def ausbildung():  # put application's code here
        print(session['eingabe'])
        # Abrufen der in der Sitzung gespeicherten Daten
        eingabe = session.get('eingabe', 'Keine Eingabe vorhanden')
        return render_template('ausbildung.html', eingabe=eingabe)

if __name__ == '__main__':
    app.run()
