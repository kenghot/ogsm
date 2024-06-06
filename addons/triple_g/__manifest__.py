# -*- coding: utf-8 -*-

{
    'name' : 'Triple G Solution',
    'version' : '1.1',
    'summary': 'Triple G Solution',
    'sequence': 1,
    'description': """Triple G Solution""",
    'category': 'Triple G',
    'website': 'http://www.gggsolution.com',
    'images' : ['images/accounts.jpeg','images/bank_statement.jpeg','images/cash_register.jpeg','images/chart_of_accounts.jpeg','images/customer_invoice.jpeg','images/journal_entries.jpeg'],
    'depends' : ['web','base','hr','hr_contract'],
    'data': [
        'data/lov.xml',
        'data/province.xml',
        'security/ir.model.access.csv',
        'security/ggg_access_rights.xml',
        'views/ggg.xml',
        'views/lov.xml',
        'views/main_company.xml',
        'views/view_partner_form.xml',
        'views/template.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}
