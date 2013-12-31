from flask import Flask, render_template

import leds


app = Flask(__name__)


@app.route('/')
def main_route():
    return render_template('main.html')


@app.route('/flash/red', methods=['POST'])
def red_route():
    leds.flash_red()
    return "success"


@app.route('/flash/green', methods=['POST'])
def green_route():
    leds.flash_green()
    return "success"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug = True)
