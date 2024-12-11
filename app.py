import requests
from flask import Flask, request, redirect
from datetime import datetime
import logging
import sys

app = Flask(__name__)

# Loggly URL (replace with your actual Loggly customer token)
LOGGLY_URL = "http://logs-01.loggly.com/inputs/bbdf6498-55d9-4642-8cce-67eaca20be35/tag/http/"
HEADERS = {"Content-Type": "application/json"}

# Set up logging to console (stdout)
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(asctime)s - %(message)s")

# Function to send logs to Loggly
def send_log_to_loggly(email, timestamp):
    log_data = {
        "email": email,
        "timestamp": timestamp
    }
    print(f"Sending log to Loggly: {log_data}")  # Debugging: Print log data
    response = requests.post(LOGGLY_URL, json=log_data, headers=HEADERS)
    if response.status_code != 200:
        logging.error(f"Failed to send log to Loggly: {response.text}")

# Redirect URL after logging the click
REDIRECT_URL = "https://www.talenthr.io"

@app.route("/track", methods=["GET"])
def track_click():
    email = request.args.get("email")

    # Get the current time and format it as 12-hour time with AM/PM
    timestamp = datetime.now().strftime("%I:%M:%S %p, %B %d, %Y")  # Example: 02:30:00 PM, December 11, 2024

    if email:
        # Send the log data to Loggly
        send_log_to_loggly(email, timestamp)

        # Redirect to the target website
        return redirect(REDIRECT_URL, code=302)
    else:
        return "Invalid request. Missing email parameter.", 400

if __name__ == "__main__":
    app.run(debug=True)
