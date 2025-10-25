from flask import Flask, request, jsonify
import csv
import json
import time
from threading import Lock
from markupsafe import escape

app = Flask(__name__)

# Create a lock for thread-safe file access
file_lock = Lock()

@app.route("/", methods=["POST"])
def hook():
    try:
        # Ensure the request data is not empty
        if not request.data:
            return jsonify({"error": "Empty request body"}), 400

        # Decode and parse the JSON data
        try:
            data = json.loads(request.data.decode("utf-8"))
        except json.JSONDecodeError:
            return jsonify({"error": "Invalid JSON format"}), 400

        # Validate the expected fields
        if not all(key in data for key in ["name", "email"]):
            return jsonify({"error": "Missing required fields: 'name' and 'email'"}), 400

        # Sanitize the input (basic sanitization and escaping)
        name = escape(str(data["name"]).strip())
        email = escape(str(data["email"]).strip())

        # Ensure the fields are not excessively long
        if len(name) > 100 or len(email) > 100:
            return jsonify({"error": "Field length exceeds limit"}), 400

        # Log the data to a CSV file with thread safety
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        with file_lock:
            with open("log.csv", "a", newline="") as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=';')
                csvwriter.writerow([timestamp, name, email])

        return jsonify({"message": "Data logged successfully"}), 200

    except Exception as e:
        # Catch unexpected errors
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

if __name__ == "__main__":
    app.run()
