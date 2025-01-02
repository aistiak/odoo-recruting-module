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

class RecruitingLicense(models.Model):
    _name = 'recruiting.license'
    _description = 'Recruiting License'
    _order = 'create_date desc'

    name = fields.Char(string='License Name', required=True)
    license_id = fields.Char(string='License ID', required=True)
    country = fields.Selection([
        ('malaysia', 'Malaysia'),
        ('saudi_arabia', 'Saudi Arabia')
    ], string='Country', required=True)
    create_date = fields.Datetime(string='Created at', default=lambda self: fields.Datetime.now(), readonly=True)

    _sql_constraints = [
        ('unique_license_id', 'unique(license_id)', 'License ID must be unique!')
    ] 

class RecruitingJob(models.Model):
    attachment_filename = fields.Char(string='Attachment Filename')
    _name = 'recruiting.job'
    _description = 'Recruiting Job'
    _order = 'date desc'

    license_id = fields.Many2one('recruiting.license', string='License', required=True)
    job_type = fields.Selection([
        ('recruiting', 'Recruiting'),
        ('processing', 'Processing')
    ], string='Type', required=True)
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ], string='Status', default='active')
    
    date = fields.Date(string='Date', required=True)
    sln = fields.Char(string='SLN', required=True)
    pp_name = fields.Char(string='PP Name', required=True)
    client = fields.Many2one('recruiting.clients', string='Client')
    pp_number = fields.Char(string='PP Number', required=True)
    
    visa_number = fields.Char(string='Visa Number')
    occupation = fields.Char(string='Occupation')
    company_id_number = fields.Char(string='Company ID Number')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender', required=True, default='male')
    worker_number = fields.Char(string='Worker Number')
    
    p_rate = fields.Float(string='P Rate', digits=(10,2))
    country = fields.Selection([
        ('malaysia', 'Malaysia'),
        ('saudi_arabia', 'KSA')
    ], string='Country', required=True)
    company = fields.Char(string='Company', required=False)
    others = fields.Float(string="Other's", digits=(10,2))
    total = fields.Float(string='Total', compute='_compute_total', store=True)
    attachment_filename = fields.Char(string='Attachment Filename', required=False)
    updated_by = fields.Many2one('res.users', string='Updated By', 
                                default=lambda self: self.env.user, 
                                readonly=True)
    create_date = fields.Datetime(string='Created at', 
                                default=lambda self: fields.Datetime.now(), 
                                readonly=True)
    
    _sql_constraints = [
        ('unique_sln', 'unique(sln)', 'SLN must be unique!')
    ]

    # Boolean Fields
    diving_licence = fields.Boolean(string='Diving Licence', default=False)
    police_clearance = fields.Boolean(string='Police Clearance', default=False)
    medical = fields.Boolean(string='Medical', default=False)
    musaned = fields.Boolean(string='Musaned', default=False)
    okala = fields.Boolean(string='Okala', default=False)
    mofa = fields.Boolean(string='Mofa', default=False)
    stamping = fields.Boolean(string='Stamping', default=False)
    finger = fields.Boolean(string='Finger', default=False)
    manpower = fields.Boolean(string='Manpower', default=False)

    # Date Fields
    musaned_date = fields.Date(string='Musaned Date')
    okala_date = fields.Date(string='Okala Date')
    mofa_date = fields.Date(string='Mofa Date')
    stamping_date = fields.Date(string='Stamping Date')
    finger_date = fields.Date(string='Finger Date')
    manpower_date = fields.Date(string='Manpower Date')

    # Medical Status
    medical_status = fields.Selection([
        ('fit', 'Fit'),
        ('unfit', 'Unfit')
    ], string='Medical Status')

    # Remarks
    remarks = fields.Text(string='Remarks')

    @api.depends('p_rate', 'others')
    def _compute_total(self):
        for record in self:
            record.total = (record.p_rate or 0) + (record.others or 0) 