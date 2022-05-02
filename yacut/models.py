from datetime import datetime

from flask import url_for

from yacut import db


class URL_map(db.Model):
    """'id', 'original', 'short', 'timestamp'"""
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
            if field == 'url':
                setattr(self, 'original', data[field])
            if field == 'custom_id':
                setattr(self, 'short', data[field])