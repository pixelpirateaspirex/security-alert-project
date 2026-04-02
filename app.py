from flask import Flask
import threading
import detector

app = Flask(__name__)

@app.route('/')
def home():
    return "Cloud Security System Running"
@app.route('/alerts')
def alerts():
    try:
        with open("security_alerts.log", "r") as f:
            return f.read()
    except:
        return "No alerts yet"
    

def start_detector():
    detector.monitor_logs()

if __name__ == "__main__":
    thread = threading.Thread(target=start_detector)
    thread.daemon = True
    thread.start()

    app.run(host="0.0.0.0", port=5000)