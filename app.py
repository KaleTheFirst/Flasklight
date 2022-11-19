from flask import Flask, render_template, request

from gpiozero import LED
from time import sleep


    
app = Flask(__name__)

led = LED(17)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/animation', methods=['POST'])
def post_message():
    animation = request.form['dropdown']
    if animation == "on":
        led.on()
    elif animation == "off":
        led.off()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
