##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2015 Therp BV (<http://therp.nl>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from odoo import fields, models


class Website(models.Model):
    _inherit = "website"

    matomo_analytics_id = fields.Integer(
        "Matomo website ID",
        help="The ID Matomo uses to identify the website",
        default=1,
    )
    matomo_analytics_host = fields.Char(
        "Matomo host",
        help="The host/path your Matomo installation is "
        "accessible by on the internet. Do not include a protocol here!\n"
        "So http[s]://[this field]/matomo.php should resolve to your matomo.php",
    )
