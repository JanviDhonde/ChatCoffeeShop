from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response
import logging

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.post("/predict")
def predict():
    try:
        # Get the text from the request JSON
        text = request.get_json().get("message")
        
        # Check if the text is valid
        if not text:
            logging.error("Empty message received in request.")
            return jsonify({"error": "Invalid input. Please provide a valid message."}), 400

        # Generate response using the get_response function
        response = get_response(text)
        
        # Prepare the message to return as JSON
        message = {"answer": response}
        logging.debug(f"Response generated: {message}")

        return jsonify(message)

    except Exception as e:
        # Log the exception
        logging.error(f"Error processing the request: {e}")
        return jsonify({"error": "An error occurred while processing the request."}), 500

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
