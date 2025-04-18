import os
EMAIL_SENDER = os.getenv("smtp-email")
EMAIL_PASSWORD = os.getenv("smtp-password")
SMTP_SERVER = os.getenv("smtp-server")
SMTP_PORT = os.getenv("smtp-port")