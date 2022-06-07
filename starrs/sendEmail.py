
# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib

def sendEmail(email, id, password): 
    # creates SMTP session
    s = smtplib.SMTP('smtp-mail.outlook.com', 587)
  
    # start TLS for security
    s.starttls()
  
    # Authentication
    s.login("random.t4@outlook.com", "starrs1234")

    SUBJECT='Starss application ID: {}'.format(id)

    TEXT='Welcome, your password is {}'.format(password)
  
    # message to be sent
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

    recepient = '{}'.format(email)

    # sending the mail
    s.sendmail("random.t4@outlook.com", recepient, message)
  
    # terminating the session
    s.quit()

    print('Email sent!')

# sendEmail('mitsuy@gmail.com','1','098765')