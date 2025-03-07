from odoo import fields, models, api

class Animal(models.Model):
    _name = 'ganaderia.animal'
    _description = 'Livestock Animal'

    # Basic animal data
    name = fields.Char("Animal Name", required=True)
    specie = fields.Selection([('cow', 'Cow'), ('horse', 'Horse'), ('pig', 'Pig')], "Species", required=True)
    birth_date = fields.Date("Birth Date")
    breed = fields.Char("Breed")
    weight = fields.Float("Weight (kg)", help="Current weight of the animal")
    photo = fields.Binary("Animal Photo")

    # Health and disease data
    diseases = fields.Text("Disease History", help="Past diseases record")
    last_disease_date = fields.Date("Last Disease Date")

    # Insemination and reproduction data
    inseminated = fields.Boolean("Inseminated", help="Indicates if the animal has been inseminated")
    insemination_date = fields.Date("Insemination Date")
    birth_date = fields.Date("Birth Date")
    offspring_count = fields.Integer("Number of Offspring", help="Number of offspring born")

    # Animal use
    use = fields.Selection(
        [('meat', 'Meat Sale'), ('milk', 'Milk Sale'), ('breeding', 'Breeding'), ('other', 'Other')],
        "Animal Use")

    # Sales data
    sold = fields.Boolean("Sold", help="Indicates if the animal was sold")
    sale_date = fields.Date("Sale Date")
    sale_price = fields.Float("Sale Price")

    # Monthly weight (Weight history)
    weight_history_ids = fields.One2many('ganaderia.weight', 'animal_id', string="Weight History")

    # Health status
    health_status = fields.Selection([('healthy', 'Healthy'), ('sick', 'Sick')], "Health Status",
                                     default='healthy')

    owner = fields.Char("Owner", help="Animal owner name")
