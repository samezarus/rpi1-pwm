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

## Создание демона (под sudo)

1. Создать файл:

``` bash
> /etc/systemd/system/pwm.service
```

2. Тело файла

``` code
[Unit]
Description=PWM demon
After=network.target

[Service]
User=<USER>
WorkingDirectory=/home/<USER>/project/
ExecStart=/home/<USER>/project/venv/bin/gunicorn --bind 0.0.0.0:5000 main:app
Restart=always
[Install]
WantedBy=multi-user.target
```

3. Применить изменения

``` bash
sudo systemctl daemon-reload
```

4. Автостарт

``` bash
sudo systemctl enable pwm.service
```

5. Запуск

``` bash
sudo systemctl start pwm.service
```

6. Проверка статуса

``` bash
sudo systemctl status pwm.service
```