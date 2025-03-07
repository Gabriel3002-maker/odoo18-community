from odoo import fields, models, api

class Weight(models.Model):
    _name = 'ganaderia.weight'
    _description = 'Animal Weight History'

    animal_id = fields.Many2one('ganaderia.animal', string="Animal", required=True)
    date = fields.Date("Date", required=True)
    weight = fields.Float("Weight (kg)", required=True)
