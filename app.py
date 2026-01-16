from flask import Flask, request, jsonify, render_template
from services.diagnostics import run_diagnostics, should_run_diagnostics
from services.ai import analyze
from services.incidents import save_incident, list_incidents

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/incident", methods=["POST"])
def create_incident():
    data = request.json
    issue = data["issue"]
    severity = data["severity"]

    run_checks, reason = should_run_diagnostics(issue)

    if not run_checks:
        summary = f"{reason}\n\nSuggested actions:\n• Check charger\n• Try another outlet\n• Battery check"
    else:
        report = run_diagnostics()
        summary = analyze(issue, report)

    save_incident(issue, severity, summary)

    return jsonify({"summary": summary})

@app.route("/incidents")
def get_incidents():
    return jsonify(list_incidents())

app.run(host="0.0.0.0", port=5000, debug=True)
