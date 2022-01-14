import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

class SendMail:
    def __init__(self, from_mail, pass_mail, to_mail, subject_mail, body_mail):
        self.from_mail = from_mail
        self.pass_mail = pass_mail
        self.to_mail = to_mail
        self.subject_mail = subject_mail
        self.body_mail = body_mail
        self.mail = MIMEMultipart()
        self.server = smtplib.SMTP('smtp.gmail.com', '587')
        self.server.starttls()

    def config_mail(self):
        self.mail['From'] = self.from_mail
        self.mail['To'] = self.to_mail
        self.mail['Subject'] = self.subject_mail
        self.mail.attach(MIMEText(self.body_mail, 'plain'))

    def send_mail(self):
        self.server.login(self.mail['From'], self.pass_mail)
        file = open(os.getcwd()+'\\files\\VagasCadmus.xlsx', 'rb')
        app = MIMEApplication(file.read(), 'py')
        app.add_header('Content-Disposition', 'attachment;filename=seu_arquivo.py')
        self.mail.attach(app)
        self.server.sendmail(self.mail['From'], self.mail['To'], self.mail.as_string())
        self.server.quit()