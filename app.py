from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>OpenIntel Sentinel Dashboard</h1><p>Live Data & Crisis Monitoring</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
