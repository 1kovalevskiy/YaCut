from datetime import datetime

from flask import url_for

from yacut import db


FIELD_DICT = {
    'url': 'original',
    'custom_id': 'short'
}


class UrlMap(db.Model):
    __tablename__ = 'URL_map'
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), unique=True, nullable=False)
    short = db.Column(db.String(256), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for('open_external_page', custom_id=self.short,
                               _external=True)
        )

    def from_dict(self, data):
        for field in ['url', 'custom_id']:
            if field in FIELD_DICT:
                setattr(self, FIELD_DICT[field], data[field])
