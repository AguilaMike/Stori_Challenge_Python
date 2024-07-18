from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader
import smtplib

class SMTPEmailSender:
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def send_summary(self, to, summary_info):    
        msg = MIMEMultipart()
        msg["From"] = self.user
        msg["To"] = to
        msg["Subject"] = "Resumen de transacciones"
        
        env = Environment(loader=FileSystemLoader("templates"))
        template = env.get_template("email_template.html")
        html_content = template.render(summary_info=summary_info)

        body = html_content
        msg.attach(MIMEText(body, "html"))  # Usar formato HTML para la plantilla

        with smtplib.SMTP(self.host, self.port) as server:
            server.starttls()
            server.login(self.user, self.password)
            server.send_message(msg)