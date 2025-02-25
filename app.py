import os
os.system("pip install -r requirements.txt")
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>OpenIntel Sentinel Dashboard</h1><p>Live Data & Crisis Monitoring</p>"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
