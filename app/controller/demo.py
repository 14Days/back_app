from flask import Blueprint, request, current_app
from app.util.response import success_res

demo = Blueprint('demo', __name__)


@demo.route('/success')
def test1():
    return success_res('demo1')


@demo.route('/methods', methods=['GET', 'POST'])
def test2():
    if request.method == 'GET':
        return success_res('GET')
    if request.method == 'POST':
        return success_res('POST')
