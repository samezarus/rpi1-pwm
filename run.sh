# chmod +x run.sh

source ./venv/bin/activate && gunicorn --bind 0.0.0.0:5000 main:app