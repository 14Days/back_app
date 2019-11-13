from flask import jsonify


def success_res(data):
    return jsonify({
        'status': 'success',
        'data': data
    })


def fail_res(error):
    return jsonify({
        'status': 'error',
        'err_msg': error
    })
