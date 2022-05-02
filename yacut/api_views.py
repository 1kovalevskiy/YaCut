from flask import jsonify, request

from yacut import app, db
from yacut.error_handlers import InvalidAPIUsage
from yacut.models import URL_map
from yacut.utils import (generate_new_short, get_map_by_short_id,
                         check_short_id_correct, check_short_id_exist)


@app.route('/api/id/<string:custom_id>/')
def get_full_link(custom_id):
    # смотри yacut.views:36:40
    # if not check_short_id_correct(custom_id):
    #     raise InvalidAPIUsage('Неправильная ссылка')
    url_map = get_map_by_short_id(custom_id)
    if url_map is None:
        raise InvalidAPIUsage('Указанный id не найден', status_code=404)
    data = url_map.to_dict()
    return jsonify(url=data.get("url")), 200


@app.route('/api/id/', methods=['POST'])
def add_short():
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    short_data = data.get('custom_id')
    if short_data is None or short_data in ["", None]:
        short_data = generate_new_short()
        data["custom_id"] = short_data
    if not check_short_id_correct(short_data):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    if 'url' not in data:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')
    if check_short_id_exist(short_data):
        raise InvalidAPIUsage(f'Имя "{short_data}" уже занято.')
    url_map = URL_map()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), 201
