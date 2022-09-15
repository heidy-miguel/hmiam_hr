# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class hmiam_hr(models.Model):
    _inherit = ['hr.employee']
    middle_name = fields.Char("Middle Name")
    surname = fields.Char("Surname", required=True)
    fullname = fields.Char(default=lambda self: self._default_fullname())
    name = fields.Char(default=lambda self: self._default_fullname())
    agent_number = fields.Char("Agent Number")
    address = fields.Char("Address")
    admission_date = fields.Date(
        "Admission Date", default=date.fromisoformat('2022-02-15'))
    study_start_date = fields.Date("Start Date")
    study_end_date = fields.Date("End Date")

    def _default_fullname(self):
        return '{0} {1} {2}'.format(self.name, self.middle_name, self.surname)
        
    def name_get(self, context=None):
        if context is None:
            context = {}

        result = []
        for record in self:
            if context.get('fullname', False):
                result.append((record.id, '{0} {1}'.format(
                self.name, self.surname).title()))
            else:
                result.append((record.id, '{0} {1} {2}'.format(
                self.name, self.middle_name, self.surname).title()))
        return result

