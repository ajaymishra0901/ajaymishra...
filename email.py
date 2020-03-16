#importing smtplib
import smtplib

#write content
content = 'hello, sending mail from python code'
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()

#for login
mail.login('@gmail.com', password)
mail.sendmail('@gmail.com', '@gmail.com', content)

#closing mail
mail.close()
