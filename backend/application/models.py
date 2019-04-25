# Models

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class List(db.Model):
	__tablename__ = 'lists'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(180))
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	items = db.relationship('Item', backref='list', lazy=False)

	def to_dict(self):
		return dict(
			id=self.id,
			name=self.name,
			created_at=self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
			items = [ item.to_dict() for item in self.items ]
		)

class Item(db.Model):
	__tablename__ = 'items'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(180))
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	list_id = db.Column(db.Integer, db.ForeignKey('lists.id'))

	def to_dict(self):
		return dict(
			id=self.id,
			title=self.title,
			created_at=self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
			list_id = self.list_id
		)