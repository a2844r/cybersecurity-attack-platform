from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

# Security logs for the simulation
security_logs = [
    {
        "time": "16:30:01",
        "event": "Failed login attempt",
        "source": "192.168.1.10",
        "severity": "High"
    },
    {
        "time": "16:31:15",
        "event": "Port scan detected",
        "source": "192.168.1.25",
        "severity": "Medium"
    },
    {
        "time": "16:32:42",
        "event": "Successful login",
        "source": "192.168.1.50",
        "severity": "Low"
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/port-scan", methods=["POST"])
def port_scan():

    # Simulated port scan
    open_ports = [22, 80, 443]

    security_logs.append({
        "time": datetime.now().strftime("%H:%M:%S"),
        "event": "Port scan simulated - ports 22, 80 and 443",
        "source": "Simulation",
        "severity": "WARNING"
    })

    return jsonify({
        "success": True,
        "open_ports": open_ports
    })
@app.route("/api/brute-force", methods=["POST"])
def brute_force():
    security_logs.append({
        "time": datetime.now().strftime("%H:%M:%S"),
        "event": "Brute-force attack simulated - repeated authentication attempts",
        "source": "Simulation",
        "severity": "HIGH"
    })

    return jsonify({
        "success": True,
        "message": "Brute-force attack simulated"
    })
@app.route("/api/sql-injection", methods=["POST"])
def sql_injection():
    security_logs.append({
        "time": datetime.now().strftime("%H:%M:%S"),
        "event": "SQL injection simulation detected",
        "source": "Simulation",
        "severity": "HIGH"
    })

    return jsonify({
        "success": True,
        "message": "SQL Injection simulation complete"
    })
@app.route("/api/dos", methods=["POST"])
def dos():
    security_logs.append({
        "time": datetime.now().strftime("%H:%M:%S"),
        "event": "DoS attack simulation detected",
        "source": "Simulation",
        "severity": "HIGH"
    })

    return jsonify({
        "success": True,
        "message": "DoS simulation complete"
    })
@app.route("/api/logs")
def get_logs():
    return jsonify(security_logs[-20:])
@app.route("/api/clear-logs", methods=["POST"])
def clear_logs():
    security_logs.clear()
    return jsonify({"message": "Security logs cleared"})

@app.route("/api/statistics")
def statistics():
    high = sum(
        1 for log in security_logs
        if log["severity"].lower() == "high"
    )

    medium = sum(
        1 for log in security_logs
        if log["severity"].lower() == "medium"
    )

    low = sum(
        1 for log in security_logs
        if log["severity"].lower() == "low"
    )

    total_attacks = high + medium + low

    return jsonify({
        "total_attacks": total_attacks,
        "high": high,
        "medium": medium,
        "low": low,
        "port_scans": sum(
            1 for log in security_logs
            if "port scan" in log["event"].lower()
        ),
        "brute_force": sum(
            1 for log in security_logs
            if "brute force" in log["event"].lower()
        ),
        "sql_injection": sum(
            1 for log in security_logs
            if "sql" in log["event"].lower()
        ),
        "dos": sum(
            1 for log in security_logs
            if "dos" in log["event"].lower()
        )
    })


if __name__ == "__main__":
    app.run(debug=True)