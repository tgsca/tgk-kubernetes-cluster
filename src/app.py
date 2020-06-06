from flask import Flask, jsonify
from modules.oled96 import Oled96

app = Flask(__name__)
display = Oled96()


@app.route('/<status>', methods=['GET'])
def index(status: str = 'Running...'):
    display.clear()
    display.show(status)
    return jsonify('Status set'), 200


@app.route('/clear', methods=['GET'])
def clear():
    display.clear()
    return jsonify('Display cleared'), 200


@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return jsonify(''), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
