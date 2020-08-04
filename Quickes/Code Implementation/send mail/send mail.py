from flask import session
import smtplib
from email.mime.text import MIMEText

def send_email(reciveremail,name):
    try:
        smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
        smtp_ssl_port = 465
        username = 'contactquickes@gmail.com'
        password = 'Suji@2407'
        sender = 'contactquickes@gmail.com'
        targets = reciveremail
        msg = MIMEText('Hello  {} !,Welcome to Quickes ! Stay updated anywhere.Here after you will receive our site updates of our site.        Stay safe and stay updated.   \n \n\n                          Thank You  \n\n \n                                                 - visit again : {}'.format(name,'http://quickes.pythonanywhere.com/'))
        msg['Subject'] = 'Quickes-Reg'
        msg['From'] = sender
        msg['To'] = targets

        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        server.login(username,password)
        server.sendmail(sender,targets,msg.as_string())
        server.quit()
    except Exception as e:
        print(e)

send_email('sujithmanick@gmail.com','suji')

    
