from flask import *
import smbus
import time
import os

app = Flask(__name__)

bus = smbus.SMBus(1)
SLAVE_ADDRESS = 0x04

led_status = 2
photo_value_g = 0
auto = 0

def request_reading():
    # reading = bus.read_byte(SLAVE_ADDRESS)
    reading = bus.read_i2c_block_data(SLAVE_ADDRESS, 0, 1)
    # print(reading)
    return reading

def led_control(status):
    bus.write_byte(SLAVE_ADDRESS, status)
    return ""

@app.route('/')
def index():
    while True:
        return render_template('index.html')

@app.route('/status')
def switch():
    def read_status():
        while True:
            global led_status
            global photo_value_g
            global auto
            arduino_state = request_reading()
            photo_value_g = arduino_state[0]

            if auto == 1:
                if photo_value_g < 20:
                    led_status = 1
                else:
                    led_status = 2

            led_control(led_status)
            led_value = 0 if led_status == 2 else 1

            state = [photo_value_g, led_value]



            yield 'data: {0}\n\n'.format(state)
            time.sleep(1.0)

    return Response(read_status(), mimetype='text/event-stream')


@app.route("/led", methods=['POST'])
def led():
    global led_status

    led_status = 2 if led_status == 1 else 1
    led_control(led_status)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)