# Email sender that sends emails based on the given parameters
import smtplib
import ssl
from email.message import EmailMessage

from flask import jsonify

from config import EMAIL_SENDER, EMAIL_PASSWORD, SMTP_PORT, SMTP_SERVER


class EmailSender:
    def __init__(self):
        pass

    def send_email(self, email_receiver: str, auth_key: str):
        em = EmailMessage()
        em['From'] = EMAIL_SENDER
        em['To'] = email_receiver
        em['Subject'] = "Twój kod weryfikacyjny"
        em.set_content(f"Twój kod: {auth_key}")
        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as smtp:
                smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
                smtp.sendmail(EMAIL_SENDER, email_receiver, em.as_string())
                return jsonify({"message": f"Email sent successfully to {email_receiver}"}), 200

        except smtplib.SMTPException as e:
            return jsonify(f"Błąd SMTP: {e}"), 400
        except Exception as e:
            return jsonify(f"Nieoczekiwany bląd: {e}"), 400
