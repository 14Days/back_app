from flask import Blueprint, request, current_app
from app.util.response import success_res

demo = Blueprint('demo', __name__)


@demo.route('/success')
def test1():
    current_app.logger.info('test1 is successful')
    return success_res('demo1')


@demo.route('/methods', methods=['GET', 'POST'])
def test2():
    if request.method == 'GET':
        current_app.logger.info('test2 get is successful')
        return success_res('GET')
    if request.method == 'POST':
        current_app.logger.info('test2 post is successful')
        return success_res('POST')
