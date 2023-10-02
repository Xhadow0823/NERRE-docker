from flask import Flask, render_template, request, abort, jsonify
from utilities import get_history_result_list, get_history_result, clear_all_results

from core import NERRE

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', status="starting...")

@app.route("/submit", methods=['POST'])
def submit():
    try:
        requeset_data = request.get_json()
        text = requeset_data["text"]
        print( text )
        response = jsonify(NERRE(text))
        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
    except Exception as e:
        print(e)
        if "OPENAI_API_KEY" in str(e):
            print("KEY error")
        return abort(500, str(e)) if "OPENAI_API_KEY" in str(e) else abort(500)

@app.route("/history/results")
def history_result():
    return get_history_result_list()

@app.route("/download/<filename>")
def download(filename):
    return get_history_result(filename)

@app.route("/clearAllResults")
def clear_results():
    return "OK" if clear_all_results() else abort(500)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
