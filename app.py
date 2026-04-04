from flask import Flask, request, jsonify
from planner import plan_trip

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "AI Travel Planner API Running"

@app.route("/plan", methods=["POST"])
def plan():
    data = request.get_json()
    query = data.get("query", "")
    result = plan_trip(query)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
