from flask import Flask, request, current_app, Response


def create_global_logger(app: Flask):
    @app.before_request
    def log_request():
        method = request.method
        url = request.url

        current_app.logger.info({
            'url': url,
            'method': method
        })

    @app.after_request
    def log_response(response: Response):
        data = response.json
        current_app.logger.info(data)
        return response
