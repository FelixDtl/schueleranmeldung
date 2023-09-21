from flask import Flask, render_template, session, redirect, request
from flask_session import Session
import redis

from utils import addcompany
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
        session['start[typ]'] = eingabe
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

@app.route('/betrieb/neu', methods=['GET', 'POST'])
def betriebNeu():
    if request.method == 'POST':
        betriebName = request.form.get('betrieb[name]')
        session['betrieb_name'] = betriebName

        betriebStrasse = request.form.get('betrieb[strasse]')
        session['betrieb_strasse'] = betriebStrasse

        betriebHsnr = request.form.get('betrieb[hsnr]')
        session['betrieb_hsnr'] = betriebHsnr

        betriebPlz = request.form.get('betrieb[plz]')
        session['betrieb_plz'] = betriebPlz

        betriebOrt = request.form.get('betrieb[ort]')
        session['betrieb_ort'] = betriebOrt

        betriebTelZentrale = request.form.get('betrieb[telZentrale]')
        session['betrieb_telZentrale'] = betriebTelZentrale

        betriebKammer = request.form.get('betrieb[kammer]')
        session['betrieb_kammer'] = betriebKammer

        betriebAnsprPartner = request.form.get('betrieb[ansprPartner]')
        session['betrieb_ansprPartner'] = betriebAnsprPartner

        betriebTelDurchwahl = request.form.get('betrieb[telDurchwahl]')
        session['betrieb_telDurchwahl'] = betriebTelDurchwahl

        betriebFax = request.form.get('betrieb[fax]')
        session['betrieb_fax'] = betriebFax

        betriebEmail = request.form.get('betrieb[email]')
        session['betrieb_email'] = betriebEmail

        print(betriebEmail, betriebFax, betriebOrt, betriebKammer)
        addcompany.add_company_to_template(betriebOrt, betriebName, betriebStrasse, betriebHsnr)
        return render_template('ausbildung.html')

    return render_template('betrieb_neu.html')




@app.route('/Berufsintegrationsklasse', methods=['POST', 'GET'])
def berufsintegrationsklasse():
    if request.method == 'POST':
        deutschKenntnis = request.form.get('fluechtling[deutschKenntnis]')
        if deutschKenntnis == 'Keine Deutschkenntnisse':
            session['fluechtling_deutschKenntnis'] = 0
        elif deutschKenntnis == 'Sehr schlechte Deutschkenntnisse':
            session['fluechtling_deutschKenntnis'] = 1
        elif deutschKenntnis == 'Schlechte Deutschkenntnisse':
            session['fluechtling_deutschKenntnis'] = 2
        elif deutschKenntnis == 'Durchschnittliche Deutschkenntnisse':
            session['fluechtling_deutschKenntnis'] = 3
        elif deutschKenntnis == 'Gute Deutschkenntnisse':
            session['fluechtling_deutschKenntnis'] = 4
        elif deutschKenntnis == 'Sehr gute Deutschkenntnisse':
            session['fluechtling_deutschKenntnis'] = 5
        else:
            # Fallback für den Fall, dass keine der oben genannten Optionen ausgewählt wurde
            session['fluechtling_deutschKenntnis'] = -1

        fluechtlingAnmeldeStelle = request.form.get('fluechtling[anmeldeStelle]')
        session['fluechtling_anmeldeStelle'] = fluechtlingAnmeldeStelle

        fluechtlingAnsprechpartner = request.form.get('fluechtling[ansprechPartner]')
        session['fluechtling_ansprechPartner'] = fluechtlingAnsprechpartner

        fluechtlingTel = request.form.get('fluechtling[tel]')
        session['fluechtling_tel'] = fluechtlingTel

    eingabe = session.get('eingabe', 'Keine Eingabe vorhanden')
    return render_template('Berufsintegrationsklasse.html', eingabe=eingabe)


@app.route('/umschueler', methods=['GET', 'POST'])
def umschueler():
    if request.method == 'POST':
        umschueler_traeger = request.form.get('umschueler[traeger]')
        session['umschueler_traeger'] = umschueler_traeger
        umschueler_traegersitz = request.form.get('umschueler[traegersitz]')
        session['umschueler_traegersitz'] = umschueler_traegersitz
        umschueler_foedernummer = request.form.get('umschueler[foedernummer]')
        session['umschueler_foedernummer'] = umschueler_foedernummer

    eingabe = session.get('eingabe', 'Keine Eingabe vorhanden')
    return render_template('umschueler.html', eingabe=eingabe)


@app.route('/holztechnik', methods=['GET', 'POST'])
def holztechnik():
    if request.method == 'POST':
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
