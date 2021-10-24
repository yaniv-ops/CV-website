from flask import Flask, render_template, send_file, request, flash
import requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, TextAreaField
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField

url = "https://api.npoint.io/262095a444176df0c93e"

response = requests.get(url=url)
db = response.json()




app = Flask(__name__)
app.config['SECRET_KEY'] = "MY_SECRET"


class NamerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    e_mail = EmailField('Email ', validators=[DataRequired(), Email()])
   # message = StringField('Write your message here', validators=[DataRequired()])
    submit = SubmitField('Send message')
    text_area = TextAreaField("Write you're message", validators=[DataRequired()])

@app.route('/', methods=["GET", "POST"])
@app.route('/0', methods=["GET","POST"])
def home():
    msg_part_one = "Yaniv"
    msg_part_two = "Ayalon"
    form = NamerForm()
    if request.method == "POST":
        if form.is_submitted():
            print("submitted")
        if form.validate():
            print("valid")
        if form.validate_on_submit():
            print("okkokokokokokokokokokokokokoko")
            msg_part_one = "Message"
            msg_part_two = "Sent"
        else:
            msg_part_one= "Message"
            msg_part_two= "Failed to send"
        print(form.errors)

    return render_template('theme-clean.html', post=db, form=form, msg_one=msg_part_one, msg_two=msg_part_two)


@app.route('/getPlotCSV') # this is a job for GET, not POST
def plot_csv():
    return send_file('Yaniv_cv_il.docx',
                     mimetype='None',
                     attachment_filename='yaniv_cv_il.docx',
                     as_attachment=True)





if __name__ == '__main__':
    app.run(debug=True)
