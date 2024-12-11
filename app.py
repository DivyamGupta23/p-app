from flask import Flask, redirect, request
from datetime import datetime
import base64

app = Flask(__name__)

# A fake landing page to redirect users
REDIRECT_URL = "https://www.talenthr.io"

# Endpoint to track clicks
@app.route('/r/<encoded_email>', methods=['GET'])
def redirect_and_track(encoded_email):
    try:
        # Decode the email
        email = base64.urlsafe_b64decode(encoded_email.encode()).decode()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Log the email and timestamp to a file
        with open("phishing_logs.txt", "a") as log_file:
            log_file.write(f"{email}, {timestamp}\n")

        # Redirect the user to the landing page
        return redirect(REDIRECT_URL)
    except Exception as e:
        return "Invalid link", 400

if __name__ == "__main__":
    app.run(debug=True)
