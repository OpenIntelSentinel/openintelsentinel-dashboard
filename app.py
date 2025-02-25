import os
from flask import Flask, render_template, jsonify

# Ensure dependencies are installed
os.system("pip install -r requirements.txt")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/data')
def get_data():
    sample_data = {
        "timestamp": "2024-02-25 12:00:00",
        "alerts": [
            {"type": "Economic", "message": "Stock market drops 2.5% 
today"},
            {"type": "Geopolitical", "message": "Increased military 
activity in Eastern Europe"},
            {"type": "Cybersecurity", "message": "Major website outage 
detected globally"}
        ]
    }
    return jsonify(sample_data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)import os
from flask import Flask, render_template, jsonify

# Ensure dependencies are installed
os.system("pip install -r requirements.txt")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/data')
def get_data():
    sample_data = {
        "timestamp": "2024-02-25 12:00:00",
        "alerts": [
            {"type": "Economic", "message": "Stock market drops 2.5% 
today"},
            {"type": "Geopolitical", "message": "Increased military 
activity in Eastern Europe"},
            {"type": "Cybersecurity", "message": "Major website outage 
detected globally"}
        ]
    }
    return jsonify(sample_data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
import os
from flask import Flask, render_template, jsonify

# Ensure dependencies are installed
os.system("pip install -r requirements.txt")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/data')
def get_data():
    sample_data = {
        "timestamp": "2024-02-25 12:00:00",
        "alerts": [
            {"type": "Economic", "message": "Stock market drops 2.5% 
today"},
            {"type": "Geopolitical", "message": "Increased military 
activity in Eastern Europe"},
            {"type": "Cybersecurity", "message": "Major website outage 
detected globally"}
        ]
    }
    return jsonify(sample_data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
import os
from flask import Flask, render_template, jsonify

# Ensure dependencies are installed
os.system("pip install -r requirements.txt")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/data')
def get_data():
    sample_data = {
        "timestamp": "2024-02-25 12:00:00",
        "alerts": [
            {"type": "Economic", "message": "Stock market drops 2.5% 
today"},
            {"type": "Geopolitical", "message": "Increased military 
activity in Eastern Europe"},
            {"type": "Cybersecurity", "message": "Major website outage 
detected globally"}
        ]
    }
    return jsonify(sample_data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
import os
from flask import Flask, render_template, jsonify

# Ensure dependencies are installed
os.system("pip install -r requirements.txt")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/data')
def get_data():
    sample_data = {
        "timestamp": "2024-02-25 12:00:00",
        "alerts": [
            {"type": "Economic", "message": "Stock market drops 2.5% 
today"},
            {"type": "Geopolitical", "message": "Increased military 
activity in Eastern Europe"},
            {"type": "Cybersecurity", "message": "Major website outage 
detected globally"}
        ]
    }
    return jsonify(sample_data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
