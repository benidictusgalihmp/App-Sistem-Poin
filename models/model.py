# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Anggota(models.Model):
    _name = 'anggota.anggota' # membuat tabel anggota_anggota pada postgres
    _inherit =  ['mail.thread','mail.activity.mixin']
    _description = 'Data Anggota' # deskripsi tabel
    _order = "poin desc, id_anggota asc"

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

    # tambah
    def tambah100(self):
        poinl = self.poin
        self.poin = self.poin + 100
        self.write({'poin' : str(self.poin)})
        self.tambahRiwayat(poinl)
    def tambah200(self):
        poinl = self.poin
        self.poin = self.poin + 200
        self.write({'poin' : str(self.poin)})
        self.tambahRiwayat(poinl)
    def tambah500(self):
        poinl = self.poin
        self.poin = self.poin + 500
        self.write({'poin' : str(self.poin)})
        self.tambahRiwayat(poinl)
    def tambah1000(self):
        poinl = self.poin
        self.poin = self.poin + 1000
        self.write({'poin' : str(self.poin)})
        self.tambahRiwayat(poinl)

    # redeem
    def redeem100(self):
        if self.poin < 100:
            raise ValidationError(("Poin tidak cukup."))
        poinl = self.poin
        self.poin = self.poin - 100
        self.write({'poin' : str(self.poin)})
        self.tambahRiwayat(poinl)

    def redeem200(self):
        if self.poin < 200:
            raise ValidationError(("Poin tidak cukup."))
        poinl = self.poin
        self.poin = self.poin - 200
        self.write({'poin' : str(self.poin)})
        self.tambahRiwayat(poinl)

    def redeem500(self):
        if self.poin < 500:
            raise ValidationError(("Poin tidak cukup."))
        poinl = self.poin
        self.poin = self.poin - 500
        self.write({'poin' : str(self.poin)})
        self.tambahRiwayat(poinl)

    def redeem1000(self):
        if self.poin < 1000:
            raise ValidationError(("Poin tidak cukup."))
        poinl = self.poin
        self.poin = self.poin - 1000
        self.write({'poin' : str(self.poin)})
        self.tambahRiwayat(poinl)
    

    @api.constrains('id_anggota')
    def check_id_anggota(self):
        for rec in self:
            anggota = self.env['anggota.anggota'].search([('id_anggota','=',rec.id_anggota),('id','!=',rec.id)])
            if anggota:
                raise ValidationError(("ID %s Already Exists" % rec.id_anggota))

    def tambahRiwayat(self, poin_lama):
        perubahan_poin = self.poin - poin_lama

        transaksi = ''
        if(perubahan_poin>0):
            # tambah poin
            transaksi = transaksi + '+' + str(perubahan_poin)
        else:
            # redeem poin
            transaksi = str(perubahan_poin)

        vals = {
            'id_anggota' : self.id_anggota,
            'nama' : self.name,
            'poin_lama' : poin_lama,
            'poin_baru' : self.poin,
            'transaksi' : transaksi
        }
        self.env['riwayat.riwayat'].create(vals)

        print("TAMBAH POIN IS CLICKED")
        print(vals)

class Riwayat(models.Model):
    _name = 'riwayat.riwayat' # membuat tabel riwayat pada postgres 
    _description = 'Data riwayat' # deskripsi tabel

    id_anggota = fields.Integer(string="ID", required=True)
    nama = fields.Char(string="Nama", required=True)
    poin_lama = fields.Integer(string="Poin Lama", required=True)
    poin_baru = fields.Integer(string="Poin Baru", required=True)
    transaksi = fields.Char(string="Transaksi", required=True)
    write_date = fields.Datetime(string='Waktu')