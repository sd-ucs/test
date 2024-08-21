from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Hospital(models.Model):
    _name = 'hospital'



    image = fields.Binary(string='Image')
    name = fields.Char()
    case_no = fields.Integer()
    date = fields.Datetime()
    is_active = fields.Boolean()
    description = fields.Char()
    partner = fields.Many2many('res.partner')
    sale_order = fields.Many2one('sale.order')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ])
    age = fields.Integer()
    date_of_birth = fields.Date()
    address = fields.Char()
    hospital_ids = fields.One2many('patient', 'patient_id')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done')
    ], string='Status', default='draft')

    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done')
    ], string='Status', default='draft')

    # def action_confirm(self):
    #     # Method implementation
    # for record in
    #
    #     print("action_confirm.........")




    @api.onchange('gender')
    def onchange_orders(self):
        self.is_active  = True


    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > fields.Date.today():
                raise ValidationError(_("The entered date of birth is not acceptable !"))
            print("date_of_birth...............")

    @api.depends('name', 'age')
    def _compute_description(self):
        for record in self:
            record.description = f'Name: {record.name}, Age: {record.age}'

    @api.model
    def create(self, vals):
        record = super(Hospital, self).create(vals)
        return record

    # @api.multi
    # def activate_all_records(self):
    #     for record in self:
    #         record.is_active = True
    #     return True

    # search method
    def button_done(self):
        patients = self.env['hospital'].search([])

        for recode in patients:
            print("patients.......", recode.name)


        male_patients = self.env['hospital'].search([('gender', '=', 'male'),('age', '<=', '30'),('age', '=', '30')])

        print("male_patients......", male_patients)




        # search_count
        patient_count = self.env['hospital'].search_count([])
        print("patient_count.....",patient_count)


        # browse method
        browse_result = self.env['hospital'].browse()
        print("browse_result.....",browse_result)


        # create method
        vals = {
            'name': 'ppppppppppppppppp',
            'case_no': '1',
            'is_active': 'true',
            'description': 'hiiiiiiiiiiiiiiiiiii',

        }
        self.env['hospital'].create(vals)



        #write method

        self.write({'name':'shlok'})



        # #copy method
        # record_to_copy = self.env['hospital'].browse()
        #
        # record_to_copy.copy()
        #
        # #unlink method
        # record_to_copy = self.env['hospital'].browse()
        # record_to_copy.unlink()

    # @api.model
    # def create(self, vals):
    #     pass
    #
    #
    # def browse(self):
    #     pass
    #
    # @api.multi
    # def write(self,vals):
    #     pass
    # def unlink(self):
    #     pass


