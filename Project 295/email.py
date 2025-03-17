import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def sendEmail(sender_email,rec,subject,body,smtp_server,smtp_port,smtp_user,smtp_password):
    message=MIMEMultipart()
    message['FROM']=sender_email
    message["TO"]=','.join(rec)
    message['Subject']=subject
    message.attach(MIMEText(body,'plain'))
    try:
        server=smtplib.SMTP(smtp_server,smtp_port)
        server.login(smtp_user,smtp_password)
        server.sendmail(sender_email,rec,message.as_string())
        print("Email send successfully")
    except Exception as e:
        print("Error",e)
    finally:
        server.quit()


sender_email=''
rec=['','']
sub="project"
body="hello gaurav tomar classes"
smtp_server='smtp.mailtrap.io'
smtp_port=2525
smtp_user='username'
smtp_password='2 step wala password'


sendEmail(sender_email,rec,sub,body,smtp_server,smtp_port,smtp_user,smtp_password)