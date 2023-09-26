import requests
import re
import urllib
import datetime
from datetime import datetime, timedelta
from odoo import models, api, fields


class CustomProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def create(self, vals):
        # Check if 'default_code' exists in the value given
        if 'default_code' in vals:
            # Find if there is same product with same default code (Internal Reference)
            find_data = self.env['product.template'].search([('default_code', '=', vals['default_code'])])
            if find_data:
                try:
                    # Update the existing record using the 'write' method
                    find_data.write(vals)
                    # Change the result data by find_data
                    result = find_data
                except Exception as e:
                    # Handle any exceptions that occur during the function
                    print("Error updating existing record:", e)
            else:
                # if there is no find_data, create new record
                result = super(CustomProductTemplate, self).create(vals)
        else:
            # If this is no value 'default_code' create a new record
            result = super(CustomProductTemplate, self).create(vals)

        return result