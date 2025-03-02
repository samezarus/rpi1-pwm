"""
sudo apt-get update
sudo apt-get install python3-rpi.gpio

"""

import RPi.GPIO as GPIO
from time import sleep

# Настройка режима нумерации пинов
GPIO.setmode(GPIO.BCM)

# Выбор пина и его настройка в качестве вывода
pin = 18
GPIO.setup(pin, GPIO.OUT)

# Создание объекта PWM с частотой 1000 Гц
pwm = GPIO.PWM(pin, 1000)

pwm.start(0)  # Выставляем % мощности (от 0% до 100%)

try:
    while True:
        for dc in range(0, 101, 5):  # увеличиваем обороты
            pwm.ChangeDutyCycle(dc)
            sleep(1)
        for dc in range(100, -1, -5):  # уменьшаем обороты
            pwm.ChangeDutyCycle(dc)
            sleep(1)

pwm.stop()  # Остановка PWM
GPIO.cleanup()  # Очистка GPIO