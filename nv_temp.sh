#!/bin/bash

# chmod +x nv_temp

api_url="http://192.168.2.229:5000//api/rpi/gpio/pwm/pin18"

# Получаем температуры всех GPU и сохраняем их в переменную.
temperatures=$(nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits)

# Инициализируем переменную для хранения максимальной температуры.
max_temp=-1

# Проходим по каждой строке (температура каждого GPU) и находим максимум.
for temp in $temperatures; do
    if [[ "$temp" -gt "$max_temp" ]]; then
        max_temp=$temp
    fi
done

# Выводим максимальную температуру.
# echo "Максимальная температура GPU: ${max_temp}°C"

# Выводим результаты в зависимости от значения максимальной температуры.
if [[ "$max_temp" -le 25 ]]; then
    curl --header "Content-Type: application/json" -X POST --data '{"pwm_value": 3}' $api_url
elif [[ "$max_temp" -gt 25 && "$max_temp" -lt 35 ]]; then
    curl --header "Content-Type: application/json" -X POST --data '{"pwm_value": 30}' $api_url
elif [[ "$max_temp" -gt 35 && "$max_temp" -lt 45 ]]; then
    curl --header "Content-Type: application/json" -X POST --data '{"pwm_value": 40}' $api_url
elif [[ "$max_temp" -gt 45 && "$max_temp" -lt 55 ]]; then
    curl --header "Content-Type: application/json" -X POST --data '{"pwm_value": 50}' $api_url
elif [[ "$max_temp" -gt 55 && "$max_temp" -lt 65 ]]; then
    curl --header "Content-Type: application/json" -X POST --data '{"pwm_value": 60}' $api_url
elif [[ "$max_temp" -gt 65 && "$max_temp" -lt 75 ]]; then
    curl --header "Content-Type: application/json" -X POST --data '{"pwm_value": 70}' $api_url
else
    echo "ALARM !!!"
    curl --header "Content-Type: application/json" -X POST --data '{"pwm_value": 100}' $api_url
fi