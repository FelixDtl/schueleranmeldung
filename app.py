from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ausbildung')
def ausbildung():  # put application's code here
    return render_template('ausbildung.html')



# Konstruktorfunktion
if __name__ == '__main__':
    app.run()
