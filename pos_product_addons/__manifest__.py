# -*- coding: utf-8 -*-
{
    'name': "Product Add-ons in POS",
    'version': '14.0.1.0.4',
    'summary': """ Add product addons(flavour) to the product in POS.""",
    'description': """This module brings an option to add addon(extension) cost of the products in the point of sale.
                        You can configure the addon as a product, so it brings all the product features to the add-on. 
                        It is simple to handle by choosing the add-on from the side bar menu which doesn't affect your 
                        product screen. It shows the add-on cost in the receipt.""",
    'author': "Cybrosys Techno Solutions",
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'category': 'Point of Sale',
    'depends': ['pos_restaurant'],
    'data': [
        'views/product_addons_view.xml',
        'views/templates.xml',
    ],
    'qweb': ['static/src/xml/product_addons_template_view.xml'],
    'images': ['static/description/images/banner.png'],
    'license': 'OPL-1',
    'price': 19.99,
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
    'application': False,
}
