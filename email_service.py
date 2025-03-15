from flask import Flask, request, jsonify

from email_sender import EmailSender
import sys
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
app = Flask(__name__)

email_sender = EmailSender()


@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json
    email_receiver = data.get('email_receiver')
    auth_key = data.get('auth_key')
    logging.info("test auth_keya itp")
    if not email_receiver or not auth_key:
        return jsonify({"message": "email_receiver and body are required."}), 400
    logging.info("po test auth_keya itp")
    return email_sender.send_email(email_receiver, auth_key)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
