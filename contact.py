import smtplib
from email.message import EmailMessage

def contact_me(subject, user_mail, contents, my_mail, my_pass):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg['From'] = my_mail
    msg["To"] = my_mail
    msg.set_content(contents)
    print(msg["Subject"])
    print(msg["From"])
    print(msg["To"])

    try:
        with smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465) as connection:
            connection.login(my_mail, my_pass)
            connection.send_message(msg)
            print('msg sent!!!')
    except:
        print("Something went wrong!!!")
