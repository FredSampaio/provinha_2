#importa modulos de email
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

import pegaremail
import socket as s

temp=s.socket(s.AF_INET, s.SOCK_DGRAM)
temp.connect(("8.8.8.8",80))
ip=temp.getsockname()[0]
temp.close()

print(ip)

email, assunto, content=pegaremail.pegaemail(ip, 80)


# dados
body = content
sub = assunto
mail_from = 'freddysampaio9@gmail.com'
mail_to = email
pwd = 'fantauva'


# preeenchendo os dados
msg = MIMEMultipart('related')
msg['From'] = mail_from
msg['To'] = mail_to
msg['Subject'] = sub
msg.attach(MIMEText(body, 'plain'))


# envia email
# importa biblioteca
import smtplib
# altorizacao e autenticacao
smtp = smtplib.SMTP('smtp.gmail.com',587)
smtp.ehlo()
smtp.starttls()
smtp.login(mail_from, pwd)
smtp.sendmail(mail_from, mail_to, msg.as_string())
smtp.quit()
