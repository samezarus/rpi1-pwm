try: import RPi.GPIO as GPIO
except: pass

from flask import Flask, jsonify, request, render_template


# Пин PWM
PWM_PIN=18

# Частота PWM (Гц)
PWM_FREQ=1000

# % мощности PWM (от 0% до 100%)
PWM_VALUE=5


app = Flask(__name__)


def init_gpio():
     # Настройка режима нумерации пинов
    GPIO.setmode(GPIO.BCM)

    # Настройка PWM в качестве вывода
    GPIO.setup(PWM_PIN, GPIO.OUT)

    # Создание объекта PWM с частотой
    pwm = GPIO.PWM(PWM_PIN, PWM_FREQ)

    # Выставляем % мощности PWM
    pwm.start(PWM_VALUE)  

def set_value_gpio_pwm_pin18(val: int):
    if val > 0:
        pwm.ChangeDutyCycle(val)

@app.route("/")
def home():
    return render_template("index.html", pwm_value=PWM_VALUE)


@app.route("/api/rpi/gpio/pwm/pin18", methods=["POST"])
def set_rpi_gpio_pwm_pin18():
    data = request.get_json()

    pwm_value = data.get("pwm_value")
    temp_value = data.get("temp_value")
    
    if pwm_value:
        PWM_VALUE = pwm_value
        
        try: set_value_gpio_pwm_pin18(PWM_VALUE)
        except: pass

        return jsonify({"status": "ok"}), 201
    
    if temp_value:
        pass
    
    return jsonify({"status": "error"}), 500


# Запуск сервера
if __name__ == '__main__':
    try: init_gpio()
    except: pass

    app.run(debug=True, host='0.0.0.0')