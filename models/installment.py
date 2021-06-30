# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Installment(models.Model):
    _name = 'installment.installment'
    _description = 'Installment Records'
    _rec_name = 'patient_id'

    installment = fields.Integer(string="Installment", required=True)
    due_date = fields.Date(string="Due Date")
    patient_id = fields.Many2one('patient.patient', string='Patient', required=True)
    date = fields.Date(string="Date Of Payment")
    paied = fields.Boolean(string="Paid", default=False)

    def action_paid(self):
        for rec in self:
            rec.paied = True

    # 07 / 06 / 2021
    @api.model
    def create(self, vals_list):
        print('update')
        # print('patient = {}'.format(patient))
        # print('patient_debit_amount = {}'.format(patient.patient_debit_amount))
        # patient.patient_debit_amount += 20
        # patient['patient_debit_amount'] = 20
        # patient.update(['patient_debit_amount', '=', 20])
        result = super(Installment, self).create(vals_list)
        print("vals_list {}".format(vals_list))
        print("vals_list {}".format(type(vals_list)))
        print("vals_list {}".format(type(vals_list["patient_id"])))
        # print("vals_list {}" + vals_list["patient_id"])
        print(vals_list["patient_id"])
        # for r in result:
        #     print(r)
        #     print(type(r))
        # # print("vals_list {}".format(result["patient_id"]+2))
        # print("vals_list {}".format(type(result["patient_id"])))

        patient = self.env['patient.patient'].browse(vals_list["patient_id"])
        print(patient["patient_name"])
        print(patient.patient_debit_amount)
        patient.patient_debit_amount += vals_list["installment"]
        return result

    def write(self, values):
        print('write {}'.format(self.date))
        res = super(Installment, self).write(values)
        print('write {}'.format(self.date))
        print('write {}'.format(res))
        return res



