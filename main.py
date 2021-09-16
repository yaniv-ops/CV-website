from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/0')
def home():
    return render_template('theme-clean.html')

if __name__ == '__main__':
    app.run(debug=True)
