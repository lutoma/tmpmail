from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from playhouse.shortcuts import model_to_dict
from typing import List, Dict, Union
from models import Email
import datetime
import uuid

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=False,
	allow_methods=['GET'], allow_headers=['*'])


class InboxEmailResponse(BaseModel):
	id: uuid.UUID
	received: datetime.datetime
	header_src: str
	subject: Union[str, None] = None


@app.get("/inbox/{inbox}", response_model=List[InboxEmailResponse])
def read_inbox(inbox):
	print(inbox)
	mails = Email.select().where(Email.dst == inbox).order_by(Email.received.desc())
	return list(mails.dicts())


class EmailResponse(InboxEmailResponse):
	dst: str
	envelope_src: str
	headers: Dict
	text: str


@app.get("/email/{uuid}", response_model=EmailResponse)
def read_email(uuid):
	mail = Email.get(Email.id == uuid)
	return model_to_dict(mail)


@app.get("/email/{uuid}/raw", response_model=EmailResponse)
def read_email_raw(uuid):
	mail = Email.get(Email.id == uuid)
	return Response(mail.raw, media_type='text/plain')
