import RPi.GPIO as GPIO

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    name = "Adam"  
    return render_template('./templates/index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)