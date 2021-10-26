from flask import Flask, render_template, send_file
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, validators
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField
import requests

url = "https://api.npoint.io/262095a444176df0c93e"

response = requests.get(url=url)
db = response.json()

app = Flask(__name__)
app.config['SECRET_KEY'] = "MYSECRETKEY"

class NamerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    e_mail = EmailField('Email ', validators=[DataRequired(), Email()])
    submit = SubmitField('Send message')
    text_area = TextAreaField("Write you're message", validators=[DataRequired()])

@app.route('/', methods=["GET", "POST"])
@app.route('/Home/', methods=["GET","POST"])
def home_page():




@app.route('/getPlotCSV') # this is a job for GET, not POST
def plot_csv():
    return send_file('Yaniv_cv_il.docx',
                     mimetype='None',
                     attachment_filename='yaniv_cv_il.docx',
                     as_attachment=True)





if __name__ == '__main__':
    app.run(debug=True)
