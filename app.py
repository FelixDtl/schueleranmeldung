from flask import Flask, render_template, session, redirect, request
from flask_session import Session
import redis

from routing.routes import routes_index

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "redis" # null, filesystem, redis, cookie ...
Session(app)

r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/', methods=['GET', 'POST'])
def index():  # put application's code here
    if request.method == 'POST':
        eingabe = request.form.get('start[typ]')
        # Speichern Sie die Eingabedaten in der Sitzung
        session['eingabe'] = eingabe
        redirect_target=routes_index(eingabe)
        return redirect(redirect_target)
    return render_template('index.html')

r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/set', methods=['POST'])
def set_data():
    data = request.json  # JSON-Daten von der Anfrage erhalten
    for key, value in data.items():
        r.set(key, value)  # Daten in Redis speichern
    return "Daten wurden in Redis gespeichert."




@app.route('/ausbildung')
def ausbildung():  # put application's code here
        print(session['eingabe'])
        # Abrufen der in der Sitzung gespeicherten Daten
        eingabe = session.get('eingabe', 'Keine Eingabe vorhanden')
        return render_template('ausbildung.html', eingabe=eingabe)

@app.route('/Berufsintegrationsklasse')
def berufintegrationsklasse():
    print(session['eingabe'])
    eingabe = session.get('eingabe', 'Keine Eingabe vorhanden')
    return render_template('Berufsintegrationsklasse.html', eingabe=eingabe)



@app.route('/umschueler')
def umschueler():
    eingabe = session.get('eingabe', 'Keine Eingabe vorhanden')
    return render_template('umschueler.html', eingabe=eingabe)


@app.route('/holztechnik')
def holztechnik():
    eingabe = session.get('eingabe', 'Keine Eingabe vorhanden')
    return render_template('holztechnik.html', eingabe=eingabe)


@app.route('/Berufsintegrationsklasse')
def berufsintegrationsklasse():
    eingabe = session.get('eingabe', 'Keine Eingabe vorhanden')
    return render_template('Berufsintegrationsklasse.html', eingabe=eingabe)

@app.route('/404')
def error():
    return render_template('404.html')

if __name__ == '__main__':
    app.run()
