from bs4 import BeautifulSoup

# HTML-Datei einlesen (ersetzen Sie 'beispiel.html' durch den Pfad zu Ihrer HTML-Datei)
with open('templates/betrieb.html', 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

# BeautifulSoup-Objekt erstellen
soup = BeautifulSoup(html_content, 'html.parser')

optgroup = soup.find('optgroup', label='Wonsees')

new_option = soup.new_tag('option')
new_option['value'] = 'NEW_VALUE'  # Set the value attribute
new_option.string = 'New Option Text'  # Set the text content

# Append the new <option> element to the <optgroup>
optgroup.append(new_option)

print(soup)



