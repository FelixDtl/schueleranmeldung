from flask import Flask, render_template, session, redirect, request
from flask_session import Session
import redis

from routing.routes import routes_index

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "redis"  # null, filesystem, redis, cookie ...
Session(app)

r = redis.Redis(host='localhost', port=6379, db=0)


@app.route('/', methods=['GET', 'POST'])
def index():  # put application's code here
    if request.method == 'POST':
        eingabe = request.form.get('start[typ]')
        # Speichern Sie die Eingabedaten in der Sitzung
        session['eingabe'] = eingabe
        redirect_target = routes_index(eingabe)
        return redirect(redirect_target)
    return render_template('index.html')


r = redis.Redis(host='localhost', port=6379, db=0)


@app.route('/set', methods=['POST'])
def set_data():
    data = request.json  # JSON-Daten von der Anfrage erhalten
    for key, value in data.items():
        r.set(key, value)  # Daten in Redis speichern
    return "Daten wurden in Redis gespeichert."


@app.route('/ausbildung', methods=['GET', 'POST'])
def ausbildung():
    if request.method == 'POST':
        ausbildung_betrieb = request.form.get('ausbildung[betrieb]')
        session['ausbildung_betrieb'] = ausbildung_betrieb

        ausbildung_ausbilderemail = request.form.get('ausbildung[ausbilderemail]')
        session['ausbildung_ausbilderemail'] = ausbildung_ausbilderemail

        ausbildung_beginn = request.form.get('ausbildung[beginn]')
        session['ausbildung_beginn'] = ausbildung_beginn

        ausbildung_ende = request.form.get('ausbildung[ende]')
        session['ausbildung_ende'] = ausbildung_ende

        ausbildung_beruf = request.form.get('ausbildung[beruf]')
        session['ausbildung_beruf'] = ausbildung_beruf

        eingabe = request.form.get('start[typ]')
        session['eingabe'] = eingabe
        redirect_target = routes_index(eingabe)

        print(ausbildung_ende, ausbildung_beruf, ausbildung_beginn, ausbildung_ausbilderemail, ausbildung_betrieb)
        return redirect(redirect_target)

    eingabe = session.get('eingabe', 'Keine Eingabe vorhanden')
    return render_template('ausbildung.html', eingabe=eingabe)


@app.route('/Berufsintegrationsklasse')
def berufintegrationsklasse():
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
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
