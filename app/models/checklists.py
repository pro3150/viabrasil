from sqlalchemy import Column, Integer, String, DateTime, Boolean
from models import db


class Checklist(db.Model):
    id = db.Column(Integer, primary_key=True)
    checklist_template_id = db.relationship('ChecklistTemplate', backref='checklist', lazy=True)#db.Column(Integer)
    status = db.Column(String)
    car_id = db.Column(Integer)
    created_at = db.Column(DateTime, server_default=db.func.now())
    updated_at = db.Column(DateTime, server_default=db.func.now(), server_onupdate=db.func.now())


class ChecklistItem(db.Model):
    id = db.Column(Integer, primary_key=True)
    checklist_id = db.Column(Integer)
    template_item_id = db.Column(Integer)
    status = db.Column(Boolean)
    created_at = db.Column(DateTime, server_default=db.func.now())
    updated_at = db.Column(DateTime, server_default=db.func.now(), server_onupdate=db.func.now())


class ChecklistTemplate(db.Model):
    id = db.Column(Integer, primary_key=True)
    title = db.Column(String)
    created_at = db.Column(DateTime, server_default=db.func.now())
    updated_at = db.Column(DateTime, server_default=db.func.now(), server_onupdate=db.func.now())


class ChecklistTemplateItem(db.Model):
    id = db.Column(Integer, primary_key=True)
    checklist_template_id = db.Column(Integer)
    text = db.Column(String)
    order = db.Column(Integer)
    created_at = db.Column(DateTime, server_default=db.func.now())
    updated_at = db.Column(DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
