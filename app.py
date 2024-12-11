from flask import Flask, request, jsonify
import logging
from datetime import datetime

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    filename="click_logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

@app.route("/track", methods=["GET"])
def track_click():
    # Get the email or username from query parameters
    email = request.args.get("email")
    timestamp = datetime.now().isoformat()

    if email:
        # Log the event
        logging.info(f"Email: {email}, Timestamp: {timestamp}")
        return jsonify({"status": "success", "message": "Click tracked"}), 200
    else:
        return jsonify({"status": "error", "message": "Email parameter missing"}), 400

if __name__ == "__main__":
    app.run(debug=True)
