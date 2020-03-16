import smtplib

content = 'hello, sending mail from python code'
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()

mail.login('@gmail.com', password)
mail.sendmail('@gmail.com', '@gmail.com', content)

mail.close()
