from odoo import models, fields

class HelpdeskTicket(models.Model):
    _name= 'helpdesk.ticket'

    name= fields.Char(string='Name',required=True)
    description=fields.Text(string='Description')
    date=fields.Date(string='Date')

    state=fields.Selection(
        [('nuevo', 'Nuevo'),
        ('a','Asignado'),
        ('p','Proceso'),
        ('pend','Pendiente'),
        ('r','Resuelto'),
        ('c','Cancelado'),
        ],
        string='State',
        default='nuevo')

    time=fields.Float(string='Time')

    assigned=fields.Boolean(string='assigned',readonly=True)

    date_limit=fields.Date(String='Date limit')

    action_corrective=fields.Html(string='Corrective Action', help='Describe action to do')

    action_preventive=fields.Html(string='Preventive Action', help='Describe action to do')




