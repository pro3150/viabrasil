from sqlalchemy import Column, Integer, String, DateTime, Boolean
from models import db


class Checklist(db.Model):
    id = db.Column(Integer, primary_key=True, autoincrement=True, foreign_key=True)
    checklist_template_id = db.Column(Integer, db.ForeignKey('checklist_template.id'))
    status = db.Column(String)
    car_id = db.Column(Integer)
    created_at = db.Column(DateTime, server_default=db.func.now())
    updated_at = db.Column(DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    checklist_items = db.relationship('ChecklistItem', backref='checklist')


class ChecklistItem(db.Model):
    id = db.Column(Integer, primary_key=True)
    checklist_id = db.Column(Integer, db.ForeignKey('checklist.id'))
    template_item_id = db.Column(Integer, db.ForeignKey('checklist_template_item.id'))
    status = db.Column(Boolean)
    created_at = db.Column(DateTime, server_default=db.func.now())
    updated_at = db.Column(DateTime, server_default=db.func.now(), server_onupdate=db.func.now())


class ChecklistTemplate(db.Model):
    id = db.Column(Integer, primary_key=True)
    title = db.Column(String)
    created_at = db.Column(DateTime, server_default=db.func.now())
    updated_at = db.Column(DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    checklists = db.relationship('Checklist', backref='checklist_template')


class ChecklistTemplateItem(db.Model):
    id = db.Column(Integer, primary_key=True)
    checklist_template_id = db.Column(Integer)
    text = db.Column(String)
    order = db.Column(Integer)
    created_at = db.Column(DateTime, server_default=db.func.now())
    updated_at = db.Column(DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    checklist_items = db.relationship('ChecklistItem', backref='checklist_template_item')
