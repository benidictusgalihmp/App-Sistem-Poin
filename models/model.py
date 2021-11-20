# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Anggota(models.Model):
    _name = 'anggota.anggota' # membuat tabel anggota_anggota pada postgres
    _inherit =  ['mail.thread','mail.activity.mixin']
    _description = 'Data Anggota' # deskripsi tabel
    _order = "poin desc"

    id_anggota = fields.Integer(string="ID", required=True)
    name = fields.Char(string="Nama", required=True)
    department = fields.Selection(selection=[
        ('0', 'Ketua (G1)'), 
        ('1', 'Koordinator Akhwat (A1)'), 
        ('2', 'Kesekjenan'), 
        ('3', 'Kewilayahan'), 
        ('4', 'PSDM'), 
        ('5', 'SPDK'), 
        ('6', 'Eksternal'), 
        ('7', 'Annissa'), 
    ], string="Departemen", required=True)
    poin = fields.Integer(string="Poin", required=True, tracking = True)

    def tambah_poin(self):
        print("tambah")
    
    def redeem_poin(self):
        print("redeem")

    @api.constrains('id_anggota')
    def check_id_anggota(self):
        for rec in self:
            anggota = self.env['anggota.anggota'].search([('id_anggota','=',rec.id_anggota),('id','!=',rec.id)])
            if anggota:
                raise ValidationError(("ID %s Already Exists" % rec.id_anggota))
            


class Riwayat(models.Model):
    _name = 'riwayat.riwayat' # membuat tabel riwayat pada postgres 
    _description = 'Data riwayat' # deskripsi tabel
