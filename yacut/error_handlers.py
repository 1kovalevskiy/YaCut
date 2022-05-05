import http

from flask import render_template, jsonify

from yacut import app, db


class InvalidAPIUsage(Exception):
    status_code = http.HTTPStatus.BAD_REQUEST

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return dict(message=self.message)


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), http.HTTPStatus.NOT_FOUND


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), http.HTTPStatus.INTERNAL_SERVER_ERROR
