from flask import Flask, render_template, send_file
import requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField

url = "https://api.npoint.io/262095a444176df0c93e"

response = requests.get(url=url)
db = response.json()




app = Flask(__name__)
app.config['SECRET_KEY'] = "MY_SECRET"

msg_sent = 'msg has sent'
class NamerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    e_mail = EmailField('Email', validators=[DataRequired(), Email()])
    message = StringField('Write your message here', validators=[DataRequired()])
    submit = SubmitField('Send message')

@app.route('/', methods=["GET", "POST"])
@app.route('/0', methods=["GET","POST"])
def home():
    form = NamerForm()
    if form.validate_on_submit():
        form.submit.label = 'msg_sent'
    return render_template('theme-clean.html', post=db, form=form)

@app.route('/getPlotCSV') # this is a job for GET, not POST
def plot_csv():
    return send_file('Yaniv_cv_il.docx',
                     mimetype='None',
                     attachment_filename='yaniv_cv_il',
                     as_attachment=True)





if __name__ == '__main__':
    app.run(debug=True)
