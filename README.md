# rpi1-pwm

# Проект управления куллером через pwm ногу для Raspberry pi v1

## Зависимости

``` bash
sudo apt-get update && \
sudo apt-get install python3-rpi.gpio
```

## Создание и активация виртуального окружения

``` bash
sudo apt install -y python3-pip python3.<VER>-venv
```

``` bash
pip install --break-system-packages virtualenv
```

``` bash
python -m venv ./venv
```

``` bash
source ./venv/bin/activate
```

## Установка зависимостей

``` bash
pip install -r ./requirements.txt
```

## Выставляем обороты (fastapi) (python main-fastapi.py)

``` bash
curl --header "Content-Type: application/json" \
-X POST \
--data '{"temp_val":15}' \
http://192.168.2.229:8000/set_info
```

## Выставляем обороты (flask) (gunicorn --bind 0.0.0.0:5000 main:app)

http://192.168.2.229:5000/