import smtplib
# Set Global Variables
gmail_user = 'mygmail@gmail.com'
gmail_password = 'mygmailpassword'
# Create Email
mail_from = gmail_user
mail_to = 'destinationemail@gmail.com'

mail_subject = f'My Email Subject'
mail_message_body = 'Hi,\n\n You can Download Call Back report from link : https://192.168.0.1/CallBackReport/1.txt'

mail_message = '''\
From: %s
To: %s
Subject: %s
%s
''' % (mail_from, mail_to, mail_subject, mail_message_body)
# Sent Email
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(gmail_user, gmail_password)
server.sendmail(mail_from, mail_to, mail_message)
server.close()
