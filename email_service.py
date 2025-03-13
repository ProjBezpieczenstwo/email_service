# # Microservice used to send automated emails. Runs on port 5001
#
# from flask import Flask, request, jsonify
# from flask_mail import Mail, Message
#
# from config import EMAIL_SENDER, EMAIL_PASSWORD, MAIL_USE_SSL, MAIL_USE_TLS, MAIL_PORT, MAIL_SERVER
# import logging
# app = Flask(__name__)
# mail = Mail(app)
#
# app.config['MAIL_SERVER'] = MAIL_SERVER
# app.config['MAIL_PORT'] = MAIL_PORT
# app.config['MAIL_USERNAME'] = EMAIL_SENDER
# app.config['MAIL_PASSWORD'] = EMAIL_PASSWORD
# app.config['MAIL_USE_TLS'] = MAIL_USE_TLS
# app.config['MAIL_USE_SSL'] = MAIL_USE_SSL
# app.config['MAIL_MAX_EMAILS'] = 10
# app.config['MAIL_SUPPRESS_SEND'] = False
# app.config['TESTING'] = False
# app.testing = False
# app.debug = False
#
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#
# @app.route('/send-email', methods=['POST'])
# def send_email():
#     data = request.json
#     email_receiver = data.get('email_receiver')
#     auth_key = data.get('auth_key')
#
#     if not email_receiver or not auth_key:
#         return jsonify({"message": "email_receiver and auth_key are required."}), 400
#
#     try:
#         subject = "Twój klucz autoryzacyjny"
#         message = f"Twój kod autoryzacyjny to: {auth_key}"
#         logging.info("tworzenie message")
#         msg = Message(subject=subject,
#                       sender=EMAIL_SENDER,
#                       recipients=[email_receiver],
#                       )
#         logging.info("msg.body")
#         msg.body = message
#         logging.info("mail send")
#         logging.info(f"msg body= {msg.body}")
#         logging.info(f"msg sender= {msg.sender} and {msg.recipients} and {msg.subject}")
#         mail.send(msg)
#         logging.info("mail sie wyslal xD")
#         print(f"E-mail wysłany do {email_receiver}")
#         return jsonify({"message": f"Email sent successfully to {email_receiver}"}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#
#
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5001)

# Microservice used to send automated emails. Runs on port 5001

from flask import Flask, request, jsonify
from email_sender import EmailSender


app = Flask(__name__)

email_sender = EmailSender()
@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json
    email_receiver = data.get('email_receiver')
    auth_key = data.get('auth_key')

    if not email_receiver or not auth_key:
        return jsonify({"message": "email_receiver and body are required."}), 400

    try:
        email_sender.send_email(email_receiver, auth_key)
        return jsonify({"message": f"Email sent successfully to {email_receiver}"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5001)
