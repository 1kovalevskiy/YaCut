import re

import rstr

from yacut.models import URL_map


def generate_new_short():
    while True:
        short = rstr.xeger(r'^[a-zA-Z\d]{6}$')
        if URL_map.query.filter_by(short=short).first() is None:
            return short


def check_short_id_correct(short):
    return re.fullmatch(r'^[a-zA-Z\d]{1,6}$', short)


def get_map_by_full_url(url):
    return URL_map.query.filter_by(original=url).first()


def get_map_by_short_id(short):
    return URL_map.query.filter_by(short=short).first()


def check_full_url_exist(url):
    return get_map_by_full_url(url)


def check_short_id_exist(short):
    return get_map_by_short_id(short)
