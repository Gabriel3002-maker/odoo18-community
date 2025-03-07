from odoo import fields, models, api


class Pregnancy(models.Model):
    _name = 'ganaderia.pregnancy'
    _description = 'Pregnancy and Birth Management'

    # Datos básicos
    animal_id = fields.Many2one('ganaderia.animal', string="Animal", required=True)
    insemination_date = fields.Date("Insemination Date", required=True)
    pregnancy_status = fields.Selection([
        ('pregnant', 'Pregnant'),
        ('miscarriage', 'Miscarriage'),
        ('stillborn', 'Stillborn'),
        ('birth', 'Birth'),
        ('other', 'Other'),
    ], string="Pregnancy Status", default='pregnant', required=True)
    expected_birth_date = fields.Date("Expected Birth Date")

    # Fechas y registros de la evolución
    last_status_change_date = fields.Date("Last Status Change Date", default=fields.Date.today)
    number_of_offspring = fields.Integer("Number of Offspring")
    number_of_dead_offspring = fields.Integer("Number of Dead Offspring")

    # Seguimiento de salud durante el embarazo
    health_status = fields.Selection([
        ('healthy', 'Healthy'),
        ('sick', 'Sick'),
        ('complicated', 'Complicated')
    ], string="Health Status", default='healthy')

    # Tratamientos y medicamentos durante el embarazo
    treatments = fields.Text("Treatments Given During Pregnancy",
                             help="Medications or treatments given to the animal during pregnancy")

    # Información sobre el padre (si es relevante)
    father_id = fields.Many2one('ganaderia.animal', string="Father", help="Father of the offspring")
    father_health_status = fields.Selection([('healthy', 'Healthy'), ('sick', 'Sick')], string="Father Health Status")

    # Control de peso durante el embarazo
    weight_history = fields.One2many('ganaderia.weight', 'animal_id', string="Weight History")

    # Información post-parto
    post_birth_health_status = fields.Selection([('healthy', 'Healthy'), ('sick', 'Sick')],
                                                string="Post Birth Health Status")
    post_birth_notes = fields.Text("Post Birth Notes", help="Notes about the animal's health after birth")

    # Datos de la lactancia
    lactation_status = fields.Selection([('not_started', 'Not Started'), ('started', 'Started'), ('ended', 'Ended')],
                                        string="Lactation Status")

    # Registro de visitas veterinarias
    vet_name = fields.Char("Veterinarian Name", help="Name of the veterinarian who supervised the pregnancy")
    vet_visit_date = fields.Date("Veterinarian Visit Date", help="Date of the veterinary visit")
    vet_visit_notes = fields.Text("Veterinarian Visit Notes", help="Notes from the veterinary visit")

    # Registro de la muerte
    death_date = fields.Date("Date of Death", help="If the animal passed away during or after pregnancy")
    cause_of_death = fields.Text("Cause of Death", help="Detailed information on the cause of death")
    necropsy_report = fields.Text("Necropsy Report", help="Details of the necropsy if the animal passed away")

    # Notas adicionales
    extra_notes = fields.Text("Extra Notes", help="Any additional notes or observations during the pregnancy process")
