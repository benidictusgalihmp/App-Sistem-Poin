# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Karyawan(models.Model):
    _name = 'karyawan.akun' # membuat tabel karyawan_akun pada postgres 
    _description = 'Data karyawan' # deskripsi tabel

    id = fields.Integer(string="ID", required=True)
    name = fields.Char(string="Nama", required=True)
    department = fields.Selection(selection=[
        ('0', 'Ketua (G1)'), 
        ('1', 'Koordinator Akhwat (A1)'), 
        ('2', 'Kesekjenan'), 
        ('3', 'Kewilayahan'), 
        ('4', 'PSDM'), 
        ('5', 'SPDK'), 
        ('6', 'Ekesternal'), 
        ('7', 'Annissa'), 
    ], string="Departemen", required=True)

    # type = fields.Many2one('cats.cat.type', string="Jenis")


