from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# API Gateway URL
API_URL = "https:/--api-url/predict"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Get data from frontend
        data = request.get_json()

        payload = {
            "tenure": int(data["tenure"]),
            "monthlycharges": float(data["monthlycharges"]),
            "contract": data["contract"]
        }

        # Send request to API Gateway
        response = requests.post(API_URL, json=payload)

        # If API returns error
        if response.status_code != 200:
            return jsonify({
                "Churn Prediction": "API Error",
                "Details": response.text
            }), response.status_code

        # Return API response
        return jsonify(response.json())

    except Exception as e:
        return jsonify({
            "Churn Prediction": "Error",
            "Details": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)