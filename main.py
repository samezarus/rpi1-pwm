"""

Обязяательно запускать через:

    gunicorn --bind 0.0.0.0:5000 main:app

curl --header "Content-Type: application/json" -X POST --data '{"pwm_value":50}' http://192.168.2.229:5000/api/rpi/gpio/pwm/pin18

"""

import RPi.GPIO as GPIO

from flask import Flask, jsonify, request, render_template


app = Flask(__name__)


# Пин PWM
PWM_PIN = 18

# Частота PWM (Гц)
PWM_FREQ = 1000

# % мощности PWM (от 0% до 100%)
PWM_VALUE = 0

# Настройка режима нумерации пинов
GPIO.setmode(GPIO.BCM)

# Настройка PWM в качестве вывода
GPIO.setup(PWM_PIN, GPIO.OUT)

# Создание объекта PWM с частотой
pwm = GPIO.PWM(PWM_PIN, PWM_FREQ)

# Выставляем % мощности PWM
pwm.start(PWM_VALUE)


@app.route("/")
def home():
    return render_template("index.html", pwm_value=PWM_VALUE)


@app.route("/api/rpi/gpio/pwm/pin18", methods=["POST"])
def set_rpi_gpio_pwm_pin18():
    data = request.get_json()

    pwm_value = data.get("pwm_value")
    
    if pwm_value:
        global PWM_VALUE
        PWM_VALUE = pwm_value
        
        pwm.ChangeDutyCycle(PWM_VALUE)

        return jsonify({"status": "ok"}), 201
        
    return jsonify({"status": "error"}), 500


# Запуск сервера
if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')

    pass