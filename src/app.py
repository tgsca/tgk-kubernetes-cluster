from flask import Flask
from modules.oled96 import Oled96

app = Flask(__name__)
display = Oled96()


@app.route('/<status>', methods=['GET'])
def index(status: str = 'Running...'):
    display.clear()
    display.show(status)


@app.route('/clear', methods=['GET'])
def clear():
    display.clear()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
