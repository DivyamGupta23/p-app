import base64
import uuid
from flask import Flask, request, redirect
import requests
import logging
import sys
from datetime import datetime

app = Flask(__name__)

LOGGLY_URL = "http://logs-01.loggly.com/inputs/bbdf6498-55d9-4642-8cce-67eaca20be35/tag/http/"
HEADERS = {"Content-Type": "application/json"}

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(asctime)s - %(message)s")

def decode_email(encoded_email):
    # Decode the base64 email back to UUID bytes
    padding = '=' * (4 - len(encoded_email) % 4)
    decoded_bytes = base64.urlsafe_b64decode(encoded_email + padding)
    
    # Convert the UUID bytes back to UUID object
    email_uuid = uuid.UUID(bytes=decoded_bytes)
    
    # Decode the UUID to original email (reverse UUID generation logic)
    return str(email_uuid)

def send_log_to_loggly(email, timestamp):
    log_data = {
        "email": email,
        "timestamp": timestamp
    }
    response = requests.post(LOGGLY_URL, json=log_data, headers=HEADERS)
    if response.status_code != 200:
        logging.error(f"Failed to send log to Loggly: {response.text}")

REDIRECT_URL = "https://www.talenthr.io"

@app.route("/verify", methods=["GET"])
def verify_click():
    encoded_email = request.args.get("id")
    if not encoded_email:
        return "Invalid request. Missing id parameter.", 400
    
    # Decode the email from the encoded ID
    email = decode_email(encoded_email)

    # Get the current time and format it as 12-hour time with AM/PM
    timestamp = datetime.now().strftime("%I:%M:%S %p, %B %d, %Y")
    
    # Log the click to Loggly
    send_log_to_loggly(email, timestamp)

    # Redirect to the target website
    return redirect(REDIRECT_URL, code=302)

if __name__ == "__main__":
    app.run(debug=True)
