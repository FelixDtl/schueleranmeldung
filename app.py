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



    eingabe = session.get('eingabe', 'Keine Eingabe vorhanden')
    return render_template('ausbildung.html', eingabe=eingabe)


@app.route('/Berufsintegrationsklasse', methods=['POST', 'GET'])
def berufsintegrationsklasse():
    if request.method == 'POST':
        keineDeutschkenntnisse = request.form.get('fluechtling[deutschKenntnis]')
        session['fluechtling_deutschKenntnis_0'] = keineDeutschkenntnisse

        sehrSchlechteDeutschkenntnisse = request.form.get('fluechtling[deutschKenntnis]')
        session['fluechtling_deutschKenntnis_1'] = sehrSchlechteDeutschkenntnisse

        schlechteDeutschkenntnisse = request.form.get('fluechtling[deutschKenntnis]')
        session['fluechtling_deutschKenntnis_2'] = schlechteDeutschkenntnisse

        durchschnittlicheDeutschkenntnisse = request.form.get('fluechtling[deutschKenntnis]')
        session['fluechtling_deutschKenntnis_3'] = durchschnittlicheDeutschkenntnisse

        guteDeutschkenntnisse = request.form.get('fluechtling[deutschKenntnis]')
        session['fluechtling_deutschKenntnis_4'] = guteDeutschkenntnisse

        sehrGuteDeutschkenntnisse = request.form.get('fluechtling[deutschKenntnis]')
        session['fluechtling_deutschKenntnis_5'] = sehrGuteDeutschkenntnisse

        fluechtlingAnmeldeStelle = request.form.get('fluechtling[anmeldeStelle]')
        session['fluechtling_anmeldeStelle'] = fluechtlingAnmeldeStelle

        fluechtlingAnsprechpartner = request.form.get('fluechtling[ansprechPartner]')
        session['fluechtling_ansprechPartner'] = fluechtlingAnsprechpartner

        fluechtlingTel = request.form.get('fluechtling[tel]')
        session['fluechtling_tel'] = fluechtlingTel


    eingabe = session.get('eingabe', 'Keine Eingabe vorhanden')
    return render_template('Berufsintegrationsklasse.html', eingabe=eingabe)


@app.route('/umschueler')
def umschueler():
    eingabe = session.get('eingabe', 'Keine Eingabe vorhanden')
    return render_template('umschueler.html', eingabe=eingabe)


@app.route('/holztechnik', methods=['GET', 'POST'])
def holztechnik():
    if request.method =='POST':
        schueler_vorname = request.form.get('schueler[vorname]')
        session['schueler_vorname'] = schueler_vorname
        schueler_nachname = request.form.get('schueler[nachname]')
        session['schueler_nachname'] = schueler_nachname
        schueler_rufname = request.form.get('schueler[rufname]')
        session['schueler_rufname'] = schueler_rufname
        schueler_geschlecht = request.form.get('schueler[geschlecht]')
        session['schueler_geschlecht'] = schueler_geschlecht
        schueler_strasse = request.form.get('schueler[strasse]')
        session['schueler_strasse'] = schueler_strasse
        schueler_hsnr = request.form.get('schueler[hsnr]')
        session['schueler_hsnr'] = schueler_hsnr
        schueler_plz = request.form.get('schueler[plz]')
        session['schueler_plz'] = schueler_plz
        schueler_ort = request.form.get('schueler[ort]')
        session['schueler_ort'] = schueler_ort
        schueler_tel = request.form.get('schueler[tel]')
        session['schueler_tel'] = schueler_tel
        schueler_email = request.form.get('schueler[email]')
        session['schueler_email'] = schueler_email
        schueler_geburtsdatum = request.form.get('schueler[geburtsdatum]')
        session['schueler_geburtsdatum'] = schueler_geburtsdatum
        schueler_geburtsort = request.form.get('schueler[geburtsort]')
        session['schueler_geburtsort'] = schueler_geburtsort
        schueler_geburtsland = request.form.get('schueler[geburtsland]')
        session['schueler_geburtsland'] = schueler_geburtsland
        schueler_staatsangehoerigkeit = request.form.get('schueler[staatsangehoerigkeit]')
        session['schueler_staatsangehoerigkeit'] = schueler_staatsangehoerigkeit
        schueler_bekenntnis = request.form.get('schueler[bekenntnis]')
        session['schueler_bekenntnis'] = schueler_bekenntnis

    eingabe = session.get('eingabe', 'Keine Eingabe vorhanden')
    return render_template('holztechnik.html', eingabe=eingabe)


@app.route('/404')
def error():
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
