# Email sender that sends emails based on the given parameters

import os
from email.message import EmailMessage
import ssl
import smtplib
from config import EMAIL_SENDER, EMAIL_PASSWORD, SMTP_PORT, SMTP_SERVER
import mimetypes
import requests
import logging

logging.basicConfig(
    level=logging.INFO,  # INFO -> Będziemy widzieć komunikaty o wysyłce i błędach
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]  # Logi będą widoczne w Dockerze
)


class EmailSender:
    def __init__(self):
        pass

    def send_email(self, email_receiver: str, auth_key: str) -> None:
        logging.info(f"Przygotowywanie e-maila do: {email_receiver}")

        em = EmailMessage()
        em['From'] = EMAIL_SENDER
        em['To'] = email_receiver
        em['Subject'] = "Twój kod weryfikacyjny"
        em.set_content(f"Twój kod: {auth_key}")

        context = ssl.create_default_context()
        ## tu gdzieś connection refuse ->
        try:
            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as smtp:
                logging.info("Łączenie z serwerem SMTP...")
                smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
                logging.info("Zalogowano do serwera SMTP.")

                smtp.sendmail(EMAIL_SENDER, email_receiver, em.as_string())
                logging.info(f"E-mail wysłany do: {email_receiver}")

        except smtplib.SMTPException as e:
            logging.error(f"Błąd SMTP: {e}"),400
        except Exception as e:
            logging.error(f"Nieoczekiwany błąd: {e}"),400