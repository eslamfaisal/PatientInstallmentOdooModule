# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HospitalPatient(models.Model):
    _name = 'doctor.doctor'

    _description = 'Doctor Records'
    _rec_name = "doctor_name"

    doctor_name = fields.Char(string="Name", required=True)

    doctor_age = fields.Integer(string="Age")
    patient_id = fields.Many2many('patient.patient', string='Patients', required=True)
    patient_count = fields.Integer(string='Patients', compute='get_patient_count')

    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'other')], required=True,
                              default='male')
    notes = fields.Text(string="Notes")
    image = fields.Binary(string="Image")
    name_seq = fields.Char(string='Sequence', required=True, copy=False,
                           readonly=True, index=True, default='New')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or 'New'
        result = super(HospitalPatient, self).create(vals)
        return result

    def open_patients(self):
        return {
            'name': 'Patients',
            'domain': [('doctor_id', '=', self.id)],
            'type': 'ir.actions.act_window',
            'res_model': 'patient.patient',
            'view_type': 'form',
            'view_id': False,
            'view_mode': 'tree,form',
        }

    def get_patient_count(self):
        count = self.env['patient.patient'].search_count([('doctor_id', '=', self.id)])
        self.patient_count = count

# class om_ho(models.Model):
#     _name = 'om_ho.om_ho'
#     _description = 'om_ho.om_ho'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
