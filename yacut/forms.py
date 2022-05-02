from flask_wtf import FlaskForm
from wtforms import URLField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, ValidationError

from yacut.utils import check_short_id_correct


def short_check(form, field):
    short_data = field.data
    if short_data is None or not check_short_id_correct(short_data):
        raise ValidationError('Введите корректную короткую ссылку')


class LinkForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(1, 256),
        ]
    )
    custom_id = URLField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(1, 6),
            short_check,
            Optional()
        ]
    )

    submit = SubmitField('Создать')
