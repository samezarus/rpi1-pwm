"""
curl --header "Content-Type: application/json" -X POST --data '{"temp_val":15}' http://192.168.2.229:8000/set_info
"""

from fastapi import FastAPI, HTTPException, Header
from functools import wraps

import RPi.GPIO as GPIO
from time import sleep

app = FastAPI()

TOKENS=["12345"]

# Пример базовых данных для демонстрации
info_store = {"data": "test"}


def validate_token(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        authorization: str = kwargs.pop('authorization', None)

        if not authorization or "Bearer" not in authorization:
            raise HTTPException(status_code=401, detail="Authorization header missing or invalid")

        # Пример проверки токена. Здесь можно подключиться к сервису аутентификации.
        # token = authorization.replace("Bearer ", "")
        
        if token in TOKENS:
            return await func(*args, **kwargs)
        else:
            raise HTTPException(status_code=401, detail="Invalid token")
    return wrapper


@app.get("/get_info")
# @validate_token
async def get_info():
    """
    Получение информации. Проверяет наличие заголовка авторизации.
    
    :return: Словарь с информацией, если все верно
    """

    return {"info": info_store}

@app.post("/set_info")
# @validate_token
async def set_info(info: dict):
    """
    Установка информации. Проверяет наличие заголовка авторизации.
    
    :param info: Информация для установки
    :return: Статус обновления информации
    """
    
    temp_val = info.get("temp_val")

    if temp_val:
        if type(temp_val) == int:
            pwm.ChangeDutyCycle(temp_val)
            print("set:", temp_val)
            

    return {"status": "success", "info_stored": info}

# Запуск приложения
if __name__ == "__main__":
    import uvicorn

    # Настройка режима нумерации пинов
    GPIO.setmode(GPIO.BCM)

    # Выбор пина и его настройка в качестве вывода
    pin = 18
    GPIO.setup(pin, GPIO.OUT)

    # Создание объекта PWM с частотой 1000 Гц
    pwm = GPIO.PWM(pin, 1000)

    pwm.start(10)  # Выставляем % мощности (от 0% до 100%)

    uvicorn.run(app, host="0.0.0.0", port=8000)