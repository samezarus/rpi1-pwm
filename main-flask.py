# import RPi.GPIO as GPIO

# from flask import Flask, render_template


# app = Flask(__name__)

# @app.route('/')
# def home():
#     name = "Adam"  
#     return render_template('index.html', name=name)

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')

from flask import Flask, jsonify, request, render_template

from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize database
db = SQLAlchemy(app)


# Define a model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))

    def __repr__(self):
        return f"<Item {self.name}>"

# Create database tables
with app.app_context():
    db.create_all()

# Initialize Flask-Admin
admin = Admin(app, name='Simple API Admin', template_mode='bootstrap4')
admin.add_view(ModelView(Item, db.session))


# Define routes for paeges
@app.route('/')
def home():
    name = "Adam"  
    return render_template('index.html', name=name)


# Define routes for the API
@app.route('/api/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{'id': item.id, 'name': item.name, 'description': item.description} for item in items])


@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = Item.query.get_or_404(item_id)
    return jsonify({'id': item.id, 'name': item.name, 'description': item.description})


@app.route('/api/items', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = Item(name=data['name'], description=data['description'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'id': new_item.id, 'name': new_item.name, 'description': new_item.description}), 201


@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = Item.query.get_or_404(item_id)
    data = request.get_json()
    item.name = data['name']
    item.description = data['description']
    db.session.commit()
    return jsonify({'id': item.id, 'name': item.name, 'description': item.description})


@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return '', 204


# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')