from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>Welcome to CATS</h1>
    <h2>Built by Spoorthy</h2>
    <p>Current Time: {datetime.now()}</p>
    <p>Version: 1.0</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
