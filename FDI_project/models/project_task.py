# -*- coding: utf-8 -*-

from odoo import fields, models, api, _

class CrossoveredBudget(models.Model):
    _inherit = 'project.task'

    parent_level_1_id = fields.Many2one('project.task',string='Parent Niveau 1',
                                        domain="[('project_id', '=', project_id)]")
    parent_level_2_id = fields.Boolean('project.task',string='Parent Niveau 2',
                                       domain="[('project_id', '=', project_id)]")
