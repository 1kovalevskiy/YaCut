from flask import render_template, flash, abort, redirect

from yacut import app, db
from yacut.forms import LinkForm
from yacut.models import UrlMap
from yacut.utils import (generate_new_short, get_map_by_full_url,
                         get_map_by_short_id, check_short_id_exist)


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = LinkForm()
    if form.validate_on_submit():
        if check_short_id_exist(form.custom_id.data):
            flash(f'Имя {form.custom_id.data} уже занято!', 'info-message')
            return render_template('index.html', form=form)
        map_for_test = get_map_by_full_url(form.original_link.data)
        if map_for_test is not None:
            flash('Такое адрес уже был сокращен!', 'info-message')
            flash(f'{map_for_test.short}', 'link-message')
            return render_template('index.html', form=form)
        if form.custom_id.data == '' or form.custom_id.data is None:
            form.custom_id.data = generate_new_short()
        url_map = UrlMap(
            original=form.original_link.data,
            short=form.custom_id.data
        )
        db.session.add(url_map)
        db.session.commit()
        flash(f'{url_map.short}', 'link-message')
    return render_template('index.html', form=form)


@app.route('/<string:custom_id>')
def open_external_page(custom_id):
    url_map = get_map_by_short_id(custom_id)
    if url_map is None:
        abort(404)
    return redirect(f"{url_map.original}", code=302)
