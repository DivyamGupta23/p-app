from flask import Flask, request, redirect
import logging
from datetime import datetime
import sys

app = Flask(__name__)

# Configure logging to log to the console (stdout)
logging.basicConfig(
    stream=sys.stdout,  # Direct the log to standard output
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# Replace this with the website to redirect users to
REDIRECT_URL = "https://example.com"

@app.route("/track", methods=["GET"])
def track_click():
    # Get the email or username from query parameters
    email = request.args.get("email")
    timestamp = datetime.now().isoformat()

    if email:
        # Log the event to console (stdout)
        logging.info(f"Email: {email}, Timestamp: {timestamp}")

        # Redirect to the target website
        return redirect(REDIRECT_URL, code=302)
    else:
        return "Invalid request. Missing email parameter.", 400

if __name__ == "__main__":
    app.run(debug=True)
