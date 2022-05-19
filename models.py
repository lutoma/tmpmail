from peewee import Model, CharField, TextField, DateTimeField
from playhouse.postgres_ext import PostgresqlExtDatabase, UUIDField, JSONField
import datetime
import uuid
import os

db = PostgresqlExtDatabase('tmpmail', dsn=os.environ.get('DB_DSN', None))


class BaseModel(Model):
	class Meta:
		database = db


class Email(BaseModel):
	id = UUIDField(primary_key=True, default=uuid.uuid4)
	node = CharField()
	raw = TextField()
	received = DateTimeField(default=datetime.datetime.now)
	header_src = CharField(null=True)
	envelope_src = CharField(null=True)
	dst = CharField(null=True)
	subject = CharField(null=True)
	headers = JSONField()
	text = TextField()


db.connect()
db.create_tables([Email])
