from odoo import models, fields, api
from datetime import datetime

class RecruitingClients(models.Model):
    _name = 'recruiting.clients'
    _description = 'Recruiting Clients'
    _order = 'create_date desc'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    invoice = fields.Float(string='Invoice', digits=(10,2))
    receive = fields.Float(string='Receive', digits=(10,2))
    bill = fields.Float(string='Bill', digits=(10,2))
    bill_pay = fields.Float(string='Bill Pay', digits=(10,2))
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('pending', 'Pending')
    ], string='Status', default='active')
    create_date = fields.Datetime(string='Created at', default=lambda self: fields.Datetime.now(), readonly=True)

    _sql_constraints = [
        ('unique_email', 'unique(email)', 'Email must be unique!')
    ] 