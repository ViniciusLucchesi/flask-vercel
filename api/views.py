from flask import Flask, Blueprint, render_template, jsonify, request
from api.analises import new_user, get_all_users
from api.models import User
# from bson import ObjectId
# from datetime import datetime
# import json

# class JSONEncoder(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o, ObjectId):
#             return str(o)
#         if isinstance(o, datetime):
#             return o.isoformat()
#         return json.JSONEncoder.default(self, o)


bp = Blueprint('coleta', __name__, template_folder='templates')


@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/new_user', methods=['GET','POST'])
def new_user_route():
    if request.method == 'POST':
        user = User(
            name=request.form.get('name'),
            email=request.form.get('email'),
            password=request.form.get('password'),
        )
        if new_user(user):
            return jsonify({'status': 'success'})
        else:
            return jsonify({'status': 'error', 'user': user.__dict__})
    
    return render_template('form.html')


@bp.route('/users')
def users():
    users = get_all_users()
    return jsonify(users)


def configure(app: Flask):
    app.register_blueprint(bp)