import os
import os

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient



keyVaultName = os.getenv("key_vault_name")
FRONTEND_URL = os.getenv("frontend-uri")
KVUri = f"https://{keyVaultName}.vault.azure.net"
credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

EMAIL_SENDER = client.get_secret("smtp-email")
EMAIL_PASSWORD = client.get_secret("smtp-password")
SMTP_SERVER = client.get_secret("smtp-server")
SMTP_PORT = client.get_secret("smtp-port")
