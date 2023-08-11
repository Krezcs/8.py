from mongoengine import Document
from mongoengine.fields import StringField, BooleanField


class Contact(Document):
    fullname = StringField(required=True)
    company = StringField()
    email = StringField(required=True)
    choice_for_message = StringField(default='email')
    send_email = BooleanField(default=False)
