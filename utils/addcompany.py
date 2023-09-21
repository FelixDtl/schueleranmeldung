from bs4 import BeautifulSoup

def add_company_to_template(ort, name, strasse, hnr):
    # HTML-Datei einlesen (ersetzen Sie 'beispiel.html' durch den Pfad zu Ihrer HTML-Datei)
    with open('templates/betrieb.html', 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()

    # BeautifulSoup-Objekt erstellen
    soup = BeautifulSoup(html_content, 'html.parser')

    optgroup = soup.find('optgroup', label=ort)

    new_option = soup.new_tag('option')
    new_option.string = name, strasse, hnr  # Set the text content

    # Append the new <option> element to the <optgroup>
    optgroup.append(new_option)

