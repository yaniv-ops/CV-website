from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
@app.route('/0')
def home():
    return render_template('theme-clean.html')

@app.route('/getPlotCSV') # this is a job for GET, not POST
def plot_csv():
    return send_file('yaniv.csv',
                     mimetype='text/csv',
                     attachment_filename='yaniv.csv',
                     as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
