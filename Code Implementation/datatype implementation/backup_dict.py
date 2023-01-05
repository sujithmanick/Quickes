import shelve
from flask import session
"""from email.mime.text import MIMEText
import smtplib
def send_email(reciveremail):
    try:
        with open('input','rb') as fp:
            k=pickle.load(fp)
        smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
        smtp_ssl_port = 465
        username = 'sailatindia@gmail.com'
        password = 'szxnjzxxwvitcrnr'
        sender = 'sailatindia@gmail.com '
        targets = reciveremail
        targets=targets.casefold()
        if targets not in k:
            k.append(targets)
            with open('input','wb') as fp1:
                pickle.dump(k,fp1)
            name=targets.split('@')
            name=name[0]
            session['name1']=name
            msg = MIMEText('Hello  {} !,Welcome to Sail India Enjoy your ride with SailIndia And Explore Incredible India.Here after you will receive our site updates of our site .Once again Enjoy travel Around INDIA.   \n \n\n                          Thank You  \n\n \n                                                 -Team Sail India'.format(name))
            msg['Subject'] = 'Sail_INDIA -Reg'
            msg['From'] = sender
            msg['To'] = targets

            server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
            server.login(username, password)
            server.sendmail(sender, targets, msg.as_string())
            server.quit()

    except :
        with open('input','wb') as fp:
            pickle.dump([],fp)
        with open('input','rb') as fp:
            k=pickle.load(fp)
        smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
        smtp_ssl_port = 465
        username = 'sailatindia@gmail.com '
        password = 'svd@sailatindia'
        sender = 'sailatindia@gmail.com '
        targets = reciveremail
        targets=targets.casefold()
        if targets not in k:
            k.append(targets)
            with open('input','wb') as fp1:
                pickle.dump(k,fp1)
            name=targets.split('@')
            session['name1']=name
            name=name[0]
            msg = MIMEText('Hello  {} !,Welcome to Sail India Enjoy your ride with SailIndia And Explore Incredible India.Here after you will receive our site updates of our site .Once again Enjoy travel Around INDIA.   \n \n\n                            Thank You  \n\n \n                                                   -Team Sail India'.format(name))
            msg['Subject'] = 'Sail_INDIA -Reg'
            msg['From'] = sender
            msg['To'] = targets

            server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
            server.login(username, password)
            server.sendmail(sender, targets, msg.as_string())
            server.quit()"""

"""usr_name= input()
usr_id= input()
Password= input()
s = shelve.open('backup_test.db')
try:
    s[usr_id] = { 'user_name': usr_name, 'user_id':usr_id, 'password':Password }
finally:
    s.close()"""


key=input()
s = shelve.open('backup_test.db')
try:
    existing = s[key]
finally:
    s.close()

print(existing['password'])

