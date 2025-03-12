import smtplib
import ssl
from email.message import EmailMessage
from config import EMAIL_SENDER, EMAIL_PASSWORD, SMTP_PORT, SMTP_SERVER


class EmailSender:
    def __init__(self):
        pass

    def send_email(self, email_receiver: str, auth_key: str) -> None:
        try:
            em = EmailMessage()
            em['From'] = EMAIL_SENDER
            em['To'] = email_receiver
            em['Subject'] = "Twój klucz autoryzacyjny"
            em.set_content(f"Twój kod autoryzacyjny to: {auth_key}")

            context = ssl.create_default_context()

            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
                smtp.starttls(context=context)
                smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
                smtp.sendmail(EMAIL_SENDER, email_receiver, em.as_string())

            print(f"E-mail wysłany do {email_receiver}")

        except Exception as e:
            print(f"Błąd podczas wysyłania e-maila: {e}")