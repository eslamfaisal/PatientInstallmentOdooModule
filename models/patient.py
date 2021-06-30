# -*- coding: utf-8 -*-


from odoo import models, fields, api


class Patient(models.Model):
    _name = 'patient.patient'
    _description = 'Patient Records'
    _rec_name = 'patient_name'

    patient_name = fields.Char(string="Name", required=True)
    doctor_id = fields.Many2many('doctor.doctor', string='Doctor', required=True)
    doctor_count = fields.Integer(string='Doctors', compute='get_doctor_count')
    install_count = fields.Integer(string='Installments', compute='get_Install_count')
    patient_debit_amount = fields.Integer(string='Debit')
    patient_credit_amount = fields.Integer(string='Credit')
    patient_balance_amount = fields.Integer(string='Balance')

    patient_age = fields.Integer(string="Age")

    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'other')], required=True,
                              default='male')
    notes = fields.Text(string="Notes")
    image = fields.Binary(string="Image")
    sequence = fields.Char(string='Sequence', required=True, copy=False,
                           readonly=True, index=True, default='New')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['sequence'] = self.env['ir.sequence'].next_by_code('patient.patient.sequence') or 'New'
            result = super(Patient, self).create(vals)
            return result

    def open_doct(self):
        return {
            'name': 'Doctors',
            'domain': [('patient_id', '=', self.id)],
            'type': 'ir.actions.act_window',
            'res_model': 'doctor.doctor',
            'view_type': 'form',
            'view_id': False,
            'view_mode': 'tree,form',
        }

    def get_doctor_count(self):
        count = self.env['doctor.doctor'].search_count([('patient_id', '=', self.id)])
        self.doctor_count = count

    def open_installs(self):
        return {
            'name': 'Installments',
            'domain': [('patient_id', '=', self.id)],
            'type': 'ir.actions.act_window',
            'res_model': 'installment.installment',
            'view_type': 'form',
            'view_id': False,
            'view_mode': 'tree,form',
        }

    def get_Install_count(self):
        count = self.env['installment.installment'].search_count([('patient_id', '=', self.id)])
        self.install_count = count
