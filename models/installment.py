# -*- coding: utf-8 -*-

from odoo import models, fields


class Installment(models.Model):
    _name = 'installment.installment'
    _description = 'Installment Records'
    _rec_name = 'patient_id'

    installment = fields.Integer(string="Installment", required=True)
    maturity_date = fields.Date(string="Maturity Date")
    due_date = fields.Date(string="Due Date")
    patient_id = fields.Many2one('patient.patient', string='Patient', required=True)
    date = fields.Date(string="Date Of Payment")
    paied = fields.Boolean(string="Paid", default=False)