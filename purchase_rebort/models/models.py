# -*- coding: utf-8 -*-

from odoo import models, fields, api

from num2words import num2words as nw

import locale

class PurchaseOrderReoprt(models.Model):
    _inherit = 'purchase.order'

    # set number , language , currency_name and currency_part 
    def _get_number_format(self,number,lang,c1,c2):
        currency_text = ''
        locale.setlocale(locale.LC_ALL, lang)
        x = int((str(number).split('.'))[0])
        y = int((str(number).split('.'))[1])
        if y < 10:
            y *= 10  
        before_point = nw(x, lang=lang)
        after_point  = nw(y, lang=lang)
        currency_text+=before_point
        currency_text+=c1
        currency_text+= after_point
        currency_text+=c2
        return currency_text
 
    def get_arabic_text(self, number):
        if self.currency_id.name == 'EGP':
            text=self._get_number_format(number,'ar',' جنيه ',' قرشا ')
            return text
        elif self.currency_id.name == 'SAR':
            text=self._get_number_format(number,'ar',' ريال ',' هلاله ')
            return text
        else:
            text=self._get_number_format(number,'en',' dolar ',' cent ')
            return text