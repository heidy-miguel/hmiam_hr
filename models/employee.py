# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class hmiam_hr(models.Model):
    _inherit = ['hr.employee']
    middle_name = fields.Char("Middle Name")
    surname = fields.Char("Surname", required=True)
    fullname = fields.Char(compute='_compute_name', store=True)
    name = fields.Char(default=lambda self: self._default_fullname())
    agent_number = fields.Char("Agent Number")
    address = fields.Char("Address")
    admission_date = fields.Date(
        "Admission Date", default=date.fromisoformat('2022-02-15'))
    study_start_date = fields.Date("Start Date")
    study_end_date = fields.Date("End Date")

    _sql_constraints = [
                     ('identification_id_unique', 
                      'unique(identification_id)',
                      'Já existe um funcionário com essa identificação!')
]

    def _compute_name(self):
        for rec in self:
            name = '%s %s %s' % (rec.name, rec.middle_name, rec.surname)
            rec.fullname = name.title()
